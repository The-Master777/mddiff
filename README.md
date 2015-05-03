# mddiff
A tool to diff documents that are not in plaintext (such as docx-files) in markdown format using Kaleidoscope.

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/The-Master777/mddiff/master/LICENSE)

## Dependencies
This tool uses [Pandoc](http://pandoc.org/) to convert supported files into [Markdown](https://en.wikipedia.org/wiki/Markdown) and diffs them using [Kaleidoscope's](http://www.kaleidoscopeapp.com/) [ksdiff](http://www.kaleidoscopeapp.com/ksdiff2) tool.
Make sure to have the tools installed and in PATH.

## Usage
You can compare two office-files (such as *.docx*) by running `mddiff.py a.docx b.docx`.

```
Usage: mddiff fileA fileB
Diff the files using Kaleidoscope's ksdiff tool after converting to markdown.
```

To have the tool handy you can link to it: `ln -s ./mddiff.py ~/bin/mddiff`. Make sure `~/bin/` is in your PATH though.