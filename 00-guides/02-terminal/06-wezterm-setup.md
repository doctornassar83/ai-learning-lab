# Professional WezTerm Setup for AI Engineering on macOS

> File Name:
>
> `06-wezterm-setup.md`

---

# Purpose of This Guide

This guide configures WezTerm as a professional terminal emulator for modern AI engineering workflows on macOS.

By the end of this guide, you will have:

- a premium terminal UI
- GPU-accelerated rendering
- Nerd Font support
- optimized typography
- pane-based workflows
- professional keyboard shortcuts
- modern color themes
- AI engineering ergonomics
- maintainable terminal configuration

---

# Install WezTerm

Install using Homebrew:

```bash
brew install --cask wezterm
```

Verify installation:

```bash
wezterm --version
```

Launch WezTerm:

```bash
wezterm
```

---

# WezTerm Configuration File

WezTerm uses a Lua configuration file.

Recommended professional location:

```text
~/.config/wezterm/wezterm.lua
```

Check if it exists:

```bash
ls -la ~/.config/wezterm/wezterm.lua
```

Create it if needed:

```bash
mkdir -p ~/.config/wezterm
touch ~/.config/wezterm/wezterm.lua
```

Open it in Cursor:

```bash
cursor ~/.config/wezterm/wezterm.lua
```

---

# Install Recommended Nerd Font

This setup uses:

```text
BlexMono Nerd Font Mono
```

Install it:

```bash
brew install --cask font-blex-mono-nerd-font
```

---

# Verify the Font Is Installed

## Method 1 — macOS Font Registry

```bash
system_profiler SPFontsDataType | grep "BlexMono"
```

Expected output should include something similar to:

```text
BlexMonoNerdFontPropo-ThinItalic.ttf:
      Location: /Users/muhamednassar/Library/Fonts/BlexMonoNerdFontPropo-ThinItalic.ttf
        BlexMonoNFP-ThinItalic:
          Full Name: BlexMono Nerd Font Propo Thin Italic
          Family: BlexMono Nerd Font Propo
          Unique Name: BlexMono Nerd Font Propo Thin Italic 3.4.0
```

## Method 2 — WezTerm Font Detection

```bash
wezterm ls-fonts | grep BlexMono
```

Expected output should include:

```text
BlexMono Nerd Font Mono
```

## Method 3 — Font Book

Open:

```text
Applications → Font Book
```

Search for:

```text
BlexMono
```

---

# Restart WezTerm After Installing Fonts

Completely quit WezTerm:

```text
CMD + Q
```

Then reopen it.

---

# Final Professional WezTerm Configuration

Replace the contents of:

```text
~/.config/wezterm/wezterm.lua
```

with this:

```lua
-- ============================================================
-- WezTerm Configuration for Professional AI Engineering
-- macOS + ZSH + Python + AI Development
-- Location: ~/.config/wezterm/wezterm.lua
-- ============================================================

local wezterm = require 'wezterm'
local config = wezterm.config_builder()

-- ============================================================
-- General
-- ============================================================

config.automatically_reload_config = true
config.check_for_updates = false
config.window_close_confirmation = 'NeverPrompt'
config.scrollback_lines = 10000
config.enable_scroll_bar = false
config.adjust_window_size_when_changing_font_size = false

-- ============================================================
-- Font
-- ============================================================

config.font = wezterm.font("BlexMono Nerd Font Mono", {
  weight = "Regular",
})

config.font_size = 18
config.line_height = 1.00

config.harfbuzz_features = {
  'calt=1',
  'clig=1',
  'liga=1',
}

-- ============================================================
-- Colors
-- ============================================================

config.color_scheme = "tokyonight_night"

config.colors = {
  cursor_bg = "#7aa2f7",
  cursor_border = "#7aa2f7",
}

-- ============================================================
-- Cursor
-- ============================================================

config.default_cursor_style = "BlinkingBar"
config.cursor_blink_rate = 700

-- ============================================================
-- Window
-- ============================================================

config.window_decorations = 'INTEGRATED_BUTTONS | RESIZE'

-- Premium glass-like appearance
config.window_background_opacity = 0.92
config.macos_window_background_blur = 35

config.window_padding = {
  left = 14,
  right = 14,
  top = 18,
  bottom = 10,
}

-- ============================================================
-- Tab Bar
-- ============================================================

config.enable_tab_bar = false
config.use_fancy_tab_bar = false

-- ============================================================
-- macOS / Terminal Behavior
-- ============================================================

config.native_macos_fullscreen_mode = true
config.enable_wayland = false

-- ============================================================
-- Performance
-- ============================================================

config.front_end = "WebGpu"
config.max_fps = 120
config.animation_fps = 120

-- ============================================================
-- Key Bindings
-- ============================================================

config.keys = {

  -- Pane Management

  {
    key = 'd',
    mods = 'CMD',
    action = wezterm.action.SplitHorizontal {
      domain = 'CurrentPaneDomain',
    },
  },

  {
    key = 'd',
    mods = 'CMD|SHIFT',
    action = wezterm.action.SplitVertical {
      domain = 'CurrentPaneDomain',
    },
  },

  {
    key = 'w',
    mods = 'CMD',
    action = wezterm.action.CloseCurrentPane {
      confirm = false,
    },
  },

  -- Pane Navigation

  {
    key = 'LeftArrow',
    mods = 'OPT',
    action = wezterm.action.ActivatePaneDirection 'Left',
  },

  {
    key = 'RightArrow',
    mods = 'OPT',
    action = wezterm.action.ActivatePaneDirection 'Right',
  },

  {
    key = 'UpArrow',
    mods = 'OPT',
    action = wezterm.action.ActivatePaneDirection 'Up',
  },

  {
    key = 'DownArrow',
    mods = 'OPT',
    action = wezterm.action.ActivatePaneDirection 'Down',
  },

  -- Font Size

  {
    key = '=',
    mods = 'CMD',
    action = wezterm.action.IncreaseFontSize,
  },

  {
    key = '-',
    mods = 'CMD',
    action = wezterm.action.DecreaseFontSize,
  },

  {
    key = '0',
    mods = 'CMD',
    action = wezterm.action.ResetFontSize,
  },

  -- Clear Terminal

  {
    key = 'l',
    mods = 'CTRL',
    action = wezterm.action.SendString 'clear\n',
  },

  -- Clipboard

  {
    key = 'c',
    mods = 'CMD',
    action = wezterm.action.CopyTo 'Clipboard',
  },

  {
    key = 'v',
    mods = 'CMD',
    action = wezterm.action.PasteFrom 'Clipboard',
  },

  -- Tabs

  {
    key = 't',
    mods = 'CMD',
    action = wezterm.action.SpawnTab 'CurrentPaneDomain',
  },

  -- Fullscreen

  {
    key = 'Enter',
    mods = 'CMD|CTRL',
    action = wezterm.action.ToggleFullScreen,
  },
}

-- ============================================================
-- Return Configuration
-- ============================================================

return config
```

