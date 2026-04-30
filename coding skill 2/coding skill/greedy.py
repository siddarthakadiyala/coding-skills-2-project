# greedy.py - Greedy Algorithms for Route Optimization
# CCC Algorithm Project
#
# Algorithms implemented:
#   1. Prim's Algorithm   - Minimum Spanning Tree (MST)
#   2. Kruskal's Algorithm - MST using Union-Find

import heapq
from graph import Graph


# ──────────────────────────────────────────────
# 1. PRIM'S ALGORITHM  (Greedy MST)
# ──────────────────────────────────────────────

def prims_mst(graph: Graph, start_node: str):
    
    print("\n" + "=" * 55)
    print("  🌿  PRIM'S ALGORITHM  –  Minimum Spanning Tree")
    print("=" * 55)
    print(f"  Start node : {start_node}")
    print(f"  Greedy rule: Always pick the minimum-weight edge")
    print("=" * 55)

    visited   = set()
    mst_edges = []
    total_cost = 0

    # Min-heap: (weight, from_node, to_node)
    min_heap = [(0, start_node, start_node)]

    step = 1
    while min_heap and len(visited) < len(graph.nodes):
        weight, from_node, to_node = heapq.heappop(min_heap)

        if to_node in visited:
            continue

        visited.add(to_node)

        if from_node != to_node:          # skip the dummy start edge
            mst_edges.append((from_node, to_node, weight))
            total_cost += weight
            print(f"  Step {step:>2}: Add edge  {from_node:12} ──({weight:>2})──▶ {to_node}")
            step += 1

        # Push all edges from the newly visited node
        for neighbor, edge_weight in graph.get_neighbors(to_node):
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, to_node, neighbor))

    print("-" * 55)
    print(f"  ✅  MST Total Cost : {total_cost}")
    print(f"  ✅  Edges in MST   : {len(mst_edges)}")
    print("=" * 55)
    return mst_edges, total_cost


# ──────────────────────────────────────────────
# 2. KRUSKAL'S ALGORITHM  (Greedy MST with Union-Find)
# ──────────────────────────────────────────────

class UnionFind:
    """Disjoint-Set (Union-Find) with path compression & union by rank."""

    def __init__(self, nodes):
        self.parent = {n: n for n in nodes}
        self.rank   = {n: 0  for n in nodes}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])   # path compression
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False   # already connected → would form a cycle
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True


def kruskals_mst(graph: Graph):
    """
    Kruskal's Algorithm – Greedy approach using Union-Find.

    Strategy (Greedy):
        Sort ALL edges by weight, then greedily add the cheapest edge
        that does NOT create a cycle (detected via Union-Find).

    Time Complexity : O(E log E)
    Space Complexity: O(V)

    Returns:
        mst_edges  – list of (u, v, weight) tuples in the MST
        total_cost – sum of all edge weights in the MST
    """
    print("\n" + "=" * 55)
    print("  🔗  KRUSKAL'S ALGORITHM  –  Minimum Spanning Tree")
    print("=" * 55)
    print("  Greedy rule: Sort edges → pick cheapest, skip cycles")
    print("=" * 55)

    edges = sorted(graph.get_edges(), key=lambda e: e[2])
    uf    = UnionFind(graph.nodes)

    mst_edges  = []
    total_cost = 0
    step       = 1

    for u, v, w in edges:
        if uf.union(u, v):
            mst_edges.append((u, v, w))
            total_cost += w
            print(f"  Step {step:>2}: Accept  {u:12} ──({w:>2})──▶ {v}")
            step += 1
        else:
            print(f"         Skip   {u:12} ──({w:>2})──▶ {v}  [cycle]")

    print("-" * 55)
    print(f"  ✅  MST Total Cost : {total_cost}")
    print(f"  ✅  Edges in MST   : {len(mst_edges)}")
    print("=" * 55)
    return mst_edges, total_cost
