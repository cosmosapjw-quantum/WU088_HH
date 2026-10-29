// C++20 independent integer-scaled exact transcription check, not separate author.
// Unit = 1e-10 eV. Source values copied from the two cited primary publications.
#include <cstdint>
#include <iostream>
constexpr std::int64_t HD00=2344204966LL,HD02=2675344527LL;
constexpr std::int64_t H200=2702721432LL,H201=2849632856LL;
constexpr std::int64_t ground=395000000LL,IP=37000000LL;
constexpr std::int64_t neutral=H201-HD02;
constexpr std::int64_t crossA=ground-(HD02-HD00)+(H201-H200);
constexpr std::int64_t crossB=neutral+IP;
static_assert(neutral==174288329LL);
static_assert(crossA==210771863LL);
static_assert(crossB==211288329LL);
static_assert(crossB-crossA==516466LL);
static_assert(crossB-crossA==(H200-HD00)+IP-ground);
int main(){std::cout<<"CPP_PASS neutral="<<neutral<<" crossA="<<crossA<<" crossB="<<crossB<<" difference="<<crossB-crossA<<" (1e-10 eV)\n";}