---

# Reloading the Configuration

This line enables automatic reload:

```lua
config.automatically_reload_config = true
```

After saving the file, WezTerm reloads automatically.

Manual reload:

```text
CMD + SHIFT + R
```

or restart WezTerm.

---

# Pane Navigation Workflow

After splitting panes:

```text
┌─────────────────────┬─────────────────────┐
│ Pane 1              │ Pane 2              │
├─────────────────────┼─────────────────────┤
│ Pane 3              │ Pane 4              │
└─────────────────────┴─────────────────────┘
```

Use:

| Shortcut | Action |
|---|---|
| `OPT + LeftArrow` | move left |
| `OPT + RightArrow` | move right |
| `OPT + UpArrow` | move up |
| `OPT + DownArrow` | move down |

---

# Recommended AI Engineering Layout

```text
┌─────────────────────┬─────────────────────┐
│ Python Development  │ Git Operations      │
├─────────────────────┼─────────────────────┤
│ uv / Jupyter        │ Logs / Monitoring   │
└─────────────────────┴─────────────────────┘
```

---

# Useful Keyboard Shortcuts

| Shortcut | Action |
|---|---|
| `CMD + D` | split pane horizontally |
| `CMD + SHIFT + D` | split pane vertically |
| `OPT + Arrow Keys` | navigate panes |
| `CMD + W` | close pane |
| `CMD + =` | increase font size |
| `CMD + -` | decrease font size |
| `CMD + 0` | reset font size |
| `CTRL + L` | clear terminal |
| `CMD + T` | new tab |
| `CMD + CTRL + Enter` | toggle fullscreen |

---

# Testing Checklist

- [ ] WezTerm launches correctly
- [ ] config file exists at `~/.config/wezterm/wezterm.lua`
- [ ] BlexMono font is installed
- [ ] Tokyo Night theme loads
- [ ] transparency works
- [ ] blur effect works
- [ ] pane splitting works
- [ ] pane navigation works
- [ ] font scaling works
- [ ] no Lua errors appear

---

# Common Errors and Fixes

## Font Does Not Change

Install the font:

```bash
brew install --cask font-blex-mono-nerd-font
```

Then restart WezTerm.

## `fc-list: command not found`

This is normal on macOS.

Use:

```bash
system_profiler SPFontsDataType | grep "BlexMono"
```

or:

```bash
wezterm ls-fonts | grep BlexMono
```

## Unknown Color Scheme

Use the exact value:

```lua
config.color_scheme = "tokyonight_night"
```

## Lua Syntax Error

Common causes:

- missing comma
- missing quote
- missing brace
- copied Markdown instead of Lua into `wezterm.lua`

---

# Next Guide

Next:

```text
07-starship-prompt.md
```

The next guide will configure a professional Starship prompt optimized for AI engineering workflows.