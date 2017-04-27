---
layout: post
title: Thinning a Dataset
---

If you have a large plain text data file, that needs to be quickly plotted, it can be useful to
thin the data by selecting every nth line, particularly if the dataset is too large to be loaded
into memory using numpy. This post is based around [this SuperUser question](http://superuser.com/questions/396536/how-to-keep-only-every-nth-line-of-a-file).

If we have a a `.csv` file structured like this:

{% highlight sh %}
label,x_value,y_value,z_value
label1,1,1,1
label2,2,2,2
label3,3,3,3
label4,4,4,4
label5,5,5,5
label6,6,6,6
label7,7,7,7
label8,8,8,8
label9,9,9,9
{% endhighlight %}

And want to take every second row, and store them in a new file with the same structure,
we can use `awk` at the unix shell:

{% highlight sh %}
awk 'NR == 1 || NR % 2 == 0' DataFile.csv > NewDataFile.csv
{% endhighlight %}

awk is a powerful scripting language for manipulating line based data, which has
many functions well beyond the scope of this post, see this [guide](http://www.grymoire.com/Unix/Awk.html) for more details.
`NR` denotes the number of rows in the file, so using `NR == 1` will keep the header
row of the file (line 1) and `NR % 2 == 0` will keep any line which has a line number
divisible by 2. The contents of `NewDataFile.csv` would be:

{% highlight sh %}
label,x_value,y_value,z_value
label1,1,1,1
label3,3,3,3
label5,5,5,5
label7,7,7,7
label9,9,9,9
{% endhighlight %}

If you want to change the amount of data thinning, change the value `2` in the command `NR % 2 == 0`
to a larger value to increase the thinning amount. If you have a data file with no headers,
the command is simplified to:

{% highlight sh %}
awk 'NR % 2 == 0' DataFile.csv > NewDataFile.csv
{% endhighlight %}
