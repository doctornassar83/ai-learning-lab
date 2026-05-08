# Professional ZSH Configuration for AI Engineering on macOS

> File Name:
>
> `09-zsh-professional-configuration.md`

---

# Purpose of This Guide

This guide builds a professional `.zshrc` configuration for a modern AI engineering environment on macOS.

This configuration is designed for:

- macOS development
- Homebrew-based tooling
- WezTerm or Terminal.app
- Cursor editor
- Python development
- `uv` package management
- Git workflows
- AI engineering projects
- clean terminal productivity
- safe shell behavior

By the end of this guide, you will have a robust, safe, and maintainable ZSH configuration suitable for professional AI development.

---

# Prerequisites

Before applying this guide, you should already have completed:

```text
01-macos/
├── 01-macos-overview.md
├── 02-important-macos-settings.md
├── 03-xcode-cli-tools.md
├── 04-homebrew-guide.md

02-terminal/
├── 05-zsh-basics.md
├── 06-wezterm-setup.md
├── 07-starship-prompt.md
├── 08-modern-terminal-utilities.md
```

You should already have:

- macOS configured
- Xcode Command Line Tools installed
- Homebrew installed
- basic ZSH knowledge
- Cursor installed
- WezTerm installed or planned
- Python and `uv` planned or installed

---

# What Is `.zshrc`?

The `.zshrc` file is the main configuration file loaded when you open an interactive ZSH terminal session.

Location:

```text
~/.zshrc
```

This file controls:

- shell behavior
- aliases
- environment variables
- command history
- completion behavior
- prompt appearance
- plugin loading
- PATH configuration
- Python workflow shortcuts
- Git shortcuts
- AI project helpers

---

# Why This Configuration Matters

A professional AI engineering environment depends heavily on terminal efficiency.

You will repeatedly use the terminal for:

- creating projects
- managing Python environments
- running scripts
- using `uv`
- installing packages
- managing Git repositories
- launching Cursor
- running local servers
- working with notebooks
- connecting to servers
- managing AI/ML tools

A clean `.zshrc` makes these workflows faster, safer, and easier to reproduce.

---

# Design Philosophy

This configuration follows five principles.

## 1. Safety

Commands such as `rm`, `cp`, and `mv` are made interactive to reduce accidental file loss.

## 2. Performance

Completion caching is used to reduce terminal startup overhead.

## 3. Reliability

Tools are loaded only if they exist, preventing broken shell startup.

## 4. Professional Workflow

Aliases are optimized for Git, Python, `uv`, Cursor, and AI project development.

## 5. Maintainability

The file is divided into clean sections with clear comments.

---

# Recommended Tools Used

This `.zshrc` supports the following tools:

| Tool | Purpose |
|---|---|
| Homebrew | macOS package manager |
| Starship | modern terminal prompt |
| zsh-syntax-highlighting | command syntax highlighting |
| zsh-autosuggestions | inline command suggestions |
| eza | modern `ls` replacement |
| bat | better file preview |
| zoxide | smart directory navigation |
| Git | version control |
| Python 3 | programming language |
| uv | Python package and project manager |
| Cursor | AI-first code editor |

---

# Install Required Terminal Tools

Run this command before applying the full configuration:

```bash
brew install starship zsh-syntax-highlighting zsh-autosuggestions eza bat zoxide
```

Optional but recommended:

```bash
brew install git uv
```

Check that the tools are installed:

```bash
starship --version
eza --version
bat --version
zoxide --version
uv --version
git --version
```

---

# Back Up Your Existing `.zshrc`

Before replacing your current configuration, create a backup.

```bash
cp ~/.zshrc ~/.zshrc.backup
```

If you want a timestamped backup:

```bash
cp ~/.zshrc ~/.zshrc.backup.$(date +%Y%m%d-%H%M%S)
```

Confirm the backup exists:

```bash
ls -la ~/.zshrc*
```

---

# Open `.zshrc` in Cursor

Open your `.zshrc` file:

```bash
cursor ~/.zshrc
```

If the file does not exist:

```bash
touch ~/.zshrc
cursor ~/.zshrc
```

---

# Final Professional `.zshrc`

Copy the full configuration below into:

```text
~/.zshrc
```

