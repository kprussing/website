#!/usr/bin/env python

import os

PANDOCFLAGS = [
        "--metadata-file", File("metadata.yaml").name,
        "--data-dir", Dir(os.path.join("#", "templates")).name,
        "--filter", File("filters.py").name,
    ]

env = Environment(ENV=os.environ, PDFLATEX="lualatex",
                  tools=["default", "pandoc", "inkscape"],
                  prefix="#doc",
                  PANDOCFLAGS=" ".join(PANDOCFLAGS))

base = env.Clone()
styles, icons = SConscript(os.path.join("static", "SConscript"),
                           exports={"env" : base})
for s in styles + icons:
    base.Install(os.path.join(env["prefix"], os.path.dirname(s.path)), s)

base.AppendUnique(PANDOCFLAGS=" ".join(["",
                                        "--self-contained",
                                        "--to", "html+raw_attribute"]))
for src in ("about.markdown",
            "index.markdown"):
    root, _ = os.path.splitext(src)
    base.Pandoc(os.path.join(env["prefix"], root + ".html"), src)

for subdir in ("fun",
               ):
    SConscript(os.path.join(subdir, "SConscript"),
               exports={"env" : base})
