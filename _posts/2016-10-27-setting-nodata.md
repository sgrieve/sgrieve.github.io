---
layout: post
title: Using GDAL to fix NoData issues
---

If you grab some raster data and it has a weird NoData value set, it may not work properly in LSDTopoTools. To fix this run this command:

{% highlight sh  %}

$ gdalwarp -of ENVI -srcnodata -32768 -dstnodata -9999 input.tif output.bil

{% endhighlight %}

This will take input data in any gdal supported format and replace all NoData values with -9999. To check the NoData vale of a file, use `gdalinfo`.
