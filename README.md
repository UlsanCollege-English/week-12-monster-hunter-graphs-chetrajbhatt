[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/80z-ZS6n)
# Week 12: Monster Hunter Graphs

## Student

Name: Chet Raj Bhatt

Student ID: 2412081

## Summary

This assignment builds a graph toolkit themed around a monster-hunting scenario. Each node in the graph represents a monster sighting location such as "Old Theater" or "Train Station", and each edge represents a two-way route connecting two locations. Two graph variants are implemented: an unweighted adjacency-list graph and a weighted graph where each route carries a positive danger score. Helper utilities compute graph statistics (location and route counts, the most-connected hub), and a priority queue function uses Python's `heapq` module to rank incoming monster reports by urgency. The hardest function was `most_connected_location` because of the tie-breaking rule — a plain `max()` call does not guarantee alphabetical order when multiple nodes share the same degree, so the keys must be pre-sorted before calling `max()`.

## Approach

- `build_hunter_map`: Iterate over each edge pair `(a, b)`, ensure both keys exist in the dict, then append each direction only if the neighbour is not already listed — preventing duplicates while keeping O(1) average insertion per edge.
- `build_weighted_hunter_map`: Validate the danger score immediately and raise `ValueError` for any value ≤ 0. Use a nested dict `graph[a][b] = weight` and overwrite only when a duplicate route arrives with a strictly lower score, keeping the minimum.
- `map_summary`: Use `len(graph)` for the location count. Sum all neighbour-list lengths across every node and divide by 2 — each undirected edge appears in exactly two adjacency lists, so halving gives the true route count.
- `most_connected_location`: Guard for an empty graph and return `None`. Pre-sort keys with `sorted(graph)` so they are in alphabetical order, then pass the sorted list to `max()` with `key=lambda loc: len(graph[loc])`. When two nodes tie on degree, `max()` naturally keeps the first (alphabetically earliest) one it sees.
- `priority_hunt_order`: Copy the input list so the caller's data is not mutated. Call `heapq.heapify()` on the copy in O(n), then repeatedly call `heapq.heappop()` to extract `(priority, location)` tuples in ascending priority order, collecting only the location strings.

## Complexity

### `build_hunter_map`

- Time: O(E)
- Space: O(V + E)
- Why: One pass over E edges; the graph stores V nodes and 2E directed neighbour entries in total.

### `build_weighted_hunter_map`

- Time: O(E)
- Space: O(V + E)
- Why: Same single pass as the unweighted version; nested dict lookup and insert are O(1) average.

### `map_summary`

- Time: O(V)
- Space: O(1)
- Why: Summing neighbour-list lengths visits each node once; no additional data structures are allocated.

### `most_connected_location`

- Time: O(V log V)
- Space: O(V)
- Why: `sorted(graph)` is O(V log V); the subsequent `max()` scan is O(V). The sort dominates.

### `priority_hunt_order`

- Time: O(n log n)
- Space: O(n)
- Why: `heapify` runs in O(n); each of the n `heappop` calls costs O(log n), giving O(n log n) overall.

## Edge-Case Checklist

- [x] Empty graph
- [x] One route
- [x] Duplicate routes
- [x] Disconnected locations
- [x] Tie for most connected location
- [x] Positive weighted routes
- [x] Invalid zero or negative danger score
- [x] Empty priority report list

## Tests

Paste the result of your test run.

```bash
pytest -q
```

Result:

```text
test_hunter_graphs.py::TestBuildHunterMap::test_empty PASSED
test_hunter_graphs.py::TestBuildHunterMap::test_single_route PASSED
test_hunter_graphs.py::TestBuildHunterMap::test_two_routes PASSED
test_hunter_graphs.py::TestBuildHunterMap::test_duplicate_route_no_duplication PASSED
test_hunter_graphs.py::TestBuildHunterMap::test_all_locations_present PASSED
test_hunter_graphs.py::TestBuildHunterMap::test_disconnected_locations PASSED
test_hunter_graphs.py::TestBuildWeightedHunterMap::test_empty PASSED
test_hunter_graphs.py::TestBuildWeightedHunterMap::test_single_route PASSED
test_hunter_graphs.py::TestBuildWeightedHunterMap::test_zero_score_raises PASSED
test_hunter_graphs.py::TestBuildWeightedHunterMap::test_negative_score_raises PASSED
test_hunter_graphs.py::TestBuildWeightedHunterMap::test_duplicate_keeps_lowest PASSED
test_hunter_graphs.py::TestBuildWeightedHunterMap::test_multiple_routes PASSED
test_hunter_graphs.py::TestMapSummary::test_empty PASSED
test_hunter_graphs.py::TestMapSummary::test_example_from_docstring PASSED
test_hunter_graphs.py::TestMapSummary::test_one_route PASSED
test_hunter_graphs.py::TestMapSummary::test_triangle PASSED
test_hunter_graphs.py::TestMapSummary::test_disconnected PASSED
test_hunter_graphs.py::TestMostConnectedLocation::test_empty PASSED
test_hunter_graphs.py::TestMostConnectedLocation::test_single_node PASSED
test_hunter_graphs.py::TestMostConnectedLocation::test_clear_winner PASSED
test_hunter_graphs.py::TestMostConnectedLocation::test_tie_alphabetical PASSED
test_hunter_graphs.py::TestMostConnectedLocation::test_tie_between_equals PASSED
test_hunter_graphs.py::TestMostConnectedLocation::test_alpha_tie_resolution PASSED
test_hunter_graphs.py::TestPriorityHuntOrder::test_empty PASSED
test_hunter_graphs.py::TestPriorityHuntOrder::test_single PASSED
test_hunter_graphs.py::TestPriorityHuntOrder::test_ordered_already PASSED
test_hunter_graphs.py::TestPriorityHuntOrder::test_reverse_order PASSED
test_hunter_graphs.py::TestPriorityHuntOrder::test_does_not_mutate_input PASSED
test_hunter_graphs.py::TestPriorityHuntOrder::test_uses_heapq PASSED
29 passed in 0.06s
```

## Assistance & Sources

AI used? Yes

If yes, what did it help with?

- Claude (claude.ai) helped implement the five functions and generate the test suite.
- All logic was reviewed and understood before submission.

Other sources used:

- Course lecture notes on graphs and heaps
- Python 3.11 documentation for `heapq`: https://docs.python.org/3/library/heapq.html
