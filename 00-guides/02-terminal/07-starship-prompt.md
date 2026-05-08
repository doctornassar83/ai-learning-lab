# Professional Starship Prompt Setup for AI Engineering on macOS

> File Name:
>
> `07-starship-prompt.md`

---

# Purpose of This Guide

This guide configures Starship as a professional, modern, and readable terminal prompt for AI engineering workflows on macOS.

This setup uses the official Starship preset:

```text
Catppuccin Powerline
```

By the end of this guide, you will have:

- a clean Powerline-style prompt
- Catppuccin-inspired colors
- Git status visibility
- Python environment visibility
- directory context
- command duration display
- professional prompt aesthetics
- a maintainable `starship.toml` configuration

---

# What Is Starship?

Starship is a fast, cross-shell terminal prompt.

It works with:

- ZSH
- Bash
- Fish
- PowerShell
- Nushell

In this setup, Starship is used with:

```text
ZSH + WezTerm + BlexMono Nerd Font
```

---

# Why Starship Matters

A professional prompt gives you useful context without extra commands.

For AI engineering, this is especially useful because you often need to know:

- current project folder
- Git branch
- Git status
- Python version
- virtual environment
- command execution time
- whether the last command failed

---

# Install Starship

Install Starship using Homebrew:

```bash
brew install starship
```

Verify installation:

```bash
starship --version
```

Expected output should look similar to:

```text
starship 1.x.x
```

---

# Enable Starship in ZSH

Open your `.zshrc`:

```bash
cursor ~/.zshrc
```

Make sure this section exists:

```zsh
# ------------------------------------------------------------
# Starship Prompt
# ------------------------------------------------------------

if command -v starship >/dev/null 2>&1; then
  eval "$(starship init zsh)"
fi
```

Reload ZSH:

```bash
source ~/.zshrc
```

or:

```bash
exec zsh
```

---

# Starship Configuration File Location

The Starship configuration file is:

```text
~/.config/starship.toml
```

This is the professional recommended location.

---

# How to Check If the Config File Exists

Run:

```bash
ls -la ~/.config/starship.toml
```

If it exists, you will see output similar to:

```text
-rw-r--r--  1 muhamednassar  staff  1234 May 8 19:30 /Users/muhamednassar/.config/starship.toml
```

---

# How to Create the Config File

Create the config directory:

```bash
mkdir -p ~/.config
```

Create the Starship config file:

```bash
touch ~/.config/starship.toml
```

---

# How to Open the Config File

Open it in Cursor:

```bash
cursor ~/.config/starship.toml
```

Recommended config structure:

```text
~/.config/
├── wezterm/
│   └── wezterm.lua
└── starship.toml
```

---

# Required Font Support

Because this preset uses Powerline-style symbols, you need a Nerd Font.

This guide assumes you already installed:

```text
BlexMono Nerd Font Mono
```

Verify the font is installed:

```bash
system_profiler SPFontsDataType | grep "BlexMono"
```

You can also check inside WezTerm:

```bash
wezterm ls-fonts | grep BlexMono
```

Your WezTerm config should contain:

```lua
config.font = wezterm.font("BlexMono Nerd Font Mono", {
  weight = "Regular",
})
```

---

# Install the Official Catppuccin Powerline Preset

Starship can generate preset configuration automatically.

Run:

```bash
starship preset catppuccin-powerline -o ~/.config/starship.toml
```

This writes the preset directly into:

```text
~/.config/starship.toml
```

---

# Open the Generated Configuration

```bash
cursor ~/.config/starship.toml
```

---

# Reload the Terminal

After generating or editing the file, reload your shell:

```bash
source ~/.zshrc
```

or restart WezTerm.

---

# Final Professional `starship.toml`

Use this full configuration for a polished Catppuccin Powerline prompt optimized for AI engineering.

Replace the contents of:

```text
~/.config/starship.toml
```

with:

