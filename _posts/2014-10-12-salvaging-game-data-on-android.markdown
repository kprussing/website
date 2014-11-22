---
layout: post
title: Salvaging Game Data on Android
---

A few weeks ago, the wife's Samsung Galaxy S2 took the final plunge and
bit the dust (mostly).  It wound up caught in a cycle of powering on and
off.  Luckily, I was able to fiddle with it enough to grab the
`highscores.lua` and `settings.lua` files from her Angry Birds games
using a little script I wrote some time back.

    $ cat pullab
    #!/bin/bash
    abs=$( adb shell pm list packages | \
            awk '{RS="\r"} /rovio/ {sub(/package:/,""); print $1}' \
        )
    for app in ${abs}; do
        if [ $(echo ${app} | grep space) ]; then
        files="settings.lua highscores.lua eaglepurchases.lua \
            gamepurchases.lua episodepurchases.lua"
        else
            files="settings.lua highscores.lua"
        fi
        if [ -d ${app} ]; then
            rm -rf ${app}
        fi
        mkdir ${app}
        for f in ${files}; do
            adb pull data/data/${app}/files/$f ${app}
        done
    done

This works marvelously well if all you need is the basic files.  In
theory, one can reverse this procedure by simply issuing the `adb push`
command in the final loop.  Unfortunately, this no longer works with
Android 4.0 and newer (Ice Cream Sandwich and up) such as what is on the
Galaxy S5.

So, what do I do?  The only thing any rational person would do: Google
it.  One of my top hits was at [Angry Birds Nest][amslimfordy_how_2013].
It turns out that I should have used the baked in backup command and not
simply pulled the files.  Oh, well.  After a few hours of poking and
prodding, I was able to get my wife's games completely restored.  Keep
in mind that what follows worked for me, and I do not claim to be an
expert.  I take no responsibility for anything that happens to any
device other than my own for following these steps.  Follow these steps
at your own risk.

One of the tools mentioned on the Angry Birds Nest guide is the [Android
Backup Extractor][abe].  A bit of web searching turns up the
[development page][abedev].  Reading through the documentation, I
learned that the output of the `adb backup` command is simply an
extended tape archive and `abe.jar` handles the interconversion between
the formats!  

A word of warning: `abe.jar` requires a [Java Runtime Environment of
7][jre7] which apparently was not already installed on my MacBook Pro.
Hunting down that fact took a couple of hours.

Now, to get things rolling, download the desired versions of Angry Birds
and complete one level.  This will ensure that the file structure for
the games are in place.  Now make a backup of the games and convert to a
tape archive.

    $ adb backup -apk -f angrybirds.orig.ab $(ls -d com.rovio.angry*)
    $ java -jar abe.jar unpack angrybirds.orig.ab angrybirds.orig.tar
    $ tar -xf angrybirds.orig.tar
    $ tar -tf angrybirds.orig.tar > angrybirds.list

The first step above creates a backup of the games we want and includes
the application file.  Supposedly, the application file is not
necessary, but I couldn't get the restore to work properly without it.
The subshell launched simply creates a list of all Rovio games I
extracted files for with the script shown above.  The second and third
steps convert and extract the archive.  The fourth step is necessary for
repacking the data after we have updated the files.  Apparently, [the
order of the files in the archive][elenkov_unpacking_2012] is critical
for performing the restore.

Now I was able to explicitly update the files and generate a new tape
archive which can be converted to an Android backup.

    $ for f in $(ls -d com.rovio.angry*); do 
    > cp -i $f/*.lua apps/$f/f
    > done
    $ star -c -f angrybirds.tar -no-dirslash list=angrybirds.list
    $ java -jar abe.jar pack angrybirds.tar angrybirds.ab
    $ adb restore angrybirds.ab.

And my wife was able to get back to popping pigs!  Now, a few notes:
First, when I was originally trying to create the tape archive, I tried
using `tar`, but that does not preserve the order of the files.  I
attempted to use `pax`, but I found files with long names.  That meant I
had to use `star` instead.  Second, I was able to get all of this to
work by getting the application file even though it is supposedly not
necessary.  Finally, in the future just use `adb backup`.  The advantage
of all of this was I got to learn more about the Android backup files
and discovered two new command line tools that hadn't crossed my radar
yet: `pax` and `star`.

EDIT 2014-11-22: While in the process of cleaning up my computer to do a
clean install of Yosemite, I came across one other script I used to pull
data off of my old Android phones.  As I already discussed above, this
really a pointless script now.  However, I don't want to just throw it
out and lose my notes.  I also don't want to create a repository just
for it, and I don't want it in my `dotfiles`.  So, I'll just put it
here.

    $ cat phonebu
    #!/bin/bash

    # We will also need to pull the apks to finish backing up the apps.
    # This can be accomplished by using get_apk and simply pulling the
    # apk. The ones to look out for are the ones on the sdcard (under 
    # /mnt/asec) as these will be pulled simply to a pkg.apk. We will 
    # need to make sure we know which one we are pulling using
    #
    #   adb pull ${apk}
    #
    # We could simply use sed to remove the -#/pkg portion of the apk in
    # the data from packages (downloaded_apps). Actually, looking at the
    # results, we may only need to remove the '/pkg' portion as the 
    # other apks appear to also contain the -# tag.
    #
    # We then need to look into what other bits of information we need
    # to pull from the phone.

    # Create the base directory to store the data
    basedir=backup_$(date +%F)
    mkdir -p ${basedir}

    # Make the directory for the apk
    mkdir -p ${basedir}/apks

    # Find the downloaded applications excluding the Google ones.
    apps=$( \
            adb shell pm list packages -f | \
            awk '{RS="\r";}  \
            (/data/ || /asec/) && !/\.android\./ \
            {sub(/package:/, ""); print $1}'  \
        )

    for app in ${apps}; do
        # Get the install and the folder
        apk=$(echo ${app} | awk -F= '{print $1}')
        fld=$(echo ${app} | awk -F= '{print $2}')

        # Make the data folder
        mkdir -p ${basedir}/${fld}

        # Copy the application data
        adb pull /data/data/${fld} ${basedir}/${fld}

        # Determine the local name for the apk.
        local_apk=$( \
                echo ${apk} | sed -e 's|\/pkg||' \
                -e 's|\/[a-zA-Z]*\/[a-zA-Z]*\/||' \
            )

        # Pull the apk
        adb pull ${apk} ${basedir}/apks/${local_apk}


[amslimfordy_how_2013]: http://www.angrybirdsnest.com/how-to-back-up-angry-birds-progress-on-android-rooted-and-non-rooted/#backup-new
[abe]: http://sourceforge.net/projects/adbextractor/
[abedev]: https://github.com/nelenkov/android-backup-extractor
[jre7]: http://www.oracle.com/technetwork/java/javase/downloads/jre7-downloads-1880261.html
[elenkov_unpacking_2012]: http://nelenkov.blogspot.com/2012/06/unpacking-android-backups.html

