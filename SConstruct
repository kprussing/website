#!/usr/bin/env python

import os

PANDOCFLAGS = [
        "--metadata-file", File("metadata.yaml").name,
        "--filter", File("filters.py").name,
    ]

env = Environment(ENV=os.environ, PDFLATEX="lualatex",
                  tools=["default", "pandoc", "inkscape"],
                  prefix="#docs",
                  PANDOCFLAGS=" ".join(PANDOCFLAGS))

base = env.Clone()
html_flags =  ["", "--template",
               os.path.join("templates", "website.html")]
base.Append(PANDOCFLAGS=" ".join(html_flags))
styles, _ = SConscript(os.path.join("static", "SConscript"),
                       exports={"env" : base})
for s in styles:
    base.Append(PANDOCFLAGS=" --css " + s.path)

base.AppendUnique(PANDOCFLAGS=" ".join(["",
                                        "--self-contained",
                                        "--to", "html"]))
for src in ("about.markdown",
            "index.markdown"):
    root, _ = os.path.splitext(src)
    base.Pandoc(os.path.join(env["prefix"], root + ".html"), src)

for subdir in ("blog",
               "fun",
               ):
    SConscript(os.path.join(subdir, "SConscript"),
               exports={"env" : base})
