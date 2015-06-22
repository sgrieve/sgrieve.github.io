---
layout: post
title: Sorting a List by Another List
---

I have 3 python lists of the same dimensions, `a`, `b` and `c` and I want to reorder
them all based on the values in `b`. First create some toy data:

{% highlight py  %}
from random import shuffle
import string

a = range(10)
b = range(10)
shuffle(b)
c = list(string.ascii_lowercase)[:10]

#print the current order of the values
for q in zip(a,b,c):
  print q

q=
(0, 4, 'a')
(1, 0, 'b')
(2, 1, 'c')
(3, 3, 'd')
(4, 6, 'e')
(5, 9, 'f')
(6, 2, 'g')
(7, 5, 'h')
(8, 7, 'i')
(9, 8, 'j')

{% endhighlight %}

Now we zip the 3 lists together and sort by the first element, in our example this
will be `b`:

{% highlight py  %}
sorted_data = sorted(zip(b,a,c))
{% endhighlight %}

Finally we can unpack the sorted, zipped lists using a few list comprehensions to
get the data back sorted but in its original shape:

{% highlight py  %}

a = [x[1] for x in sorted_data]
b = [x[0] for x in sorted_data]
b = [x[2] for x in sorted_data]

#print the new order of the values
for q in zip(a,b,c):
  print q

q=
(1, 0, 'b')
(2, 1, 'c')
(6, 2, 'g')
(3, 3, 'd')
(0, 4, 'a')
(7, 5, 'h')
(4, 6, 'e')
(8, 7, 'i')
(9, 8, 'j')
(5, 9, 'f')

{% endhighlight %}
