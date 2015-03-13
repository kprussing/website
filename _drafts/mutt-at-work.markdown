---
layout: post
title: Mutt at Work
---

So, I've been using `mutt` on my personal computer for a while, and I've
started to grow really fond of it.  I also find myself beginning to get
a little sick of Outlook.  Outlook is fine and all, but I kind of want
to be able to use `mutt` more so I get more practice.

A few issues come to mind as I begin to ponder how to get things set up.
The first issue is that I don't want to have my work email on my
personal computer by default, but I _do_ want to use my `dotfiles`
repository to store my configurations.  The simple work around is to put
things in subdirectories and simply link the correct files to my home
directory.  I will need to update the install script and add one to
automate (or not) the email setup.  Following that thought, I will also
be able to use `mutt` as a front end for my personal account at work by
simply adding an IMAP interface instead of using `offlineimap`!
Eventually, I can get `offlineimap` to work for my work email as well.

Now to get a preliminary setup for Outlook.  First we get `mutt` working
by following [these steps][kitchen_my_2012].

[kitchen_my_2012]: http://blog.kitchen.io/archive/2012/08/22/my-mutt-setup/

In order to get tab completion for contacts, follow Steve Losh and
install `contacts`

    $ port install contacts

Now, we need to sync the Exchange server with the local address book.
This is done by opening Outlook and going to Outlook -> Preferences ->
Sync Services -> Contacts and checking the appropriate Exchange server
(Gatech in my case).  Actually, no.  That las part is wrong.  The guide
I saw was very old and reading the comments told me that it just doesn't
work any more.

