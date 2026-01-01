# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the Dynart Documentation repository, a Sphinx-based documentation site that aggregates documentation from multiple projects via Git submodules. The built site is published at https://docs.dynart.net.

## Build System

This project uses Sphinx with MyST parser for Markdown support and the Read the Docs theme.

### Build Commands

Build the complete documentation:
```bash
sphinx-build -M html . _build
```

On Windows, you can also use the batch file:
```bash
make.bat html
```

The generated HTML output will be in `_build/html/`.

### Dependencies

Install required Python packages:

**Debian/Ubuntu:**
```bash
sudo apt install python3 python3-sphinx python3-myst-parser python3-sphinx-rtd-theme
```

**Windows:**
```bash
pip install sphinx myst-parser sphinx-rtd-theme linkify-it-py
```

After installing on Windows, ensure the Python Scripts directory (e.g., `c:\Users\gopher\AppData\Roaming\Python\Python313\Scripts\`) is in your PATH to access `sphinx-build`.

## Repository Structure

The repository follows a Git submodules architecture where individual documentation sets are maintained in separate repositories:

- **Root**: Main documentation site configuration ([conf.py](conf.py)) and index
- **coolfox-engine/**: CoolFox Engine documentation (LibGDX-based retro platformer engine)
  - Source: https://github.com/DynartInteractive/docs-coolfox-engine
- **dos-game-engine/**: DOS Game Engine documentation (Pascal/Turbo Pascal framework)
  - Source: git@github.com:DynartInteractive/docs-dos-game-engine.git
- **legal/**: Legal documents (privacy policy, terms of use, house rules)
  - Source: https://github.com/DynartInteractive/docs-legal

### Working with Submodules

Initialize and update all submodules:
```bash
git submodule update --init --recursive
```

Update submodules to their latest commits on main branch:
```bash
git submodule update --remote
```

When making changes to submodule content, work directly in the respective submodule repository, not this parent repository.

## Sphinx Configuration

The Sphinx configuration ([conf.py](conf.py)) is set up with:

- **MyST Parser extensions enabled:**
  - `attrs_inline`: Inline IDs (e.g., `## Title {#id}`)
  - `attrs_block`: Block IDs (e.g., `{#id}\n## Title`)
  - `linkify`: Auto-converts URLs to links

- **Theme**: Read the Docs (`sphinx_rtd_theme`)
- **Custom styling**: [_static/custom.css](_static/custom.css)
- **Logo**: [_static/dynart-logo.svg](_static/dynart-logo.svg)
- **Syntax highlighting**: Dracula theme (`pygments_style = 'dracula'`)

## Documentation Organization

The main table of contents is defined in [index.md](index.md). Each submodule has its own `index.md` file that serves as the entry point for that documentation set, using Sphinx `toctree` directives to organize content.

When adding new documentation sections, update the root [index.md](index.md) to include them in the site navigation.
