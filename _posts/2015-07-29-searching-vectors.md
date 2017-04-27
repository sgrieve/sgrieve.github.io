---
layout: post
title: Find a Value in a C++ Vector
---

To search for a value in a vector we can use [find](http://www.cplusplus.com/reference/algorithm/find/), which returns an iterator
pointing to the first value found in a vector which matches the value passed in.
If an item is not in a vector, the returned iterator points to one past the end of the
vector, `myVec.end()`.

So in this example, if we want to know if `mvValue` is contained in `myVec` we can use:

{% highlight c %}
if (find(myVec.begin(), myVec.end(), myValue) != myVec.end()){
  //myValue is in the vector
}
else {
  //myValue is not in the vector
}

{% endhighlight %}

`find` searches for `myValue` between the iterators `myVec.begin()` and  `myVec.end()`
and the return value, an iterator pointing to the found item is them compared with
an iterator pointing to one past the end of the vector, the condition for not found.
This can be reversed to use `==` instead of `!=` should that make more sense for a
particular use. We could also use iterators that point to subsets of the vector if we
knew the region of the vector that our data should be found in:

{% highlight c %}
if (find(myVec.begin()+3, myVec.begin()+9, myValue) != myVec.end()){
  //myValue is in the subset of the vector
}
else {
  //myValue is not in the subset of the vector
}

{% endhighlight %}

It is important to note that this will not cope with multiple items matching `myVal` and
will always return the first match it finds.
