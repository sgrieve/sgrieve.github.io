---
layout: post
title: Getting a Random Sample From an Array
---

I wanted to quickly grab a random sample of values from a larger array to perform 
some testing. I didn't need to worry about the distribution of the sampled data: I just
needed `n` values drawn at random from the array. I used  `shuffle` from `numpy.random`
to randomise the values in my input array. `shuffle` operates in place, so I made a 
copy of the array to avoid future problems. I can then simply take a slice of the 
first `n` values in the array, which will be a random selection of `n` values drawn from
the original data:

{% highlight py  %}

def sample_from_population(a,n):
    """
    Get a random sample of length n from array a
    """
    from numpy.random import shuffle
        
    a_new = a.copy()
    shuffle(a_new)
    
    return a_new[:n]

{% endhighlight %}

This can be tested using some example data:

{% highlight py  %}

import numpy as np        

data = np.arange(0,10)

print data
print sample_from_population(data,5)

{% endhighlight %}

Which yields:

{% highlight py  %}

[0 1 2 3 4 5 6 7 8 9]
[5 2 8 1 0]

{% endhighlight %}
