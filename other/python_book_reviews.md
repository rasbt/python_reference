
<a id="table-of-contents"></a>

# Python Book Reviews

- [Matplotlib Plotting Cookbook](#matplotlib-plotting-cookbook)
- [Python High Performance Programming](#python-high-performance-programming)
- [Learning IPython for Interactive Computing and Data Visualization](#learning-ipython-for-interactive-computing-and-data-visualization)
- [The Practice of Computing Using Python (2nd Edition)](#the-practice-of-computing-using-python-(2nd-Edition))
- [How to Make Mistakes in Python](#how-to-make-mistakes-in-python)


**Where are the links?**  

I decided to **not** post any links to any online shop here - I don't want to advertise anything but merely want to leave my brief thoughts in hope that it might be helpful to one or the other.


**About the rating scale/review scores**  

Most popular review sites provide some sort of rating, e.g., 7/10, 90/100, 3 stars out of 5 etc.  
I have to admit that I am not a big fan of those review scores - and you won't find them here. Based on my experience, review scores are just kindling all sorts of arguments, destructive debates, and hate-mails. Let's be honest, every opinion is subjective, and I think that boiling it down to a final score is just an annoyance for everyone.

---

### Matplotlib Plotting Cookbook

***by Alexandre Devert***

- Paperback: 222 pages   
- Release Date: March 2014  
- ISBN: 1849513260  
- ISBN 13: 9781849513265
- Publisher: Packt

**A good alternative to the official matplotlib documentation**



As a frequent matplotlib user I have to say that this book really fulfills it's promise as a cookbook by covering the most common use cases, and it is a pretty good and thorough introduction for beginners too (Python beginners as well as matplotlib beginners). However, the problem of this book is that there is the (free) matplotlib gallery (http://matplotlib.org/gallery.html) which also has plenty of very good examples, and I can imagine that it is a tough job as an author to add additional value to that.


What this book does very well is introducing matplotlib quite gently in the first chapter, which makes it quite attractive for Python & matplotlib beginners. But also here, we have the alternative free user guide available online http://matplotlib.org/contents.html

My main point of criticism why I find the matplotlib.org resources more accessible might be that they are actually in color: the plot and the code syntax. Unfortunately, the book only uses colors throughout the first chapter (and very very rarely for a handful of other plots later on), so that the largest portion of the plots are in gray-scale - also no syntax highlighting throughout this book. Since I have the ebook version, I do not fully understand why there is no coloring throughout the other chapters (especially the 2nd chapter, which is called "Chapter 2: Customizing Colors and Styles").

But overall, it covers matplotlib pretty well, and I'd recommend it as an alternative to the resources matplotlib.org.

But to it's defense, my hard copy of the "Gnuplot in Action" is also presented in gray-scales, and the "R Graphic's cookbook" also only makes use of colors rather sparingly. However, I think, nowadays in 2014 I'd at least expect the ebook to be in color - especially if you want to make it more attractive than the freely available online resources.


Not a real point of criticism but more like a suggestion for future editions: as big fan of it, I was actually looking for this section that mentions how to use it in IPython notebooks (%pylab inline vs. matplotlib inline), and maybe also plotly for additional value :)

---

### Python High Performance Programming

***by Gabriele Lanaro***


- Paperback: 108 pages  
- Release Date: December 2013  
- ISBN: 1783288450  
- ISBN 13: 9781783288458
- Publisher: Packt

**Really recommended book for Python beginners**

A really nice read! It covered 4 important topics: how to profile & benchmark Python code, NumPy, C-extensions via Cython, and parallel programming. However, I found it a little bit too brief on all of the topics, a little bit more depth would have been nice.
Also, I missed a few parts, like general Python tricks for better performance (e.g., in-place operators for mutable types and many many others that I started to create benchmarks for here: https://github.com/rasbt/One-Python-benchmark-per-day)
And another thing that I think would be worth adding in a future addition would be the JIT (just-in-time) compilers, such as parakeet or Numba, especially since Numexpr was briefly mentioned in the NumPy section.

But overall I think it is a very recommended read for Python beginners!

---

### Learning Ipython for Interactive Computing and Data Visualization


***by Cyrille Rossant***



- Paperback: 138 pages  
- Release Date: April 2013  
- ISBN: 1782169938  
- ISBN 13: 9781782169932
- Publisher: Packt



**A short intro book that I would recommend to everyone to get a taste of IPython's greatest features**

It's a brief but good book that provides a good introduction to the IPython environment. I think the high-performance chapter that explained the usage of NumPy among others was a little bit redundant, since it is a general Python topic and is not necessarily specific to IPython. And on the other hand, the chapters on customizing IPython and especially writing own IPython magic extensions were way too brief - when I wrote my own extensions, I needed to look more closely at the IPython extension source code to be able to handle this task.
But still, this is a nice book that I would recommend to people who are fairly new to Python and people who want to get a taste of IPython!﻿

---

### The Practice of Computing Using Python (2nd Edition)


***by William F. Punch and Richard Enbody***


- Paperback: 792 pages  
- Release Date: February 25, 2012  
- ISBN-10: 013280557X  
- ISBN-13: 978-0132805575
- Publisher: Pearson

**A great first Python book**

This was actually my first Python book. It is not meant to be a thorough coverage of all the greatest Python features and capabilities, but it provides a great introduction to computing and programming in general by using the Python language.  
It is maybe a little bit to trivial for programmers who just want to pick up the syntax Python language, but I would really recommend this book as a first introduction to people who have never programmed before - I think that Python is a very nice language to pick up this valuable skill.  
I am a big fan of books that contains self-assessments: from short exercises up to bigger project assignments, and this book comes with a huge abundance of valuable material, which is a big bonus point.


---

### How to Make Mistakes in Python


***by Mike Pirnat***


- e-Book: 154 pages  
- Release Date: October, 2015   
- Publisher: O'Reilly  


Although I already have many years of experience with coding in Python, I thought that it couldn't hurt to read through this book -- I got the free copy via O'Reilly, and it's relatively short. Sure, many topics throughout this book are trivial for an experienced Python programmer, but I believe that it's a great summary for someone who just got started with this programming language. Although the author doesn't go into technical depths regarding e.g., pylint, unit testing, etc., I think that his descriptions are sufficient, and a reader can always look at the online documentation of the respective tools. What's more important is that the author gives good reasons WHY we should use/do certain things, and I really like the use of paraphrased examples from real-world use cases. It's a solid book overall!
