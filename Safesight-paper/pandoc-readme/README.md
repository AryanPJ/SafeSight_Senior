# CS Senior Research Paper — Setup Guide

**This is AI generated. And lightly edited by a human. I don't use Windows so I can't test most of it. Also the VSCode extensions are NOT TESTED or ENDORSED by me yet!**

## File Structure

Put everything in one folder:

```
my-paper/
├── .vscode/
│   └── settings.json   ← VS Code config (provided below)
├── paper.md            ← your paper (edit this)
├── references.bib      ← your bibliography entries
├── ieee.csl            ← citation style (downloaded below)
└── figures/
    ├── confusion_matrix.png
    ├── loss_curve.png
    └── app_screenshot.png
```

## One-Time Setup

### 1. Download the IEEE citation style

Open PowerShell in your paper folder and run:

```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/citation-style-language/styles/master/ieee.csl" -OutFile "ieee.csl"
```

### 2. Install pandoc-crossref (optional — enables auto-numbered figures/tables)

1. Go to <https://github.com/lierdakil/pandoc-crossref/releases>
2. Download the **Windows** zip that matches your Pandoc version (`pandoc --version` to check)
3. Extract `pandoc-crossref.exe`
4. Move it to the same folder as `pandoc.exe` (usually `C:\Users\YourName\AppData\Local\Pandoc\`)

Verify it works:

```powershell
pandoc-crossref --version
```

### 3. VS Code Extensions

Install these from the terminal (copy-paste the whole block):

```powershell
code --install-extension notZaki.pandocciter
code --install-extension ChrisChinchilla.vscode-pandoc
code --install-extension yzhang.markdown-all-in-one
code --install-extension streetsidesoftware.code-spell-checker
```

What each one does:

| Extension              | What it gives you                                                  |
|------------------------|--------------------------------------------------------------------|
| **Pandoc Citer**       | Type `@` and get autocomplete from your `references.bib`           |
| **vscode-pandoc**      | `Ctrl+K` then `P` to build PDF/HTML/DOCX without leaving VS Code  |
| **Markdown All in One**| Table formatting, TOC generation, list continuation, shortcuts     |
| **Code Spell Checker** | Red squiggles under misspelled words, custom dictionary support    |

### 4. VS Code Settings

Copy the `.vscode/settings.json` file provided in this repo into your paper folder. It pre-configures the Pandoc extension so `Ctrl+K P → pdf` automatically runs with `--citeproc`, `--number-sections`, and `--filter pandoc-crossref`.

If you don't have pandoc-crossref installed, remove the `--filter pandoc-crossref` part from the `pandoc.pdfOptString` line in `settings.json`.

## Build Your Paper

Open PowerShell, `cd` into your paper folder, and run:

**With pandoc-crossref** (auto-numbered figures and tables):

```powershell
pandoc paper.md -o paper.pdf --filter pandoc-crossref --citeproc --number-sections -V geometry:margin=1in -V fontsize=12pt
```

**Without pandoc-crossref** (manual numbering):

```powershell
pandoc paper.md -o paper.pdf --citeproc --number-sections -V geometry:margin=1in -V fontsize=12pt
```

Your PDF appears as `paper.pdf` in the same folder.

## Quick Reference

| What you want to do              | Syntax                                          |
|----------------------------------|-------------------------------------------------|
| Cite a source                    | `[@smith2024]`                                  |
| Cite multiple sources            | `[@smith2024; @jones2025]`                      |
| Add a figure                     | `![Caption](figures/img.png){#fig:name width=70%}` |
| Reference a figure               | `[@fig:name]` → renders as "Figure 1"           |
| Add a table label                | `{#tbl:name}` after the caption line            |
| Reference a table                | `[@tbl:name]` → renders as "Table 1"            |
| Add a footnote                   | `Some text[^1].` then `[^1]: Footnote content.` |
| Add a new bibliography entry     | Add a `@type{key, ...}` block to `references.bib` |

> **Tip:** Google Scholar → click **Cite** → **BibTeX** to auto-generate `.bib` entries.

## Troubleshooting

- **"pandoc-crossref not found"** — make sure the `.exe` is in the same directory as `pandoc.exe`, or add its location to your system PATH.
- **"ieee.csl not found"** — make sure the file is in the same folder as `paper.md`.
- **No PDF output / LaTeX errors** — you need a LaTeX distribution. Install [MiKTeX](https://miktex.org/download) and let it auto-install packages on first build.
- **Bibliography not appearing** — make sure every `[@key]` in your paper has a matching entry in `references.bib`.
