[Sebastian Raschka](http://sebastianraschka.com)  
last updated: 05/24/2014

<br>

**This is a subsection of ["A collection of not-so-obvious Python stuff you should know!"](http://nbviewer.ipython.org/github/rasbt/python_reference/blob/master/not_so_obvious_python_stuff.ipynb?create=1)**

<a id='sections'></a>

<br>

## Key differences between Python 2 and 3
<br>

There are some good articles already that are summarizing the differences between Python 2 and 3, e.g.,  

- [https://wiki.python.org/moin/Python2orPython3](https://wiki.python.org/moin/Python2orPython3)

- [https://docs.python.org/3.0/whatsnew/3.0.html](https://docs.python.org/3.0/whatsnew/3.0.html)

- [http://python3porting.com/differences.html](http://python3porting.com/differences.html)

- [https://docs.python.org/3/howto/pyporting.html](https://docs.python.org/3/howto/pyporting.html)  

etc.

But it might be still worthwhile, especially for Python newcomers, to take a look at some of those!
(Note: the the code was executed in Python 3.4.0 and Python 2.7.5 and copied from interactive shell sessions.)

<a id='py23_overview'></a>

<br>

### Overview - Key differences between Python 2 and 3




- [Unicode](#unicode)
- [The print statement](#print)
- [Integer division](#integer_div)
- [xrange()](#xrange)
- [Raising exceptions](#raising_exceptions)
- [Handling exceptions](#handling_exceptions)
- [next() function and .next() method](#next_next)
- [Loop variables and leaking into the global scope](#loop_leak)
- [Comparing unorderable types](#compare_unorder)

<br>
<br>

	
<a id='unicode'></a>
<br>
<br>

### Unicode...

[[back to Python 2.x vs 3.x overview](#py23_overview)]


####- Python 2: 
We have ASCII `str()` types, separate `unicode()`, but no `byte` type
####- Python 3: 
Now, we finally have Unicode (utf-8) `str`ings, and 2 byte classes: `byte` and `bytearray`s

<br>

<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #888888">#############</span>
<span style="color: #888888"># Python 2</span>
<span style="color: #888888">#############</span>

<span style="color: #333333">&gt;&gt;&gt;</span> <span style="color: #007020">type</span>(unicode(<span style="background-color: #fff0f0">&#39;is like a python3 str()&#39;</span>))
<span style="color: #333333">&lt;</span><span style="color: #007020">type</span> <span style="background-color: #fff0f0">&#39;unicode&#39;</span><span style="color: #333333">&gt;</span>

<span style="color: #333333">&gt;&gt;&gt;</span> <span style="color: #007020">type</span>(b<span style="background-color: #fff0f0">&#39;byte type does not exist&#39;</span>)
<span style="color: #333333">&lt;</span><span style="color: #007020">type</span> <span style="background-color: #fff0f0">&#39;str&#39;</span><span style="color: #333333">&gt;</span>

<span style="color: #333333">&gt;&gt;&gt;</span> <span style="background-color: #fff0f0">&#39;they are really&#39;</span> <span style="color: #333333">+</span> b<span style="background-color: #fff0f0">&#39; the same&#39;</span>
<span style="background-color: #fff0f0">&#39;they are really the same&#39;</span>

<span style="color: #333333">&gt;&gt;&gt;</span> <span style="color: #007020">type</span>(<span style="color: #007020">bytearray</span>(b<span style="background-color: #fff0f0">&#39;bytearray oddly does exist though&#39;</span>))
<span style="color: #333333">&lt;</span><span style="color: #007020">type</span> <span style="background-color: #fff0f0">&#39;bytearray&#39;</span><span style="color: #333333">&gt;</span>

<span style="color: #888888">#############</span>
<span style="color: #888888"># Python 3</span>
<span style="color: #888888">#############</span>

<span style="color: #333333">&gt;&gt;&gt;</span> <span style="color: #007020">print</span>(<span style="background-color: #fff0f0">&#39;strings are now utf-8 </span><span style="color: #666666; font-weight: bold; background-color: #fff0f0">\u03BC</span><span style="background-color: #fff0f0">nico</span><span style="color: #666666; font-weight: bold; background-color: #fff0f0">\u0394</span><span style="background-color: #fff0f0">é!&#39;</span>)
strings are now utf<span style="color: #333333">-</span><span style="color: #0000DD; font-weight: bold">8</span> μnicoΔé<span style="color: #FF0000; background-color: #FFAAAA">!</span>


<span style="color: #333333">&gt;&gt;&gt;</span> <span style="color: #007020">type</span>(b<span style="background-color: #fff0f0">&#39; and we have byte types for storing data&#39;</span>)
<span style="color: #333333">&lt;</span><span style="color: #008800; font-weight: bold">class</span> <span style="color: #FF0000; background-color: #FFAAAA">&#39;</span><span style="color: #BB0066; font-weight: bold">bytes</span><span style="background-color: #fff0f0">&#39;&gt;</span>

<span style="color: #333333">&gt;&gt;&gt;</span> <span style="color: #007020">type</span>(<span style="color: #007020">bytearray</span>(b<span style="background-color: #fff0f0">&#39;but also bytearrays for those who prefer them over strings&#39;</span>))
<span style="color: #333333">&lt;</span><span style="color: #008800; font-weight: bold">class</span> <span style="color: #FF0000; background-color: #FFAAAA">&#39;</span><span style="color: #BB0066; font-weight: bold">bytearray</span><span style="background-color: #fff0f0">&#39;&gt;</span>

<span style="color: #333333">&gt;&gt;&gt;</span> <span style="background-color: #fff0f0">&#39;string&#39;</span> <span style="color: #333333">+</span> b<span style="background-color: #fff0f0">&#39;bytes for data&#39;</span>
Traceback (most recent call last):s
  File <span style="background-color: #fff0f0">&quot;&lt;stdin&gt;&quot;</span>, line <span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #000000; font-weight: bold">in</span> <span style="color: #333333">&lt;</span>module<span style="color: #333333">&gt;</span>
<span style="color: #FF0000; font-weight: bold">TypeError</span>: Can<span style="background-color: #fff0f0">&#39;t convert &#39;</span><span style="color: #007020">bytes</span><span style="background-color: #fff0f0">&#39; object to str implicitly</span>
</pre></div>


<a id='print'></a>
<br>
<br>

### The print statement

[[back to Python 2.x vs 3.x overview](#py23_overview)]

Very trivial, but this change makes sense, Python 3 now only accepts `print`s with proper parentheses - just like the other function calls ...

<br>
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #888888"># Python 2</span>
<span style="color: #333333">&gt;&gt;&gt;</span> <span style="color: #007020">print</span> <span style="background-color: #fff0f0">&#39;Hello, World!&#39;</span>
Hello, World<span style="color: #FF0000; background-color: #FFAAAA">!</span>
<span style="color: #333333">&gt;&gt;&gt;</span> <span style="color: #007020">print</span>(<span style="background-color: #fff0f0">&#39;Hello, World!&#39;</span>)
Hello, World<span style="color: #FF0000; background-color: #FFAAAA">!</span>

<span style="color: #888888"># Python 3</span>
<span style="color: #333333">&gt;&gt;&gt;</span> <span style="color: #007020">print</span>(<span style="background-color: #fff0f0">&#39;Hello, World!&#39;</span>)
Hello, World<span style="color: #FF0000; background-color: #FFAAAA">!</span>
<span style="color: #333333">&gt;&gt;&gt;</span> <span style="color: #007020">print</span> <span style="background-color: #fff0f0">&#39;Hello, World!&#39;</span>
  File <span style="background-color: #fff0f0">&quot;&lt;stdin&gt;&quot;</span>, line <span style="color: #0000DD; font-weight: bold">1</span>
    <span style="color: #007020">print</span> <span style="background-color: #fff0f0">&#39;Hello, World!&#39;</span>
                        <span style="color: #333333">^</span>
<span style="color: #FF0000; font-weight: bold">SyntaxError</span>: invalid syntax
</pre></div>

<br>

And if we want to print the output of 2 consecutive print functions on the same line, you would use a comma in Python 2, and a `end=""` in Python 3:

<br>

<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #888888"># Python 2</span>
<span style="color: #333333">&gt;&gt;&gt;</span> <span style="color: #007020">print</span> <span style="background-color: #fff0f0">&quot;line 1&quot;</span>, ; <span style="color: #007020">print</span> <span style="background-color: #fff0f0">&#39;same line&#39;</span>
line <span style="color: #0000DD; font-weight: bold">1</span> same line

<span style="color: #888888"># Python 3</span>
<span style="color: #333333">&gt;&gt;&gt;</span> <span style="color: #007020">print</span>(<span style="background-color: #fff0f0">&quot;line 1&quot;</span>, end<span style="color: #333333">=</span><span style="background-color: #fff0f0">&quot;&quot;</span>) ; <span style="color: #007020">print</span> (<span style="background-color: #fff0f0">&quot; same line&quot;</span>)
line <span style="color: #0000DD; font-weight: bold">1</span> same line
</pre></div>


<a id='integer_div'></a>
<br>
<br>

### Integer division

[[back to Python 2.x vs 3.x overview](#py23_overview)]


This is a pretty dangerous thing if you are porting code, or executing Python 3 code in Python 2 since the change in integer-division behavior can often go unnoticed.  
So, I still tend to use a `float(3)/2` or `3/2.0` instead of a `3/2` in my Python 3 scripts to save the Python 2 guys some trouble ... (PS: and vice versa, you can `from __future__ import division` in your Python 2 scripts).

<br>
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #888888"># Python 2</span>
<span style="color: #333333">&gt;&gt;&gt;</span> <span style="color: #0000DD; font-weight: bold">3</span> <span style="color: #333333">/</span> <span style="color: #0000DD; font-weight: bold">2</span>
<span style="color: #0000DD; font-weight: bold">1</span>
<span style="color: #333333">&gt;&gt;&gt;</span> <span style="color: #0000DD; font-weight: bold">3</span> <span style="color: #333333">//</span> <span style="color: #0000DD; font-weight: bold">2</span>
<span style="color: #0000DD; font-weight: bold">1</span>
<span style="color: #333333">&gt;&gt;&gt;</span> <span style="color: #0000DD; font-weight: bold">3</span> <span style="color: #333333">/</span> <span style="color: #6600EE; font-weight: bold">2.0</span>
<span style="color: #6600EE; font-weight: bold">1.5</span>
<span style="color: #333333">&gt;&gt;&gt;</span> <span style="color: #0000DD; font-weight: bold">3</span> <span style="color: #333333">//</span> <span style="color: #6600EE; font-weight: bold">2.0</span>
<span style="color: #6600EE; font-weight: bold">1.0</span>

<span style="color: #888888"># Python 3</span>
<span style="color: #333333">&gt;&gt;&gt;</span> <span style="color: #0000DD; font-weight: bold">3</span> <span style="color: #333333">/</span> <span style="color: #0000DD; font-weight: bold">2</span>
<span style="color: #6600EE; font-weight: bold">1.5</span>
<span style="color: #333333">&gt;&gt;&gt;</span> <span style="color: #0000DD; font-weight: bold">3</span> <span style="color: #333333">//</span> <span style="color: #0000DD; font-weight: bold">2</span>
<span style="color: #0000DD; font-weight: bold">1</span>
<span style="color: #333333">&gt;&gt;&gt;</span> <span style="color: #0000DD; font-weight: bold">3</span> <span style="color: #333333">/</span> <span style="color: #6600EE; font-weight: bold">2.0</span>
<span style="color: #6600EE; font-weight: bold">1.5</span>
<span style="color: #333333">&gt;&gt;&gt;</span> <span style="color: #0000DD; font-weight: bold">3</span> <span style="color: #333333">//</span> <span style="color: #6600EE; font-weight: bold">2.0</span>
<span style="color: #6600EE; font-weight: bold">1.0</span>
</pre></div>


<a id='xrange'></a>
<br>
<br>

###`xrange()` 

[[back to Python 2.x vs 3.x overview](#py23_overview)]

 
`xrange()` was pretty popular in Python 2.x if you wanted to create an iterable object. The behavior was quite similar to a generator ('lazy evaluation'), but you could iterate over it infinitely. The advantage was that it was generally faster than `range()` (e.g., in a for-loop) - not if you had to iterate over the list multiple times, since the generation happens every time from scratch!  
In Python 3, the `range()` was implemented like the `xrange()` function so that a dedicated `xrange()` function does not exist anymore.


<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #888888"># Python 2</span>
<span style="color: #333333">&gt;</span> python <span style="color: #333333">-</span>m timeit <span style="background-color: #fff0f0">&#39;for i in range(1000000):&#39;</span> <span style="background-color: #fff0f0">&#39; pass&#39;</span>
<span style="color: #0000DD; font-weight: bold">10</span> loops, best of <span style="color: #0000DD; font-weight: bold">3</span>: <span style="color: #0000DD; font-weight: bold">66</span> msec per loop

    <span style="color: #333333">&gt;</span> python <span style="color: #333333">-</span>m timeit <span style="background-color: #fff0f0">&#39;for i in xrange(1000000):&#39;</span> <span style="background-color: #fff0f0">&#39; pass&#39;</span>
<span style="color: #0000DD; font-weight: bold">10</span> loops, best of <span style="color: #0000DD; font-weight: bold">3</span>: <span style="color: #6600EE; font-weight: bold">27.8</span> msec per loop

<span style="color: #888888"># Python 3</span>
<span style="color: #333333">&gt;</span> python3 <span style="color: #333333">-</span>m timeit <span style="background-color: #fff0f0">&#39;for i in range(1000000):&#39;</span> <span style="background-color: #fff0f0">&#39; pass&#39;</span>
<span style="color: #0000DD; font-weight: bold">10</span> loops, best of <span style="color: #0000DD; font-weight: bold">3</span>: <span style="color: #6600EE; font-weight: bold">51.1</span> msec per loop

<span style="color: #333333">&gt;</span> python3 <span style="color: #333333">-</span>m timeit <span style="background-color: #fff0f0">&#39;for i in xrange(1000000):&#39;</span> <span style="background-color: #fff0f0">&#39; pass&#39;</span>
Traceback (most recent call last):
  File <span style="background-color: #fff0f0">&quot;/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/timeit.py&quot;</span>, line <span style="color: #0000DD; font-weight: bold">292</span>, <span style="color: #000000; font-weight: bold">in</span> main
    x <span style="color: #333333">=</span> t<span style="color: #333333">.</span>timeit(number)
  File <span style="background-color: #fff0f0">&quot;/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/timeit.py&quot;</span>, line <span style="color: #0000DD; font-weight: bold">178</span>, <span style="color: #000000; font-weight: bold">in</span> timeit
    timing <span style="color: #333333">=</span> <span style="color: #007020">self</span><span style="color: #333333">.</span>inner(it, <span style="color: #007020">self</span><span style="color: #333333">.</span>timer)
  File <span style="background-color: #fff0f0">&quot;&lt;timeit-src&gt;&quot;</span>, line <span style="color: #0000DD; font-weight: bold">6</span>, <span style="color: #000000; font-weight: bold">in</span> inner
    <span style="color: #008800; font-weight: bold">for</span> i <span style="color: #000000; font-weight: bold">in</span> xrange(<span style="color: #0000DD; font-weight: bold">1000000</span>):
<span style="color: #FF0000; font-weight: bold">NameError</span>: name <span style="background-color: #fff0f0">&#39;xrange&#39;</span> <span style="color: #000000; font-weight: bold">is</span> <span style="color: #000000; font-weight: bold">not</span> defined
</pre></div>


<a id='raising_exceptions'></a>
<br>
<br>

### Raising exceptions

[[back to Python 2.x vs 3.x overview](#py23_overview)]



Where Python 2 accepts both notations, the 'old' and the 'new' way, Python 3 chokes (and raises a `SyntaxError` in turn) if we don't enclose the exception argument in parentheses:

<br>
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #888888"># Python 2</span>
<span style="color: #333333">&gt;&gt;&gt;</span> <span style="color: #008800; font-weight: bold">raise</span> <span style="color: #FF0000; font-weight: bold">IOError</span>, <span style="background-color: #fff0f0">&quot;file error&quot;</span>
Traceback (most recent call last):
  File <span style="background-color: #fff0f0">&quot;&lt;stdin&gt;&quot;</span>, line <span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #000000; font-weight: bold">in</span> <span style="color: #333333">&lt;</span>module<span style="color: #333333">&gt;</span>
<span style="color: #FF0000; font-weight: bold">IOError</span>: file error
<span style="color: #333333">&gt;&gt;&gt;</span> <span style="color: #008800; font-weight: bold">raise</span> <span style="color: #FF0000; font-weight: bold">IOError</span>(<span style="background-color: #fff0f0">&quot;file error&quot;</span>)
Traceback (most recent call last):
  File <span style="background-color: #fff0f0">&quot;&lt;stdin&gt;&quot;</span>, line <span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #000000; font-weight: bold">in</span> <span style="color: #333333">&lt;</span>module<span style="color: #333333">&gt;</span>
<span style="color: #FF0000; font-weight: bold">IOError</span>: file error

    
<span style="color: #888888"># Python 3    </span>
<span style="color: #333333">&gt;&gt;&gt;</span> <span style="color: #008800; font-weight: bold">raise</span> <span style="color: #FF0000; font-weight: bold">IOError</span>, <span style="background-color: #fff0f0">&quot;file error&quot;</span>
  File <span style="background-color: #fff0f0">&quot;&lt;stdin&gt;&quot;</span>, line <span style="color: #0000DD; font-weight: bold">1</span>
    <span style="color: #008800; font-weight: bold">raise</span> <span style="color: #FF0000; font-weight: bold">IOError</span>, <span style="background-color: #fff0f0">&quot;file error&quot;</span>
                 <span style="color: #333333">^</span>
<span style="color: #FF0000; font-weight: bold">SyntaxError</span>: invalid syntax
<span style="color: #333333">&gt;&gt;&gt;</span> <span style="color: #008800; font-weight: bold">raise</span> <span style="color: #FF0000; font-weight: bold">IOError</span>(<span style="background-color: #fff0f0">&quot;file error&quot;</span>)
Traceback (most recent call last):
  File <span style="background-color: #fff0f0">&quot;&lt;stdin&gt;&quot;</span>, line <span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #000000; font-weight: bold">in</span> <span style="color: #333333">&lt;</span>module<span style="color: #333333">&gt;</span>
<span style="color: #FF0000; font-weight: bold">OSError</span>: file error
</pre></div>


<a id='handling_exceptions'></a>
<br>
<br>

### Handling exceptions

[[back to Python 2.x vs 3.x overview](#py23_overview)]



Also the handling of exceptions has slightly changed in Python 3. Now, we have to use the `as` keyword!

<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #888888"># Python 2</span>
<span style="color: #333333">&gt;&gt;&gt;</span> <span style="color: #008800; font-weight: bold">try</span>:
<span style="color: #333333">...</span>     blabla
<span style="color: #333333">...</span> <span style="color: #008800; font-weight: bold">except</span> <span style="color: #FF0000; font-weight: bold">NameError</span>, err:
<span style="color: #333333">...</span>     <span style="color: #007020">print</span> err, <span style="background-color: #fff0f0">&#39;--&gt; our error msg&#39;</span>
<span style="color: #333333">...</span> 
name <span style="background-color: #fff0f0">&#39;blabla&#39;</span> <span style="color: #000000; font-weight: bold">is</span> <span style="color: #000000; font-weight: bold">not</span> defined <span style="color: #333333">--&gt;</span> our error msg

<span style="color: #888888"># Python 3</span>
<span style="color: #333333">&gt;&gt;&gt;</span> <span style="color: #008800; font-weight: bold">try</span>:
<span style="color: #333333">...</span>     blabla
<span style="color: #333333">...</span> <span style="color: #008800; font-weight: bold">except</span> <span style="color: #FF0000; font-weight: bold">NameError</span> <span style="color: #008800; font-weight: bold">as</span> err:
<span style="color: #333333">...</span>     <span style="color: #007020">print</span>(err, <span style="background-color: #fff0f0">&#39;--&gt; our error msg&#39;</span>)
<span style="color: #333333">...</span> 
name <span style="background-color: #fff0f0">&#39;blabla&#39;</span> <span style="color: #000000; font-weight: bold">is</span> <span style="color: #000000; font-weight: bold">not</span> defined <span style="color: #333333">--&gt;</span> our error msg
</pre></div>


<a id='next_next'></a>
<br>
<br>

### The `next()` function and `.next()` method

[[back to Python 2.x vs 3.x overview](#py23_overview)]

Where you can use both function and method in Python 2.7.5, the `next()` function is all that remain in Python 3!

<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #888888"># Python 2</span>
<span style="color: #333333">&gt;&gt;&gt;</span> my_generator <span style="color: #333333">=</span> (letter <span style="color: #008800; font-weight: bold">for</span> letter <span style="color: #000000; font-weight: bold">in</span> <span style="background-color: #fff0f0">&#39;abcdefg&#39;</span>)
<span style="color: #333333">&gt;&gt;&gt;</span> my_generator<span style="color: #333333">.</span>next()
<span style="background-color: #fff0f0">&#39;a&#39;</span>
<span style="color: #333333">&gt;&gt;&gt;</span> <span style="color: #007020">next</span>(my_generator)
<span style="background-color: #fff0f0">&#39;b&#39;</span>

<span style="color: #888888"># Python 3</span>
<span style="color: #333333">&gt;&gt;&gt;</span> my_generator <span style="color: #333333">=</span> (letter <span style="color: #008800; font-weight: bold">for</span> letter <span style="color: #000000; font-weight: bold">in</span> <span style="background-color: #fff0f0">&#39;abcdefg&#39;</span>)
<span style="color: #333333">&gt;&gt;&gt;</span> <span style="color: #007020">next</span>(my_generator)
<span style="background-color: #fff0f0">&#39;a&#39;</span>
<span style="color: #333333">&gt;&gt;&gt;</span> my_generator<span style="color: #333333">.</span>next()
Traceback (most recent call last):
  File <span style="background-color: #fff0f0">&quot;&lt;stdin&gt;&quot;</span>, line <span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #000000; font-weight: bold">in</span> <span style="color: #333333">&lt;</span>module<span style="color: #333333">&gt;</span>
<span style="color: #FF0000; font-weight: bold">AttributeError</span>: <span style="background-color: #fff0f0">&#39;generator&#39;</span> <span style="color: #007020">object</span> has no attribute <span style="background-color: #fff0f0">&#39;next&#39;</span>
</pre></div>


<a id='loop_leak'></a>
<br>
<br>

### In Python 3.x for-loop variables don't leak into the global namespace anymore

[[back to Python 2.x vs 3.x overview](#py23_overview)]

This goes back to a change that was made in Python 3.x and is described in [What’s New In Python 3.0](https://docs.python.org/3/whatsnew/3.0.html) as follows:

"List comprehensions no longer support the syntactic form `[... for var in item1, item2, ...]`. Use `[... for var in (item1, item2, ...)]` instead. Also note that list comprehensions have different semantics: they are closer to syntactic sugar for a generator expression inside a `list()` constructor, and in particular the loop control variables are no longer leaked into the surrounding scope."

<br>
`[In:]`
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">from</span> <span style="color: #0e84b5; font-weight: bold">platform</span> <span style="color: #008800; font-weight: bold">import</span> python_version
<span style="color: #007020">print</span>(<span style="background-color: #fff0f0">&#39;This code cell was executed in Python&#39;</span>, python_version())

i <span style="color: #333333">=</span> <span style="color: #0000DD; font-weight: bold">1</span>
<span style="color: #007020">print</span>([i <span style="color: #008800; font-weight: bold">for</span> i <span style="color: #000000; font-weight: bold">in</span> <span style="color: #007020">range</span>(<span style="color: #0000DD; font-weight: bold">5</span>)])
<span style="color: #007020">print</span>(i, <span style="background-color: #fff0f0">&#39;-&gt; i in global&#39;</span>)
</pre></div>

<br>
`[Out:]`
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">This code cell was executed in Python 3.3.5
[0, 1, 2, 3, 4]
1 -&gt; i in global
</pre></div>


<br>
<br>
<br>
`[In:]`
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">from</span> <span style="color: #0e84b5; font-weight: bold">platform</span> <span style="color: #008800; font-weight: bold">import</span> python_version
<span style="color: #007020">print</span> <span style="background-color: #fff0f0">&#39;This code cell was executed in Python&#39;</span>, python_version()

i <span style="color: #333333">=</span> <span style="color: #0000DD; font-weight: bold">1</span>
<span style="color: #007020">print</span> [i <span style="color: #008800; font-weight: bold">for</span> i <span style="color: #000000; font-weight: bold">in</span> <span style="color: #007020">range</span>(<span style="color: #0000DD; font-weight: bold">5</span>)]
<span style="color: #007020">print</span> i, <span style="background-color: #fff0f0">&#39;-&gt; i in global&#39;</span> 
</pre></div>

<br>
`[Out:]`
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">This code cell was executed in Python 2.7.6
[0, 1, 2, 3, 4]
4 -&gt; i in global
</pre></div>


<a id='compare_unorder'></a>
<br>
<br>

#### Python 3.x prevents us from comparing unorderable types

[[back to Python 2.x vs 3.x overview](#py23_overview)]

<br>
`[In:]`
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">from</span> <span style="color: #0e84b5; font-weight: bold">platform</span> <span style="color: #008800; font-weight: bold">import</span> python_version
<span style="color: #007020">print</span> <span style="background-color: #fff0f0">&#39;This code cell was executed in Python&#39;</span>, python_version()

<span style="color: #007020">print</span> [<span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #0000DD; font-weight: bold">2</span>] <span style="color: #333333">&gt;</span> <span style="background-color: #fff0f0">&#39;foo&#39;</span>
<span style="color: #007020">print</span> (<span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #0000DD; font-weight: bold">2</span>) <span style="color: #333333">&gt;</span> <span style="background-color: #fff0f0">&#39;foo&#39;</span>
<span style="color: #007020">print</span> [<span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #0000DD; font-weight: bold">2</span>] <span style="color: #333333">&gt;</span> (<span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #0000DD; font-weight: bold">2</span>)
</pre></div>

<br>
`[Out:]`
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">This code cell was executed in Python 2.7.6
False
True
False
</pre></div>

<br>
<br>
<br>

`[In:]`
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">from</span> <span style="color: #0e84b5; font-weight: bold">platform</span> <span style="color: #008800; font-weight: bold">import</span> python_version
<span style="color: #007020">print</span>(<span style="background-color: #fff0f0">&#39;This code cell was executed in Python&#39;</span>, python_version())

<span style="color: #007020">print</span>([<span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #0000DD; font-weight: bold">2</span>] <span style="color: #333333">&gt;</span> <span style="background-color: #fff0f0">&#39;foo&#39;</span>)
<span style="color: #007020">print</span>((<span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #0000DD; font-weight: bold">2</span>) <span style="color: #333333">&gt;</span> <span style="background-color: #fff0f0">&#39;foo&#39;</span>)
<span style="color: #007020">print</span>([<span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #0000DD; font-weight: bold">2</span>] <span style="color: #333333">&gt;</span> (<span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #0000DD; font-weight: bold">2</span>))
</pre></div>

`[Out:]`
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">This code cell was executed <span style="color: #000000; font-weight: bold">in</span> Python <span style="color: #6600EE; font-weight: bold">3.3</span><span style="color: #333333">.</span><span style="color: #0000DD; font-weight: bold">5</span>
<span style="color: #333333">---------------------------------------------------------------------------</span>
<span style="color: #FF0000; font-weight: bold">TypeError</span>                                 Traceback (most recent call last)
<span style="color: #333333">&lt;</span>ipython<span style="color: #333333">-</span><span style="color: #007020">input</span><span style="color: #333333">-</span><span style="color: #0000DD; font-weight: bold">3</span><span style="color: #333333">-</span><span style="color: #0000DD; font-weight: bold">1</span>d774c677f73<span style="color: #333333">&gt;</span> <span style="color: #000000; font-weight: bold">in</span> <span style="color: #333333">&lt;</span>module<span style="color: #333333">&gt;</span>()
      <span style="color: #0000DD; font-weight: bold">2</span> <span style="color: #007020">print</span>(<span style="background-color: #fff0f0">&#39;This code cell was executed in Python&#39;</span>, python_version())
      <span style="color: #0000DD; font-weight: bold">3</span> 
<span style="color: #333333">----&gt;</span> <span style="color: #0000DD; font-weight: bold">4</span> [<span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #0000DD; font-weight: bold">2</span>] <span style="color: #333333">&gt;</span> <span style="background-color: #fff0f0">&#39;foo&#39;</span>
      <span style="color: #0000DD; font-weight: bold">5</span> (<span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #0000DD; font-weight: bold">2</span>) <span style="color: #333333">&gt;</span> <span style="background-color: #fff0f0">&#39;foo&#39;</span>
      <span style="color: #0000DD; font-weight: bold">6</span> [<span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #0000DD; font-weight: bold">2</span>] <span style="color: #333333">&gt;</span> (<span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #0000DD; font-weight: bold">2</span>)

<span style="color: #FF0000; font-weight: bold">TypeError</span>: unorderable types: <span style="color: #007020">list</span>() <span style="color: #333333">&gt;</span> <span style="color: #007020">str</span>()
</pre></div>
