#include <cmath>
#include <array>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <limits>
// Independent compiled representation of conditional model, not source rate source.
static constexpr long double h=6.62607015e-34L, c=299792458.0L;
static constexpr long double e=1.602176634e-19L, kb=1.380649e-23L;
static constexpr std::array<int,10> Ts={15,55,105,255,505,1005,1505,2005,2505,3005};
static constexpr std::array<long double,10> rates={3.99e-20L,2.92e-17L,1.15e-16L,2.74e-16L,3.33e-16L,3.18e-16L,2.85e-16L,2.55e-16L,2.30e-16L,2.08e-16L};
int main(){
    constexpr long double mec=h*c*100.0L*1000.0L/e;
    constexpr long double bo_approx=3.4L+118.48684L*mec;
    constexpr long double spectro=20.95002099384045759056749544382632657967L;
    const long double delta=spectro-bo_approx;
    if(!(bo_approx>18.09L&&bo_approx<18.091L&&delta>2.859L&&delta<2.860L)) return 11;
    long double minbar=1e3L,maxbar=-1e3L;
    for(int i=0;i<9;i++){
        const long double Ti=Ts[i],Tj=Ts[i+1];
        const long double effective=kb*1000.0L/e*(std::log(rates[i+1]/rates[i])+0.5L*std::log(Tj/Ti))/(1.0L/Ti-1.0L/Tj);
        minbar=std::min(minbar,effective);maxbar=std::max(maxbar,effective);
    }
    if(!(minbar<0 && maxbar>26.0L))return 12;
    const long double factor15=std::exp(-(delta*e/1000.0L)/(kb*Ts[0]));
    const long double factor105=std::exp(-(delta*e/1000.0L)/(kb*Ts[2]));
    if(!(factor15>0.109L && factor15<0.110L && factor105>0.729L && factor105<0.730L))return 13;
    // Independent C++ long-double implementation of Maxwell-Laplace SUPPORT,
    // with fixed state-specific cross section and strictly nonnegative E*sigma(E).
    const long double betagap=e/(1000.0L*kb)*(1.0L/15.0L-1.0L/55.0L);
    const long double bound=(std::log(rates[1]/rates[0])+1.5L*std::log(55.0L/15.0L))/betagap;
    const long double rounded=(std::log(2.925e-17L/3.985e-20L)+1.5L*std::log(55.0L/15.0L))/betagap;
    const long double reject_bo=std::exp((bo_approx-bound)*betagap);
    const long double reject_spec=std::exp((spectro-bound)*betagap);
    if(!(bound>15.18630L&&bound<15.18631L&&rounded>15.19157L&&rounded<15.19158L))return 14;
    if(!(reject_bo>5.1244L&&reject_bo<5.1246L&&reject_spec>25.6082L&&reject_spec<25.6085L))return 15;
    std::printf("CPP_MAXWELL_SUPPORT_PASS bound_meV=%.18Lf rounded_bound_meV=%.18Lf bo_violation=%.12Lf spect_violation=%.12Lf\n",bound,rounded,reject_bo,reject_spec);
    std::printf("CPP_PASS bo_approx_meV=%.18Lf delta_spect_minus_bo_meV=%.18Lf minbar=%.8Lf maxbar=%.8Lf ratio15=%.15Lf ratio105=%.15Lf\n",bo_approx,delta,minbar,maxbar,factor15,factor105);
}
