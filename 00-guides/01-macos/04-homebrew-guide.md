> [!NOTE] For the best reading experience in Cursor, right-click the `.md` file tab or filename and select `Open Preview` (shortcut: `CMD + SHIFT + V`).

# Homebrew Guide for Professional AI Engineering on macOS

> Install and configure Homebrew professionally to manage developer tooling, Python environments, AI dependencies, terminal utilities, and modern macOS engineering workflows.

---

# Purpose

This guide installs and configures:

```text
Homebrew
```

the industry-standard package manager for macOS.

You will learn how to:

- install Homebrew correctly
- understand package management
- manage developer tools
- install terminal utilities
- update and maintain packages
- configure Homebrew professionally
- understand Apple Silicon Homebrew paths
- prepare macOS for AI engineering workflows

Homebrew becomes foundational infrastructure for your entire development environment.

---

# What Is Homebrew?

Homebrew is the most widely used package manager for macOS.

It allows developers to install software directly from the terminal.

Without Homebrew, installing development tools manually becomes:

- slow
- inconsistent
- difficult to maintain
- difficult to update

---

# Why Homebrew Matters for AI Engineering

Modern AI engineering requires many tools:

- Python
- Git
- FFmpeg
- databases
- CLI utilities
- shell enhancements
- AI runtimes
- Docker-related tooling

Homebrew standardizes installation and maintenance.

---

# What Homebrew Can Install

Examples:

| Category | Examples |
|---|---|
| Development Tools | Git, Python, Node.js |
| AI Utilities | Ollama, FFmpeg |
| Databases | PostgreSQL, Redis |
| Terminal Tools | eza, bat, fzf |
| Shell Enhancements | zsh-autosuggestions |
| Networking Tools | wget, curl |
| Productivity Tools | tmux, lazygit |

---

# Verify Xcode Command Line Tools First

Before installing Homebrew, ensure Xcode Command Line Tools are already installed.

Run:

```bash
xcode-select -p
```

Expected:

```text
/Library/Developer/CommandLineTools
```

If missing, complete:

```text
03-xcode-cli-tools.md
```

before continuing.

---

# Install Homebrew

Open:

```text
WezTerm
```

Run:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

---

# What This Command Does

The installer:

- downloads Homebrew
- installs package infrastructure
- configures directories
- prepares the package manager
- detects Apple Silicon architecture

---

# During Installation

You may be asked for:

- macOS password
- administrator access

This is normal.

---

# Apple Silicon Homebrew Location

On Apple Silicon Macs, Homebrew installs into:

```text
/opt/homebrew
```

This is the correct and modern location.

---

# Verify Installation

Run:

```bash
brew --version
```

Expected:

```text
Homebrew X.X.X
```

---

# Verify Homebrew Path

Run:

```bash
which brew
```

Expected:

```text
/opt/homebrew/bin/brew
```

This confirms the Apple Silicon version is installed correctly.

---

# Important Apple Silicon Note

Avoid Intel/Rosetta Homebrew installations.

Correct:

```text
/opt/homebrew
```

Incorrect legacy Intel path:

```text
/usr/local
```

---

# Add Homebrew to Shell Environment

Your `.zshrc` should include:

```bash
eval "$(/opt/homebrew/bin/brew shellenv)"
```

Open `.zshrc`:

```bash
zshconfig
```

Verify the line exists.

---

# Reload Shell

After installation:

```bash
source ~/.zshrc
```

or:

```bash
reload
```

---

# Verify Homebrew Environment

Run:

```bash
brew doctor
```

Expected:

```text
Your system is ready to brew.
```

This validates your Homebrew installation.

---

# What `brew doctor` Does

Checks for:

- broken configurations
- missing dependencies
- permission problems
- conflicting packages
- environment issues

Professional developers use this command frequently.

---

# Understanding Homebrew Terminology

| Term | Meaning |
|---|---|
| Formula | CLI package |
| Cask | GUI/macOS application |
| Tap | Additional package repository |
| Cellar | Installed package storage |
| Brewfile | Reproducible package list |

---

# Install Your First Package

Example:

```bash
brew install wget
```

---

# Verify Installation

Run:

```bash
wget --version
```

---

# Install GUI Applications

Homebrew can also install desktop apps.

Example:

```bash
brew install --cask wezterm
```

---

# Formula vs Cask

| Type | Usage |
|---|---|
| Formula | Terminal tools |
| Cask | GUI applications |

Examples:

| Package | Type |
|---|---|
| Git | Formula |
| Python | Formula |
| WezTerm | Cask |
| Cursor | Cask |
| Docker Desktop | Cask |

---

# Search Packages

Run:

```bash
brew search python
```

This searches available formulas and casks.

---

# Get Package Information

Run:

```bash
brew info python
```

Displays:

- version
- install path
- dependencies
- documentation

---

# Update Homebrew

Professional developers update Homebrew regularly.

Run:

```bash
brew update
```

This updates package definitions.

---

# Upgrade Installed Packages

Run:

```bash
brew upgrade
```

This upgrades installed packages.

---

# Cleanup Old Packages

Run:

```bash
brew cleanup
```

Removes:

- old package versions
- unnecessary caches
- unused files

---

# Recommended Maintenance Workflow

Monthly maintenance:

```bash
brew update
brew upgrade
brew cleanup
brew doctor
```

This keeps the environment stable and clean.

---

# Where Homebrew Stores Packages

Apple Silicon path:

