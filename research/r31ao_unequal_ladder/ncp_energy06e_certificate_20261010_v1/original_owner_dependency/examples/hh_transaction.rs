use rei_microphysics::paired_runtime::*;
use rei_microphysics::coupled_primary::HhMode;
use rei_microphysics::Interval;
use std::fmt::Write;
fn array(v:&[f64])->String{format!("[{}]",v.iter().map(|x|format!("{:.17e}",x)).collect::<Vec<_>>().join(","))}
fn boxes(v:&[Interval])->String{format!("[{}]",v.iter().map(|x|array(&[x.lo,x.hi])).collect::<Vec<_>>().join(","))}
fn state_json(s:&HhPairedState)->String{
 let b=s.base();let mut out=String::new();
 write!(out,"{{\"time\":{:.17e},\"gas\":{},\"gas_box\":{},\"escape\":{:.17e},\"photons\":{},\"photon_boxes\":{},\"lower_n\":{},\"lower_u\":{},\"lower_nb\":{},\"lower_ub\":{},\"ledgers\":{},\"ledger_comp\":{},\"energy_comp\":{:.17e},\"hh_J\":{:.17e},\"hh_heat\":{:.17e},\"hh_comp\":{}}}",b.time_s,array(&[b.gas.fractions[0],b.gas.fractions[1],b.gas.fractions[2],b.gas.w_ev_per_h]),boxes(&b.gas_box),b.gas.escape_ev_per_h,array(&b.photons),boxes(&b.photon_boxes),array(&b.lower_guard_n),array(&b.lower_guard_u),boxes(&b.lower_guard_n_box),boxes(&b.lower_guard_u_box),array(&[b.redshift_work_ev_per_h,b.thermal_work_ev_per_h,b.source_photons_per_h,b.source_energy_ev_per_h,b.absorbed_photons_per_h]),array(&b.ledger_comp),b.energy_comp,s.hh_events_per_h(),s.hh_heat_ev_per_h(),array(&s.hh_compensation())).unwrap();out
}
fn main()->Result<(),Box<dyn std::error::Error>>{
 let out=std::env::args().nth(1).expect("create-only output directory");std::fs::create_dir(&out)?;
 let mut cs=Vec::new();let mut labels=Vec::new();
 for (label,h) in [("FLRW",[1e-14;3]),("BIANCHI_I",[1.01e-14,0.99e-14,1e-14])]{for mode in [HhMode::Off,HhMode::Lcs91]{cs.push(HhRunConfig::new(PairedConfig{spectral_subdivisions:8,n_mu:4,n_phi:8},h,mode)?);labels.push((label,if mode==HhMode::Off{"OFF"}else{"LCS"}));}}
 let mut states=cs.iter().map(hh_paired_initial).collect::<Result<Vec<_>,_>>()?;let initial=states.clone();
 let before=cs.iter().zip(&states).map(|(c,s)|hh_checkpoint_encode(c,s)).collect::<Result<Vec<_>,_>>()?;
 let mut chosen=None;let mut attemptlog=String::new();
 for dt in [1e10,5e9,2.5e9,1.25e9]{match try_hh_paired_ensemble(&cs,&mut states,dt){
  Ok(t)=>{writeln!(attemptlog,"{{\"dt\":{:.17e},\"status\":\"ACCEPTED_ALL_FOUR\"}}",dt)?;chosen=Some((dt,t));break},
  Err(e)=>{for ((c,s),bytes) in cs.iter().zip(&states).zip(&before){assert_eq!(&hh_checkpoint_encode(c,s)?,bytes);}
   writeln!(attemptlog,"{{\"dt\":{:.17e},\"status\":\"REJECTED_ATOMIC\",\"error\":\"{}\",\"all_states_unchanged\":true}}",dt,e.code())?;}
 }}
 std::fs::write(format!("{out}/attempts.jsonl"),&attemptlog)?;print!("{attemptlog}");
 let(dt,trials)=chosen.ok_or("no common accepted first transaction")?;
 let mut records=String::new();
 for (i,((c,t),(geometry,mode))) in cs.iter().zip(&trials).zip(&labels).enumerate(){
  let name=format!("{geometry}_{mode}");let bytes=hh_checkpoint_encode(c,&states[i])?;std::fs::write(format!("{out}/{name}.hhcp"),&bytes)?;
  let restored=hh_checkpoint_decode(c,&bytes)?;assert_eq!(hh_checkpoint_encode(c,&restored)?,bytes);assert_eq!(format!("{:?}",restored),format!("{:?}",states[i]));
  writeln!(records,"{{\"kind\":\"transaction\",\"geometry\":\"{}\",\"mode\":\"{}\",\"dt\":{:.17e},\"hubble\":{},\"nodes\":{},\"initial\":{},\"state\":{},\"local\":{:.17e},\"width\":{:.17e},\"max_ledger\":{:.17e},\"site_hh_events\":{},\"site_hh_heat\":{},\"audits\":[{}],\"checkpoint_bytes\":{},\"checkpoint_restored\":true,\"step_controller_accepted\":true}}",geometry,mode,dt,array(&c.hubble()),array(&energy_nodes(c.grid())?),state_json(&initial[i]),state_json(&states[i]),t.local_bound,t.public_width,t.max_ledger,array(&t.source_hh_events),array(&t.source_hh_heat),t.audits.join(","),bytes.len())?;
 }
 std::fs::write(format!("{out}/transactions.jsonl"),records)?;
 println!("{{\"complete\":true,\"transactions\":4,\"accepted_sources\":8,\"trial_sources\":12,\"chosen_dt\":{:.17e},\"directions\":32,\"energy_nodes\":33}}",dt);Ok(())
}