```zsh
# ============================================================
# ZSH Configuration for Professional AI Engineering
# macOS + Homebrew + Cursor + Python + uv + Git
# ============================================================


# ------------------------------------------------------------
# Safety / Shell Behavior
# ------------------------------------------------------------

setopt AUTO_CD
setopt INTERACTIVE_COMMENTS
setopt HIST_IGNORE_DUPS
setopt HIST_IGNORE_SPACE
setopt HIST_REDUCE_BLANKS
setopt SHARE_HISTORY
setopt INC_APPEND_HISTORY

HISTSIZE=50000
SAVEHIST=50000
HISTFILE="$HOME/.zsh_history"


# ------------------------------------------------------------
# Homebrew
# ------------------------------------------------------------

if [[ -x /opt/homebrew/bin/brew ]]; then
  eval "$(/opt/homebrew/bin/brew shellenv)"
elif [[ -x /usr/local/bin/brew ]]; then
  eval "$(/usr/local/bin/brew shellenv)"
fi

if command -v brew >/dev/null 2>&1; then
  BREW_PREFIX="$(brew --prefix)"
fi


# ------------------------------------------------------------
# ZSH Completion System
# ------------------------------------------------------------

autoload -Uz compinit

ZSH_COMPDUMP="${ZDOTDIR:-$HOME}/.zcompdump"

if [[ -n "$ZSH_COMPDUMP"(#qN.mh+24) ]]; then
  compinit -d "$ZSH_COMPDUMP"
else
  compinit -C -d "$ZSH_COMPDUMP"
fi

setopt AUTO_MENU
setopt AUTO_LIST
unsetopt MENU_COMPLETE

zstyle ':completion:*' menu select
zstyle ':completion:*' matcher-list 'm:{a-zA-Z}={A-Za-z}'
zstyle ':completion:*' verbose yes
zstyle ':completion:*' group-name ''

zstyle ':completion:*:descriptions' format '%F{cyan}-- %d --%f'
zstyle ':completion:*:messages' format '%F{yellow}-- %d --%f'
zstyle ':completion:*:warnings' format '%F{red}-- no matches found --%f'


# ------------------------------------------------------------
# Environment Variables
# ------------------------------------------------------------

export EDITOR="cursor"
export VISUAL="cursor"

export PYTHONUNBUFFERED=1
export PYTHONDONTWRITEBYTECODE=1
export PIP_DISABLE_PIP_VERSION_CHECK=1
export PIP_REQUIRE_VIRTUALENV=false

export UV_LINK_MODE=copy

# Do not force TERM unless needed.
# Let WezTerm / terminal emulator set it automatically.
# export TERM="xterm-256color"


# ------------------------------------------------------------
# PATH Configuration
# ------------------------------------------------------------

path_prepend() {
  [[ -d "$1" ]] && [[ ":$PATH:" != *":$1:"* ]] && export PATH="$1:$PATH"
}

path_prepend "$HOME/.local/bin"
path_prepend "$HOME/bin"
path_prepend "$HOME/.cargo/bin"


# ------------------------------------------------------------
# Starship Prompt
# ------------------------------------------------------------

if command -v starship >/dev/null 2>&1; then
  eval "$(starship init zsh)"
fi


# ------------------------------------------------------------
# ZSH Syntax Highlighting
# ------------------------------------------------------------

if [[ -n "$BREW_PREFIX" ]]; then
  ZSH_SYNTAX_FILE="$BREW_PREFIX/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh"

  if [[ -f "$ZSH_SYNTAX_FILE" ]]; then
    source "$ZSH_SYNTAX_FILE"

    (( ${+ZSH_HIGHLIGHT_STYLE} )) || typeset -A ZSH_HIGHLIGHT_STYLE
    ZSH_HIGHLIGHT_STYLE[path]=none
    ZSH_HIGHLIGHT_STYLE[path_prefix]=none
  fi
fi


# ------------------------------------------------------------
# ZSH Autosuggestions
# ------------------------------------------------------------

ZSH_AUTOSUGGEST_STRATEGY=(completion history)
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=#6c7086'
ZSH_AUTOSUGGEST_USE_ASYNC=true

if [[ -n "$BREW_PREFIX" ]]; then
  ZSH_AUTOSUGGEST_FILE="$BREW_PREFIX/share/zsh-autosuggestions/zsh-autosuggestions.zsh"

  if [[ -f "$ZSH_AUTOSUGGEST_FILE" ]]; then
    source "$ZSH_AUTOSUGGEST_FILE"
  fi
fi


# ------------------------------------------------------------
# Modern Terminal Utilities
# ------------------------------------------------------------

if command -v eza >/dev/null 2>&1; then
  alias ls="eza --icons --group-directories-first"
  alias l="eza --icons --group-directories-first"
  alias la="eza --icons --group-directories-first -la"
  alias ll="eza --icons --group-directories-first -lh"
  alias lla="eza --icons --group-directories-first -lha"
  alias tree="eza --tree --icons --group-directories-first"
else
  alias ll="ls -lh"
  alias la="ls -la"
fi

if command -v bat >/dev/null 2>&1; then
  alias bcat="bat"
  alias preview="bat"
  alias cat="bat --paging=never"
fi

if command -v zoxide >/dev/null 2>&1; then
  eval "$(zoxide init zsh)"
fi


# ------------------------------------------------------------
# Navigation Aliases
# ------------------------------------------------------------

alias ..="cd .."
alias ...="cd ../.."
alias ....="cd ../../.."

alias dev='cd "/Volumes/Ai Agents/Developer"'
alias lab='cd "/Volumes/Ai Agents/Developer/ai-learning-lab"'


# ------------------------------------------------------------
# Utility Aliases
# ------------------------------------------------------------

alias c="clear"
alias cls="clear"

alias reload="source ~/.zshrc"
alias zshconfig="cursor ~/.zshrc"

alias path="echo $PATH | tr ':' '\n'"
alias ports="lsof -i -P -n | grep LISTEN"
alias myip="ipconfig getifaddr en0"

alias serve="python3 -m http.server"


# ------------------------------------------------------------
# Safe File Operations
# ------------------------------------------------------------

alias rm="rm -i"
alias cp="cp -i"
alias mv="mv -i"


# ------------------------------------------------------------
# Git Aliases
# ------------------------------------------------------------

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


# ------------------------------------------------------------
# Python Aliases
# ------------------------------------------------------------

alias py="python3"
alias python="python3"

alias venv="python3 -m venv .venv"
alias activate="source .venv/bin/activate"

alias pipup="python3 -m pip install --upgrade pip setuptools wheel"


# ------------------------------------------------------------
# uv Aliases
# ------------------------------------------------------------

alias uvi="uv init"
alias uvs="uv sync"
alias uva="uv add"
alias uvd="uv add --dev"
alias uvr="uv remove"

alias uvp="uv run python"
alias uvxrun="uv run"

alias uvl="uv lock"
alias uvt="uv tree"
alias uvf="uv pip freeze"

alias uvc="uv cache clean"


# ------------------------------------------------------------
# AI / Python Project Helpers
# ------------------------------------------------------------

mkpyproject() {
  mkdir -p "$1"
  cd "$1" || return
  uv init
  mkdir -p src notebooks data tests assets docs
  touch README.md .env.example .gitignore
  cursor .
}

newlab() {
  mkdir -p "/Volumes/Ai Agents/Developer/$1"
  cd "/Volumes/Ai Agents/Developer/$1" || return
  uv init
  mkdir -p guides assets notebooks src tests data
  touch README.md .env.example .gitignore
  cursor .
}


# ------------------------------------------------------------
# Cursor Aliases
# ------------------------------------------------------------

alias code="cursor"
alias c.="cursor ."


# ------------------------------------------------------------
# Final Cleanup
# ------------------------------------------------------------

unset ZSH_SYNTAX_FILE
unset ZSH_AUTOSUGGEST_FILE
```