```text
/opt/homebrew
```

Important directories:

| Directory | Purpose |
|---|---|
| `/opt/homebrew/bin` | Executables |
| `/opt/homebrew/etc` | Config files |
| `/opt/homebrew/Cellar` | Installed packages |
| `/opt/homebrew/share` | Shared resources |

---

# Understand PATH

Run:

```bash
echo $PATH
```

This tells the shell where to look for commands.

Because your `.zshrc` initializes Homebrew correctly, commands such as:

```bash
brew
git
python
starship
```

are automatically available.

---

# Recommended AI Engineering Packages

Later in the setup, you will install tools such as:

```bash
brew install git
brew install python
brew install uv
brew install fzf
brew install bat
brew install eza
brew install zoxide
brew install lazygit
```

and GUI apps:

```bash
brew install --cask wezterm
brew install --cask docker
```

---

# Recommended Terminal Tooling

These packages dramatically improve terminal workflows.

---

## `fzf`

Interactive fuzzy finder.

Useful for:

- searching history
- finding files
- project navigation

Install:

```bash
brew install fzf
```

---

## `eza`

Modern replacement for:

```bash
ls
```

Install:

```bash
brew install eza
```

Benefits:

- icons
- Git integration
- cleaner output

---

## `bat`

Modern replacement for:

```bash
cat
```

Install:

```bash
brew install bat
```

Benefits:

- syntax highlighting
- line numbers
- better readability

---

## `zoxide`

Smart directory jumping.

Install:

```bash
brew install zoxide
```

Example:

```bash
z ai
```

instead of manually typing long paths.

---

# Configure Premium Terminal Utilities

After installation, some tools require shell configuration to work properly.

---

# Configure `zoxide`

`zoxide` requires shell initialization before the `z` command becomes available.

Open `.zshrc`:

```bash
zshconfig
```

Add:

```bash
# ------------------------------------------------------------
# Zoxide
# ------------------------------------------------------------

eval "$(zoxide init zsh)"
```

---

# Configure `eza`

`eza` works immediately after installation, but aliases greatly improve usability.

Add to `.zshrc`:

```bash
# ------------------------------------------------------------
# Eza Aliases
# ------------------------------------------------------------

alias ls="eza --icons"
alias l="eza --icons"

alias la="eza --icons -la"
alias ll="eza --icons -lh"
alias lla="eza --icons -lha"
```

This upgrades:

```bash
ls
```

into a modern file viewer with:

- icons
- improved formatting
- cleaner output
- better readability

---

# Configure `bat`

`bat` also works immediately after installation.

Recommended alias:

```bash
# ------------------------------------------------------------
# Bat Alias
# ------------------------------------------------------------

alias cat="bat"
```

This upgrades:

```bash
cat
```

with:

- syntax highlighting
- line numbers
- Git integration
- cleaner formatting

---

# Reload ZSH Configuration

After updating `.zshrc`:

```bash
reload
```

or:

```bash
source ~/.zshrc
```

---

# Verify `eza`

Run:

```bash
ls
```

You should now see:

- icons
- colors
- improved formatting

---

# Verify `bat`

Run:

```bash
cat ~/.zshrc
```

Expected improvements:

- syntax highlighting
- line numbers
- cleaner file rendering

---

# Verify `zoxide`

First visit directories normally:

```bash
cd "/Volumes/Ai Agents/Developer"
cd "/Volumes/Ai Agents/Developer/ai-learning-lab"
```

Then test:

```bash
z dev
```

or:

```bash
z lab
```

`zoxide` learns directory usage history automatically.

---

# Recommended Daily Workflow

Example:

```bash
z lab
ls
cat pyproject.toml
```

This creates a significantly faster terminal workflow compared to standard macOS defaults.

---

# Recommended AI Engineering GUI Apps

Install later:

```bash
brew install --cask wezterm
brew install --cask docker
brew install --cask raycast
```

---

# Common Homebrew Problems

---

## `command not found: brew`

Usually caused by:

- shell not reloaded
- Homebrew PATH missing
- broken installation

Fix:

```bash
source ~/.zshrc
```

---

## `command not found: z`

Usually caused by missing `zoxide` initialization.

Fix:

```bash
eval "$(zoxide init zsh)"
```

inside `.zshrc`.

Then reload:

```bash
reload
```

---

## Permission Errors

Avoid using:

```bash
sudo brew
```

Homebrew should NOT normally run with sudo.

---

## Wrong Architecture

Verify:

```bash
which brew
```

Correct:

```text
/opt/homebrew/bin/brew
```

Wrong:

```text
/usr/local/bin/brew
```

---

# Professional Engineering Insight

Homebrew is not just a package installer.

It becomes:

- infrastructure management
- developer environment automation
- reproducible system configuration
- dependency management layer

Most professional macOS engineering environments depend heavily on Homebrew.

---

# Recommended Engineering Mindset

Treat your development machine as infrastructure.

Your goals should be:

- reproducibility
- maintainability
- stability
- automation
- clean tooling management

Homebrew is a major part of that philosophy.

---

# Expected Outcome

After completing this guide, your system will have:

- professional package management
- stable developer tooling
- premium terminal utilities
- Apple Silicon-compatible package infrastructure
- reproducible installation workflows
- scalable AI engineering environment

Your Mac is now ready for:

- Python installation
- UV package management
- AI tooling
- advanced terminal workflows

---

# Next Guide

Continue with:

```text
05-wezterm-setup.md
```