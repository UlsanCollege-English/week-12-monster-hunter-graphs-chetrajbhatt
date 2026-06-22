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
            raise ValueError("Weight must be positive")

        if a not in graph:
            graph[a] = {}
        if b not in graph:
            graph[b] = {}

        if b not in graph[a] or weight < graph[a][b]:
            graph[a][b] = weight
            graph[b][a] = weight

    return graph


def map_summary(graph: dict[str, list[str]]) -> dict[str, int]:
    """Return the number of locations and undirected routes."""
    locations = len(graph)
    routes = sum(len(neighbors) for neighbors in graph.values()) // 2

    return {
        "locations": locations,
        "routes": routes,
    }


def most_connected_location(graph: dict[str, list[str]]) -> str | None:
    """Return the location with the most neighbors."""
    if not graph:
        return None

    return min(
        graph,
        key=lambda location: (-len(graph[location]), location)
    )


def priority_hunt_order(reports: list[tuple[int, str]]) -> list[str]:
    """Return monster sighting locations from most urgent to least urgent."""
    heap = reports.copy()
    heapq.heapify(heap)

    result: list[str] = []

    while heap:
        _, location = heapq.heappop(heap)
        result.append(location)

    return result