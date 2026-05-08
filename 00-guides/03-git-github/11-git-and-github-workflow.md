# Professional Git & GitHub Workflow for AI Engineering on macOS

> File Name:
>
> `11-git-and-github-workflow.md`

---

# Purpose of This Guide

This guide builds a complete professional Git and GitHub workflow for AI engineering on macOS.

This guide is specifically designed for your environment:

- macOS
- ZSH
- WezTerm
- Cursor
- Python
- uv
- AI engineering projects
- GitHub repositories
- SSH authentication
- professional repository management

By the end of this guide, you will know how to:

- install Git professionally
- configure Git globally
- configure SSH authentication
- understand HTTPS token authentication
- create GitHub repositories
- connect local projects to GitHub
- manage project history safely
- retrieve previous project versions
- work with branches professionally
- use your Git aliases efficiently
- manage AI engineering repositories safely

---

# Git vs GitHub

| Git | GitHub |
|---|---|
| local version control system | cloud repository hosting |
| works offline | collaboration platform |
| tracks file history | stores repositories online |

---

# Your Git Alias Ecosystem

Your `.zshrc` already includes:

```zsh
alias g="git"

alias gs="git status"

alias ga="git add"
alias gaa="git add --all"

alias gc="git commit -m"

alias gp="git push"
alias gpl="git pull"

alias gb="git branch"
alias gco="git checkout"
alias gcb="git checkout -b"

alias gd="git diff"
alias gds="git diff --staged"

alias glog="git log --oneline --graph --decorate --all"

alias amend="git commit --amend --no-edit"

alias unstage="git restore --staged"
alias discard="git restore"
```

This guide uses your aliases whenever possible.

---

# PART 1 — Install Git

## Verify Git Installation

```bash
git --version
```

Expected:

```text
git version 2.x.x
```

---

# Install Git Using Homebrew

If Git is not installed:

```bash
brew install git
```

---

# Verify Git Binary

```bash
which git
```

Expected:

```text
/opt/homebrew/bin/git
```

---

# PART 2 — Professional Git Configuration

---

# Configure Username

Current configuration:

```bash
git config --global user.name "doctornassar83"
```

Professional alternative:

```bash
git config --global user.name "Mohamed Nassar"
```

---

# Configure Email

```bash
git config --global user.email "dr.mohamedissanassar@gmail.com"
```

---

# Configure Default Branch

```bash
git config --global init.defaultBranch main
```

---

# Configure Cursor as Git Editor

```bash
git config --global core.editor "cursor --wait"
```

---

# Configure Colored Output

```bash
git config --global color.ui auto
```

---

# Configure Pull Behavior

```bash
git config --global pull.rebase false
```

---

# Recommended Professional Enhancements

```bash
git config --global merge.conflictstyle zdiff3
git config --global push.autoSetupRemote true
git config --global fetch.prune true
git config --global diff.colorMoved zebra
git config --global rerere.enabled true
git config --global core.autocrlf input
```

---

# Verify Final Configuration

```bash
git config --global --list
```

Your target configuration should look similar to:

```text
user.name=doctornassar83
user.email=dr.mohamedissanassar@gmail.com
init.defaultbranch=main
core.editor=cursor --wait
color.ui=auto
pull.rebase=false
merge.conflictstyle=zdiff3
push.autosetupremote=true
fetch.prune=true
diff.colormoved=zebra
rerere.enabled=true
core.autocrlf=input
```

---

# PART 3 — Professional SSH Setup

SSH is the recommended professional GitHub authentication method.

---

# Verify Existing SSH Keys

```bash
ls -la ~/.ssh
```

Your current setup already contains:

```text
id_ed25519
id_ed25519.pub
known_hosts
```

This means your SSH keys already exist.

---

# Generate SSH Key (Only If Missing)

Only run if keys do not exist:

```bash
ssh-keygen -t ed25519 -C "dr.mohamedissanassar@gmail.com"
```

---

# Add SSH Key to macOS Keychain

```bash
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
```

---

# Verify Key Is Loaded

```bash
ssh-add -l
```

Expected:

```text
ED25519 ...
```

---

# Configure SSH Client

Open SSH config:

```bash
cursor ~/.ssh/config
```

Add:

```sshconfig
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519
  AddKeysToAgent yes
  UseKeychain yes
```

---

# Test GitHub SSH Authentication

```bash
ssh -T git@github.com
```

Expected:

```text
Hi doctornassar83! You've successfully authenticated, but GitHub does not provide shell access.
```

This confirms:
- SSH works
- GitHub authentication works
- Keychain integration works

---

# PART 4 — HTTPS Authentication and GitHub Tokens

Sometimes Git asks:

```text
Username for 'https://github.com':
Password for 'https://USERNAME@github.com':
```

This happens when repositories use:

