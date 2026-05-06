# AI Learning Lab

A full Python AI development environment using:

- LLM providers (OpenAI, Anthropic, Groq, Gemini)
- LangChain ecosystem
- RAG (ChromaDB + embeddings)
- Local models (Transformers, Ollama)
- ML + visualization tools
- Managed with `uv` and Python 3.14

---

# 1. Start fresh

```bash
cd "/Volumes/Ai Agents"
ls

uv init ai_learning_lab
cd ai_learning_lab
```

---

# 2. Pin Python version

```bash
uv python pin 3.14
```

Verify:

```bash
cat .python-version
```

Expected:

```text
3.14
```

---

# 3. Create virtual environment

```bash
uv venv
source .venv/bin/activate
```

Verify:

```bash
which python
python --version
```

---

# 4. Open project

```bash
cursor .
```

---

# 5. Install dependencies

```bash
uv add --link-mode=copy \
openai anthropic google-genai groq \
litellm \
langchain langchain-community langchain-openai langchain-text-splitters langchain-experimental \
chromadb langchain-chroma sentence-transformers tiktoken \
torch transformers ollama langchain-huggingface langchain-ollama \
beautifulsoup4 feedparser datasets \
scikit-learn scipy xgboost \
matplotlib plotly \
ipykernel ipywidgets nbformat \
pydub \
modal \
wandb psutil speedtest-cli
```

This will:
- install all dependencies
- update `pyproject.toml`
- create `uv.lock`

---

# 6. Resulting `pyproject.toml`

```toml
[project]
name = "ai-mega-course"
version = "0.1.0"
description = "AI mega course environment with LLMs, RAG, local models, and ML tooling"
readme = "README.md"
requires-python = ">=3.14,<3.15"

dependencies = [
    # --- LLM Providers ---
    "openai>=2.34.0",
    "anthropic>=0.98.1",
    "google-genai>=1.75.0",
    "groq>=1.2.0",

    # --- LLM Routing ---
    "litellm>=1.83.0",

    # --- LangChain ---
    "langchain>=1.2.17",
    "langchain-community>=0.4.1",
    "langchain-openai>=1.2.1",
    "langchain-text-splitters>=1.1.2",
    "langchain-experimental>=0.4.1",
    "langchain-chroma>=1.1.0",
    "langchain-huggingface>=1.2.2",
    "langchain-ollama>=1.1.0",

    # --- RAG ---
    "chromadb>=1.5.9",
    "sentence-transformers>=5.4.1",
    "tiktoken>=0.12.0",

    # --- Local Models ---
    "torch>=2.11.0",
    "transformers>=5.7.0",
    "ollama>=0.6.2",

    # --- Data ---
    "beautifulsoup4>=4.14.3",
    "feedparser>=6.0.12",
    "datasets>=4.8.5",

    # --- ML ---
    "scikit-learn>=1.8.0",
    "scipy>=1.17.1",
    "xgboost>=3.2.0",

    # --- Visualization ---
    "matplotlib>=3.10.9",
    "plotly>=6.7.0",

    # --- Notebook ---
    "ipykernel>=7.2.0",
    "ipywidgets>=8.1.8",
    "nbformat>=5.10.4",

    # --- Infra ---
    "modal>=1.4.2",
    "wandb>=0.26.1",
    "psutil>=7.2.2",

    # --- Misc ---
    "pydub>=0.25.1",
    "speedtest-cli>=2.1.3",
]
```

---

# 7. Verify installation

```bash
uv pip list
```

Check compatibility:

```bash
uv pip check
```

---

# 8. Test the environment

### Import test

```bash
uv run python -c "import torch, transformers, chromadb, langchain; print('OK')"
```

---

### Transformers test

```bash
uv run python -c "from transformers import pipeline; print(pipeline('sentiment-analysis')('working'))"
```

---

### Torch test

```bash
uv run python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
```

---

### Chroma test

```bash
uv run python -c "import chromadb; client=chromadb.Client(); print('chroma OK')"
```

---

# 9. Git setup

Initialize repo:

```bash
git init
```

Check status:

```bash
git status
```

---

# 10. First commit

```bash
git add .
git commit -m "Initial project setup with full AI stack and uv lockfile"
```

---

# 11. Create GitHub repository

- Name: `ai_mega_course`
- Do NOT add README
- Do NOT add .gitignore

---

# 12. Connect and push

```bash
git remote add origin https://github.com/doctornassar83/ai_mega_course.git
git branch -M main
git push -u origin main
```

---

# 13. Authentication

Use GitHub Personal Access Token:

- Username: `doctornassar83`
- Password: `<your token>`

---

# 14. uv.lock (important)

- created automatically after install
- MUST be committed

```bash
git add uv.lock
```

---

# 15. Important rules

### Always commit:
- `pyproject.toml`
- `uv.lock`
- `.python-version`
- `.gitignore`

### Never commit:
- `.venv/`
- `.env`
- model files
- vector databases

---

# 16. Useful commands

```bash
uv sync
uv pip check
uv pip list
uv add package-name
```

After changes:

```bash
git add pyproject.toml uv.lock
git commit -m "Update dependencies"
git push
```

---

# Final Result

You now have a:

- reproducible AI environment
- clean dependency management
- production-ready project baseline