---

# Apply the Configuration

After saving the file, reload ZSH:

```bash
source ~/.zshrc
```

Alternative:

```bash
exec zsh
```

If the terminal opens without errors, the configuration loaded successfully.

---

# Step-by-Step Explanation

---

# Section 1: Safety and Shell Behavior

```zsh
setopt AUTO_CD
setopt INTERACTIVE_COMMENTS
setopt HIST_IGNORE_DUPS
setopt HIST_IGNORE_SPACE
setopt HIST_REDUCE_BLANKS
setopt SHARE_HISTORY
setopt INC_APPEND_HISTORY
```

## What This Does

| Option | Meaning |
|---|---|
| `AUTO_CD` | Allows entering a directory name directly without typing `cd` |
| `INTERACTIVE_COMMENTS` | Allows comments in interactive terminal commands |
| `HIST_IGNORE_DUPS` | Avoids saving duplicate history entries |
| `HIST_IGNORE_SPACE` | Commands starting with a space are not saved in history |
| `HIST_REDUCE_BLANKS` | Removes unnecessary blanks from command history |
| `SHARE_HISTORY` | Shares history between open terminal sessions |
| `INC_APPEND_HISTORY` | Saves commands immediately instead of only on shell exit |

## Why It Matters

For AI development, you may have multiple terminals open:

- one for Python scripts
- one for Git
- one for Jupyter
- one for servers
- one for package management

Shared and clean history makes your workflow more reliable.

---

# Section 2: History Configuration

