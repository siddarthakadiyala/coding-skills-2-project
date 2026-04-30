# 🚗 Route Optimization Using Algorithms

> **CCC Algorithm Project** — Demonstrating Greedy & Dynamic Programming through City Route Optimization


| Registration No. | Name |
|------|------------------|
|AP24110011332  |	P.Lalith |
|AP24110011060	| K.V.Siddharth |
|AP24110011344	| SK.Mubhasir |
|AP24110011503 	| CH.Ashish |
|AP24110010723	| ATHIPARAMPIL JOEL SABU |
---

## 📌 Project Overview

This project models a **city road network as a weighted graph** and solves two classic route-optimization problems:

| Problem | Approach | Algorithm |
|---|---|---|
| Build cheapest road network | **Greedy** | Prim's MST, Kruskal's MST |
| Find shortest travel path | **Dynamic Programming** | Dijkstra, Bellman-Ford, Floyd-Warshall |

---

## 📁 File Structure

```
route_optimizer/
├── main.py      ← Entry point, interactive menu
├── graph.py     ← Graph data structure (adjacency list)
├── greedy.py    ← Greedy algorithms (Prim's + Kruskal's)
├── dp.py        ← DP algorithms (Dijkstra + Bellman-Ford + Floyd-Warshall)
└── README.md    ← This file
```

---

## 🧠 Algorithms Explained

### 🟢 Greedy Algorithms

#### 1. Prim's Algorithm — Minimum Spanning Tree
- **Idea:** Start from any node. At every step, greedily pick the **cheapest edge** connecting the visited set to an unvisited node.
- **Why Greedy?** The locally optimal choice (cheapest edge) always leads to a globally optimal MST.
- **Complexity:** O(E log V)

#### 2. Kruskal's Algorithm — Minimum Spanning Tree
- **Idea:** Sort all edges by weight. Greedily add the cheapest edge that **doesn't form a cycle** (detected via Union-Find).
- **Why Greedy?** Always choosing the globally smallest safe edge produces the MST.
- **Complexity:** O(E log E)

---

### 🔵 Dynamic Programming Algorithms

#### 3. Dijkstra's Algorithm — Single-Source Shortest Path
- **Idea:** Maintain a `dist[]` table. Relax edges using the recurrence:  
  `dist[v] = min(dist[v], dist[u] + weight(u,v))`
- **DP Property:** Optimal Substructure — shortest path to `v` through `u` requires the shortest path to `u`.
- **Complexity:** O((V + E) log V)

#### 4. Bellman-Ford Algorithm — Shortest Path (with Negative Weights)
- **Idea:** Repeat edge relaxation **V-1 times**. After `k` iterations, `dist[v]` = shortest path using ≤ k edges.
- **DP Property:** Each iteration builds on the previous — classic DP recurrence over number of edges.
- **Bonus:** Detects negative-weight cycles.
- **Complexity:** O(V × E)

#### 5. Floyd-Warshall — All-Pairs Shortest Path
- **Idea:** DP over intermediate nodes:  
  `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`
- **DP Property:** Uses results of smaller sub-problems to solve larger ones.
- **Complexity:** O(V³)

---

## 🗺️ Sample City Graph

```
Airport ─(4)─ BusStand ─(8)─ Downtown
  │                │               │
 (8)             (11)             (2)
  │                │               │
CityCenter ─(7)─ EastMarket ─(6)─ Fort ─(2)─ EndPoint
     └──────(1)──────────────────────┘
```

---

## ▶️ How to Run

**Requirements:** Python 3.7+ (no external libraries needed)

```bash
# Clone the repo
git clone https://github.com/<your-username>/route-optimizer.git
cd route-optimizer

# Run the program
python main.py
```

### Menu Options
```
1. View Graph              → See the city road network
2. Prim's MST             → Greedy: minimum spanning tree
3. Kruskal's MST          → Greedy: MST via Union-Find
4. Dijkstra               → DP: shortest path from source
5. Bellman-Ford           → DP: shortest path (negative weights)
6. Floyd-Warshall         → DP: all-pairs shortest paths
7. Run ALL (Demo Mode)    → See everything at once
8. Custom Graph Input     → Build and test your own graph
```

---

## 📊 Algorithm Comparison

| Algorithm | Type | Time | Negative Weights | Use Case |
|---|---|---|---|---|
| Prim's | Greedy | O(E log V) | No | Minimum network cost |
| Kruskal's | Greedy | O(E log E) | No | Minimum network cost |
| Dijkstra | DP | O((V+E) log V) | No | Fastest route, GPS |
| Bellman-Ford | DP | O(VE) | ✅ Yes | Finance, routing |
| Floyd-Warshall | DP | O(V³) | ✅ Yes | All-pairs distances |

---

## 👥 Team

| Name | Role |
|---|---|
| Member 1 | Graph Design & Greedy Algorithms |
| Member 2 | DP Algorithms |
| Member 3 | Testing & Documentation |

---

## 📚 References

- Introduction to Algorithms (CLRS) — Cormen et al.
- GeeksForGeeks — Graph Algorithms
- Python Documentation — heapq module
