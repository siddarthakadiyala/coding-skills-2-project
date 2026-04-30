
import heapq
from graph import Graph

INF = float('inf')


# ──────────────────────────────────────────────
# 1. DIJKSTRA'S ALGORITHM
# ──────────────────────────────────────────────

def dijkstra(graph: Graph, source: str):
    """
    Dijkstra's Algorithm – Shortest path using DP + priority queue.

    DP Principle (Optimal Substructure):
        dist[v] = dist[u] + weight(u, v)
        If the shortest path to v goes through u, then the prefix path
        to u must also be the shortest path to u.  Each sub-problem
        (shortest distance to a node) is solved once and stored.

    Time Complexity : O((V + E) log V)
    Space Complexity: O(V)

    Returns:
        dist      – dict of shortest distances from source
        prev      – dict for path reconstruction
    """
    print("\n" + "=" * 55)
    print("  🗺️   DIJKSTRA'S ALGORITHM  –  Shortest Path (DP)")
    print("=" * 55)
    print(f"  Source : {source}")
    print(f"  DP rule: dist[v] = min(dist[v], dist[u] + w(u,v))")
    print("=" * 55)

    # Ensure all nodes reachable from the adjacency list are included.
    nodes = set(graph.nodes)
    for u, neighbors in graph.adjacency_list.items():
        nodes.add(u)
        for v, _ in neighbors:
            nodes.add(v)

    if source not in nodes:
        raise ValueError(f"Source node {source!r} is not in the graph.")

    dist = {node: INF for node in nodes}
    prev = {node: None for node in nodes}
    dist[source] = 0

    # Min-heap: (distance, node)
    heap = [(0, source)]

    visited = set()
    step    = 1

    while heap:
        d, u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)

        for v, w in graph.get_neighbors(u):
            new_dist = dist[u] + w
            if new_dist < dist[v]:              # DP relaxation
                dist[v] = new_dist
                prev[v] = u
                heapq.heappush(heap, (new_dist, v))
                print(f"  Step {step:>2}: Relax  {u:12} ──({w:>2})──▶ {v:12}  dist={new_dist}")
                step += 1

    print("-" * 55)
    print(f"\n  📊 Shortest distances from '{source}':")
    for node in sorted(dist):
        d = dist[node]
        path = _reconstruct_path(prev, source, node)
        dist_str = str(d) if d != INF else "∞ (unreachable)"
        print(f"    {node:15} : {dist_str:>5}   path: {' → '.join(path)}")
    print("=" * 55)

    return dist, prev


# ──────────────────────────────────────────────
# 2. BELLMAN-FORD ALGORITHM
# ──────────────────────────────────────────────

def bellman_ford(graph: Graph, source: str):
    """
    Bellman-Ford Algorithm – Shortest path supporting negative weights.

    DP Principle:
        Relax ALL edges (V-1) times.  After k iterations, dist[v] holds
        the shortest path using at most k edges — a classic DP recurrence.

        Recurrence: dist_k[v] = min over all u of (dist_{k-1}[u] + w(u,v))

    Also detects negative-weight cycles (run one more iteration).

    Time Complexity : O(V × E)
    Space Complexity: O(V)

    Returns:
        dist              – dict of shortest distances
        prev              – dict for path reconstruction
        has_negative_cycle – bool
    """
    print("\n" + "=" * 55)
    print("  ⚡  BELLMAN-FORD ALGORITHM  –  Shortest Path (DP)")
    print("=" * 55)
    print(f"  Source      : {source}")
    print(f"  DP Iterations: V-1 = {len(graph.nodes) - 1}")
    print(f"  DP rule     : dist[v] = min(dist[u] + w(u,v))  ∀ edges")
    print("=" * 55)

    dist = {node: INF for node in graph.nodes}
    prev = {node: None for node in graph.nodes}
    dist[source] = 0

    edges = graph.get_edges()
    V     = len(graph.nodes)

    for iteration in range(V - 1):
        updated = False
        for u, v, w in edges:
            # Relax edge u → v
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                updated = True
            # Relax edge v → u (undirected)
            if dist[v] != INF and dist[v] + w < dist[u]:
                dist[u] = dist[v] + w
                prev[u] = v
                updated = True

        print(f"  Iteration {iteration + 1:>2}: {'changes made' if updated else 'no changes (converged early)'}")
        if not updated:
            break

    # Negative-cycle detection (V-th iteration)
    has_negative_cycle = False
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            has_negative_cycle = True
            break

    print("-" * 55)
    if has_negative_cycle:
        print("  ⚠️  Negative-weight cycle DETECTED!")
    else:
        print(f"\n  📊 Shortest distances from '{source}':")
        for node in sorted(dist):
            d    = dist[node]
            path = _reconstruct_path(prev, source, node)
            dist_str = str(d) if d != INF else "∞"
            print(f"    {node:15} : {dist_str:>5}   path: {' → '.join(path)}")
    print("=" * 55)

    return dist, prev, has_negative_cycle


# ──────────────────────────────────────────────
# 3. FLOYD-WARSHALL  (All-Pairs Shortest Path — Pure DP)
# ──────────────────────────────────────────────

def floyd_warshall(graph: Graph):
    """
    Floyd-Warshall – All-pairs shortest path using pure DP.

    DP Recurrence:
        dist[i][j][k] = min(
            dist[i][j][k-1],              # don't use node k as intermediate
            dist[i][k][k-1] + dist[k][j][k-1]   # use node k
        )
    We use a 2-D table (space-optimised) updating in place.

    Time Complexity : O(V³)
    Space Complexity: O(V²)
    """
    print("\n" + "=" * 55)
    print("  🔄  FLOYD-WARSHALL  –  All-Pairs Shortest Path (DP)")
    print("=" * 55)
    print("  DP rule: dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])")
    print("=" * 55)

    nodes     = sorted(graph.nodes)
    n         = len(nodes)
    idx       = {node: i for i, node in enumerate(nodes)}

    # Initialize distance matrix
    dist = [[INF] * n for _ in range(n)]
    next_node = [[None] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for u, v, w in graph.get_edges():
        i, j = idx[u], idx[v]
        dist[i][j] = w
        dist[j][i] = w
        next_node[i][j] = v
        next_node[j][i] = u

    # DP main loop
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    print(f"\n  📊 All-Pairs Shortest Distance Matrix (first 5 nodes):")
    show = nodes[:5]
    header = f"  {'':15}" + "".join(f"{n:>12}" for n in show)
    print(header)
    for u in show:
        row = f"  {u:15}"
        for v in show:
            d = dist[idx[u]][idx[v]]
            row += f"{'∞':>12}" if d == INF else f"{d:>12}"
        print(row)
    print("=" * 55)

    return dist, nodes, next_node


# ──────────────────────────────────────────────
# HELPER
# ──────────────────────────────────────────────

def _reconstruct_path(prev: dict, source: str, target: str):
    """Reconstruct shortest path from source to target using prev dict."""
    path = []
    cur  = target
    while cur is not None:
        path.append(cur)
        if cur == source:
            break
        cur = prev[cur]
    path.reverse()
    if path and path[0] == source:
        return path
    return [target]   # unreachable
