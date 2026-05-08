> [!NOTE] For the best reading experience in Cursor, right-click the `.md` file tab or filename and select `Open Preview` (shortcut: `CMD + SHIFT + V`).

# Important macOS Settings for Professional AI Development

> Optimize macOS for terminal-first AI engineering workflows, Python development, local AI tooling, external SSD workflows, and long productive coding sessions.

---

# Purpose

These macOS settings are designed to improve:

- terminal workflows
- Python development
- AI engineering ergonomics
- notebook workflows
- multitasking efficiency
- external SSD organization
- long development sessions
- system navigation
- project organization

A properly configured operating system significantly improves developer productivity and reduces workflow friction.

---

# 1. Show Hidden Files

AI development environments heavily rely on hidden configuration files.

Common examples:

```text
.env
.gitignore
.python-version
.venv
.zshrc
.wezterm.lua
```

---

## Toggle Hidden Files in Finder

Shortcut:

```text
CMD + SHIFT + .
```

This is one of the most important shortcuts for developers.

You will use it constantly during:

- Git workflows
- environment management
- Python setup
- shell configuration
- secret management
- debugging hidden project files

---

# 2. Configure Finder for Development

Open:

```text
Finder → Settings
```

---

## General Settings

Recommended:

```text
New Finder windows show:
Home Folder
```

This provides faster access to:

- user directory
- external drives
- development folders
- configuration files
- repositories

---

## Sidebar Configuration

Enable:

- Applications
- Desktop
- Documents
- Downloads
- External Drives
- Home Folder

This improves navigation speed during development workflows.

---

## Advanced Settings

Enable:

```text
Show all filename extensions
```

Critical for working with:

```text
.py
.md
.json
.toml
.yaml
.env
.ipynb
.zshrc
.lua
```

Developers should always see full file extensions.

---

# 3. Use External SSD for AI Development

AI projects consume large amounts of storage.

Examples:

- local LLMs
- datasets
- vector databases
- Docker images
- notebook outputs
- cached dependencies
- model checkpoints

In this setup, the external SSD is:

```text
Ai Agents
```

Mounted location:

```text
/Volumes/Ai Agents
```

---

## Check Connected Volumes

Open WezTerm or Terminal and run:

```bash
ls /Volumes
```

Example output:

```text
Ai Agents       Macintosh HD
```

This confirms the external SSD is mounted.

---

## Navigate to External SSD

Because the drive name contains a space, use quotes:

```bash
cd "/Volumes/Ai Agents"
```

Verify location:

```bash
pwd
```

Expected:

```text
/Volumes/Ai Agents
```

---

## Create Developer Folder

Create the main development workspace:

```bash
mkdir Developer
```

Navigate into it:

```bash
cd Developer
```

Verify:

```bash
pwd
```

Expected:

```text
/Volumes/Ai Agents/Developer
```

---

## Recommended Structure

```text
/Volumes/Ai Agents/
└── Developer/
    ├── ai-learning-lab/
    ├── ai-projects/
    ├── datasets/
    ├── experiments/
    ├── local-models/
    ├── scripts/
    ├── docker-data/
    └── archive/
```

---

## Why This Matters

Benefits include:

- cleaner project organization
- reduced internal SSD usage
- better scalability for AI workloads
- easier backup strategy
- better separation between system files and development files
- improved long-term project structure

Avoid storing serious development projects inside:

- Desktop
- Downloads
- random cloud folders
- deeply nested personal folders

---

# 4. Optimize Keyboard Settings

Open:

```text
System Settings → Keyboard
```

Recommended:

| Setting | Value |
|---|---|
| Key Repeat | Fast |
| Delay Until Repeat | Short |

---

## Why This Matters

Improves:

- coding speed
- terminal navigation
- editor responsiveness
- command-line efficiency

Especially important for:

- terminal usage
- rapid editing workflows
- shell navigation
- Cursor editing
- notebook development

---

# 5. Disable Automatic Text Corrections

Code editors and terminals should never auto-correct commands or source code.

Open:

```text
System Settings → Keyboard → Input Sources → Edit
```

Disable:

- Correct spelling automatically
- Capitalize words automatically
- Add period with double-space
- Smart quotes
- Smart dashes