```toml
# ============================================================
# Starship Prompt Configuration
# Professional AI Engineering Setup
# Preset Base: Catppuccin Powerline
# Location: ~/.config/starship.toml
# ============================================================

"$schema" = 'https://starship.rs/config-schema.json'

format = """
[](mauve)\
$username\
[](bg:peach fg:mauve)\
$directory\
[](fg:peach bg:yellow)\
$git_branch\
$git_status\
[](fg:yellow bg:green)\
$python\
$nodejs\
$rust\
[](fg:green bg:blue)\
$cmd_duration\
[](fg:blue bg:surface0)\
$time\
[ ](fg:surface0)\
$line_break\
$character
"""

palette = "catppuccin_mocha"

# ============================================================
# Username
# ============================================================

[username]
show_always = true
style_user = "bg:mauve fg:base"
style_root = "bg:red fg:base"
format = '[ $user ]($style)'

# ============================================================
# Directory
# ============================================================

[directory]
style = "bg:peach fg:base"
format = '[ $path ]($style)'
truncation_length = 3
truncation_symbol = "…/"
home_symbol = "~"

# ============================================================
# Git Branch
# ============================================================

[git_branch]
symbol = ""
style = "bg:yellow fg:base"
format = '[ $symbol $branch ]($style)'

# ============================================================
# Git Status
# ============================================================

[git_status]
style = "bg:yellow fg:base"
format = '[$all_status$ahead_behind ]($style)'

conflicted = "=${count} "
ahead = "⇡${count} "
behind = "⇣${count} "
diverged = "⇕⇡${ahead_count}⇣${behind_count} "
untracked = "?${count} "
stashed = "\\$${count} "
modified = "!${count} "
staged = "+${count} "
renamed = "»${count} "
deleted = "✘${count} "

# ============================================================
# Python
# ============================================================

[python]
symbol = ""
style = "bg:green fg:base"
format = '[ $symbol $version $virtualenv ]($style)'
pyenv_version_name = false
python_binary = ["python3", "python"]
detect_extensions = ["py"]
detect_files = ["pyproject.toml", "requirements.txt", ".python-version"]
detect_folders = [".venv"]

# ============================================================
# Node.js
# ============================================================

[nodejs]
symbol = ""
style = "bg:green fg:base"
format = '[ $symbol $version ]($style)'
detect_extensions = ["js", "mjs", "cjs", "ts", "tsx"]
detect_files = ["package.json"]

# ============================================================
# Rust
# ============================================================

[rust]
symbol = ""
style = "bg:green fg:base"
format = '[ $symbol $version ]($style)'
detect_extensions = ["rs"]
detect_files = ["Cargo.toml"]

# ============================================================
# Command Duration
# ============================================================

[cmd_duration]
min_time = 500
style = "bg:blue fg:base"
format = '[  $duration ]($style)'

# ============================================================
# Time
# ============================================================

[time]
disabled = false
time_format = "%H:%M"
style = "bg:surface0 fg:text"
format = '[ $time ]($style)'

# ============================================================
# Character
# ============================================================

[character]
success_symbol = '[❯](bold green)'
error_symbol = '[❯](bold red)'
vimcmd_symbol = '[❮](bold green)'

# ============================================================
# Disabled Modules
# ============================================================

[aws]
disabled = true

[gcloud]
disabled = true

[azure]
disabled = true

[docker_context]
disabled = true

[package]
disabled = true

# ============================================================
# Catppuccin Mocha Palette
# ============================================================

[palettes.catppuccin_mocha]
rosewater = "#f5e0dc"
flamingo = "#f2cdcd"
pink = "#f5c2e7"
mauve = "#cba6f7"
red = "#f38ba8"
maroon = "#eba0ac"
peach = "#fab387"
yellow = "#f9e2af"
green = "#a6e3a1"
teal = "#94e2d5"
sky = "#89dceb"
sapphire = "#74c7ec"
blue = "#89b4fa"
lavender = "#b4befe"
text = "#cdd6f4"
subtext1 = "#bac2de"
subtext0 = "#a6adc8"
overlay2 = "#9399b2"
overlay1 = "#7f849c"
overlay0 = "#6c7086"
surface2 = "#585b70"
surface1 = "#45475a"
surface0 = "#313244"
base = "#1e1e2e"
mantle = "#181825"
crust = "#11111b"
```

---

# Prompt Layout Explanation

The prompt is arranged like this:

```text
username → directory → git → languages → duration → time
```

Example:

```text
muhamednassar  ai-learning-lab  main  Python 3.14  1s  19:30
❯
```

---

# Section-by-Section Explanation

---

# Username

```toml
[username]
show_always = true
```

This always displays your username.

Useful when working across:

- local Mac
- VPS
- SSH sessions
- containers

---

# Directory

```toml
[directory]
truncation_length = 3
```

This prevents long paths from overwhelming the prompt.

Example:

```text
Developer/ai-learning-lab/src
```

may become:

```text
…/ai-learning-lab/src
```

---

# Git Branch

```toml
[git_branch]
symbol = ""
```

Shows the current Git branch.

Example:

```text
main
```

This is critical for professional development work.

---

# Git Status

```toml
[git_status]
```

Shows repository changes.

Examples:

| Symbol | Meaning |
|---|---|
| `?` | untracked files |
| `!` | modified files |
| `+` | staged files |
| `✘` | deleted files |
| `⇡` | commits ahead |
| `⇣` | commits behind |

---

# Python Module

```toml
[python]
symbol = ""
```

