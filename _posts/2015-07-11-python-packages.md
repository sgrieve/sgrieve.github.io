---
layout: post
title: Upgrading Python Packages on Windows
---

Today I decided to install [openCV](http://opencv.org/) to explore some image processing stuff I
had been thinking about. This required that I upgrade my numpy install to a newer
version. Windows is an awful environment to do things like this, so here is a guide
to save myself the pain the next time I have to do this.

## 1. Install pip

The python package manager [pip](https://pip.pypa.io/en/stable/) allows simple command line installation of python
packages using a command something like this:

`pip install <package name>`

But if you don't have it installed by default, as is the case for any python installs
before version 2.7.8 and 3.3, you need to install it first. Download the file
`get-pip.py` from [here](https://raw.github.com/pypa/pip/master/contrib/get-pip.py)
and run it at the command prompt with administrator privileges:

`python get-pip.py`

This will download and install pip to your local python install.

## 2. Download The Wheel

Pip will attempt to compile the desired python module on the fly, and on Windows
that can lead to a lot of problems. The solution is to get the wheel file and direct
pip to install from that, ensuring that the source files are correct for your hardware.
A good resource for wheel files is [here](http://www.lfd.uci.edu/~gohlke/pythonlibs). The
key is to download the correct file for your environment. I needed to upgrade numpy, so
I used the file:

`numpy-1.9.2+mkl-cp27-none-win32.whl`

**cp27** corresponds to the version of python you are running, in my case I use 2.7 and
**win32** indicates that I am using a 32 bit version of python.

## 3. Install The Package

Finally, at the shell, navigate to the folder where the wheel file was downloaded
to, and install from it:

`pip install numpy-1.9.2+mkl-cp27-none-win32.whl`

If you give it an incorrect wheel file version it will give the following message:

`<Filename> is not supported wheel on this platform`

But if you use the correct file, it should upgrade or install the package as required.
So now I can use numpy 1.9.2.