---

## Why This Matters

Auto-correction can break:

- terminal commands
- Python syntax
- Git commands
- shell scripts
- Markdown files
- configuration files

Development environments must remain predictable.

---

# 6. Enable Tap to Click

Open:

```text
System Settings → Trackpad
```

Enable:

```text
Tap to click
```

---

## Benefit

Improves:

- navigation speed
- multitasking
- workflow ergonomics
- window management

Especially useful during long coding sessions.

---

# 7. Use Dark Mode

Open:

```text
System Settings → Appearance
```

Select:

```text
Dark
```

---

## Why Dark Mode Is Preferred

Better for:

- terminal workflows
- notebook sessions
- long development hours
- eye comfort
- code readability
- documentation writing

Most developer tooling is optimized around dark themes.

---

# 8. Install Rectangle for Window Management

Rectangle improves professional window management on macOS.

Website:

```text
https://rectangleapp.com
```

---

## Why Rectangle Is Important

Useful for:

- terminal + editor layouts
- notebook multitasking
- documentation workflows
- browser + Cursor layouts
- split-screen productivity

Recommended development layout:

```text
Left Side:
WezTerm

Right Side:
Cursor
```

Efficient window management significantly improves development speed.

---

# 9. Configure Screenshot Workflow

Screenshots are essential for:

- documentation
- tutorials
- debugging
- issue reporting
- project guides
- AI learning notes

---

## Essential Screenshot Shortcuts

| Shortcut | Action |
|---|---|
| `CMD + SHIFT + 3` | Full screenshot |
| `CMD + SHIFT + 4` | Area selection |
| `CMD + SHIFT + 5` | Screenshot tools panel |
| `CMD + SHIFT + 4`, then `SPACE` | Screenshot selected window |

---

# 10. Prevent Sleep During Long AI Tasks

AI workflows may involve long-running operations such as:

- model downloads
- dependency installations
- embeddings generation
- vector indexing
- local inference
- fine-tuning experiments
- notebook execution

Open:

```text
System Settings → Lock Screen
```

Adjust:

- display sleep timing
- battery sleep behavior
- power settings

---

## Recommendation

Prevent aggressive sleep behavior during development sessions.

Interrupted AI tasks can corrupt:

- downloads
- environments
- indexing operations
- notebook executions
- long-running scripts

---

# 11. Keep the Dock Minimal

Recommended pinned applications:

- Finder
- WezTerm
- Cursor
- Browser

---

## Why Minimalism Matters

A clean workspace improves:

- focus
- context switching
- workflow speed
- mental clarity

Developer productivity benefits heavily from reduced visual clutter.

---

# 12. Recommended Browser Setup

Recommended browsers:

- Chrome
- Brave
- Arc

Useful for:

- AI platforms
- GitHub
- API dashboards
- documentation
- notebooks
- developer tools
- cloud consoles

---

# 13. External SSD Recommendation

AI projects consume storage quickly.

Storage usage comes from:

- local models
- datasets
- vector databases
- notebook outputs
- Docker images
- dependency caches
- embeddings
- checkpoints

---

## Recommended Specification

```text
1TB+ External SSD
```

Better:

```text
2TB+ External SSD
```

Especially useful for:

- local LLM workflows
- AI datasets
- backups
- archived experiments
- multi-project AI labs

---

# 14. Essential macOS Shortcuts for AI Developers

These shortcuts are important for daily professional workflows.

---

## System Navigation Shortcuts

| Shortcut | Action | Use Case |
|---|---|---|
| `CMD + SPACE` | Spotlight search | Launch apps quickly |
| `CMD + TAB` | Switch applications | Move between Cursor, WezTerm, browser |
| `CMD + ~` | Switch windows of same app | Move between multiple app windows |
| `CMD + Q` | Quit application | Fully close app |
| `CMD + W` | Close current window/tab | Close current active window |
| `CMD + H` | Hide current app | Reduce visual clutter |
| `CMD + M` | Minimize window | Temporarily hide window |

---

## Finder Shortcuts

