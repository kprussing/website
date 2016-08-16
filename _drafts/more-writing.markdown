
+   And some more notes on writing with Pandoc.  For equation numbering, 
    see [pandoc-eqnos](https://github.com/tomduck/pandoc-eqnos).
+   See this snippet from a `SConstruct` file to get Pandoc to work.  
    The key point is that the LaTeX specific parameters are ignored by 
    Word builder and vise versa.

        pandoccmd = [
                "pandoc", "--standalone",
                "--latex-engine=lualatex",
                "--include-in-header=preamble.tex",
                "-o", "$TARGET", "$SOURCES"
            ]
        Pandoc = Builder(
                action=" ".join(pandoccmd),
                src_suffix=[".md", ".markdown", ".txt"]
            )
        env.AppendUnique(BUILDERS={"Pandoc" : Pandoc})

+   If you install a new font from MacPorts, you may well need to update
    the LuaLaTeX font database.  Run

        OSFONTDIR=/opt/local/share/fonts luaotfload-tool -u

    to update the database.  Then `luaotfloat-tool --find DejaVuSerif`
    should work.

+   To change the font in a LaTeX document add

        \usepackage{fontspec}
        \setmainfong{DejaVuSerif}

    to the preamble.