```zsh
HISTSIZE=50000
SAVEHIST=50000
HISTFILE="$HOME/.zsh_history"
```

## What This Does

This allows ZSH to store a large command history.

This is useful because AI engineering work involves many repeated commands:

- `uv sync`
- `uv run python`
- `git status`
- `jupyter lab`
- `python scripts`
- `docker compose`
- `ssh`

A large history makes command recall much more powerful.

---

# Section 3: Homebrew Initialization

```zsh
if [[ -x /opt/homebrew/bin/brew ]]; then
  eval "$(/opt/homebrew/bin/brew shellenv)"
elif [[ -x /usr/local/bin/brew ]]; then
  eval "$(/usr/local/bin/brew shellenv)"
fi
```

## What This Does

This supports both major Homebrew installation paths.

| Mac Type | Homebrew Path |
|---|---|
| Apple Silicon | `/opt/homebrew/bin/brew` |
| Intel Mac | `/usr/local/bin/brew` |

This makes the file portable across different Macs.

---

# Section 4: Homebrew Prefix Detection

```zsh
if command -v brew >/dev/null 2>&1; then
  BREW_PREFIX="$(brew --prefix)"
fi
```

## What This Does

This stores the active Homebrew prefix in:

```text
BREW_PREFIX
```

Example on Apple Silicon:

```text
/opt/homebrew
```

This allows plugins to be loaded reliably.

---

# Section 5: ZSH Completion System

```zsh
autoload -Uz compinit
```

This loads ZSH's completion system.

```zsh
ZSH_COMPDUMP="${ZDOTDIR:-$HOME}/.zcompdump"
```

This defines where the completion cache is stored.

```zsh
if [[ -n "$ZSH_COMPDUMP"(#qN.mh+24) ]]; then
  compinit -d "$ZSH_COMPDUMP"
else
  compinit -C -d "$ZSH_COMPDUMP"
fi
```

## What This Does

This uses a cached completion dump to make terminal startup faster.

## Why It Matters

Without caching, ZSH can become slower as you add more tools and completions.

For a professional AI environment, you want shell startup to remain fast.

---

# Section 6: Completion Behavior

```zsh
setopt AUTO_MENU
setopt AUTO_LIST
unsetopt MENU_COMPLETE
```

## What This Does

These options improve how autocomplete behaves.

| Option | Meaning |
|---|---|
| `AUTO_MENU` | Shows a completion menu |
| `AUTO_LIST` | Lists possible completions |
| `unsetopt MENU_COMPLETE` | Avoids instantly inserting first match |

This gives you a more predictable completion workflow.

---

# Section 7: Completion Styling

```zsh
zstyle ':completion:*' menu select
zstyle ':completion:*' matcher-list 'm:{a-zA-Z}={A-Za-z}'
zstyle ':completion:*' verbose yes
zstyle ':completion:*' group-name ''
```

## What This Does

This makes completions:

- selectable
- case-insensitive
- grouped
- verbose

Example:

```bash
cd doc
```

can match:

```text
Documents
```

---

# Section 8: Completion Message Colors

```zsh
zstyle ':completion:*:descriptions' format '%F{cyan}-- %d --%f'
zstyle ':completion:*:messages' format '%F{yellow}-- %d --%f'
zstyle ':completion:*:warnings' format '%F{red}-- no matches found --%f'
```

## What This Does

This formats completion descriptions, messages, and warnings with readable colors.

---

# Section 9: Editor Variables

```zsh
export EDITOR="cursor"
export VISUAL="cursor"
```

## What This Does

This tells command-line programs to use Cursor as your default editor.

Tools that may use this:

- Git
- shell commands
- Python tools
- CLI utilities

Example:

```bash
git commit
```

can open Cursor for the commit message editor.

---

# Section 10: Python Environment Variables

```zsh
export PYTHONUNBUFFERED=1
export PYTHONDONTWRITEBYTECODE=1
export PIP_DISABLE_PIP_VERSION_CHECK=1
export PIP_REQUIRE_VIRTUALENV=false
```

## What These Do

| Variable | Purpose |
|---|---|
| `PYTHONUNBUFFERED=1` | Prints Python output immediately |
| `PYTHONDONTWRITEBYTECODE=1` | Prevents creation of `__pycache__` files |
| `PIP_DISABLE_PIP_VERSION_CHECK=1` | Removes pip version check noise |
| `PIP_REQUIRE_VIRTUALENV=false` | Allows pip outside venv |

## Professional Note

For strict production workflows, some developers set:

```zsh
export PIP_REQUIRE_VIRTUALENV=true
```

