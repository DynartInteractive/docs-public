# Dynart Documentation

The source of the [Dynart Documentation](https://docs.dynart.net)

## Install requirements

Install Python 3, the Sphinx library, the myst_parser for the .md file support, and the
Read the Docs theme.

### Debian

```bash
sudo apt install python3 python3-sphinx python3-myst-parser python3-sphinx-rtd-theme
```

### Windows

```batch
pip install sphinx myst-parser sphinx-rtd-theme linkify-it-py
```

Search for your sphinx package:

```batch
pip show sphinx
```

You will need the `Scripts` at the end, add to your PATH in with the *Edit the system environment variables*:
`c:\Users\gopher\AppData\Roaming\Python\Python313\Scripts\`, after this if you restart your terminal you should be able to run `sphinx-build`.


## Clone the repository with submodules

```bash
git clone git@github.com:DynartInteractive/docs-public.git
git submodule update --init --recursive
```

## Update the submodules

Getting latest documentation for every submodule:

```bash
git submodule update --recursive --remote
```

## Build

Go to the root folder of cloned repository and run the following command:

```bash
sphinx-build -M html . _build
```
 
This will create the documentation in HTML format in the `_build/html` folder, open the `index.html` for the main page.


