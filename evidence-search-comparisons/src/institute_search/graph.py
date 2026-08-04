from __future__ import annotations

from pathlib import Path
from typing import Any

import networkx as nx


class EvidenceGraph:
    """Canonical directed graph. The dendrogram is only a projection."""

    def __init__(self) -> None:
        self.g = nx.DiGraph()

    def add_record(self, record_id: str, **attrs: Any) -> None:
        self.g.add_node(record_id, **attrs)

    def add_discovery_edge(self, source: str, target: str, **attrs: Any) -> None:
        self.g.add_edge(source, target, **attrs)

    def prune(self, record_id: str, reason: str) -> None:
        self.g.nodes[record_id]["pruned"] = True
        self.g.nodes[record_id]["pruning_reason"] = reason

    def write_graphml(self, path: str | Path) -> None:
        nx.write_graphml(self.g, path)

    def generation_projection(self) -> dict[int, list[str]]:
        buckets: dict[int, list[str]] = {}
        for node, attrs in self.g.nodes(data=True):
            generation = int(attrs.get("generation", 0))
            buckets.setdefault(generation, []).append(node)
        for generation in buckets:
            buckets[generation].sort()
        return dict(sorted(buckets.items()))

    def render_dot(self, path: str | Path, compressed_by_study_family: bool = False) -> None:
        path = Path(path)
        lines = ["digraph evidence {", "  rankdir=LR;", "  graph [splines=true];"]

        if compressed_by_study_family:
            mapping: dict[str, str] = {}
            for node, attrs in sorted(self.g.nodes(data=True)):
                mapping[node] = str(attrs.get("study_family_id") or node)
            visible_nodes = sorted(set(mapping.values()))
            for node in visible_nodes:
                lines.append(f'  "{_esc(node)}" [shape=box, style="rounded"];')
            visible_edges = sorted({(mapping[u], mapping[v]) for u, v in self.g.edges() if mapping[u] != mapping[v]})
            for u, v in visible_edges:
                lines.append(f'  "{_esc(u)}" -> "{_esc(v)}";')
        else:
            state_colors = {
                "included": "green",
                "excluded": "red",
                "duplicate": "gray",
                "unresolved": "gold",
                "inaccessible": "gray30",
                "blocked": "orange",
                "registry_unpublished": "purple",
            }
            for node, attrs in sorted(self.g.nodes(data=True)):
                state = str(attrs.get("state", "unresolved"))
                color = state_colors.get(state, "black")
                style = "dashed" if attrs.get("pruned") else "solid"
                label = str(attrs.get("label") or node)
                if attrs.get("pruned") and attrs.get("pruning_reason"):
                    label += f"\\nPRUNE: {attrs['pruning_reason']}"
                lines.append(f'  "{_esc(node)}" [label="{_esc(label)}", color="{color}", style="{style}"];')
            for u, v, attrs in sorted(self.g.edges(data=True)):
                route = str(attrs.get("discovery_route", "database"))
                edge_style = {
                    "database": "solid",
                    "backward_citation": "dashed",
                    "forward_citation": "dotted",
                    "author_search": "dashdot",
                }.get(route, "solid")
                lines.append(f'  "{_esc(u)}" -> "{_esc(v)}" [style="{edge_style}"];')

        for generation, nodes in self.generation_projection().items():
            lines.append("  { rank=same; " + "; ".join(f'"{_esc(n)}"' for n in nodes) + "; }")
        lines.append("}")
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _esc(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')
