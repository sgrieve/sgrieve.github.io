---
layout: post
title: Checking For nans in a Numpy Array
---

I was trying to debug some code today and found that I had a `nan` value propagating
through some calculations, causing very weird behavior. I figured there must be a
quick way to check numpy arrays for nan values. We can use the numpy function `isnan`:

{% highlight py  %}
>>> a = np.array(range(5,20,2))
>>> a
array([ 5,  7,  9, 11, 13, 15, 17, 19])
>>> b = np.append(a,np.nan)
>>> b
array([  5.,   7.,   9.,  11.,  13.,  15.,  17.,  19.,  nan])
>>> np.isnan(a)
array([False, False, False, False, False, False, False, False], dtype=bool)
>>> np.isnan(b)
array([False, False, False, False, False, False, False, False,  True], dtype=bool)
{% endhighlight %}

Here we can see that `isnan` returns a boolean array in the same shape as the input data,
with a value of `True` indicating that the value at that point in the array is a `nan`. We
can use these booleans to slice the arrays to access the nans:

{% highlight py  %}
>>> b[np.isnan(b)]
array([ nan])
{% endhighlight %}

But that's not particularly useful, so lets invert the logic using `~` so we can get all of the
non `nan` data:

{% highlight py  %}
>>> b[~np.isnan(b)]
array([  5.,   7.,   9.,  11.,  13.,  15.,  17.,  19.])
{% endhighlight %}

This performs a [unary bitwise inversion](https://docs.python.org/2/reference/expressions.html#unary-arithmetic-and-bitwise-operations) on each element in our array, swapping `True` to `False` and `False` to `True`. Finally,
if we are not interested in where the nans are, but just want to know if they are there
or not, we can use [any()](https://docs.python.org/2/library/functions.html#any) to return a boolean if any value in the array is true:

{% highlight py  %}
>>> np.isnan(a).any()
False
>>> np.isnan(b).any()
True
{% endhighlight %}

Or if we wanted to check that every value in an array was true, for example if we had
all nans, we can use [all()](https://docs.python.org/2/library/functions.html#all):

{% highlight py  %}
>>> c = np.array([np.nan,np.nan])
>>> c
array([ nan,  nan]
>>> np.isnan(a).all()
False
>>> np.isnan(b).all()
False
>>> np.isnan(c).all()
True
{% endhighlight %}

Or to check that every value is not a `nan` we can use `all()` and `~` together:

{% highlight py  %}
>>> ~np.isnan(a).all()
True
>>> ~np.isnan(b).all()
True
>>> ~np.isnan(c).all()
False
{% endhighlight %}
