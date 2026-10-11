//! HH-ON06E continuation from a SHA-verified completed ON06D generation32.
//! Qualified experimental scope: total32..64, time4e10..8e10 proper seconds.
//! Existing paired_history caps, state codec and all physics stay unchanged.
//! Single writer; immutable generations, not an untrusted proof format.
use rei_microphysics::coupled_primary::HhMode;
use rei_microphysics::paired_runtime::{hh_checkpoint_decode,hh_checkpoint_encode,
    try_hh_paired_ensemble,HhPairedState,HhRunConfig,PairedConfig};
use std::{io,fs::{self,File,OpenOptions},io::Write,path::{Path,PathBuf}};
const SOURCE:&str="746b6a824e51511bee8817c6c9fc4ef18508edd1c223bb31daa240c968d71224";
const START_TIME:f64=4e10;
const END_TIME:f64=8e10;
const MAX_TOTAL:usize=64;
fn err(s:&str)->io::Error{io::Error::other(s)}
fn fwd(e:rei_microphysics::ForwardError)->io::Error{err(e.code())}
fn fi(s:&str)->io::Result<f64>{u64::from_str_radix(s,16).map(f64::from_bits).map_err(|_|err("HH_D_ENCODING"))}
fn check_target(accepted:usize,target:usize)->io::Result<()>{
 if accepted<32 || accepted>MAX_TOTAL || target<accepted || target>MAX_TOTAL {Err(err("HH_D_SCOPE"))} else {Ok(())}
}
fn configs()->io::Result<Vec<HhRunConfig>>{
 let mut c=vec![];
 for h in [[1e-14;3],[1.01e-14,0.99e-14,1e-14]]{
  for mode in [HhMode::Off,HhMode::Lcs91]{
   c.push(HhRunConfig::new(PairedConfig{spectral_subdivisions:8,n_mu:8,n_phi:16},h,mode).map_err(fwd)?);
  }
 }
 Ok(c)
}
struct Generation {states:Vec<HhPairedState>,accepted:usize,rejected:usize,dt:f64,metrics:[f64;3]}
fn fnv(bytes:&[u8])->u64{bytes.iter().fold(0xcbf29ce484222325,|h,&b|(h^b as u64).wrapping_mul(0x100000001b3))}
fn read_generation(p:&Path,c:&[HhRunConfig])->io::Result<Generation>{
 if p.extension().is_some_and(|x|x=="pending"){return Err(err("HH_E_PENDING_INPUT"));}
 let text=fs::read_to_string(p.join("scheduler.txt"))?;
 let (body,tail)=text.rsplit_once("checksum ").ok_or_else(||err("HH_D_SCHEDULER_CHECKSUM"))?;
 let check=tail.strip_suffix('\n').filter(|s|s.len()==16).ok_or_else(||err("HH_D_SCHEDULER_CHECKSUM"))?;
 if u64::from_str_radix(check,16).ok()!=Some(fnv(body.as_bytes())){return Err(err("HH_D_SCHEDULER_CHECKSUM"));}
 let v:Vec<_>=body.split_whitespace().collect();
 if v.len()!=8 || !matches!(v[0],"HH06D_V1"|"HH06E_V1") || v[7]!=SOURCE{return Err(err("HH_D_SOURCE_IDENTITY"));}
 let accepted=v[1].parse::<usize>().map_err(|_|err("HH_D_HEADER"))?;
 let rejected=v[2].parse::<usize>().map_err(|_|err("HH_D_HEADER"))?;
 check_target(accepted,accepted)?;
 if v[0]=="HH06D_V1" && accepted!=32 {return Err(err("HH_E_LEGACY_IMPORT_SCOPE"));}
 let dt=fi(v[3])?;let metrics=[fi(v[4])?,fi(v[5])?,fi(v[6])?];
 if !dt.is_finite() || !(1000.0..=1.25e9).contains(&dt) || rejected>1000000 ||
  metrics.iter().any(|x|!x.is_finite()||*x<0.0) || metrics[0]>=2e-4 || metrics[1]>=2e-3 || metrics[2]>1e-12 {
  return Err(err("HH_D_CONTROL"));
 }
 let mut states=vec![];
 for(i,cfg)in c.iter().enumerate(){
  let bytes=fs::read(p.join(format!("member{i}.bin")))?;
  let s=hh_checkpoint_decode(cfg,&bytes).map_err(fwd)?;
  if hh_checkpoint_encode(cfg,&s).map_err(fwd)?!=bytes{return Err(err("HH_D_STATE_ROUNDTRIP"));}
  states.push(s);
 }
 let t=states[0].base().time_s;
 if !t.is_finite() || !(START_TIME..=END_TIME).contains(&t) ||
    (accepted==32 && t!=START_TIME) || states.iter().any(|s|s.base().time_s.to_bits()!=t.to_bits()) {
  return Err(err("HH_D_TIME_ALIGNMENT"));
 }
 Ok(Generation{states,accepted,rejected,dt,metrics})
}
fn scheduler(r:&Generation)->String{
 let b=format!("HH06E_V1 {} {} {:016x} {:016x} {:016x} {:016x} {}\n",r.accepted,r.rejected,r.dt.to_bits(),r.metrics[0].to_bits(),r.metrics[1].to_bits(),r.metrics[2].to_bits(),SOURCE);
 format!("{}checksum {:016x}\n",b,fnv(b.as_bytes()))
}
fn write_new(path:&Path,data:&[u8])->io::Result<()>{
 let mut f=OpenOptions::new().write(true).create_new(true).open(path)?;f.write_all(data)?;f.sync_all()
}
fn summary(r:&Generation)->String{
 let members=r.states.iter().enumerate().map(|(i,s)|{let b=s.base();format!("{{\"member\":{},\"mode\":\"{}\",\"geometry\":\"{}\",\"time_s\":{:.17e},\"gas\":[{:.17e},{:.17e},{:.17e},{:.17e}],\"hh_events_per_h\":{:.17e},\"hh_heat_ev_per_h\":{:.17e}}}",i,if i%2==0{"OFF"}else{"LCS"},if i<2{"FLRW"}else{"BIANCHI_I"},b.time_s,b.gas.fractions[0],b.gas.fractions[1],b.gas.fractions[2],b.gas.w_ev_per_h,s.hh_events_per_h(),s.hh_heat_ev_per_h())}).collect::<Vec<_>>().join(",");
 format!("{{\"schema\":\"HH_ON06E_bounded_continuation\",\"accepted_total\":{},\"rejected_total\":{},\"dt_s\":{:.17e},\"max_local\":{:.17e},\"max_width\":{:.17e},\"max_ledger\":{:.17e},\"members\":[{}],\"full_history_qualified\":false,\"physical_admission\":false}}\n",r.accepted,r.rejected,r.dt,r.metrics[0],r.metrics[1],r.metrics[2],members)
}
fn publish(root:&Path,c:&[HhRunConfig],r:&Generation,trace:&str,sequence:usize,parent:&Path)->io::Result<PathBuf>{
 let tmp=root.join(format!("generation_{sequence:06}.pending"));let dst=root.join(format!("generation_{sequence:06}"));
 if dst.exists(){return Err(err("HH_D_OUTPUT_EXISTS"));}fs::create_dir(&tmp)?;
 for (i,(cfg,s))in c.iter().zip(&r.states).enumerate(){write_new(&tmp.join(format!("member{i}.bin")),&hh_checkpoint_encode(cfg,s).map_err(fwd)?)?;}
 write_new(&tmp.join("scheduler.txt"),scheduler(r).as_bytes())?;
 write_new(&tmp.join("trace.jsonl"),trace.as_bytes())?;
 write_new(&tmp.join("summary.json"),summary(r).as_bytes())?;
 write_new(&tmp.join("parent_path.txt"),format!("{}\n",parent.display()).as_bytes())?;
 File::open(&tmp)?.sync_all()?;fs::rename(&tmp,&dst)?;File::open(root)?.sync_all()?;Ok(dst)
}
fn main()->io::Result<()>{
 let v:Vec<String>=std::env::args().skip(1).collect();
 if v.len()!=3{return Err(err("usage: hh_prefix_next VERIFIED_GENERATION NEW_OUTPUT TOTAL_STEPS_32_TO_64"));}
 let input=PathBuf::from(&v[0]);let output=PathBuf::from(&v[1]);let target=v[2].parse::<usize>().map_err(|_|err("HH_D_SCOPE"))?;
 let c=configs()?;let mut r=read_generation(&input,&c)?;check_target(r.accepted,target)?;
 fs::create_dir(&output)?;write_new(&output.join("SOURCE_DIGEST.txt"),format!("{SOURCE}\n").as_bytes())?;
 let original=r.accepted;let mut sequence=0;let mut parent=input;
 while r.accepted<target {
  if r.states[0].base().time_s+r.dt>END_TIME{return Err(err("HH_D_TIME_LIMIT"));}
  let before=c.iter().zip(&r.states).map(|(c,s)|hh_checkpoint_encode(c,s).map_err(fwd)).collect::<io::Result<Vec<_>>>()?;
  let trace=match try_hh_paired_ensemble(&c,&mut r.states,r.dt){
   Ok(trials)=>{
    r.accepted+=1;let mut text=String::new();
    for(i,t)in trials.iter().enumerate(){
     r.metrics[0]=r.metrics[0].max(t.local_bound);r.metrics[1]=r.metrics[1].max(t.public_width);r.metrics[2]=r.metrics[2].max(t.max_ledger);
     let s=&r.states[i];
     text.push_str(&format!("{{\"kind\":\"accepted\",\"macro\":{},\"member\":{},\"mode\":\"{}\",\"geometry\":\"{}\",\"time_s\":{:.17e},\"dt_s\":{:.17e},\"local\":{:.17e},\"width\":{:.17e},\"ledger\":{:.17e},\"hh_events_per_h\":{:.17e},\"hh_heat_ev_per_h\":{:.17e},\"site_hh_events\":[{:.17e},{:.17e},{:.17e}],\"site_hh_heat\":[{:.17e},{:.17e},{:.17e}],\"audits\":[{}]}}\n",r.accepted,i,if i%2==0{"OFF"}else{"LCS"},if i<2{"FLRW"}else{"BIANCHI_I"},s.base().time_s,r.dt,t.local_bound,t.public_width,t.max_ledger,s.hh_events_per_h(),s.hh_heat_ev_per_h(),t.source_hh_events[0],t.source_hh_events[1],t.source_hh_events[2],t.source_hh_heat[0],t.source_hh_heat[1],t.source_hh_heat[2],t.audits.join(",")));
    }text
   },
   Err(e)=>{
    for((cfg,s),old)in c.iter().zip(&r.states).zip(&before){if hh_checkpoint_encode(cfg,s).map_err(fwd)?!=*old{return Err(err("HH_D_ROLLBACK"));}}
    let msg=format!("{{\"kind\":\"rejected\",\"time_s\":{:.17e},\"dt_s\":{:.17e},\"error\":\"{}\",\"all_states_unchanged\":true}}\n",r.states[0].base().time_s,r.dt,e.code());
    if !matches!(e.code(),"PAIRED_LOCAL_GATE"|"PAIRED_WIDTH_GATE"|"PAIRED_LEDGER_GATE"|"PRIMARY_NONCONVERGENCE"|"PRIMARY_ROOT_NONCONVERGENCE") || r.dt/2.0<1000.0{
     write_new(&output.join("FAILURE.jsonl"),msg.as_bytes())?;return Err(fwd(e));
    }
    r.rejected+=1;r.dt/=2.0;msg
   }
  };
  sequence+=1;parent=publish(&output,&c,&r,&trace,sequence,&parent)?;
  println!("{{\"accepted_total\":{},\"time_s\":{:.17e},\"generation\":\"{}\"}}",r.accepted,r.states[0].base().time_s,parent.display());io::stdout().flush()?;
 }
 write_new(&output.join("FINAL_GENERATION.txt"),format!("{}\n",parent.display()).as_bytes())?;
 write_new(&output.join("SUMMARY.json"),summary(&r).as_bytes())?;
 println!("{{\"status\":\"COMPLETE\",\"new_macros\":{},\"target\":{}}}",r.accepted-original,target);Ok(())
}

