# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

The source of the Dynart Documentation, published at https://docs.dynart.net. It is Markdown
only: the site is a [dpress](https://github.com/goph-R/dynart-dpress) install with the
[Docs plugin](https://github.com/goph-R/dynart-dpress-docs), which reads this repository and
renders it. There is no build step here, and no Sphinx any more - there is no `conf.py`, and
`sphinx-build` is not how the site is made.

## Repository Structure

Each documentation set is its own repository, included as a git submodule:

- **Root**: [index.md](index.md), the top of the tree
- **lisa-engine/**: Lisa Engine (LibGDX-based retro platformer engine, base of NeonSignal and
  CoolFox) - https://github.com/DynartInteractive/docs-lisa-engine
- **dos-game-engine/**: DOS Game Engine (Turbo Pascal framework) -
  https://github.com/DynartInteractive/docs-dos-game-engine
- **legal/**: privacy policy, terms of use, house rules -
  https://github.com/DynartInteractive/docs-legal

**Change submodule content in the submodule's own repository**, commit and push it there, and
then commit the submodule's new commit in this repository (`git add <submodule>`) and push this
one. The server checks out what this repository records: a submodule change that is not
recorded here is not published.

The submodule addresses are `https://` on purpose - the server has no GitHub key.

## Publishing

A push to this repository triggers a Jenkins job (its pipeline is the `Jenkinsfile` in
https://github.com/DynartInteractive/docs.dynart.net). It runs `dpress docs:build` on the server,
which pulls this repository and its submodules, and rebuilds every page.

## What the build understands

CommonMark, plus this subset of MyST:

- ```` ```{toctree} ```` with `:maxdepth:`, `:caption:`, `:hidden:` - defines the tree. A page is
  published only if a `toctree` reaches it from the root `index.md`, so files like this one and
  `README.md` never are. Entries are paths relative to the file, without `.md`.
- Admonitions: `note`, `tip`, `hint`, `important`, `seealso`, `attention`, `warning`, `caution`,
  `danger`, `error`, `admonition`.
- `{#id}` / `{#id .class}` / `{.class}` on the line before a heading, or at the end of it.
- ``{ref}`id` `` - a link to the heading with that id.
- Relative links to `.md` files, which become links to those pages.
- Fenced code with a language is highlighted (`pascal` included); a fence with none is a plain box.

Heading ids follow Sphinx's rule (`## VGA Graphics` is `#vga-graphics`), so old links keep
working - keep headings stable when editing, since their ids are addresses people have saved.

When adding a documentation set, add its `index` to the root [index.md](index.md) `toctree`.