Shows Python version and virtual environment.

This is important for AI engineering because projects often depend on:

- Python version
- virtual environment
- `uv`
- isolated dependencies

---

# Node.js Module

```toml
[nodejs]
```

Useful for full-stack AI projects, dashboards, and web apps.

---

# Rust Module

```toml
[rust]
```

Useful because some AI and terminal tooling is Rust-based.

---

# Command Duration

```toml
[cmd_duration]
min_time = 500
```

Shows duration only when commands take more than 500ms.

This is useful for:

- Python scripts
- package installation
- tests
- model downloads
- indexing jobs

---

# Time

```toml
[time]
disabled = false
```

Shows the current time in the prompt.

Useful during:

- experiments
- logs
- trading workflows
- long-running AI jobs
- debugging sessions

---

# Character

```toml
[character]
success_symbol = '[❯](bold green)'
error_symbol = '[❯](bold red)'
```

The prompt symbol changes color depending on command success or failure.

---

# Why Some Modules Are Disabled

```toml
[aws]
disabled = true

[gcloud]
disabled = true

[azure]
disabled = true

[docker_context]
disabled = true

[package]
disabled = true
```

These are disabled to keep the prompt clean.

You can enable them later if needed.

---

# Testing the Prompt

Reload ZSH:

```bash
source ~/.zshrc
```

or restart WezTerm.

Then test inside your project:

```bash
cd "/Volumes/Ai Agents/Developer/ai-learning-lab"
```

Check:

- username appears
- directory appears
- Git branch appears
- Python appears in Python projects
- command duration appears after slow commands
- time appears
- prompt symbol appears on a new line

---

# Test Command Duration

Run:

```bash
sleep 1
```

You should see the command duration appear.

---

# Test Git Status

Inside a Git repository:

```bash
touch test-file.md
```

You should see untracked file status.

Remove it after testing:

```bash
rm test-file.md
```

---

# Test Python Detection

Inside a Python project:

```bash
ls pyproject.toml
```

Then run:

```bash
python3 --version
```

Starship should show Python information when it detects a Python project.

---

# Common Errors and Fixes

---

# Error: Prompt Does Not Change

## Cause

Starship is not initialized in `.zshrc`.

## Fix

Add this to `~/.zshrc`:

```zsh
if command -v starship >/dev/null 2>&1; then
  eval "$(starship init zsh)"
fi
```

Reload:

```bash
source ~/.zshrc
```

---

# Error: Symbols Look Broken

## Cause

Nerd Font is not installed or WezTerm is not using it.

## Fix

Install the font:

```bash
brew install --cask font-blex-mono-nerd-font
```

Verify:

```bash
system_profiler SPFontsDataType | grep "BlexMono"
```

Then confirm WezTerm uses:

```lua
config.font = wezterm.font("BlexMono Nerd Font Mono", {
  weight = "Regular",
})
```

Restart WezTerm.

---

# Error: Colors Look Wrong

## Cause

Terminal theme, font, or color palette mismatch.

## Fix

Make sure WezTerm uses:

```lua
config.color_scheme = "tokyonight_night"
```

and Starship uses:

```toml
palette = "catppuccin_mocha"
```

This combination gives a premium but balanced appearance.

---

# Error: `starship preset` Command Fails

## Cause

Starship may not be installed or may be outdated.

## Fix

```bash
brew upgrade starship
```

Then try:

```bash
starship preset catppuccin-powerline -o ~/.config/starship.toml
```

---

# Maintenance Notes

## Keep It Minimal

Do not enable every module.

A professional prompt should show only information that helps decision-making.

---

## Avoid Overcrowding

If the prompt becomes too long, reduce modules before changing fonts or window size.

---

## Version Control Your Configs Later

Later, you can store this file in a dotfiles repository:

```text
dotfiles/
├── wezterm/
│   └── wezterm.lua
└── starship/
    └── starship.toml
```

---

# Final Checklist

Before moving to the next guide:

- [ ] Starship is installed
- [ ] Starship is initialized in `.zshrc`
- [ ] `~/.config/starship.toml` exists
- [ ] Catppuccin Powerline preset is applied
- [ ] Nerd Font is installed
- [ ] WezTerm uses BlexMono Nerd Font Mono
- [ ] prompt symbols render correctly
- [ ] Git branch appears
- [ ] Git status appears
- [ ] Python version appears in Python projects
- [ ] command duration works
- [ ] time appears
- [ ] prompt looks clean and readable

---

# Next Guide

Next:

```text
08-modern-terminal-utilities.md
```

The next guide will install and configure modern terminal utilities such as:

- `eza`
- `bat`
- `zoxide`
- `fzf`
- `ripgrep`
- `fd`