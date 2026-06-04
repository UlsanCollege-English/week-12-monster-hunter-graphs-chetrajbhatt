"""Week 12: Monster Hunter Graphs.

Complete each function using Python 3.11+.

Rules:
- Standard library only.
- Use type hints.
- Keep public function docstrings.
- Run tests with: pytest -q
"""

import heapq


def build_hunter_map(edges: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Build an undirected adjacency list from route pairs."""
    graph: dict[str, list[str]] = {}
 
    for a, b in edges:
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
 
        if b not in graph[a]:
            graph[a].append(b)
        if a not in graph[b]:
            graph[b].append(a)
 
    return graph
 
 
def build_weighted_hunter_map(
    edges: list[tuple[str, str, int]]
) -> dict[str, dict[str, int]]:
    """Build an undirected weighted graph from route triples."""
    graph: dict[str, dict[str, int]] = {}
 
    for a, b, weight in edges:
        if weight <= 0:
            raise ValueError(
                f"Danger score must be a positive integer, got {weight} "
                f"for route ({a!r}, {b!r})."
            )
 
        if a not in graph:
            graph[a] = {}
        if b not in graph:
            graph[b] = {}
 
        if b not in graph[a] or weight < graph[a][b]:
            graph[a][b] = weight
        if a not in graph[b] or weight < graph[b][a]:
            graph[b][a] = weight
 
    return graph
 
 
def map_summary(graph: dict[str, list[str]]) -> dict[str, int]:
    """Return the number of locations and undirected routes."""
    locations = len(graph)
    total_degree = sum(len(neighbors) for neighbors in graph.values())
    routes = total_degree // 2
    return {"locations": locations, "routes": routes}
 
 
def most_connected_location(graph: dict[str, list[str]]) -> str | None:
    """Return the location with the most neighbors."""
    if not graph:
        return None
 
    return max(sorted(graph), key=lambda loc: len(graph[loc]))
 
 
def priority_hunt_order(reports: list[tuple[int, str]]) -> list[str]:
    """Return monster sighting locations from most urgent to least urgent."""
    heap = list(reports)  
    heapq.heapify(heap)
 
    result: list[str] = []
    while heap:
        _, location = heapq.heappop(heap)
        result.append(location)
 
    return result