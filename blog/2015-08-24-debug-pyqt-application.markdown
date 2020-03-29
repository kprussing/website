---
title: Setting a Break Point Under PyQt
date: 2015-08-24
author: Keith F. Prussing, Ph.D.
abstract: >
    This is simply a note to myself so I can quit googling how to do
    this.  From [this answer] on Stack Overflow, to set a break point in
    a PyQt4 application insert
post: true
---

    import pdb, PyQt4
    PyQt4.QtCore.pyqtRemoveInputHook()
    pdb.set_trace()

[this answer]: http://stackoverflow.com/questions/1736015/debugging-a-pyqt4-app

