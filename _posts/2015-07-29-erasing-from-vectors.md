---
layout: post
title: Erasing a value from a vector in C++
---

To remove a value from a vector we must follow the [erase-remove idiom](https://en.wikipedia.org/wiki/Erase%E2%80%93remove_idiom),
the first step is to find the value that we wish to remove and move it to the front of the
container. This is performed using [remove](http://www.cplusplus.com/reference/algorithm/remove/)
which returns an iterator pointing to the new end of the vector, effectively ignoring the removed values.
For example:

{% highlight c %}

vector<int> myVec;

myVec.push_back(5);
myVec.push_back(3);
myVec.push_back(4);
myVec.push_back(5);
myVec.push_back(1);
myVec.push_back(5);

//print current vector contents to screen
for (vector<int>::iterator it = myVec.begin(); it !=  myVec.end(); ++it){
 cout << *it << " ";
}
cout << endl;  

{% endhighlight %}

Will print this to screen:

{% highlight sh %}
5 3 4 5 1 5
{% endhighlight %}

If we want to remove all `5` values from `myVec` we can do this:

{% highlight c %}
int myValue = 5;
vector<int>::iterator NewEnd = remove(myVec.begin(), myVec.end(), myValue);
//NewEnd points to one past the end of the vector with the value 5 removed

for (vector<int>::iterator it = myVec.begin(); it != NewEnd; ++it){
 cout << *it<< " ";

}
cout << endl;  

{% endhighlight %}

Which will produce the following data on the screen:

Will print this to screen:

{% highlight sh %}
3 4 1
{% endhighlight %}

However, the vector's size has not changed. The removed values are now at the end of the vector
and could still be accessed by using `myVec.end()` instead of `NewEnd`. So now we will
remove the values using [erase](http://www.cplusplus.com/reference/vector/vector/erase/),
to complete the process. If `erase` is passed 2 iterators it will erase all of the values between
those 2 points. So we want to erase every value between `NewEnd` and `myVec.end()`:

{% highlight c %}

myVec.erase(NewEnd, myVec.end());

{% endhighlight %}

We can test that this has worked by attempting to write the whole vector to screen:

{% highlight c %}
for (vector<int>::iterator it = myVec.begin(); it !=  myVec.end(); ++it){
 cout << *it << " ";
}
cout << endl;  

{% endhighlight %}

Which gives us a vector completely free of our erased data:

{% highlight sh %}
3 4 1
{% endhighlight %}

It is also possible to combine this idiom into a one liner:

{% highlight c %}

myVec.erase(remove(myVec.begin(), myVec.end(), myValue), myVec.end());

{% endhighlight %}

It should be noted that this code will modify vectors in place so should be used with
caution.
