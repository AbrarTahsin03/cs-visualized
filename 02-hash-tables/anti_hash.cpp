// Hash table attack benchmark from the CS Visualized video "Why Hash Tables Are O(1), and When They Aren't".
// Build: g++ -O2 -o anti_hash anti_hash.cpp      Run: ./anti_hash 200000 172933
// Inserts n keys into std::unordered_map three ways: random keys, multiples of prime P (attack), and the
// same attack keys with a randomized splitmix64 hash (fix). With GCC's libstdc++, P = 172933 is a bucket
// count the table passes through at this size, so all attack keys land in one bucket.
// Measured in the video (g++ 13.3, -O2): random 0.019 s, attack 31.4 s, attack + custom_hash 0.03 s.
#include <bits/stdc++.h>
using namespace std;

struct custom_hash {
    static uint64_t splitmix64(uint64_t x) {
        x += 0x9e3779b97f4a7c15;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
        x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
        return x ^ (x >> 31);
    }
    size_t operator()(uint64_t x) const {
        static const uint64_t SEED = chrono::steady_clock::now().time_since_epoch().count();
        return splitmix64(x + SEED);
    }
};

template <class Map> double seconds(const vector<long long>& keys) {
    auto t0 = chrono::steady_clock::now();
    Map m;
    for (long long k : keys) m[k]++;
    return chrono::duration<double>(chrono::steady_clock::now() - t0).count();
}

int main(int argc, char** argv) {
    int n = argc > 1 ? atoi(argv[1]) : 200000;
    long long P = argc > 2 ? atoll(argv[2]) : 172933;
    vector<long long> rnd(n), bad(n);
    mt19937_64 gen(1);
    for (int i = 0; i < n; i++) { rnd[i] = gen() % 1000000000000LL; bad[i] = (long long)(i + 1) * P; }
    printf("n=%d  P=%lld\n", n, P);
    printf("random keys:              %.4f s\n", seconds<unordered_map<long long, int>>(rnd));
    printf("crafted keys:             %.4f s\n", seconds<unordered_map<long long, int>>(bad));
    printf("crafted keys + fix:       %.4f s\n", seconds<unordered_map<long long, int, custom_hash>>(bad));
}