However, for a flexible learning and AI lab environment, `false` is more convenient.

---

# Section 11: uv Environment Variable

```zsh
export UV_LINK_MODE=copy
```

## What This Does

This tells `uv` to copy packages instead of hardlinking them.

This is useful when projects live on external volumes or cross-filesystem locations.

For your structure using:

```text
/Volumes/Ai Agents/Developer
```

this is a sensible default.

---

# Section 12: TERM Variable

```zsh
# export TERM="xterm-256color"
```

## Why It Is Commented Out

You should usually allow your terminal emulator to set `TERM`.

This avoids compatibility problems with:

- WezTerm
- SSH
- terminal themes
- color rendering
- remote systems

Only enable it if you encounter a specific terminal compatibility issue.

---

# Section 13: PATH Helper Function

```zsh
path_prepend() {
  [[ -d "$1" ]] && [[ ":$PATH:" != *":$1:"* ]] && export PATH="$1:$PATH"
}
```

## What This Does

This function safely adds directories to the beginning of `PATH`.

It checks that:

- the directory exists
- the directory is not already in `PATH`

This prevents duplicate PATH entries.

---

# Section 14: PATH Entries

```zsh
path_prepend "$HOME/.local/bin"
path_prepend "$HOME/bin"
path_prepend "$HOME/.cargo/bin"
```

## What These Paths Are For

| Path | Purpose |
|---|---|
| `$HOME/.local/bin` | User-installed CLI tools |
| `$HOME/bin` | Personal scripts |
| `$HOME/.cargo/bin` | Rust/Cargo-installed tools |

This keeps local developer tools discoverable.

---

# Section 15: Starship Prompt

```zsh
if command -v starship >/dev/null 2>&1; then
  eval "$(starship init zsh)"
fi
```

## What This Does

This initializes Starship only if it is installed.

Starship provides a modern prompt showing useful project context such as:

- current directory
- Git branch
- Python environment
- package version
- command status
- execution time

## Why This Is Professional

A good prompt gives you context without needing extra commands.

---

# Section 16: Syntax Highlighting

```zsh
if [[ -n "$BREW_PREFIX" ]]; then
  ZSH_SYNTAX_FILE="$BREW_PREFIX/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh"

  if [[ -f "$ZSH_SYNTAX_FILE" ]]; then
    source "$ZSH_SYNTAX_FILE"

    (( ${+ZSH_HIGHLIGHT_STYLE} )) || typeset -A ZSH_HIGHLIGHT_STYLE
    ZSH_HIGHLIGHT_STYLE[path]=none
    ZSH_HIGHLIGHT_STYLE[path_prefix]=none
  fi
fi
```

## What This Does

This loads ZSH syntax highlighting safely.

Syntax highlighting helps detect:

- invalid commands
- valid commands
- quoted strings
- paths
- shell syntax issues

## Why Path Underline Is Disabled

```zsh
ZSH_HIGHLIGHT_STYLE[path]=none
ZSH_HIGHLIGHT_STYLE[path_prefix]=none
```

This removes underlined path styling, producing a cleaner terminal appearance.

---

# Section 17: Autosuggestions

```zsh
ZSH_AUTOSUGGEST_STRATEGY=(completion history)
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=#6c7086'
ZSH_AUTOSUGGEST_USE_ASYNC=true
```

## What This Does

Autosuggestions show predicted commands while typing.

Suggestions are based on:

- completions
- command history

The suggestion color is a muted gray.

Async mode helps avoid terminal lag.

---

# Section 18: Loading Autosuggestions

```zsh
if [[ -n "$BREW_PREFIX" ]]; then
  ZSH_AUTOSUGGEST_FILE="$BREW_PREFIX/share/zsh-autosuggestions/zsh-autosuggestions.zsh"

  if [[ -f "$ZSH_AUTOSUGGEST_FILE" ]]; then
    source "$ZSH_AUTOSUGGEST_FILE"
  fi
fi
```

## What This Does

This safely loads autosuggestions only if the plugin file exists.

This prevents shell errors if the package is not installed.

---

# Section 19: Modern `ls` With `eza`

```zsh
if command -v eza >/dev/null 2>&1; then
  alias ls="eza --icons --group-directories-first"
  alias l="eza --icons --group-directories-first"
  alias la="eza --icons --group-directories-first -la"
  alias ll="eza --icons --group-directories-first -lh"
  alias lla="eza --icons --group-directories-first -lha"
  alias tree="eza --tree --icons --group-directories-first"
else
  alias ll="ls -lh"
  alias la="ls -la"
fi
```

