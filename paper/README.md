# CS Senior Research Paper — Setup Guide

This repository contains a starter template for writing a research paper using Pandoc and Markdown, pre-configured for PDF generation with citations.

## File Structure

*   `paper.md`: Your main paper content. Edit this file.
*   `references.bib`: Your bibliography entries (in BibTeX format).
*   `ieee.csl`: The IEEE citation style file.
*   `figures/`: A folder to store your images and figures.
*   `.vscode/`: Contains recommended settings for Visual Studio Code to automate builds.

## Local Setup (One-Time)

### 1. Install Core Tools

You need three main tools:

1.  **Pandoc**: A universal document converter. [Installation instructions](https://pandoc.org/installing.html).
2.  **A LaTeX Distribution**: Required for Pandoc to create PDFs. [MiKTeX](https://miktex.org/download) (Windows) or [MacTeX](http://www.tug.org/mactex/) (macOS) are good choices.
3.  **pandoc-crossref** (Optional but Recommended): For auto-numbering figures, tables, and equations.
    *   Go to the [pandoc-crossref releases page](https://github.com/lierdakil/pandoc-crossref/releases).
    *   Download the binary for your OS.
    *   Move the executable (`pandoc-crossref.exe` or `pandoc-crossref`) to the same folder as your Pandoc installation. You can find Pandoc's location by running `where pandoc` (Windows) or `which pandoc` (macOS/Linux).

### 2. Download Citation Style

Open a terminal or PowerShell in your local repository folder (`paper/`) and run this command to download the IEEE citation style:

```sh
# For PowerShell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/citation-style-language/styles/master/ieee.csl" -OutFile "ieee.csl"

# For macOS/Linux
curl -o ieee.csl "https://raw.githubusercontent.com/citation-style-language/styles/master/ieee.csl"
```

### 3. VS Code Extensions

If you use Visual Studio Code, these extensions are highly recommended. Run this in your terminal:

```sh
code --install-extension notZaki.pandocciter
code --install-extension ChrisChinchilla.vscode-pandoc
code --install-extension yzhang.markdown-all-in-one
code --install-extension streetsidesoftware.code-spell-checker
```

| Extension           | Functionality                                              |
|---------------------|------------------------------------------------------------|
| **Pandoc Citer**    | Autocompletes citation keys from `references.bib` when you type `@`. |
| **vscode-pandoc**   | Builds your PDF directly from VS Code (`Ctrl+K` then `P`). |
| **Markdown All in One**| Provides shortcuts for formatting, table of contents, etc. |
| **Code Spell Checker**| Catches spelling mistakes.                                 |

The `.vscode/settings.json` file in this repository is pre-configured to work with these extensions.

## How to Build Your Paper

To generate `paper.pdf` from your `paper.md`, `cd` into the `paper` directory and run the following command in your terminal:

```bash
pandoc paper.md -o paper.pdf --filter pandoc-crossref --citeproc --csl=ieee.csl --number-sections -V geometry:margin=1in -V fontsize=12pt
```

**Using VS Code:** Simply press `Ctrl+K` then `P` and select `pdf`. The settings in `.vscode/settings.json` automatically apply the command above.

## Quick Reference

| Task                          | Syntax                                             |
|-------------------------------|----------------------------------------------------|
| Cite a source                 | `[@key]` (e.g., `[@smith2024]`)                    |
| Cite multiple sources         | `[@key1; @key2]` (e.g., `[@smith2024; @jones2025]`) |
| Add a figure with a label     | `![Caption text.](figures/my_image.png){#fig:label}` |
| Reference a figure            | `See [-@fig:label].` → renders as "See Fig. 1."      |
| Add a table with a label      | `Table: Caption text. {#tbl:label}` (place above table) |
| Reference a table             | `As shown in [-@tbl:label]...` → renders as "As shown in Table 1..." |
| Add a footnote                | `Some text[^1].` followed by `[^1]: Footnote text.` at the bottom. |

> **Tip:** Use Google Scholar's "Cite" → "BibTeX" feature to quickly get bibliography entries for `references.bib`.
