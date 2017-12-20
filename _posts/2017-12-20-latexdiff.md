---
layout: post
title: Fixing latexdiff issues
---

I was getting some really odd problems with running `latexdiff` for some paper revisions. The first few pages would build fine, and then all of the remaining pages would be marked up as new insertions. It turns out that the problem was caused by `latexdiff` only working correctly on files with unix style line endings. So if you have a file that doesn't work properly, try running `dos2unix` on the file to correct the endings and then try again.

I also had problems with diffing references, where changed inline citations would stretch off the page. The solution is to use `latexdiffcite`, a python tool that fixes this issue. See [this link](https://pypi.python.org/pypi/latexdiffcite) for more details.