## What This Does

If `eza` exists, it replaces traditional `ls` with a more readable version.

Benefits:

- icons
- directory grouping
- better formatting
- tree view

## Aliases

| Alias | Meaning |
|---|---|
| `ls` | enhanced directory listing |
| `l` | short listing |
| `la` | all files including hidden |
| `ll` | long human-readable format |
| `lla` | long format including hidden |
| `tree` | directory tree view |

---

# Section 20: Better File Preview With `bat`

```zsh
if command -v bat >/dev/null 2>&1; then
  alias bcat="bat"
  alias preview="bat"
  alias cat="bat --paging=never"
fi
```

## What This Does

`bat` is a modern alternative to `cat`.

It provides:

- syntax highlighting
- line numbers
- Git integration
- better readability

## Professional Note

This aliases `cat` to `bat --paging=never`.

If you ever need original `cat`, use:

```bash
command cat filename.txt
```

or:

```bash
/bin/cat filename.txt
```

---

# Section 21: Smart Directory Navigation With `zoxide`

```zsh
if command -v zoxide >/dev/null 2>&1; then
  eval "$(zoxide init zsh)"
fi
```

## What This Does

`zoxide` remembers directories you visit frequently.

Instead of typing full paths, you can jump using partial names.

Example:

```bash
z lab
```

However, `zoxide` only works after it has learned directories you have visited.

Your direct aliases still remain useful:

```bash
lab
dev
```

---

# Section 22: Navigation Aliases

```zsh
alias ..="cd .."
alias ...="cd ../.."
alias ....="cd ../../.."

alias dev='cd "/Volumes/Ai Agents/Developer"'
alias lab='cd "/Volumes/Ai Agents/Developer/ai-learning-lab"'
```

## What This Does

These aliases speed up navigation.

| Alias | Destination |
|---|---|
| `..` | parent folder |
| `...` | two levels up |
| `....` | three levels up |
| `dev` | main Developer folder |
| `lab` | AI learning lab project |

This is especially helpful because your development folder lives on an external volume path with spaces.

---

# Section 23: Utility Aliases

```zsh
alias c="clear"
alias cls="clear"

alias reload="source ~/.zshrc"
alias zshconfig="cursor ~/.zshrc"

alias path="echo $PATH | tr ':' '\n'"
alias ports="lsof -i -P -n | grep LISTEN"
alias myip="ipconfig getifaddr en0"

alias serve="python3 -m http.server"
```

## What These Do

| Alias | Purpose |
|---|---|
| `c` | clear terminal |
| `cls` | clear terminal |
| `reload` | reload `.zshrc` |
| `zshconfig` | open `.zshrc` in Cursor |
| `path` | show PATH entries line by line |
| `ports` | show listening ports |
| `myip` | show Wi-Fi IP address |
| `serve` | start local HTTP server |

---

# Section 24: Safe File Operations

```zsh
alias rm="rm -i"
alias cp="cp -i"
alias mv="mv -i"
```

## What This Does

These aliases ask for confirmation before destructive or overwriting operations.

Examples:

```bash
rm old_file.txt
```

will ask before deleting.

```bash
mv file.txt existing-file.txt
```

will ask before overwriting.

## Professional Note

This safety layer is useful for development machines.

For scripts, avoid relying on aliases. Use explicit commands.

---

# Section 25: Git Aliases

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

## What These Do

| Alias | Full Command |
|---|---|
| `g` | `git` |
| `gs` | `git status` |
| `ga` | `git add` |
| `gaa` | `git add --all` |
| `gc` | `git commit -m` |
| `gp` | `git push` |
| `gpl` | `git pull` |
| `gb` | `git branch` |
| `gco` | `git checkout` |
| `gcb` | `git checkout -b` |
| `gd` | `git diff` |
| `gds` | `git diff --staged` |
| `glog` | compact visual Git log |
| `amend` | amend last commit without editing message |
| `unstage` | remove files from staging |
| `discard` | restore changed files |

## Why `ga` Is Safer Than `git add .`

This configuration uses:

```zsh
alias ga="git add"
```

Instead of:

```zsh
alias ga="git add ."
```

This is safer because it forces you to intentionally choose what to stage.

Example:

```bash
ga README.md
```

For adding everything:

```bash
gaa
```

---

# Section 26: Python Aliases

```zsh
alias py="python3"
alias python="python3"

alias venv="python3 -m venv .venv"
alias activate="source .venv/bin/activate"

alias pipup="python3 -m pip install --upgrade pip setuptools wheel"
```

## What These Do