#[cfg(test)]
mod tests {
 use super::*;
 fn seed()->PathBuf{Path::new(env!("CARGO_MANIFEST_DIR")).join("../../../seed")}
 fn copied_seed(name:&str)->PathBuf{let p=std::env::temp_dir().join(format!("hh_e_{}_{}",name,std::process::id()));fs::create_dir(&p).unwrap();for n in ["scheduler.txt","member0.bin","member1.bin","member2.bin","member3.bin"]{fs::copy(seed().join(n),p.join(n)).unwrap();}p}
 #[test] fn e_qualified_32_to_64(){assert!(check_target(32,64).is_ok());}
 #[test] fn e_no_rewind_to_old_prefix(){assert!(check_target(8,16).is_err());}
 #[test] fn e_no_full_history(){assert!(check_target(32,65).is_err());}
 #[test] fn e_no_backward_target(){assert!(check_target(32,31).is_err());}
 #[test] fn e_exact_d32_import_roundtrip(){let c=configs().unwrap();let r=read_generation(&seed(),&c).unwrap();assert_eq!(r.accepted,32);for(i,(cfg,s))in c.iter().zip(&r.states).enumerate(){assert_eq!(hh_checkpoint_encode(cfg,s).unwrap(),fs::read(seed().join(format!("member{i}.bin"))).unwrap());}}
 #[test] fn e_output_schema_is_distinct(){let r=read_generation(&seed(),&configs().unwrap()).unwrap();assert!(scheduler(&r).starts_with("HH06E_V1 "));}
 #[test] fn e_pending_input_is_not_committed(){let p=copied_seed("pending.pending");let q=p.with_extension("pending");fs::rename(&p,&q).unwrap();let r=read_generation(&q,&configs().unwrap());fs::remove_dir_all(q).unwrap();assert!(r.is_err());}
 #[test] fn e_legacy_header_wrong_count_is_rejected(){let p=copied_seed("wrongcount");let text=fs::read_to_string(p.join("scheduler.txt")).unwrap();let(body,_)=text.rsplit_once("checksum ").unwrap();let body=body.replacen("HH06D_V1 32 ","HH06D_V1 31 ",1);fs::write(p.join("scheduler.txt"),format!("{}checksum {:016x}\n",body,fnv(body.as_bytes()))).unwrap();let r=read_generation(&p,&configs().unwrap());fs::remove_dir_all(p).unwrap();assert!(r.is_err());}
 #[test] fn e_model_order_mismatch_rejected(){let mut c=configs().unwrap();c.swap(0,1);assert!(read_generation(&seed(),&c).is_err());}
}
