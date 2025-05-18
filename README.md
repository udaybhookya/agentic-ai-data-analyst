[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Agentic AI Data Analyst

A Python-based agentic analytics framework that autonomously ingests, explores, and reports on tabular datasets using LangGraph, LangChain, and LLMs.

## 📝 Overview

* **Data Understanding:** Automated profiling and summary of input tables based on schemas.
* **Agent Planning:** Dynamically generate analysis plans (aggregations, charts, narratives).
* **Execution & Error Handling:** Run pandas queries, loop on failures (up to 3 retries) with LLM-assisted fixes.
* **Report Generation:** Compile results and narratives into PDF/HTML reports.

## 🚀 Quick Start

1. **Clone the repo**

   ```bash
   git clone https://github.com/USERNAME/agentic-ai-data-analyst.git
   cd agentic-ai-data-analyst
   ```
2. **Create & activate a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
4. **Configure environment variables**
   Copy `.env.example` to `.env` and fill in your keys:

   ```bash
   cp .env.example .env
   # then edit .env to add OPENAI_API_KEY etc.
   ```
5. **Run the project**

   ```bash
   python main.py --config langgraph.json
   ```

## 📂 Project Structure

```
.
├── agents/
│   ├── plan_analytics.py      # Build and sequence analysis steps
│   └── understand_data.py     # Data profiling agent
├── utils/
│   ├── load_data.py           # Schema-driven CSV loader
│   ├── preprocess_data.py     # Cleaning & type conversion
│   └── load_llm.py            # LLM initialization
├── data/
│   ├── df/                    # Raw CSV datasets
│   └── schema/                # Corresponding schema files
├── prompts/                   # Static prompt templates
│   └── data_understanding_prompt.txt
├── output/                    # Intermediate outputs (logs, graphs)
├── reports/                   # Final report artifacts
├── langgraph.json             # Workflow definition for LangGraph
├── workflow.py                # Orchestrator engine
├── state.py                   # Workflow state management
├── main.py                    # Entry-point script
├── requirements.txt
├── .env                       # API keys & secrets (gitignored)
└── .gitignore
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m "Add my feature"`
4. Push to your branch: `git push origin feature/my-feature`
5. Open a Pull Request and describe your changes

## 📜 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
