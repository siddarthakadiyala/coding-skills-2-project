# graph.py - Graph Data Structure for Route Optimization
# CCC Algorithm Project

from collections import defaultdict

class Graph:
    """
    Weighted undirected/directed graph using adjacency list representation.
    Supports both Greedy and DP algorithm demonstrations.
    """

    def __init__(self, directed=False):
        self.adjacency_list = defaultdict(list)  # {node: [(neighbor, weight), ...]}
        self.nodes = set()
        self.directed = directed

    def add_node(self, node):
        """Add a node to the graph."""
        self.nodes.add(node)
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, u, v, weight):
        """Add a weighted edge between nodes u and v."""
        self.nodes.add(u)
        self.nodes.add(v)
        self.adjacency_list[u].append((v, weight))
        if not self.directed:
            self.adjacency_list[v].append((u, weight))

    def get_edges(self):
        """Return all unique edges as (u, v, weight) tuples."""
        edges = []
        seen = set()
        for u in self.adjacency_list:
            for v, w in self.adjacency_list[u]:
                edge = (min(u, v), max(u, v), w)
                if edge not in seen:
                    edges.append((u, v, w))
                    seen.add(edge)
        return edges

    def get_neighbors(self, node):
        """Return neighbors of a node."""
        return self.adjacency_list.get(node, [])

    def display(self):
        """Display the graph's adjacency list."""
        print("\n📍 Graph Adjacency List:")
        print("-" * 40)
        for node in sorted(self.nodes):
            neighbors = self.adjacency_list[node]
            conn = ", ".join(f"{v}(w={w})" for v, w in neighbors)
            print(f"  {node} → {conn if conn else 'No connections'}")
        print("-" * 40)

    @staticmethod
    def sample_city_graph():
        """
        Returns a sample city-road network graph.
        Cities: A (Airport), B (Bus Stand), C (City Center),
                D (Downtown), E (East Market), F (Fort)
        """
        g = Graph()
        edges = [
            ("Airport",     "BusStand",   4),
            ("Airport",     "CityCenter",  8),
            ("BusStand",    "CityCenter",  11),
            ("BusStand",    "Downtown",    8),
            ("CityCenter",  "EastMarket",  7),
            ("CityCenter",  "Fort",        1),
            ("Downtown",    "EastMarket",  2),
            ("Downtown",    "Fort",        6),
            ("EastMarket",  "Fort",        6),
            ("EastMarket",  "EndPoint",    9),
            ("Fort",        "EndPoint",    2),
        ]
        for u, v, w in edges:
            g.add_edge(u, v, w)
        return g
