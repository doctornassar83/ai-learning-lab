# Professional AI Engineering Terminal Workflows on macOS

> File Name:
>
> `10-common-terminal-commands.md`

---

# Purpose of This Guide

This guide teaches the actual terminal workflows used in your professional AI engineering environment.

This is not a generic Unix guide.

It is specifically designed for your setup:

- macOS
- ZSH
- WezTerm
- Starship
- Homebrew
- Python
- uv
- Git
- Cursor
- AI engineering workflows

This guide combines:
- core terminal commands
- your aliases
- your productivity workflows
- your AI engineering shell environment

---

# Philosophy

Professional engineers rarely use:
- complicated shell scripts
- hundreds of commands
- bloated workflows

Instead they master:
- navigation
- searching
- Git
- Python environments
- project workflows
- shell productivity

The goal is:

```text
speed + clarity + repeatability
```

---

# Your Terminal Environment

Your setup already includes:

| Component | Purpose |
|---|---|
| WezTerm | terminal emulator |
| ZSH | shell |
| Starship | prompt |
| eza | modern ls |
| bat | modern cat |
| zoxide | smart cd |
| fzf | fuzzy search |
| ripgrep | fast search |
| fd | fast find |
| uv | Python package/project manager |
| Git | version control |
| Cursor | editor |

---

# 1. Navigation Workflows

---

# Show Current Directory

```bash
pwd
```

Example:

```text
/Volumes/Ai Agents/Developer/ai-learning-lab
```

---

# List Files

```bash
ls
```

Your environment automatically uses:

```text
eza
```

behind the scenes.

---

# Long File Listing

```bash
ll
```

Shows:
- permissions
- file sizes
- modification dates
- icons

---

# Full File Listing

```bash
lla
```

Includes hidden files.

---

# Tree View

```bash
lt
```

Shows project structure visually.

Very useful for:
- AI repositories
- Python projects
- documentation
- debugging

---

# Git-Aware Listing

```bash
lg
```

Shows:
- files
- Git status
- icons

---

# Change Directory

```bash
cd folder-name
```

Example:

```bash
cd guides
```

---

# Go Back One Directory

```bash
..
```

Equivalent to:

```bash
cd ..
```

---

# Go Back Two Directories

```bash
...
```

---

# Go Back Three Directories

```bash
....
```

---

# Jump to Developer Folder

```bash
dev
```

Equivalent to:

```bash
cd "/Volumes/Ai Agents/Developer"
```

---

# Jump to AI Learning Lab

```bash
lab
```

Equivalent to:

```bash
cd "/Volumes/Ai Agents/Developer/ai-learning-lab"
```

---

# Smart Navigation with `zoxide`

```bash
z lab
```

or:

```bash
z guides
```

or:

```bash
z python
```

Much faster than normal `cd`.

---

# Show Learned Directories

```bash
zoxide query -ls
```

---

# 2. File and Directory Workflows

---

# Create File

```bash
touch README.md
```

---

# Create Directory

```bash
mkdir notebooks
```

---

# Create Nested Directories

```bash
mkdir -p src/utils/helpers
```

---

# Remove File

```bash
rm file.txt
```

Your environment safely asks for confirmation.

---

# Remove Directory

```bash
rm -r folder-name
```

Be careful.

---

# Copy File

```bash
cp source.txt destination.txt
```

---

# Move or Rename File

```bash
mv old.txt new.txt
```

---

# View File Contents

```bash
cat file.py
```

Your environment automatically uses:

```text
bat
```

with syntax highlighting.

---

# Preview Config Files

```bash
preview ~/.zshrc
```

---

# Open Current Folder in Cursor

```bash
c.
```

Equivalent to:

```bash
cursor .
```

---

# Open `.zshrc`

```bash
zshconfig
```

---

# 3. Search and Productivity Workflows

---

# Search Entire Project

```bash
rg "LangChain"
```

Searches recursively.

Very fast.

---

# Search TODO Comments

```bash
rg "TODO"
```

---

# Find Files

```bash
fd pyproject
```

---

# Find Markdown Files

```bash
fd -e md
```

---

# Find Python Files

```bash
fd -e py
```

---

# Fuzzy Command History Search

Keyboard shortcut:

```text
CTRL + R
```

One of the most important productivity tools.

---

# Fuzzy File Search

Keyboard shortcut:

```text
CTRL + T
```

---

# Fuzzy Directory Jump

Keyboard shortcut:

```text
ALT + C
```

---

# Show PATH

```bash
path
```

Displays all PATH entries line-by-line.

---

# Clear Terminal

```bash
c
```

or:

```text
CTRL + L
```

---

# Reload `.zshrc`

```bash
reload
```

Equivalent to:

```bash
source ~/.zshrc
```

---

# 4. Git Workflows

---

# Check Git Status

```bash
gs
```

Equivalent to:

```bash
git status
```

---

# Add File

```bash
ga file.py
```

---

# Add All Files

```bash
gaa
```

---

# Commit Changes

```bash
gc "message"
```

Example:

```bash
gc "add wezterm guide"
```

---

# Push Changes

```bash
gp
```

---

