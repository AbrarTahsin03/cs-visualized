# CS Visualized

Runnable code for every [CS Visualized](https://www.youtube.com/@CSVisualizedShorts) video. Every race, benchmark and number on screen comes from this code, so you can rerun it, change it, and try to break it.

| # | Video | Code | Run |
|---|-------|------|-----|
| 1 | [Dijkstra vs A*: Same Shortest Path, 6× Less Work](https://youtu.be/KavxrUy_vJg) | [`01-dijkstra-vs-astar/race.py`](01-dijkstra-vs-astar/race.py) | `python race.py` |
| 2 | [Why Hash Tables Are O(1), and How to Make Them 1,000× Slower](https://youtu.be/SHXTxKDBHAA) | [`02-hash-tables/anti_hash.cpp`](02-hash-tables/anti_hash.cpp) | `g++ -O2 -o anti_hash anti_hash.cpp && ./anti_hash 200000 172933` |

No dependencies beyond Python 3 and a C++17 compiler (GCC for the hash-table attack: it targets GCC's libstdc++).

## 01 — Dijkstra vs A*

Expected output:

```
city  Dijkstra       checked   846  path 54
city  A*             checked   142  path 54
city  A* with 3 x h  checked    80  path 60
trap  Dijkstra       checked  1325  path 58
trap  A*             checked   318  path 58
```

Challenge: change the `3` in the weighted A* run to `1.2`. Does A* still find the 54-step path? Try other values of `SEED` too.

## 02 — Hash tables

Measured in the video (g++ 13.3, -O2): random keys 0.019 s, crafted keys 31.4 s, crafted keys with `custom_hash` 0.03 s. Your numbers will differ by machine; the ratio is the point.
