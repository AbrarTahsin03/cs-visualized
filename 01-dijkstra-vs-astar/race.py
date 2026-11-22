"""Dijkstra vs A* on a grid - the exact simulations from the CS Visualized video.

Run:  python race.py
Prints squares checked and path length for each race. Change SEED or the maps and try to break A*.
"""
import heapq, random

C, R = 48, 30      # grid size (columns, rows)
SEED = 12          # the city map used in the video

def make_map(kind, seed=SEED):
    g = [[0] * C for _ in range(R)]
    rnd = random.Random(seed)
    if kind == 'city':                       # random rectangular "buildings"
        for _ in range(42):
            w, h = rnd.randint(2, 6), rnd.randint(2, 5)
            x, y = rnd.randint(4, C - 8), rnd.randint(0, R - h)
            for yy in range(y, y + h):
                for xx in range(x, x + w):
                    g[yy][xx] = 1
        s, t = (2, 15), (45, 14)
    else:                                    # U-shaped trap opening away from the goal
        for y in range(7, 23): g[y][24] = 1
        for x in range(10, 25): g[7][x] = 1; g[22][x] = 1
        s, t = (18, 15), (42, 15)
    for x, y in (s, t): g[y][x] = 0
    return g, s, t

def search(g, s, t, w=0.0):
    """w = 0 -> Dijkstra; w = 1 -> A* with Manhattan distance; w > 1 -> weighted A* (overestimates)."""
    h = lambda p: abs(p[0] - t[0]) + abs(p[1] - t[1])
    dist, par, closed, order = {s: 0}, {}, set(), []
    pq = [(w * h(s), 0, s)]                  # (f, -g for tie-breaking, node)
    while pq:
        _, _, u = heapq.heappop(pq)
        if u in closed: continue             # stale entry - skip it
        closed.add(u); order.append(u)
        if u == t: break
        x, y = u
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            v = (x + dx, y + dy)
            if 0 <= v[0] < C and 0 <= v[1] < R and not g[v[1]][v[0]] and v not in closed:
                nd = dist[u] + 1
                if nd < dist.get(v, float('inf')):
                    dist[v], par[v] = nd, u
                    heapq.heappush(pq, (nd + w * h(v), -nd, v))
    return len(order), dist.get(t)

if __name__ == '__main__':
    g, s, t = make_map('city')
    for name, w in (('Dijkstra', 0), ('A*', 1), ('A* with 3 x h', 3)):
        checked, length = search(g, s, t, w)
        print(f'city  {name:14s} checked {checked:5d}  path {length}')
    g, s, t = make_map('trap')
    for name, w in (('Dijkstra', 0), ('A*', 1)):
        checked, length = search(g, s, t, w)
        print(f'trap  {name:14s} checked {checked:5d}  path {length}')
