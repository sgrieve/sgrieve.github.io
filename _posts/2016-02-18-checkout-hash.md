---
layout: post
title: Checking out a specific revision using git
---

If I need to grab a specific version of a git repository, for example, to run latexdiff on an old version of a paper I can do the following. Firstly get the SHA for the particular commit, either through the command line:

{% highlight sh %}

$ git log -1

{% endhighlight %}

Or from the web interface for the repo. For example the SHA for a recent post on this blog is a29c140c8aad0706694115ff66fc6321218fe38b and

{% highlight sh %}

commit a29c140c8aad0706694115ff66fc6321218fe38b
Author: sgrieve >
Date:   Fri Dec 11 16:24:43 2015 +0000

    New post

{% endhighlight %}

So we can check out this specific revision using:

{% highlight sh %}

$ git clone <repository url>
$ git checkout a29c140c8aad0706694115ff66fc6321218fe38b

{% endhighlight %}

This will return all files in the repository to their status at the time of the commit.
