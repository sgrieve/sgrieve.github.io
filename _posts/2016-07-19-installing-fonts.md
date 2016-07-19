---
layout: post
title: Installing fonts in Ubuntu 14.04
---

To install fonts on Ubuntu, first download the fonts that you want. For example I wanted the [Font Awsome](http://fontawesome.io/) symbols for my CV.

Once the files have been downloaded, copy them into your fonts directory `/usr/share/fonts/`. Depending on your system you will probably need to use `sudo` to get permissions to copy files into that directory. This will make the fonts available for every user of the computer.

A local directory can be created at `~/.fonts/` which will make the fonts available for just the current user.

Once all the new font files have been copied into the required folders, the font cache needs to be updated, or the computer restarted. Updating the cache is less hassle and is done with this command:

{% highlight sh  %}

$ fc-cache -f -v

{% endhighlight %}

The `-f` switch forces a complete rebuild of the cache, and the `-v` (note lower case!) gives a verbose output so you can check the fonts are all installed correctly.