# Pull Changes

```bash
gpl
```

---

# View Branches

```bash
gb
```

---

# Create New Branch

```bash
gcb feature-name
```

---

# Checkout Branch

```bash
gco main
```

---

# View Diff

```bash
gd
```

---

# View Staged Diff

```bash
gds
```

---

# View Git History Graph

```bash
glog
```

One of the most useful Git visualizations.

---

# Amend Previous Commit

```bash
amend
```

---

# Unstage Files

```bash
unstage
```

---

# Discard Changes

```bash
discard file.py
```

Be careful.

---

# 5. Python and uv Workflows

---

# Check Python Version

```bash
python --version
```

or:

```bash
py --version
```

---

# Create Virtual Environment

```bash
venv
```

Equivalent to:

```bash
python3 -m venv .venv
```

---

# Activate Virtual Environment

```bash
activate
```

Equivalent to:

```bash
source .venv/bin/activate
```

---

# Upgrade pip Tooling

```bash
pipup
```

---

# Initialize New uv Project

```bash
uvi
```

Equivalent to:

```bash
uv init
```

---

# Sync Dependencies

```bash
uvs
```

Equivalent to:

```bash
uv sync
```

---

# Add Package

```bash
uva requests
```

Equivalent to:

```bash
uv add requests
```

---

# Add Development Package

```bash
uvd pytest
```

Equivalent to:

```bash
uv add --dev pytest
```

---

# Remove Package

```bash
uvr requests
```

---

# Run Python Using uv

```bash
uvp main.py
```

Equivalent to:

```bash
uv run python main.py
```

---

# Run Generic uv Command

```bash
uvxrun command
```

---

# Lock Dependencies

```bash
uvl
```

Equivalent to:

```bash
uv lock
```

---

# Show Dependency Tree

```bash
uvt
```

Equivalent to:

```bash
uv tree
```

---

# Freeze Dependencies

```bash
uvf
```

Equivalent to:

```bash
uv pip freeze
```

---

# Clean uv Cache

```bash
uvc
```

---

# 6. AI Engineering Project Workflows

---

# Create New Python Project

```bash
mkpyproject my-project
```

Automatically creates:
- uv project
- src folder
- notebooks
- tests
- docs
- README
- `.gitignore`

and opens Cursor.

---

# Create New AI Lab

```bash
newlab my-lab
```

Creates a full AI engineering structure.

---

# Explore Repository Structure

```bash
lt
```

---

# Search AI Codebase

```bash
rg "OpenAI"
```

---

# Find Config Files

```bash
fd toml
```

---

# View Configs Beautifully

```bash
bat ~/.zshrc
```

---

# 7. Networking and Utility Workflows

---

# Show Open Ports

```bash
ports
```

Useful for:
- FastAPI
- Jupyter
- AI servers
- Docker
- local APIs

---

# Show Local IP Address

```bash
myip
```

---

# Start Local HTTP Server

```bash
serve
```

Equivalent to:

```bash
python3 -m http.server
```

---

# 8. Terminal Productivity Shortcuts

| Shortcut | Action |
|---|---|
| `CTRL + A` | move to line start |
| `CTRL + E` | move to line end |
| `CTRL + U` | clear before cursor |
| `CTRL + K` | clear after cursor |
| `CTRL + W` | delete previous word |
| `CTRL + L` | clear screen |
| `CTRL + R` | fuzzy history search |
| `TAB` | autocomplete |
| `↑` / `↓` | command history |

---

# 9. Daily AI Engineering Workflow Example

Typical professional session:

```bash
lab
ll
uvs
cursor .
rg "TODO"
gs
glog
```

---

# 10. Most Important Commands to Master

Focus heavily on these:

```bash
z
ll
lt
rg
fd
bat
gs
glog
uvs
uvp
CTRL + R
```

These provide the biggest productivity gains.

---

# Common Mistakes

---

# Using `rm -rf` Carelessly

Dangerous command:

```bash
rm -rf folder
```

Always verify current directory first:

```bash
pwd
```

---

# Forgetting Virtual Environments

Always verify Python version:

```bash
python --version
```

inside projects.

---

# Searching with `grep` Instead of `rg`

Prefer:

```bash
rg
```

for modern codebases.

---

# Using Mouse Too Much

Professional terminal workflows minimize:
- mouse usage
- trackpad usage

Learn:
- fuzzy search
- shortcuts
- pane navigation

---

# Final Checklist

Before moving to the next guide:

- [ ] aliases work
- [ ] Git aliases work
- [ ] uv aliases work
- [ ] `zoxide` works
- [ ] `fzf` shortcuts work
- [ ] `rg` works
- [ ] `fd` works
- [ ] project helper functions work
- [ ] terminal productivity shortcuts understood

---

# Recommended Commands to Practice Daily

```bash
lab
ll
lt
gs
glog
uvs
uvt
rg "TODO"
fd pyproject
reload
```

---

# Next Guide

Next:

```text
11-git-and-github-workflow.md
```

The next guide will cover:

- Git fundamentals
- GitHub workflows
- branching strategies
- commits
- pull requests
- SSH authentication
- professional repository management