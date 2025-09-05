# Dynart Documentation

The source of the [Dynart Documentation](https://docs.dynart.net)

## Install requirements

Install Python 3, the Sphinx library, the myst_parser for the .md file support, and the
Read the Docs theme.

### Debian

```bash
sudo apt install python3 python3-sphinx python3-myst-parser python3-sphinx-rtd-theme
```

## Build

Go to the root folder of cloned repository and run the following command:

```bash
sphinx-build -M html . _build
```

This will create the documentation in HTML format in the `_build/html` folder.