| Alias | Purpose |
|---|---|
| `py` | run Python 3 |
| `python` | force Python 3 |
| `venv` | create `.venv` |
| `activate` | activate `.venv` |
| `pipup` | upgrade pip tooling |

## Professional Note

For modern AI projects, prefer `uv` over manual `venv` and `pip`.

However, these aliases remain useful when working with older Python projects.

---

# Section 27: uv Aliases

```zsh
alias uvi="uv init"
alias uvs="uv sync"
alias uva="uv add"
alias uvd="uv add --dev"
alias uvr="uv remove"

alias uvp="uv run python"
alias uvxrun="uv run"

alias uvl="uv lock"
alias uvt="uv tree"
alias uvf="uv pip freeze"

alias uvc="uv cache clean"
```

## What These Do

| Alias | Full Command |
|---|---|
| `uvi` | `uv init` |
| `uvs` | `uv sync` |
| `uva` | `uv add` |
| `uvd` | `uv add --dev` |
| `uvr` | `uv remove` |
| `uvp` | `uv run python` |
| `uvxrun` | `uv run` |
| `uvl` | `uv lock` |
| `uvt` | `uv tree` |
| `uvf` | `uv pip freeze` |
| `uvc` | `uv cache clean` |

## Example Workflow

Create a new project:

```bash
uv init
```

Add dependencies:

```bash
uva langchain openai python-dotenv
```

Add development dependencies:

```bash
uvd pytest ruff ipykernel
```

Run Python:

```bash
uvp
```

Run a script:

```bash
uvxrun python main.py
```

Sync environment:

```bash
uvs
```

---

# Section 28: AI / Python Project Helper: `mkpyproject`

```zsh
mkpyproject() {
  mkdir -p "$1"
  cd "$1" || return
  uv init
  mkdir -p src notebooks data tests assets docs
  touch README.md .env.example .gitignore
  cursor .
}
```

## What This Does

This creates a new Python project folder with a professional structure.

Example:

```bash
mkpyproject rag-experiment
```

Creates:

```text
rag-experiment/
├── src/
├── notebooks/
├── data/
├── tests/
├── assets/
├── docs/
├── README.md
├── .env.example
├── .gitignore
└── pyproject.toml
```

Then it opens the project in Cursor.

---

# Section 29: AI Lab Helper: `newlab`

```zsh
newlab() {
  mkdir -p "/Volumes/Ai Agents/Developer/$1"
  cd "/Volumes/Ai Agents/Developer/$1" || return
  uv init
  mkdir -p guides assets notebooks src tests data
  touch README.md .env.example .gitignore
  cursor .
}
```

## What This Does

This creates a new AI lab project inside your main Developer directory.

Example:

```bash
newlab local-rag-agent
```

Creates:

```text
/Volumes/Ai Agents/Developer/local-rag-agent/
├── guides/
├── assets/
├── notebooks/
├── src/
├── tests/
├── data/
├── README.md
├── .env.example
├── .gitignore
└── pyproject.toml
```

Then it opens the project in Cursor.

## Important Note

This function assumes this path exists:

```text
/Volumes/Ai Agents/Developer
```

If your external drive is disconnected, the command will fail.

---

# Section 30: Cursor Aliases

```zsh
alias code="cursor"
alias c.="cursor ."
```

## What This Does

These aliases make Cursor behave like a standard code editor command.

| Alias | Purpose |
|---|---|
| `code` | opens Cursor like VS Code style command |
| `c.` | opens current folder in Cursor |

Example:

```bash
c.
```

opens the current project in Cursor.

---

# Section 31: Final Cleanup

```zsh
unset ZSH_SYNTAX_FILE
unset ZSH_AUTOSUGGEST_FILE
```

## What This Does

This removes temporary helper variables after startup.

It keeps the shell environment cleaner.

---

# Testing the Configuration

After running:

```bash
source ~/.zshrc
```

test each section.

---

## Test Homebrew

```bash
brew --version
```

---

## Test Starship

```bash
starship --version
```

---

## Test eza

```bash
ls
ll
la
tree
```

---

## Test bat

```bash
preview ~/.zshrc
```

---

## Test zoxide

First visit your lab folder:

```bash
lab
```

Then go home:

```bash
cd ~
```

Then try:

```bash
z ai-learning-lab
```

If it does not work immediately, visit the folder a few times so `zoxide` can learn it.

---

## Test Git Aliases

Inside a Git project:

```bash
gs
glog
gd
```

---

## Test Python

```bash
py --version
python --version
```

---

## Test uv

```bash
uv --version
uvt
```

