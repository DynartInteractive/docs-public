# Dynart Documentation

The source of the [Dynart Documentation](https://docs.dynart.net): Markdown, in one repository per
project, gathered here as git submodules.

The site is built by [dpress](https://github.com/goph-R/dynart-dpress) and its
[Docs plugin](https://github.com/goph-R/dynart-dpress-docs), not by Sphinx any more. Nothing is
built in this repository: the server clones it, and turns the Markdown into pages.

## How a change gets published

1. Change the Markdown - in the submodule's own repository, for anything below `legal/`,
   `dos-game-engine/` or `lisa-engine/` - and push it.
2. **If you changed a submodule, commit its new commit here too**, and push this repository. The
   server checks out what this repository records, so a submodule's push alone is not published:

   ```bash
   git add dos-game-engine
   git commit -m "dos-game-engine: what changed"
   git push
   ```

3. A push to this repository starts the Jenkins job, which has the server pull it and rebuild -
   `dpress docs:build` on the server. A red job means the pull or the build failed; its console
   says which, and the site keeps what it had.

## Clone it

```bash
git clone --recurse-submodules https://github.com/DynartInteractive/docs-public.git
```

The submodules are listed with `https://` addresses so that a machine with no GitHub key - the
server - can clone them. To keep **pushing** over SSH from your own machine, tell git once:

```bash
git config --global url."git@github.com:".pushInsteadOf "https://github.com/"
```

## Update the submodules

To the commits this repository records:

```bash
git pull --recurse-submodules
```

To the newest commit of each submodule's `main` - then commit the result here, as in step 2:

```bash
git submodule update --remote
```

## Writing

Plain Markdown, plus the parts of [MyST](https://myst-parser.readthedocs.io/) the site understands:

| Syntax | What it does |
|---|---|
| ```` ```{toctree} ```` with `:maxdepth:`, `:caption:`, `:hidden:` | the tree: a page appears on the site only if a `toctree` reaches it, starting from `index.md` |
| ```` ```{note} ````, `tip`, `hint`, `important`, `seealso`, `attention`, `warning`, `caution`, `danger`, `error`, `admonition` | a callout |
| `{#some-id}` on the line before a heading, `## Title {#some-id}`, `{.a-class}` | an id or a class on that heading |
| ``{ref}`some-id` `` | a link to the heading with that id, its title as the text |
| `[text](../ENGINE/BASEGAME.md)` | a link to that page |
| ```` ```pascal ```` and other languages | a highlighted code block; a fence with no language is a plain box |

Every heading gets the id Sphinx gave it - `## VGA Graphics` is `#vga-graphics` - so the links
people saved from the Sphinx site still land. A construct the build does not know is shown as it
is and listed as a problem in the build's report.

## Previewing locally

Any dpress site with the Docs plugin can build from a local clone: point **Source folder** under
Settings > Documentation at it, and press **Build now**.
