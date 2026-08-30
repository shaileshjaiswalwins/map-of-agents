#!/usr/bin/env python3
"""Shape docs/raw_live_data.json (live GitHub metrics, from fetch_live_data.py)
into the hierarchical docs/data.json the page consumes, with derived signals
for the Engineering and Product lenses:

  - maintenance: active (<90d since push) / moderate (<365d) / stale (>=365d) / archived
  - momentum: crude proxy from stars-per-day-since-creation (not true growth,
    since we don't have historical snapshots) — labeled as "traction" for honesty
  - risk flags: no license, archived, stale
"""
import json
from datetime import datetime, timezone

CATEGORY_LABELS = {
    "agent-frameworks": "Agent Frameworks & SDKs",
    "autonomous-agents": "Autonomous & General-Purpose Agents",
    "agent-protocols-infra": "Protocols, Orchestration & Infrastructure",
    "agent-memory-tools": "Memory, RAG & Retrieval",
    "agent-eval-observability": "Evaluation & Observability",
    "coding-agents": "Coding Agents & Dev Tools",
    "multi-agent-simulation": "Multi-Agent Simulation & Research",
}

MAX_PER_CATEGORY = 22
SNAPSHOT_DATE = datetime(2026, 8, 30, tzinfo=timezone.utc)


def maintenance_status(p):
    if p["archived"]:
        return "archived"
    d = p["days_since_push"]
    if d is None:
        return "unknown"
    if d < 0:
        d = 0
    if d <= 90:
        return "active"
    if d <= 365:
        return "moderate"
    return "stale"


def traction_score(p):
    created = p.get("created_at")
    if not created:
        return 0.0
    dt = datetime.strptime(created, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    age_days = max((SNAPSHOT_DATE - dt).days, 1)
    return round(p["stars"] / age_days, 2)


def build():
    raw = json.load(open("docs/raw_live_data.json"))

    by_cat = {}
    for p in raw:
        by_cat.setdefault(p["category"], []).append(p)

    root = {"name": "AI Agent Ecosystem", "children": []}
    total_projects = 0
    total_stars = 0

    for key, label in CATEGORY_LABELS.items():
        items = by_cat.get(key, [])
        items.sort(key=lambda p: -p["stars"])
        items = items[:MAX_PER_CATEGORY]

        children = []
        for p in items:
            status = maintenance_status(p)
            children.append({
                "name": p["name"],
                "full_name": p["full_name"],
                "description": p["description"] or "No description provided.",
                "url": p["url"],
                "value": max(p["stars"], 50),
                "stars": p["stars"],
                "forks": p["forks"],
                "open_issues": p["open_issues"],
                "language": p["language"],
                "license": p["license"],
                "archived": p["archived"],
                "pushed_at": p["pushed_at"],
                "days_since_push": max(p["days_since_push"], 0) if p["days_since_push"] is not None else None,
                "maintenance": status,
                "traction": traction_score(p),
            })
        total_projects += len(children)
        total_stars += sum(c["stars"] for c in children)
        root["children"].append({
            "name": label,
            "key": key,
            "children": children,
        })

    root["children"].sort(key=lambda c: -sum(p["stars"] for p in c["children"]))
    root["meta"] = {
        "total_projects": total_projects,
        "total_stars": total_stars,
        "categories": len(root["children"]),
        "snapshot_date": "2026-08-30",
    }

    print(f"categories={len(root['children'])} projects={total_projects} total_stars={total_stars:,}")
    with open("docs/data.json", "w") as f:
        json.dump(root, f, indent=2)


if __name__ == "__main__":
    build()
