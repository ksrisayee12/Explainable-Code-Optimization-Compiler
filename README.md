# 🔍 Explainable Code Optimization Compiler Using RAG-Enhanced Analysis

> Making compiler optimization decisions **transparent, visual, and human-readable** through graph analysis and AI-assisted explanations.

---

## 📌 Overview

Most compiler tools show you *what* was optimized — this project explains *why*.

The **Explainable Code Optimization Compiler** is a web-based platform that accepts simple C/Java-style arithmetic expressions, transforms them through a full compiler pipeline, and generates **human-readable explanations** for every optimization decision made — powered by a RAG (Retrieval-Augmented Generation) layer backed by a local LLM.

---

## ✨ Features

- 🔄 **Source → TAC Conversion** — Three Address Code generation from arithmetic expressions
- 📊 **Static Analysis** — Live variable analysis, dependency tracking, live-range computation
- ⚙️ **Optimization Pipeline** — Modular, plugin-based optimization techniques
- 🕸️ **Graph Visualizations** — Scheduled Dependency Graph, DAG, and CFG
- 🤖 **RAG-Powered Explanations** — Contextual, human-readable reasoning for every optimization
- 🖥️ **Interactive Web Interface** — Built with Streamlit for ease of exploration

---

## 🏗️ System Architecture

```
User Input (C/Java-style expression)
         │
         ▼
   Frontend Parser
         │
         ▼
Three Address Code Generator
         │
         ▼
   Static Analysis Engine
   (Live Variables · Dependencies · Live Ranges)
         │
         ▼
   Optimization Pipeline
         │
         ▼
   Visualization Engine
   ├── Scheduled Dependency Graph
   ├── Directed Acyclic Graph (DAG)
   └── Control Flow Graph (CFG)
         │
         ▼
RAG Explainability Layer (Ollama + Knowledge Base)
         │
         ▼
   Streamlit Web Interface
```

---

## ⚙️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| Web Interface | Streamlit |
| Visualization | Graphviz |
| LLM Backend | Ollama |
| Explainability | RAG (Retrieval-Augmented Generation) |
| Compiler Concepts | TAC, Live Variable Analysis, DAG, CFG |

---

## 📂 Project Modules

### 1 — Frontend Parsing Module
Parses C/Java-style arithmetic expressions and prepares them for intermediate code generation.

### 2 — Three Address Code (TAC) Generator
Transforms source expressions into TAC form using temporary variables.

### 3 — Static Analysis Module
Performs live variable analysis, dependency tracking, and live-range computation.

### 4 — Optimization Pipeline
Applies compiler optimizations via a modular, plugin-based architecture — starting with live-range compression.

### 5 — Visualization & Explainability Module
Generates Dependency Graphs, DAGs, and CFGs alongside RAG-powered natural language explanations for every optimization.

---

## 🧪 Example

### Input
```c
a = b + c;
d = b + c;
e = a * d;
```

### Generated TAC
```
t1 = b + c
a  = t1

t2 = b + c
d  = t2

t3 = a * d
e  = t3
```

### RAG Explanation (sample output)
> *"The temporary variable was rescheduled closer to its first use, reducing its live range and improving resource utilization while preserving program correctness."*

---

## 🖼️ Visualizations

The system auto-generates three graph types per input:

- **Scheduled Dependency Graph** — instruction-level data dependencies
- **Directed Acyclic Graph (DAG)** — expression structure and redundancy detection
- **Control Flow Graph (CFG)** — basic block structure and branching

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- [Ollama](https://ollama.ai) installed locally

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd <repository-folder>

# Create and activate virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Run

```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## 🎓 Applications

- Compiler Design coursework & labs
- Program analysis visualization
- Explainable AI for software systems
- Academic research & demonstrations
- Capstone / final year projects

---

## 🔮 Future Enhancements

- [ ] Constant Folding
- [ ] Common Subexpression Elimination (CSE)
- [ ] Dead Code Elimination
- [ ] Register Allocation Visualization
- [ ] Loop Optimization Support
- [ ] Multi-language Frontend (Python, Rust)
- [ ] Optimization Benchmarking Suite

---

## 📜 License

Developed for academic and educational purposes.