| Shortcut | Action | Use Case |
|---|---|---|
| `CMD + SHIFT + .` | Show hidden files | View `.env`, `.gitignore`, `.zshrc` |
| `CMD + SHIFT + G` | Go to folder path | Open `/Volumes/Ai Agents` quickly |
| `CMD + C` | Copy selected file/folder | Copy item |
| `CMD + V` | Paste copied file/folder | Paste item |
| `CMD + OPTION + V` | Move copied file/folder | Finder equivalent of `mv` |
| `CMD + DELETE` | Move to Trash | Safer delete |
| `SPACE` | Quick Look preview | Preview files quickly |
| `RETURN` | Rename selected file | Fast renaming |
| `CMD + I` | Get Info | Check file/folder details |

---

## Cursor Shortcuts

| Shortcut | Action | Use Case |
|---|---|---|
| `CMD + SHIFT + P` | Command Palette | Access all Cursor commands |
| `CMD + P` | Quick file open | Fast file navigation |
| `CMD + B` | Toggle sidebar | More editor space |
| `CMD + J` | Toggle terminal panel | Show/hide integrated terminal |
| `CMD + SHIFT + V` | Markdown preview | Preview `.md` guides |
| `CMD + S` | Save file | Save changes |
| `CMD + /` | Toggle comment | Comment code quickly |
| `CMD + F` | Find in file | Search current file |
| `CMD + SHIFT + F` | Search project | Search entire repository |

---

## Terminal Editing Shortcuts

| Shortcut | Action | Use Case |
|---|---|---|
| `CTRL + A` | Move to beginning of line | Edit command start |
| `CTRL + E` | Move to end of line | Accept inline suggestion / jump end |
| `CTRL + U` | Delete from cursor to beginning | Clear command prefix |
| `CTRL + K` | Delete from cursor to end | Clear command suffix |
| `CTRL + W` | Delete previous word | Fast correction |
| `CTRL + Y` | Paste deleted text | Restore deleted command text |
| `CTRL + L` | Clear terminal screen | Same as `clear` |
| `CTRL + C` | Stop process | Stop running command |
| `CTRL + D` | Exit shell/input | Exit Python REPL or terminal input |

---

## Terminal History Shortcuts

| Shortcut | Action | Use Case |
|---|---|---|
| `UP ARROW` | Previous command | Reuse recent command |
| `DOWN ARROW` | Next command | Move forward in history |
| `CTRL + R` | Reverse search history | Find previous command |
| `CTRL + G` | Exit history search | Cancel search |

---

## Autocomplete & Suggestion Shortcuts

| Shortcut | Action | Use Case |
|---|---|---|
| `TAB` | Autocomplete file/folder/command | Faster typing |
| `TAB TAB` | Show possible completions | Useful for multiple matches |
| `RIGHT ARROW` | Accept gray inline suggestion | Accept autosuggestion |
| `CTRL + E` | Move to end / accept suggestion | Fast suggestion acceptance |

---

## WezTerm Shortcuts

These depend on your WezTerm configuration.

| Shortcut | Action | Purpose |
|---|---|---|
| `CMD + D` | Split pane horizontally | Side-by-side terminal panes |
| `CMD + SHIFT + D` | Split pane vertically | Top-bottom terminal panes |
| `CMD + W` | Close current pane | Fast pane cleanup |
| `CTRL + L` | Clear pane | Clean terminal output |

---

# 15. Recommended Daily macOS Workflow

A strong professional workflow looks like this:

```text
Open WezTerm
↓
Navigate to project
↓
Open Cursor
↓
Use split panes
↓
Run Git / Python / UV commands
↓
Document work in Markdown
```

Example:

```bash
dev
cd ai-learning-lab
c.
gs
```

---

# Professional Engineering Mindset

Your operating system is part of your engineering infrastructure.

A clean and optimized development environment reduces:

- debugging time
- workflow friction
- environment conflicts
- setup instability
- productivity loss
- project disorganization

Professional developers optimize their operating system intentionally.

---

# Expected Outcome

After applying these settings, macOS will provide:

- cleaner development workflows
- better multitasking
- faster navigation
- improved terminal ergonomics
- better project organization
- external SSD-based AI workspace
- more stable AI development sessions

---

# Next Guide

Continue with:

```text
03-xcode-cli-tools.md
```