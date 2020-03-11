#!/usr/bin/env python

import os

PANDOCFLAGS = [
        "--metadata-file", File("metadata.yaml").name,
        "--data-dir", Dir(os.path.join("#", "templates")).name,
        "--filter", File("filters.py").name,
    ]

env = Environment(ENV=os.environ, PDFLATEX="lualatex",
                  tools=["default", "pandoc", "inkscape"],
                  PANDOCFLAGS=" ".join(PANDOCFLAGS))

base = env.Clone()

base.AppendUnique(PANDOCFLAGS=" ".join(["",
                                        "--standalone",
                                        "--to", "html+raw_attribute"]))
for src in ("about.markdown",
            "dnd.markdown",
            "fun.markdown",
            "index.markdown"):
    root, _ = os.path.splitext(src)
    base.Pandoc(root + ".html", src)

