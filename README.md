# AI Engineering & Evaluation Benchmark Harness (`ai-eval-harness`)

A rigorous, modular benchmarking and engineering suite designed to test, validate, and evaluate algorithmic problem solving, asynchronous backend architectures, and LLM-powered code generation.

## 🎯 Overview

The `ai-eval-harness` provides standardized environments, rubrics, and automated testing pipelines across four foundational engineering pillars:

- **Algorithms & Problem Solving**: NeetCode core patterns implemented in pure Python with mathematical rigor, edge-case testing, and explicit asymptotic complexity constraints.
- **Backend Concurrency & Systems**: Production-grade asynchronous patterns including token-bucket rate limiters, connection pools, and real-time execution profiling (`tracemalloc`, `cProfile`).
- **LLM Evaluation & Rubrics**: Deterministic scoring frameworks, structured schema validation (`code_eval_schema.json`), and adversarial testing for LLM code generation.
- **Agent Workflows & Graph Architectures**: State machines and graph-based orchestration for multi-step agentic execution.

---

## 📁 Repository Structure

```tree
ai-eval-harness/
├── algorithms/
│   └── neetcode/           # Pattern drills (Arrays, Two Pointers, Sliding Window, etc.)
├── backend/
│   └── async_patterns/     # AsyncIO pipelines, token buckets, and connection managers
├── evals/
│   └── rubrics/            # Evaluation schemas, adversarial prompts, and scoring scripts
├── agents/
│   └── graphs/             # Multi-agent state charts and orchestration graphs
├── .gitignore              # Standard Python and environment exclusions
└── README.md               # Harness overview and roadmap documentation
```

---

## 🚀 Engineering Roadmap & Milestones

1. **NeetCode Core Pattern Drills**
   - Pure Python solutions for Arrays, Hashing, Two-Pointer, and Window patterns.
   - Comprehensive unit testing with `pytest`.
   - Strict adherence to $O(N)$ runtime and $O(1)$ auxiliary space complexity.

2. **Asynchronous Rate Limiting & Concurrency**
   - High-throughput token-bucket rate limiter built with `asyncio`.
   - Simulated stress testing (50 concurrent workers against 5 req/sec quotas).
   - CPU and memory overhead profiling.

3. **LLM Evaluation Rubric & Scoring Script**
   - Automated grading pipeline measuring correctness, efficiency, and security.
   - Adversarial prompt suite probing edge cases, race conditions, and JSON validity.
   - Pairwise model judgment outputting standardized evaluation matrices.

4. **Agent Graph Orchestration**
   - Graph-based agent pipelines with state checkpoints and failure recovery.

---

## 🛠️ Setup & Prerequisites

### Requirements
- **Python**: 3.10+
- **Git** & **GitHub CLI (`gh`)**

### Quickstart
```bash
# Clone the repository
git clone https://github.com/<owner>/ai-eval-harness.git
cd ai-eval-harness

# Set up virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies & run tests
pip install -r requirements.txt  # when initialized
pytest
```

---

## 📜 License
MIT License. See LICENSE file for details.