---

## Test Cursor

```bash
c.
```

---

# Common Errors and Fixes

---

# Error: `command not found: brew`

## Cause

Homebrew is not installed or not properly added to PATH.

## Fix

Install Homebrew first, then reopen the terminal.

---

# Error: `command not found: starship`

## Cause

Starship is not installed.

## Fix

```bash
brew install starship
```

---

# Error: `command not found: eza`

## Cause

`eza` is not installed.

## Fix

```bash
brew install eza
```

---

# Error: `command not found: bat`

## Cause

`bat` is not installed.

## Fix

```bash
brew install bat
```

---

# Error: `command not found: zoxide`

## Cause

`zoxide` is not installed.

## Fix

```bash
brew install zoxide
```

---

# Error: `zoxide: no match found`

## Cause

`zoxide` has not learned that directory yet.

## Fix

Visit the directory first:

```bash
cd "/Volumes/Ai Agents/Developer/ai-learning-lab"
```

Then later try:

```bash
z lab
```

You can always use your direct alias:

```bash
lab
```

---

# Error: Cursor Does Not Open

## Cause

The `cursor` command is not installed in your shell PATH.

## Fix

Open Cursor, then install the shell command from Cursor’s command palette.

Typical workflow:

```text
Cursor → Command Palette → Shell Command: Install 'cursor' command in PATH
```

Then restart the terminal.

---

# Error: `.zshrc` Reload Shows Syntax Error

## Cause

There is likely a copy/paste issue.

Common causes:

- missing quote
- missing `fi`
- missing `}`
- smart quotes instead of normal quotes
- accidental markdown formatting copied into `.zshrc`

## Fix

Open the file:

```bash
cursor ~/.zshrc
```

Check the line number shown in the error.

---

# Error: External Volume Path Does Not Work

## Cause

The external drive is not mounted.

Expected path:

```text
/Volumes/Ai Agents/Developer
```

## Fix

Connect or mount the drive.

Then test:

```bash
ls "/Volumes/Ai Agents/Developer"
```

---

# Maintenance Rules

## Rule 1: Keep `.zshrc` Organized

Always add new settings under the correct section.

Good:

```zsh
# ------------------------------------------------------------
# Docker Aliases
# ------------------------------------------------------------
```

Bad:

```zsh
alias randomthing="something"
```

in the middle of unrelated code.

---

## Rule 2: Always Check If a Tool Exists

Professional pattern:

```zsh
if command -v toolname >/dev/null 2>&1; then
  alias example="toolname command"
fi
```

This prevents shell startup errors.

---

## Rule 3: Avoid Heavy Startup Commands

Do not put slow commands directly into `.zshrc`.

Avoid:

```zsh
brew update
```

Avoid:

```zsh
conda activate something
```

Avoid:

```zsh
python some_script.py
```

The terminal should start quickly.

---

## Rule 4: Avoid Secrets in `.zshrc`

Do not store API keys directly in `.zshrc`.

Avoid:

```zsh
export OPENAI_API_KEY="secret-key"
```

Better:

```text
.env
```

or a secrets manager.

This protects:

- OpenAI keys
- GitHub tokens
- broker API keys
- Hugging Face tokens
- cloud credentials

---

## Rule 5: Back Up Before Major Changes

Before editing:

```bash
cp ~/.zshrc ~/.zshrc.backup.$(date +%Y%m%d-%H%M%S)
```

---

# Recommended Future Additions

After you become comfortable with this configuration, you can add guides for:

- Starship prompt customization
- WezTerm configuration
- GitHub SSH setup
- Python and `uv` workflow
- Docker setup
- Jupyter setup
- AI project templates
- environment variable management
- shell scripting basics
- terminal productivity with `fzf`
- terminal multiplexing with `tmux`

---

# Final Checklist

Before moving to the next guide, confirm:

- [ ] Homebrew loads correctly
- [ ] `.zshrc` reloads without errors
- [ ] Starship prompt works
- [ ] syntax highlighting works
- [ ] autosuggestions work
- [ ] `eza` replaces `ls`
- [ ] `bat` previews files
- [ ] `zoxide` initializes
- [ ] `lab` opens your AI learning lab
- [ ] `dev` opens your Developer directory
- [ ] Git aliases work
- [ ] Python aliases work
- [ ] `uv` aliases work
- [ ] Cursor opens from terminal
- [ ] no secrets are stored in `.zshrc`

---

# Next Guide

Next:

```text
10-common-terminal-commands.md
```

The next guide will configure WezTerm as a professional terminal emulator for AI engineering workflows.