```text
HTTPS
```

instead of:

```text
SSH
```

---

# Important

GitHub no longer accepts account passwords.

The password must be:

```text
GitHub Personal Access Token
```

---

# Create Personal Access Token

Open:

```text
GitHub → Settings → Developer Settings → Personal Access Tokens
```

Recommended:
- Fine-grained token
- repository read/write permissions

---

# Professional Recommendation

Prefer:

```text
SSH
```

instead of HTTPS.

SSH avoids:
- token prompts
- password prompts
- authentication friction

---

# PART 5 — Verify Repository Authentication Method

Check repository remote:

```bash
git remote -v
```

Your repository now correctly uses:

```text
git@github.com:doctornassar83/ai-learning-lab.git
```

This means:
- SSH authentication is active
- GitHub tokens are no longer required
- pushes/pulls are seamless

---

# Convert HTTPS Repository to SSH

If repository uses HTTPS:

```text
https://github.com/USERNAME/REPO.git
```

convert it:

```bash
git remote set-url origin git@github.com:USERNAME/REPO.git
```

Verify:

```bash
git remote -v
```

---

# PART 6 — Create Local Project

Using your helper:

```bash
newlab ai-learning-lab
```

or:

```bash
mkpyproject ai-learning-lab
```

or manually:

```bash
mkdir ai-learning-lab
cd ai-learning-lab
```

---

# Initialize Git Repository

```bash
git init
```

---

# Verify Repository

```bash
gs
```

Equivalent to:

```bash
git status
```

---

# PART 7 — Professional `.gitignore`

Your current `.gitignore` is already very strong and professional.

It is optimized for:

- Python
- uv
- AI engineering
- ML artifacts
- vector databases
- notebooks
- macOS
- editors
- experiment tracking

---

# Your Current `.gitignore`

```gitignore
# =========================================================
# Python cache / compiled files
# =========================================================
__pycache__/
*.py[cod]
*$py.class
*.so

# =========================================================
# Virtual environments
# =========================================================
.venv/
venv/
env/
ENV/
.envrc

# =========================================================
# Environment variables / secrets
# =========================================================
.env
.env.*
!.env.example

# =========================================================
# Python packaging / build artifacts
# =========================================================
build/
dist/
wheels/
*.egg-info/
.eggs/
*.egg
MANIFEST

# =========================================================
# uv / Python versioning
# =========================================================
# DO NOT ignore these:
# uv.lock
# .python-version

# =========================================================
# Jupyter / notebooks
# =========================================================
.ipynb_checkpoints/
.virtual_documents/

# =========================================================
# Testing / coverage / lint caches
# =========================================================
.pytest_cache/
.mypy_cache/
.ruff_cache/
.cache/
.coverage
.coverage.*
htmlcov/

# =========================================================
# IDE / editor files
# =========================================================
.idea/
.vscode/
.DS_Store
Thumbs.db

# =========================================================
# Logs / runtime files
# =========================================================
*.log
logs/
nohup.out
report.txt
**/report.txt

# =========================================================
# AI / ML model artifacts (large + generated)
# =========================================================
*.pth
*.pt
*.onnx
*.safetensors
*.ckpt
*.h5
*.bin

# HuggingFace / model caches
model_cache/
hf_cache/
.cache/huggingface/

# =========================================================
# Vector databases / embeddings stores
# =========================================================
chroma/
vector_db/
vectorstore/
*.faiss
*.sqlite
*.sqlite3
*.db

# =========================================================
# Data artifacts (optional: uncomment if needed)
# =========================================================
# data/
# *.csv
# *.parquet
# *.jsonl

# =========================================================
# Experiment tracking
# =========================================================
wandb/
mlruns/

# =========================================================
# Gradio / UI artifacts
# =========================================================
.gradio/

# =========================================================
# Temporary / scraping / local outputs
# =========================================================
scraper_cache/
tmp/
temp/
local/

# =========================================================
# Misc tools
# =========================================================
speedtest-cli.json

# =========================================================
# OS-specific junk
# =========================================================
.DS_Store
.AppleDouble
.LSOverride
Icon?

# Windows
Thumbs.db
ehthumbs.db

# =========================================================
# Optional: images (uncomment if auto-generated only)
# =========================================================
# *.png
# *.jpg
# *.jpeg
# *.gif
```

---

# Why This `.gitignore` Is Excellent

It properly excludes:

| Category | Covered |
|---|---|
| Python cache | yes |
| virtual environments | yes |
| secrets | yes |
| notebooks | yes |
| ML models | yes |
| vector DBs | yes |
| HuggingFace cache | yes |
| experiment tracking | yes |
| temporary outputs | yes |
| macOS junk | yes |

This is already:
- AI-engineering-grade
- production-quality
- professional

---

# PART 8 — Create GitHub Repository

