#!/usr/bin/env python3
"""Dedupe and shape the researched agent-ecosystem data into a hierarchical
JSON tree consumable by the D3 treemap (categories -> projects, sized by stars)."""
import json

RAW = {
  "agent-frameworks": {
    "label": "Agent Frameworks & SDKs",
    "projects": [
      ("LangChain", "Framework for building LLM-powered applications with chains, tools, and agents", "langchain-ai/langchain", 95000),
      ("LangGraph", "Library for building stateful, multi-actor agent applications as graphs", "langchain-ai/langgraph", 12000),
      ("CrewAI", "Framework for orchestrating role-playing, autonomous AI agents as collaborative crews", "crewAIInc/crewAI", 27000),
      ("AutoGen", "Multi-agent conversation framework from Microsoft for building LLM applications", "microsoft/autogen", 41000),
      ("Semantic Kernel", "Microsoft's SDK for integrating LLMs into apps with plugins, planners, and agents", "microsoft/semantic-kernel", 22000),
      ("LlamaIndex", "Data framework for LLM applications with agent and RAG capabilities", "run-llama/llama_index", 37000),
      ("Haystack", "End-to-end framework for building production-ready LLM and RAG/agent applications", "deepset-ai/haystack", 17000),
      ("Rasa", "Open-source framework for building conversational AI and task-oriented agents", "RasaHQ/rasa", 18000),
      ("Claude Agent SDK", "Anthropic's SDK for building autonomous agents on top of Claude", "anthropics/claude-agent-sdk-python", 2000),
      ("OpenAI Agents SDK", "OpenAI's lightweight Python SDK for building multi-agent workflows", "openai/openai-agents-python", 9000),
      ("Google ADK", "Google's open-source framework for building and deploying multi-agent systems", "google/adk-python", 9000),
      ("Pydantic AI", "Python agent framework built on Pydantic for type-safe LLM applications", "pydantic/pydantic-ai", 8000),
      ("Agno", "Lightweight framework for building multi-modal, multi-agent systems (formerly Phidata)", "agno-agi/agno", 18000),
      ("smolagents", "Hugging Face's minimal library for building code-writing LLM agents", "huggingface/smolagents", 15000),
      ("DSPy", "Framework for programming (not prompting) language models, including agentic pipelines", "stanfordnlp/dspy", 20000),
      ("Griptape", "Python framework for building modular AI agents and workflows with structured pipelines", "griptape-ai/griptape", 2000),
      ("Letta (MemGPT)", "Framework for building stateful LLM agents with long-term memory", "letta-ai/letta", 15000),
      ("AG2 (AutoGen fork)", "Community fork continuing multi-agent conversation framework development", "ag2ai/ag2", 2000),
      ("XAgent", "Autonomous LLM agent framework for solving complex tasks with planning and tool use", "OpenBMB/XAgent", 8000),
      ("Swarm", "OpenAI's lightweight experimental framework for orchestrating multi-agent handoffs", "openai/swarm", 18000),
    ],
  },
  "autonomous-agents": {
    "label": "Autonomous & General-Purpose Agents",
    "projects": [
      ("AutoGPT", "Early influential autonomous GPT-4 agent that pursues goals with minimal human input", "Significant-Gravitas/AutoGPT", 172000),
      ("BabyAGI", "Minimal task-driven autonomous agent loop that creates, prioritizes, and executes tasks", "yoheinakajima/babyagi", 21000),
      ("AgentGPT", "Browser-based tool to configure and deploy autonomous AI agents", "reworkd/AgentGPT", 33000),
      ("SuperAGI", "Open-source framework/platform to build, manage, and run autonomous agents with a UI", "TransformerOptimus/SuperAGI", 15000),
      ("OpenHands", "Platform of AI software-engineer agents that modify code, run commands, and browse", "All-Hands-AI/OpenHands", 50000),
      ("GPT Engineer", "Agent that generates an entire codebase from a natural-language prompt", "AntonOsika/gpt-engineer", 52000),
      ("MetaGPT", "Multi-agent framework that simulates a software company with role-based agents", "geekan/MetaGPT", 45000),
      ("ChatDev", "Virtual software company where multiple LLM agents collaborate to build software", "OpenBMB/ChatDev", 25000),
      ("Aider", "AI pair-programming CLI agent that edits code in your local git repo", "Aider-AI/aider", 30000),
      ("SWE-agent", "Agent that autonomously fixes GitHub issues and solves SWE-bench tasks", "SWE-agent/SWE-agent", 14000),
      ("Open Interpreter", "Natural-language interface letting an LLM autonomously run code locally", "OpenInterpreter/open-interpreter", 58000),
      ("browser-use", "Library/agent that lets LLMs autonomously control a web browser", "browser-use/browser-use", 58000),
      ("Skyvern", "Autonomous browser-automation agent using LLMs and computer vision", "Skyvern-AI/skyvern", 12000),
      ("Devika", "Open-source agentic AI software engineer that plans, researches, and writes code", "stitionai/devika", 19000),
      ("GPT-Pilot", "AI dev-tool agent that writes production-ready apps step by step, human-in-the-loop", "Pythagora-io/gpt-pilot", 32000),
      ("AGiXT", "Task-completing autonomous agent runtime for chaining LLM tasks with tools and memory", "Josh-XT/AGiXT", 3000),
      ("Moatless Tools", "Autonomous coding agent aimed at resolving real-world GitHub issues with minimal context tools", "aorwall/moatless-tools", 800),
      ("Codex CLI", "OpenAI's lightweight coding agent that runs in a terminal to autonomously edit code", "openai/codex", 30000),
      ("Cline", "Autonomous coding agent VS Code extension that can edit files, run commands, and browse", "cline/cline", 42000),
    ],
  },
  "agent-protocols-infra": {
    "label": "Protocols, Orchestration & Infrastructure",
    "projects": [
      ("Model Context Protocol", "Open standard from Anthropic for connecting LLM apps to tools and data sources", "modelcontextprotocol/servers", 45000),
      ("Agent2Agent (A2A)", "Google-led open protocol for interoperable communication between AI agents", "google-a2a/A2A", 15000),
      ("LangServe", "Library for deploying LangChain runnables/chains as REST APIs", "langchain-ai/langserve", 2200),
      ("Ray", "Distributed computing framework widely used to scale agent/LLM workloads", "ray-project/ray", 34000),
      ("Temporal", "Durable execution engine for building reliable, long-running agent workflows", "temporalio/temporal", 12000),
      ("E2B", "Secure cloud sandboxes for running AI-generated code with isolated execution", "e2b-dev/e2b", 8500),
      ("CopilotKit", "React toolkit for building in-app AI copilots and agentic UI experiences", "CopilotKit/CopilotKit", 15000),
      ("Composio", "Integration/tool-calling platform giving agents authenticated access to SaaS APIs", "ComposioHQ/composio", 8000),
    ],
  },
  "agent-memory-tools": {
    "label": "Memory, RAG & Retrieval",
    "projects": [
      ("Mem0", "Memory layer for AI agents/assistants providing persistent, personalized memory", "mem0ai/mem0", 25000),
      ("Zep", "Long-term memory store for LLM apps with a temporal knowledge graph", "getzep/zep", 3000),
      ("Chroma", "Open-source embedding database for building AI apps with retrieval", "chroma-core/chroma", 16000),
      ("Weaviate", "Open-source vector database with hybrid search and modules for AI apps", "weaviate/weaviate", 11000),
      ("Qdrant", "Vector similarity search engine and database written in Rust", "qdrant/qdrant", 21000),
      ("Milvus", "Open-source vector database built for scalable similarity search", "milvus-io/milvus", 30000),
      ("txtai", "All-in-one embeddings database for semantic search and RAG workflows", "neuml/txtai", 9000),
      ("Instructor", "Library for structured outputs from LLMs using Pydantic validation", "jxnl/instructor", 9000),
      ("Guardrails", "Framework for adding structure, validation, and correction to LLM outputs", "guardrails-ai/guardrails", 4500),
      ("FAISS", "Library for efficient similarity search and clustering of dense vectors", "facebookresearch/faiss", 30000),
      ("LiteLLM", "Unified API/proxy for calling 100+ LLMs with function-calling support", "BerriAI/litellm", 15000),
    ],
  },
  "agent-eval-observability": {
    "label": "Evaluation & Observability",
    "projects": [
      ("Langfuse", "Open-source LLM engineering platform for tracing, evaluation, and observability", "langfuse/langfuse", 8000),
      ("Helicone", "Open-source observability platform for logging, monitoring, and debugging LLM apps", "Helicone/helicone", 2500),
      ("Promptfoo", "CLI and library for testing, evaluating, and red-teaming LLM prompts and agent outputs", "promptfoo/promptfoo", 6000),
      ("DeepEval", "Open-source LLM evaluation framework with pytest-like unit testing", "confident-ai/deepeval", 4500),
      ("Ragas", "Evaluation framework focused on RAG pipelines: faithfulness, relevance, context quality", "explodinggradients/ragas", 8000),
      ("AgentBench", "Benchmark suite for evaluating LLMs as agents across diverse interactive environments", "THUDM/AgentBench", 2300),
      ("Arize Phoenix", "Open-source AI observability and evaluation library for tracing LLM apps and agents", "Arize-ai/phoenix", 4500),
      ("TruLens", "Library for evaluating and tracking LLM app quality, including agent reasoning", "truera/trulens", 2400),
      ("OpenAI Evals", "Framework and registry of benchmarks for evaluating LLMs and LLM-based systems", "openai/evals", 15500),
      ("AgentOps", "Observability and monitoring SDK purpose-built for AI agents", "AgentOps-AI/agentops", 3800),
      ("OpenLLMetry", "OpenTelemetry-based observability for LLM applications and agents", "traceloop/openllmetry", 2000),
      ("Giskard", "Testing framework for ML and LLM systems: vulnerability scanning and quality evaluation", "Giskard-AI/giskard", 4200),
    ],
  },
  "coding-agents": {
    "label": "Coding Agents & Dev Tools",
    "projects": [
      ("Claude Code", "Anthropic's official agentic CLI coding assistant", "anthropics/claude-code", 15000),
      ("Continue.dev", "Open-source IDE extension for building custom AI coding assistants", "continuedev/continue", 22000),
      ("Sweep", "AI junior developer bot that turns GitHub issues into pull requests", "sweepai/sweep", 7500),
      ("Plandex", "Terminal-based AI coding agent for large, multi-file programming tasks", "plandex-ai/plandex", 13000),
      ("Bolt.new", "Browser-based AI agent that scaffolds and runs full-stack web apps in-browser", "stackblitz/bolt.new", 15000),
      ("opencode", "Open-source terminal AI coding agent, provider-agnostic alternative to Claude Code", "sst/opencode", 9000),
    ],
  },
  "multi-agent-simulation": {
    "label": "Multi-Agent Simulation & Research",
    "projects": [
      ("Generative Agents", "Simulated town of LLM-driven agents with memory, planning, and reflection", "joonspk-research/generative_agents", 18000),
      ("CAMEL", "Framework for autonomous cooperative agents via role-playing communication", "camel-ai/camel", 8000),
      ("AgentVerse", "Framework for multi-agent environments enabling collaboration and simulation", "OpenBMB/AgentVerse", 4400),
      ("JARVIS / HuggingGPT", "LLM orchestrates specialized HuggingFace models to solve multimodal tasks", "microsoft/JARVIS", 24000),
      ("Voyager", "LLM-powered lifelong learning agent that autonomously explores Minecraft", "MineDojo/Voyager", 5900),
      ("ChatArena", "Multi-agent language game environments for studying LLM communication", "Farama-Foundation/chatarena", 1600),
      ("Concordia", "DeepMind library for building generative agent-based social simulations", "google-deepmind/concordia", 2600),
      ("AgentSims", "Sandbox simulation platform for evaluating LLM-based agents", "py499372727/AgentSims", 500),
      ("MindAgent", "Multi-agent collaboration benchmark/framework in gaming environments", "cuijiaxun/MindAgent", 700),
    ],
  },
}

def build():
    root = {"name": "AI Agent Ecosystem", "children": []}
    total_projects = 0
    for key, cat in RAW.items():
        seen = set()
        children = []
        for name, desc, repo, stars in cat["projects"]:
            if repo in seen:
                continue
            seen.add(repo)
            children.append({
                "name": name,
                "description": desc,
                "repo": repo,
                "url": f"https://github.com/{repo}" if repo else None,
                "value": max(stars, 300),
            })
        children.sort(key=lambda c: -c["value"])
        total_projects += len(children)
        root["children"].append({
            "name": cat["label"],
            "key": key,
            "children": children,
        })
    root["children"].sort(key=lambda c: -sum(p["value"] for p in c["children"]))
    print(f"categories={len(root['children'])} projects={total_projects}")
    return root

if __name__ == "__main__":
    data = build()
    with open("docs/data.json", "w") as f:
        json.dump(data, f, indent=2)
