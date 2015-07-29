---
layout: post
title: Using gdb To Debug C++
---

When trying to find the precise point in your code that causes a crash, it is often useful to
use [gdb](http://www.gnu.org/software/gdb/documentation/) to debug the code. I always forget the basic syntax to get it running so
here is a very simple overview. This is by no means exhaustive, but should serve as a
jumping off point for using gdb.

## Compiler Flags

The first thing to do is make sure that the flag `-g` is within your makefile or included
in your gcc command. The line in the makefile should look something like this:


{% highlight c  %}
CFLAGS= -c -Wall -g
{% endhighlight %}

Where:

* `-c` - Compile but do not link the source files.
* `-Wall` - Warn All - Outputs all compiler warnings.
* `-g` - Debug - Produce debugging information

More info on these and other args can be found [here](http://courses.cs.washington.edu/courses/cse326/02wi/unix/g++.html).

## Run gdb

Once the code (`a.out`) is compiled with the `-g` flag, run it using gdb:

{% highlight sh  %}
s0675405@achray debug $ gdb a.out
{% endhighlight  %}

## Execute Code

Now, at the gdb prompt, give it any arguments and the code will run until it reaches
an exception:

{% highlight sh  %}
(gdb) run <arg1> <arg2> <arg3>
{% endhighlight  %}

## Backtrace

The last step is to get some detailed info on where an exception occurred, a good starting
point from this is to use `backtrace`

{% highlight sh  %}
(gdb) bt
{% endhighlight  %}

There is obviously much more to gdb than what is here, but this guide will get you
to the point of being able to better interrogate errors using the [gdb man page](http://www.gnu.org/software/gdb/documentation/).