Go to:

```text
https://github.com/new
```

Recommended:

| Setting | Recommendation |
|---|---|
| Repository Name | ai-learning-lab |
| Description | AI Engineering Learning Lab |
| Visibility | Private |
| Initialize README | NO |
| Initialize .gitignore | NO |

IMPORTANT:

Do NOT initialize:
- README
- `.gitignore`

if they already exist locally.

---

# PART 9 — Connect Local Repository to GitHub

Add remote:

```bash
git remote add origin git@github.com:doctornassar83/ai-learning-lab.git
```

---

# Verify Remote

```bash
git remote -v
```

Expected:

```text
origin  git@github.com:doctornassar83/ai-learning-lab.git
```

---

# PART 10 — First Commit Workflow

---

# Check Status

```bash
gs
```

---

# Stage Files

```bash
gaa
```

---

# Verify Staged Files

```bash
gs
```

---

# Create Commit

```bash
gc "initial ai engineering setup"
```

---

# Push to GitHub

```bash
gp
```

If upstream is not configured:

```bash
git push -u origin main
```

---

# PART 11 — Daily Professional Workflow

Every project change follows this workflow.

---

# Step 1 — Check Status

```bash
gs
```

---

# Step 2 — Edit Files

Open project:

```bash
c.
```

---

# Step 3 — Review Changes

```bash
gd
```

---

# Step 4 — Stage Files

Single file:

```bash
ga file.py
```

All files:

```bash
gaa
```

---

# Step 5 — Review Staged Changes

```bash
gds
```

---

# Step 6 — Commit

```bash
gc "update rag workflow"
```

---

# Step 7 — Push

```bash
gp
```

---

# Full Professional Workflow Example

```bash
lab
gs
rg "TODO"
gd
gaa
gds
gc "add vector database guide"
gp
```

---

# PART 12 — Retrieve Previous Project Versions

Git is a project time machine.

---

# View Commit History

```bash
glog
```

Example:

```text
a1b2c3 add rag workflow
d4e5f6 initial setup
```

---

# View Specific Commit

```bash
git show COMMIT_ID
```

---

# Temporarily Open Old Version

```bash
git checkout COMMIT_ID
```

Example:

```bash
git checkout a1b2c3
```

You are now viewing the old project version.

---

# Return to Latest Version

```bash
gco main
```

---

# Restore Old File Version

```bash
git checkout COMMIT_ID -- file.py
```

---

# Compare Two Versions

```bash
git diff COMMIT1 COMMIT2
```

---

# Recover Deleted File

```bash
git checkout COMMIT_ID -- deleted-file.py
```

---

# PART 13 — Branch Workflow

---

# Create Branch

```bash
gcb feature-rag
```

---

# Switch Branch

```bash
gco main
```

---

# Professional Branch Naming

Recommended:

```text
feature/rag-system
fix/python-env
docs/update-guides
refactor/zsh-config
```

---

# PART 14 — Undo Mistakes

---

# Unstage Files

```bash
unstage
```

---

# Discard File Changes

```bash
discard file.py
```

Danger:
- removes uncommitted changes

---

# Amend Previous Commit

```bash
amend
```

Useful for:
- forgotten files
- typo fixes

---

# PART 15 — Professional AI Engineering Git Rules

---

# Never Commit Secrets

Never commit:
- `.env`
- API keys
- broker credentials
- passwords
- tokens

---

# Commit Frequently

Small commits are safer.

---

# Push Frequently

GitHub is backup protection.

---

# Keep `main` Stable

Use branches for experiments.

---

# Review Before Commit

Always use:

```bash
gs
gd
gds
```

---

# PART 16 — Most Important Commands to Master

```bash
gs
ga
gaa
gc
gp
gpl
gb
gco
gcb
gd
gds
glog
unstage
discard
amend
```

---

# PART 17 — Daily Professional AI Engineering Workflow

Typical session:

```bash
lab
gs
rg "TODO"
gd
gaa
gds
gc "update embeddings workflow"
gp
```

---

# Final Checklist

Before continuing:

- [ ] Git installed
- [ ] Git configured
- [ ] SSH authentication works
- [ ] SSH key loaded into Keychain
- [ ] GitHub repository connected
- [ ] repository uses SSH
- [ ] `.gitignore` configured
- [ ] commits work
- [ ] pushes work
- [ ] aliases work
- [ ] retrieving old versions understood

---

# Recommended Commands to Practice Daily

```bash
gs
gaa
gc "message"
gp
glog
gd
gcb feature-name
gco main
```

---

# Next Guide

Next:

```text
12-python-and-uv-workflow.md
```

The next guide will cover:

- Python installation
- uv workflows
- virtual environments
- dependency management
- reproducible AI engineering environments
- project architecture
- professional Python workflows