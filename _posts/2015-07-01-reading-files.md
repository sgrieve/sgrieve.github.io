---
layout: post
title: Reading Data From Files with C++
---

I want to read some data from a text file of unknown length using C++. If the file
is space delimited this is quite easy. I can use `infile` to break each line up
into tokens divided by the spaces and then load them into temp variables.

If our data file is structured as follows:

{% highlight sh  %}

s0675405@achray loadtest $ head spaces.txt
1 4
2 5 
55 56
2131 5
5544 1
11 465
5 0
4 49875
6 1

{% endhighlight %}

I can use the following code to load the data and print each value to the terminal:

{% highlight c  %}

#include <string>
#include <fstream>

int main()
{

  string path = "/home/test/";

  ifstream infile;  
                     
  stringstream ss;
  ss << path << "spaces.txt";                
  infile.open(ss.str().c_str());
  
  int a, b;
  while (infile >> a >> b)
  {
    cout << a << " " << b << endl;
  }

}

{% endhighlight %}

Which results in:

{% highlight sh  %}

s0675405@achray driver_functions_swdg $ ./Load.out 
1 4
2 5
55 56
2131 5
5544 1
11 465
5 0
4 49875
6 1

{% endhighlight %}

If more data is included on each row it is easy to expand this to add in more variables, which 
can be operated on however you wish now that they are in memory. But what if our data is
not space delimited? 

Using the file `commas.txt`:

{% highlight sh  %}

s0675405@achray loadtest $ head commas.txt 
1,1,1,4
2,2,2,5 
5,5,55,56
2,2,2131,5
5,5,5544,1
1,1,11,465
5,5,5,0
4,4,4,49875
6,6,6,1

{% endhighlight %}

Will result in us getting no data printed to the terminal, as 1,4 is identified as a
single token, but is an invalid integer and so is ignored.

So we need to use a slightly [different approach](http://stackoverflow.com/a/7868998/1627162),
which explicitly defines the comma as our delimiter:

{% highlight c  %}

#include <string>
#include <fstream>

int main()
{
  string path = "/home/test/";

  ifstream infile;  
                     
  stringstream ss;
  ss << path << "commas.txt";                
  infile.open(ss.str().c_str());
   
  int a, b, c, d;
  char delimiter;
  while ((infile >> a >> delimiter >> b >> delimiter >> c >> delimiter >> d) && (delimiter == ','))
  {
    cout << a << " " << b << " " << c << " " << d << endl;
  }

}

{% endhighlight %}

And this method again parses the file correctly:

{% highlight sh %}

s0675405@achray driver_functions_swdg $ ./Load.out 
1 1 1 4
2 2 2 5
5 5 55 56
2 2 2131 5
5 5 5544 1
1 1 11 465
5 5 5 0
4 4 4 49875
6 6 6 1

{% endhighlight %}
