# CS Visualized

Runnable code for every [CS Visualized](https://www.youtube.com/@CSVisualizedShorts) video. Every race and number on screen comes from this code, so you can rerun it, change it, and try to break it.

| # | Video | Code |
|---|-------|------|
| 1 | [Dijkstra vs A*: Same Shortest Path, 6× Less Work](https://youtu.be/wsePG5K6MWo) | [`01-dijkstra-vs-astar/race.py`](01-dijkstra-vs-astar/race.py) |

## Run

```bash
python 01-dijkstra-vs-astar/race.py
```

No dependencies beyond Python 3.

Expected output:

```
city  Dijkstra       checked   846  path 54
city  A*             checked   142  path 54
city  A* with 3 x h  checked    80  path 60
trap  Dijkstra       checked  1325  path 58
trap  A*             checked   318  path 58
```

## Challenge

Change the `3` in the weighted A* run to `1.2`. Does A* still find the 54-step path? Try other values of `SEED` too.
