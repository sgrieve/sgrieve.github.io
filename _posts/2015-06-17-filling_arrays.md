---
layout: post
title: Initializing numpy arrays
---


You can create numpy arrays in a bunch of ways. To create an array of empty values
I use `np.empty(shape)` where shape is the dimensions of the array to be created:

{% highlight py  %}

In [4]: a = np.empty(5)

In [5]: a
Out[5]:
array([  1.16649532e-293,   1.15621717e-293,   8.89883728e-300,
         9.92174091e+247,   6.59686091e-310])

In [11]: a = np.empty((2,2))

In [12]: a
Out[12]:
array([[  9.09689384e-297,   8.89883726e-300],
        [  1.52776817e-316,   1.36680489e-163]])

{% endhighlight %}

Using this you have to be careful that all the values will be initialized, or you
might get weird behaviours. The same process can be used to get an array of zeros or
ones. Simply use `np.ones(shape)` and `np.zeros(shape)`. There are also the commands
`np.ones_like(array)`, `np.zeros_like(array)` and `np.empty_like(array)` which use the
template array define the dimensions:

{% highlight py %}

In [13]: template = np.ones((3,2))

In [14]: template
Out[14]:
array([[ 1.,  1.],
       [ 1.,  1.],
       [ 1.,  1.]])

In [15]: a = np.zeros_like(template)

In [16]: a
Out[16]:
array([[ 0.,  0.],
       [ 0.,  0.],
       [ 0.,  0.]])

{% endhighlight %}

But if I want to fill an array with a value other than 1 or 0? There are lots of options,
I could do something like this:

{% highlight py  %}
In [24]: a = np.ones((2,2))

In [25]: a = a * 17

In [26]: a
Out[26]:
array([[ 17.,  17.],
       [ 17.,  17.]])
{% endhighlight %}

where I create an array of ones and then multiply each value by my desired initial
value. Or I could create an array of the right shape and then assign all of the values
at once using slice notation:

{% highlight py %}
In [20]: a = np.empty((2,2))

In [21]: a[:][:] = 147

In [22]: a
Out[22]:
array([[ 147.,  147.],
       [ 147.,  147.]])
{% endhighlight %}

This is nice because it is explicit, and makes sense without any other docs. The final
method is to use `fill` **which modifies the array in place**:

{% highlight py %}
In [17]: a = np.empty((2,2))

In [18]: a.fill(22)

In [19]: a
Out[19]:
array([[ 22.,  22.],
       [ 22.,  22.]])
{% endhighlight %}

According to discussions [here](http://stackoverflow.com/questions/1704823/initializing-numpy-matrix-to-something-other-than-zero-or-one) using fill is faster for small datasets, but as n increases the performance gain is lost, so
it mainly depends on remembering the syntax.
