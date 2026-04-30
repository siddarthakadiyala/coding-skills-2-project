# main.py - Route Optimization Project (Main Entry Point)
# CCC Algorithm Project
# Algorithms: Greedy (Prim's, Kruskal's) + DP (Dijkstra, Bellman-Ford, Floyd-Warshall)

from graph import Graph
from greedy import prims_mst, kruskals_mst
from dp import dijkstra, bellman_ford, floyd_warshall


BANNER = """
╔══════════════════════════════════════════════════════╗
║      🚗  ROUTE OPTIMIZATION USING ALGORITHMS  🚗     ║
║                  CCC — Algorithm Project             ║
╠══════════════════════════════════════════════════════╣
║  Algorithms Demonstrated:                            ║
║  [GREEDY]  1. Prim's MST                             ║
║  [GREEDY]  2. Kruskal's MST                          ║
║  [DP    ]  3. Dijkstra's Shortest Path               ║
║  [DP    ]  4. Bellman-Ford Shortest Path             ║
║  [DP    ]  5. Floyd-Warshall All-Pairs SP            ║
╚══════════════════════════════════════════════════════╝
"""

MENU = """
  ┌────────────────────────────────────────┐
  │             MAIN MENU                  │
  ├────────────────────────────────────────┤
  │  1. View Graph (City Road Network)     │
  │  2. Greedy → Prim's MST               │
  │  3. Greedy → Kruskal's MST            │
  │  4. DP     → Dijkstra Shortest Path   │
  │  5. DP     → Bellman-Ford             │
  │  6. DP     → Floyd-Warshall (All)     │
  │  7. Run ALL Algorithms (Demo Mode)    │
  │  8. Custom Graph Input                │
  │  0. Exit                              │
  └────────────────────────────────────────┘
"""


def get_source_node(graph: Graph) -> str:
    """Prompt user to pick a source node."""
    nodes = sorted(graph.nodes)
    print("\n  Available nodes:")
    for i, n in enumerate(nodes, 1):
        print(f"    {i}. {n}")
    while True:
        choice = input("  Enter node name (or number): ").strip()
        if choice in nodes:
            return choice
        if choice.isdigit() and 1 <= int(choice) <= len(nodes):
            return nodes[int(choice) - 1]
        print("  ⚠️  Invalid choice. Try again.")


def custom_graph_input() -> Graph:
    """Let the user build their own graph interactively."""
    print("\n  ── Custom Graph Builder ──")
    print("  Enter edges as:  NodeA NodeB Weight  (type 'done' to finish)")
    g = Graph()
    while True:
        line = input("  Edge: ").strip()
        if line.lower() == "done":
            break
        parts = line.split()
        if len(parts) != 3:
            print("  ⚠️  Format: NodeA NodeB Weight")
            continue
        try:
            u, v, w = parts[0], parts[1], int(parts[2])
            g.add_edge(u, v, w)
            print(f"  ✅  Added edge: {u} ──({w})──▶ {v}")
        except ValueError:
            print("  ⚠️  Weight must be an integer.")
    if not g.nodes:
        print("  ⚠️  No edges entered. Using sample graph instead.")
        return Graph.sample_city_graph()
    return g


def run_all(graph: Graph):
    """Demo mode — run every algorithm in sequence."""
    print("\n  🚀  Running ALL algorithms on the city graph...\n")
    prims_mst(graph, "Airport")
    kruskals_mst(graph)
    dijkstra(graph, "Airport")
    bellman_ford(graph, "Airport")
    floyd_warshall(graph)


def main():
    print(BANNER)
    graph = Graph.sample_city_graph()   # default graph

    while True:
        print(MENU)
        choice = input("  Select option: ").strip()

        if choice == "0":
            print("\n  👋  Goodbye!\n")
            break

        elif choice == "1":
            graph.display()

        elif choice == "2":
            src = get_source_node(graph)
            prims_mst(graph, src)

        elif choice == "3":
            kruskals_mst(graph)

        elif choice == "4":
            src = get_source_node(graph)
            dijkstra(graph, src)

        elif choice == "5":
            src = get_source_node(graph)
            bellman_ford(graph, src)

        elif choice == "6":
            floyd_warshall(graph)

        elif choice == "7":
            run_all(graph)

        elif choice == "8":
            graph = custom_graph_input()
            print("\n  ✅  Custom graph loaded!")
            graph.display()

        else:
            print("  ⚠️  Invalid option. Please try again.")


if __name__ == "__main__":
    main()
