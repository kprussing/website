#!/usr/bin/env python
__doc__ = """A collection of filters I need for processing my website
into the correct format.
"""

#
# Copyright (c) 2019, Keith F. Prussing
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     1. Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#
#     2. Redistributions in binary form must reproduce the above
#     copyright notice, this list of conditions and the following
#     disclaimer in the documentation and/or other materials provided
#     with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

import datetime
import os

import panflute

_root = os.path.basename(__file__)

def masthead(doc):
    """Generate the masthead based on the metadata
    """
    if doc.format != "html":
        return

    avatar = "<a href='{0}/' class='site-avatar'><img src='{1}' /></a>"
    name = "<h1 class='site-name'><a href='{0}/'>{1}</a></h1>"
    desc = "<p class='site-description'>{0}</p>"
    metadata = doc.get_metadata()
    url = metadata.get("url", "")
    nav = "<a href='{0}/{1}'>{2}</a>"
    author = doc.get_metadata("author")
    if isinstance(author, (list, tuple)):
        author = author[0]

    masthead = [ "",
        "<div class='wrapper-masthead'>",
        "\t<div class='container'>",
        "\t\t<header class='masthead clearfix'>",
        "\t\t\t" + avatar.format(url, metadata.get("avatar", "")),
        "\t\t\t<div class='site-info'>",
        "\t\t\t\t" + name.format(url, author),
        "\t\t\t\t" + desc.format(metadata.get("description", "")),
        "\t\t\t</div>",
        "\t\t\t<nav>",
        "\t\t\t" + nav.format(url, "website/index.html", "Home"),
        "\t\t\t" + nav.format(url, "website/about.html", "About"),
        "\t\t\t" + nav.format(url, "website/blog/index.html", "Blog"),
        "\t\t\t" + nav.format(url, "website/fun/index.html", "Fun"),
        "\t\t\t" + nav.format(url, "resume/index.html", "Resume"),
        "\t\t\t</nav>",
        "\t\t</header>",
        "\t</div>",
        "</div>",
        "<div id='main' role='main' class='container'>"
    ]
    doc.metadata["include-before"] = panflute.MetaList(
                *doc.get_metadata("include-before", ()),
                panflute.RawBlock("\n".join(masthead), format="html"))

def footer(doc):
    """Generate the footer for the HTML version
    """
    if doc.format != "html" or "footer-links" not in doc.metadata:
        return

    links = doc.get_metadata("footer-links", [])
    # panflute.debug(_root + ":footer: links {0}".format(links))
    keys = (("email", "mailto: {0}"),
            ("github", "https://github.com/{0}"),
            ("linkedin", "https://linkedin.com/in/{0}"),
            ("stackoverflow", "https://stackoverflow.com/users/{0}"),
           )
    href = "<a href='{0}'><img src='static/svg-icons/{1}.svg'/></a>"
    logos = [href.format(url.format(links[key]), key)
             for key, url in keys if links.get(key, False)]

    # panflute.debug(logos)
    year = datetime.date.today().year
    author = doc.get_metadata("author")
    if isinstance(author, (list, tuple)):
        author = author[0]

    # Build up the footer for each page to include the logos and the
    # copy right notice.
    footer = "\n" \
           + "\n</div>" \
           + "\n<div class='wrapper-footer'>" \
           + "\n\t<div class='container'>" \
           + "\n\t\t<footer class='footer'>" \
           + "\n\t\t\t".join([""] + logos) \
           + "\n\t\t\t<div>" \
           + "&#169; Copyright {0}, {1}".format(year, author) \
           + ("" if author[-1] == "." else ".") + "  Created using " \
           + "<a href='https://scons.org'>SCons</a> and " \
           + "<a href='https://pandoc.org'>Pandoc</a>" \
           + "\n\t\t\t</div>" \
           + "\n\t\t</footer>" \
           + "\n\t</div>" \
           + "\n</div>" \
           + "\n"
    doc.metadata["include-after"] = panflute.MetaList(
                *doc.get_metadata("include-after", ()),
                panflute.RawBlock(footer, format="html"))

def format_post(doc):
    """Do some formatting for posts

    We want the author list to be formatted in a single span in the
    text, but as individuals in the meta data.  So, we migrate the
    author list to the meta field if it does not exist and we just joint
    the authors into a single string.  However, we only do this for HTML
    output with the `post` field set to True.
    """
    if doc.format != "html" or not doc.get_metadata("post", False):
        return

    author = doc.get_metadata("author")
    if "author-meta" not in doc.metadata:
        doc.metadata["author-meta"] = author

    if isinstance(author, list):
        if len(author) == 1:
            doc.metadata["author"] = author[0]
        elif len(author) == 2:
            doc.metadata["author"] = " and ".join(author)
        else:
            doc.metadata["author"] = ", ".join(author[:-1]) \
                    + ", and " + author[-1]

def finalize(doc):
    """Run the finalization steps"""
    for f in (masthead,
              footer,
              format_post,
             ):
        f(doc)


def main(doc=None):
    """The main routine"""
    return panflute.run_filters([],
                                finalize=finalize,
                                doc=doc)

if __name__ == "__main__":
    main()

