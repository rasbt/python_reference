<link rel="stylesheet" type="text/css" href="../CSS/hover.css" media="screen" />




# Numeric matrix manipulation - The cheat sheet for MATLAB, Python NumPy, R, and Julia

At its core, this article is about a simple cheat sheet for basic operations on numeric matrices, which can be very useful if you working and experimenting with some of the most popular languages that are used for scientific computing, statistics, and data analysis.

<a id='sections'></a>

## Sections

- [Introduction](#introduction)

- [Language overview](#overview)

	- [MATLAB/Octave](#matlab)
	
	- [Python NumPy](#numpy)
	
	- [R](#r)
	
	- [Julia](#julia)

- [Matrix cheat sheet](#cheatsheet)

- [Alternative data structures: NumPy matrices vs. NumPy arrays](#numpy_arrays)



<br>


<a id='introduction'></a>

## Introduction

[[back to section overview](#sections)]
<br>

Matrices (or multidimensional arrays) are not only presenting the fundamental elements of many algebraic equations that are used in many popular fields, such as pattern classification, machine learning, data mining, and math and engineering in general. But in context of scientific computing, they also come in very handy for managing and storing data in an more organized tabular form.  
Such multidimensional data structures are also very powerful performance-wise thanks to the concept of automatic vectorization: instead of the individual and sequential processing of operations on scalars in loop-structures, the whole computation can be parallelized in order to make optimal use of modern computer architectures.  


<br>

![R matrix](../Images/matcheat_matrix.png)

<br>
<br>

<font size=1em>
<hr>
**Note:**  
This article originated from an older article with containing a cheat sheet that was just about MATLAB matrices and NumPy arrays. Since then, I added a couple of more rows and doubled the width of the cheat sheet by adding those two other languages R and Julia. Instead of making further modifications, I wanted to keep this old article as is - for future reference and for people who may only be interested in this slimmer version:  
[Moving from MATLAB matrices to NumPy arrays - A Matrix Cheatsheet](http://sebastianraschka.com/Articles/2014_matlab_vs_numpy.html).
<hr>
</font>

<br>
<br>

<a id='overview'></a>

### Language overview

[[back to section overview](#sections)]
<br>

Before we **[jump to the actual cheat sheet](#cheatsheet)**, I wanted to give you at least a brief overview of the different languages that we are dealing with.


All four languages, MATLAB/Octave, Python, R, and Julia are dynamically typed, have a command line interface for the interpreter, and come with great number of additional and useful libraries to support scientific and technical computing. Conveniently, these languages also offer great solutions for easy plotting and visualizations.  

Combined with interactive notebook interfaces or dynamic report generation engines ([MuPAD](http://www.mathworks.com/discovery/mupad.html) for MATLAB, [IPython Notebook](http://ipython.org/notebook.html) for Python, [knitr](http://yihui.name/knitr/) for R, and [IJulia](https://github.com/JuliaLang/IJulia.jl) for Julia based on IPython Notebook) data analysis and documentation has never been easier.

<br>
<br>

<a id="matlab"></a>

# MATLAB/Octave

[[back to section overview](#sections)]
<br>

<br>
<a href="http://www.mathworks.com/products/matlab/" class="hover_dark_light">
![matlab logo](../Images/matcheat_matlab_logo.png)
</a>

<br>

[MATLAB](http://www.mathworks.com/products/matlab/) (stands for MATrix LABoratory) is the name of an application and language that was developed by [MathWorks](http://www.mathworks.com/index.html?s_tid=gn_logo) back in 1984. One of its strengths is the variety of different and highly optimized "toolboxes" (including very powerful functions for image and other signal processing task), which makes suitable for tackling basically every possible science and engineering task.  
Like the other languages, which will be covered in this article, it has cross-platform support and is using dynamic types, which allows for a convenient interface, but can also be quite "memory hungry" for computations on large data sets.

Even today, MATLAB is probably (still) the most popular language for numeric computation used for engineering tasks in academia as well as in industry.

#### GNU Octave

<br>
<a href="http://www.gnu.org/software/octave/" class="hover_dark_light">
![matlab logo](../Images/matcheat_octave_logo.png)
</a>

<br>

It is also worth mentioning that MATLAB is the only language in this cheat sheet which is not free and open-sourced. But since it is so immensely popular, I want to mention it nonetheless. And as an alternative there is also the free [GNU Octave re-implementation](http://www.gnu.org/software/octave/) that follows the same syntactic rules so that the code is compatible to MATLAB (except for very specialized libraries).

<br>

*<font size=1em> This [image](http://commons.wikimedia.org/wiki/File:Matlab_Logo.png) is a freely usable media under public domain and represents the first eigenfunction of the L-shaped membrane, resembling (but not identical to) MATLAB's logo trademarked by MathWorks Inc.</font>

<br>
<br>

<a id="numpy"></a>




# Python NumPy

[[back to section overview](#sections)]
<br>

<br>
<a href="http://www.numpy.org" class="hover_dark_light"/>
![python logo](../Images/matcheat_numpy_logo.png)
</a>

<br>

Initially, the [NumPy](http://www.numpy.org) project started out under the name "Numeric" in 1995 (renamed to NumPy in 2006) as a Python library for numeric computations based on multi-dimensional data structures, such as arrays and matrices. Since it makes use of pre-compiled C code for operations on its "`ndarray`" objects, it is considerably faster than using equivalent approaches in (C)Python.


Python NumPy is my personal favorite since I am a big fan of the Python programming language. Although similar tools exist for other languages, I found myself to be most productive doing my research and data analyses in [IPython notebooks](http://ipython.org/notebook.html).  
It allows me to easily combine Python code (sometimes optimized by compiling it via the [Cython](http://cython.org) C-Extension or the just-in-time (JIT) [Numba](http://numba.pydata.org) compiler if speed is a concern) with different libraries from the [Scipy stack](http://www.scipy.org/) including [matplotlib](http://matplotlib.org) for inline data visualization (you can find some of my example benchmarks in this [GitHub repository](http://github.com/rasbt/One-Python-benchmark-per-day)).

<br>
<br>

<a id="r"></a>

# R

[[back to section overview](#sections)]
<br>

<br>
<a href="http://www.r-project.org" class="hover_dark_light"/>
![R logo](../Images/matcheat_R_logo.png)
</a>
<br>

The [R](http://www.r-project.org) programming language was developed in 1993 and is a modern GNU implementation of an older statistical programming language called [S](http://stat.bell-labs.com/S/), which was developed in the [Bell Laboratories](http://stat.bell-labs.com) in 1976. Since its release, it has a fast-growing user base and is particularly popular among statisticians.  

R was also the first language which kindled my fascination for statistics and computing. I have used it quite extensively a couple of years ago before I discovered Python as my new favorite language for data analysis.  
Although R has great in-built functions for performing all sorts statistics, as well as a plethora of freely available libraries developed by the large R community, I often hear people complaining about its rather unintuitive syntax.

<br>
<br>

<a id="julia"></a>

# Julia

[[back to section overview](#sections)]
<br>

<br>
<a href="http://julialang.org" class="hover_dark_light"/>
![python logo](../Images/matcheat_julia_logo.png)
</a>

<br>


With its first release in 2012, [Julia](http://julialang.org) is by far the youngest of the programming languages mentioned in this article.  a
While Julia can also be used as an interpreted language with dynamic types from the command line, it aims for high-performance in scientific computing that is superior to the other dynamic programming languages for technical computing thanks to its LLVM-based just-in-time (JIT) compiler.

Personally, I haven't used Julia that extensively, yet, but there are some exciting benchmarks that look very promising:

<a href="http://julialang.org/benchmarks/">
![Julia benchmark](../Images/matcheat_julia_benchmark.png)
</a>

<font size=1em>
C compiled by gcc 4.8.1, taking best timing from all optimization levels (-O0 through -O3). C, Fortran and Julia use OpenBLAS v0.2.8. The Python implementations of rand_mat_stat and rand_mat_mul use NumPy (v1.6.1) functions; the rest are pure Python implementations.<br>

Bezanson, J., Karpinski, S., Shah, V.B. and Edelman, A. (2012), “Julia: A fast dynamic language for technical computing”.  
(Source: [http://julialang.org/benchmarks/](http://julialang.org/benchmarks/), with permission from the copyright holder)
</font>

<br>
<br>
<br>
<a id="cheatsheet"></a>
<br>



# Cheat sheet

<a id='cheat_overview'></a>
<br>

<br><a href='#cheat_overview'>[back to cheat sheet overview]



### Cheat sheet overview


- [Creating matrices](#creating)

- Accessing matrix elements

- Manipulating shape

- Basic matrix operations

- Advanced matrix operations

<br>
<br>
<br>
<br>

<table cellspacing="0" border="0">
	<colgroup width="383"></colgroup>
	<colgroup width="387"></colgroup>
	<colgroup width="447"></colgroup>
	<colgroup width="469"></colgroup>
	<colgroup width="511"></colgroup>
	<colgroup width="690"></colgroup>
	<tr>
		<td height="57" align="center" valign=middle bgcolor="#0066CC"><b><font face="Arial" size=5 color="#FFFFFF">Task</font></b></td>
		<td align="center" valign=middle bgcolor="#0066CC"><b><font face="Andale Mono" size=5 color="#FFFFFF">MATLAB/Octave</font></b></td>
		<td align="center" valign=middle bgcolor="#0066CC"><b><font face="Andale Mono" size=5 color="#FFFFFF">Python NumPy</font></b></td>
		<td align="center" valign=middle bgcolor="#0066CC"><b><font face="Andale Mono" size=5 color="#FFFFFF">R</font></b></td>
		<td align="center" valign=middle bgcolor="#0066CC"><b><font face="Andale Mono" size=5 color="#FFFFFF">Julia</font></b></td>
		<td align="center" valign=middle bgcolor="#0066CC"><b><font face="Arial" size=5 color="#FFFFFF">Task</font></b></td>
	</tr>
	<tr> <a id='creating'></a>
		<td colspan=6 height="70" align="center" valign=middle bgcolor="#FFFFFF"><b><font face="Arial" size=4 color="#000000">CREATING MATRICES</font><br><a href='#cheat_overview'>[back to cheat sheet overview]</a></b></td>
		</tr>		
	<tr>
		<td style="border-right: 1px solid #000000" height="158" align="left" valign=top bgcolor="#FFFFFF"><b><font face="Arial" size=2 color="#000000">Creating Matrices&nbsp;<br>(here: 3x3 matrix)</font></b></td>
		<td style="border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>M&gt; A = [1 2 3; 4 5 6; 7 8 9]<br>A =<br>&nbsp;&nbsp; 1 &nbsp; 2 &nbsp; 3<br>&nbsp;&nbsp; 4 &nbsp; 5 &nbsp; 6<br>&nbsp;&nbsp; 7 &nbsp; 8 &nbsp; 9</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>P&gt; A = np.array([ [1,2,3], [4,5,6], [7,8,9] ])<br><br>P&gt; A<br>array([[1, 2, 3],<br>&nbsp;&nbsp; &nbsp; &nbsp; [4, 5, 6],<br>&nbsp;&nbsp; &nbsp; &nbsp; [7, 8, 9]])</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>R&gt; A = matrix(c(1,2,3,4,5,6,7,8,9),nrow=3,byrow=T)<br> # equivalent to <br># A = matrix(1:9,nrow=3,byrow=T)  <br><br>R&gt; A<br>     [,1] [,2] [,3]<br>[1,]    1    2    3<br>[2,]    4    5    6<br>[3,]    7    8    9</font></td>
		<td style="border-left: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>J&gt; A=[1 2 3; 4 5 6; 7 8 9]<br>3x3 Array{Int64,2}:<br> 1  2  3<br> 4  5  6<br> 7  8  9</font></td>
		<td style="border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=top bgcolor="#FFFFFF"><b><font face="Arial" size=2 color="#000000">Creating Matrices&nbsp;<br>(here: 3x3 matrix)</font></b></td>
	</tr>
	<tr>
		<td style="border-right: 1px solid #000000" height="128" align="left" valign=top bgcolor="#CFE7F5"><b><font face="Arial" size=2 color="#000000">Creating an 1D column vector</font></b></td>
		<td style="border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>M&gt; a = [1; 2; 3]<br>a =<br>&nbsp;&nbsp; 1<br>&nbsp;&nbsp; 2<br>&nbsp;&nbsp; 3</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>P&gt; a = np.array([[1],[2],[3]])<br>P&gt; a<br>array([[1],<br>&nbsp;&nbsp; &nbsp; &nbsp; [2],<br>&nbsp;&nbsp; &nbsp; &nbsp; [3]])</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>R&gt; a = matrix(c(1,2,3), nrow=3, byrow=T)<br>R&gt; a<br>     [,1]<br>[1,]    1<br>[2,]    2<br>[3,]    3<br>R&gt;</font></td>
		<td style="border-left: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>J&gt; a=[1; 2; 3]<br>3-element Array{Int64,1}:  <br> 1<br> 2<br> 3</font></td>
		<td style="border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=top bgcolor="#CFE7F5"><b><font face="Arial" size=2 color="#000000">Creating an 1D column vector</font></b></td>
	</tr>
	<tr>
		<td style="border-right: 1px solid #000000" height="128" align="left" valign=top bgcolor="#FFFFFF"><b><font face="Arial" size=2 color="#000000">Creating an<br>1D row vector</font></b></td>
		<td style="border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>M&gt; b = [1 2 3]<br>b =<br>&nbsp;&nbsp; 1 &nbsp; 2 &nbsp; 3</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>P&gt; b = np.array([1,2,3])<br><br>P&gt; b<br>array([1, 2, 3])</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>R&gt; b = matrix(c(1,2,3), ncol=3)<br><br>R&gt; b<br>     [,1] [,2] [,3]<br>[1,]    1    2    3</font></td>
		<td style="border-left: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>J&gt; b=[1 2 3]  <br>1x3 Array{Int64,2}:<br> 1  2  3<br><br># note that this is a 2D array. # vectors in Julia are columns</font></td>
		<td style="border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=top bgcolor="#FFFFFF"><b><font face="Arial" size=2 color="#000000">Creating an<br>1D row vector</font></b></td>
	</tr>
	<tr>
		<td style="border-right: 1px solid #000000" height="128" align="left" valign=top bgcolor="#CFE7F5"><b><font face="Arial" size=2 color="#000000">Creating a <br>random m x n matrix</font></b></td>
		<td style="border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>M&gt; rand(3,2)<br>ans =<br>&nbsp;&nbsp; 0.21977 &nbsp; 0.10220<br>&nbsp;&nbsp; 0.38959 &nbsp; 0.69911<br>&nbsp;&nbsp; 0.15624 &nbsp; 0.65637</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>P&gt; np.random.rand(3,2)<br>array([[ 0.29347865,&nbsp; 0.17920462],<br>&nbsp;&nbsp; &nbsp; &nbsp; [ 0.51615758,&nbsp; 0.64593471],<br>&nbsp;&nbsp; &nbsp; &nbsp; [ 0.01067605,&nbsp; 0.09692771]])</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>R&gt; matrix(runif(3*2), ncol=2)<br>          [,1]      [,2]<br>[1,] 0.5675127 0.7751204<br>[2,] 0.3439412 0.5261893<br>[3,] 0.2273177 0.223438</font></td>
		<td style="border-left: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>J&gt; rand(3,2)<br>3x2 Array{Float64,2}:<br> 0.36882   0.267725<br> 0.571856  0.601524<br> 0.848084  0.858935</font></td>
		<td style="border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=top bgcolor="#CFE7F5"><b><font face="Arial" size=2 color="#000000">Creating a <br>random m x n matrix</font></b></td>
	</tr>
	<tr>
		<td style="border-right: 1px solid #000000" height="128" align="left" valign=top bgcolor="#FFFFFF"><b><font face="Arial" size=2 color="#000000">Creating a<br>zero&nbsp;m x n matrix&nbsp;</font></b></td>
		<td style="border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>M&gt; zeros(3,2)<br>ans =<br>&nbsp;&nbsp; 0 &nbsp; 0<br>&nbsp;&nbsp; 0 &nbsp; 0<br>&nbsp;&nbsp; 0 &nbsp; 0</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>P&gt; np.zeros((3,2))<br>array([[ 0.,&nbsp; 0.],<br>&nbsp;&nbsp; &nbsp; &nbsp; [ 0.,&nbsp; 0.],<br>&nbsp;&nbsp; &nbsp; &nbsp; [ 0.,&nbsp; 0.]])</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>R&gt; mat.or.vec(3, 2)<br>     [,1] [,2]<br>[1,]    0    0<br>[2,]    0    0<br>[3,]    0    0</font></td>
		<td style="border-left: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>J&gt; zeros(3,2)<br>3x2 Array{Float64,2}:<br> 0.0  0.0<br> 0.0  0.0<br> 0.0  0.0</font></td>
		<td style="border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=top bgcolor="#FFFFFF"><b><font face="Arial" size=2 color="#000000">Creating a<br>zero&nbsp;m x n matrix&nbsp;</font></b></td>
	</tr>
	<tr>
		<td style="border-right: 1px solid #000000" height="128" align="left" valign=top bgcolor="#CFE7F5"><b><font face="Arial" size=2 color="#000000">Creating an<br>m x n matrix of ones</font></b></td>
		<td style="border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>M&gt; ones(3,2)<br>ans =<br>&nbsp;&nbsp; 1 &nbsp; 1<br>&nbsp;&nbsp; 1 &nbsp; 1<br>&nbsp;&nbsp; 1 &nbsp; 1</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>P&gt; np.ones([3,2])<br>array([[ 1.,&nbsp; 1.],<br>&nbsp;&nbsp; &nbsp; &nbsp; [ 1.,&nbsp; 1.],<br>&nbsp;&nbsp; &nbsp; &nbsp; [ 1.,&nbsp; 1.]])</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>R&gt; mat.or.vec(3, 2) + 1<br>     [,1] [,2]<br>[1,]    1    1<br>[2,]    1    1<br>[3,]    1    1</font></td>
		<td style="border-left: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>J&gt; ones(3,2)<br>3x2 Array{Float64,2}:<br> 1.0  1.0<br> 1.0  1.0<br> 1.0  1.0</font></td>
		<td style="border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=top bgcolor="#CFE7F5"><b><font face="Arial" size=2 color="#000000">Creating an<br>m x n matrix of ones</font></b></td>
	</tr>
	<tr>
		<td style="border-right: 1px solid #000000" height="128" align="left" valign=top bgcolor="#FFFFFF"><b><font face="Arial" size=2 color="#000000">Creating an<br>identity matrix</font></b></td>
		<td style="border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>M&gt; eye(3)<br>ans =<br>Diagonal Matrix<br>&nbsp;&nbsp; 1 &nbsp; 0 &nbsp; 0<br>&nbsp;&nbsp; 0 &nbsp; 1 &nbsp; 0<br>&nbsp;&nbsp; 0 &nbsp; 0 &nbsp; 1</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>P&gt; np.eye(3)<br>array([[ 1.,&nbsp; 0.,&nbsp; 0.],<br>&nbsp;&nbsp; &nbsp; &nbsp; [ 0.,&nbsp; 1.,&nbsp; 0.],<br>&nbsp;&nbsp; &nbsp; &nbsp; [ 0.,&nbsp; 0.,&nbsp; 1.]])</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>R&gt; diag(3)<br>     [,1] [,2] [,3]<br>[1,]    1    0    0<br>[2,]    0    1    0<br>[3,]    0    0    1</font></td>
		<td style="border-left: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>J&gt; eye(3)<br>3x3 Array{Float64,2}:<br> 1.0  0.0  0.0<br> 0.0  1.0  0.0<br> 0.0  0.0  1.0</font></td>
		<td style="border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=top bgcolor="#FFFFFF"><b><font face="Arial" size=2 color="#000000">Creating an<br>identity matrix</font></b></td>
	</tr>
	<tr>
		<td style="border-right: 1px solid #000000" height="217" align="left" valign=top bgcolor="#CFE7F5"><b><font face="Arial" size=2 color="#000000">Creating a<br>diagonal matrix</font></b></td>
		<td style="border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>M&gt; a = [1 2 3]<br><br>M&gt; diag(a)<br>ans =<br>Diagonal Matrix<br>&nbsp;&nbsp; 1 &nbsp; 0 &nbsp; 0<br>&nbsp;&nbsp; 0 &nbsp; 2 &nbsp; 0<br>&nbsp;&nbsp; 0 &nbsp; 0 &nbsp; 3</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>P&gt; a = np.array([1,2,3])<br><br>P&gt; np.diag(a)<br>array([[1, 0, 0],<br>&nbsp;&nbsp; &nbsp; &nbsp; [0, 2, 0],<br>&nbsp;&nbsp; &nbsp; &nbsp; [0, 0, 3]])</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>R&gt; diag(1:3)<br>     [,1] [,2] [,3]<br>[1,]    1    0    0<br>[2,]    0    2    0<br>[3,]    0    0    3</font></td>
		<td style="border-left: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>J&gt; a=[1, 2, 3] <br><br># added commas because julia<br># vectors are columnar<br><br>J&gt; diagm(a)<br>3x3 Array{Int64,2}:<br> 1  0  0<br> 0  2  0<br> 0  0  3</font></td>
		<td style="border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=top bgcolor="#CFE7F5"><b><font face="Arial" size=2 color="#000000">Creating a<br>diagonal matrix</font></b></td>
	</tr>
	<tr>
		<td colspan=6 height="128" align="center" valign=middle bgcolor="#FFFFFF"><b><font face="Arial" size=4 color="#000000">ACESSING MATRIX ELEMENTS</font></b></td>
		</tr>
	<tr>
		<td style="border-right: 1px solid #000000" height="159" align="left" valign=top bgcolor="#FFFFFF"><b><font face="Arial" size=2 color="#000000">Getting the dimension<br>of a matrix<br>(here: 2D, rows x cols)</font></b></td>
		<td style="border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>M&gt; A = [1 2 3; 4 5 6]<br>A =<br>&nbsp; &nbsp;1 &nbsp; 2 &nbsp; 3<br>&nbsp; &nbsp;4 &nbsp; 5 &nbsp; 6<br><br>M&gt; size(A)<br>ans =<br>&nbsp; &nbsp;2 &nbsp; 3</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>P&gt; A = np.array([ [1,2,3], [4,5,6] ])<br><br>P&gt; A<br>array([[1, 2, 3],<br>&nbsp; &nbsp; &nbsp; &nbsp;[4, 5, 6]])<br><br>P&gt; A.shape<br>(2, 3)</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>R&gt; A = matrix(1:6,nrow=2,byrow=T)<br><br>R&gt; A<br>     [,1] [,2] [,3]<br>[1,]    1    2    3<br>[2,]    4    5    6 R&gt; dim(A)<br>[1] 2 3</font></td>
		<td style="border-left: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>J&gt; A=[1 2 3; 4 5 6]<br>2x3 Array{Int64,2}:<br> 1  2  3<br> 4  5  6<br><br>J&gt; size(A)<br>(2,3)</font></td>
		<td style="border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=top bgcolor="#FFFFFF"><b><font face="Arial" size=2 color="#000000">Getting the dimension<br>of a matrix<br>(here: 2D, rows x cols)</font></b></td>
	</tr>
	<tr>
		<td style="border-right: 1px solid #000000" height="240" align="left" valign=top bgcolor="#CFE7F5"><b><font face="Arial" size=2 color="#000000">Selecting rows&nbsp;</font></b></td>
		<td style="border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>M&gt; A = [1 2 3; 4 5 6; 7 8 9]<br><br>% 1st row<br>M&gt; A(1,:)<br>ans =<br>&nbsp;&nbsp; 1 &nbsp; 2 &nbsp; 3<br><br>% 1st 2 rows<br>M&gt; A(1:2,:)<br>ans =<br>&nbsp;&nbsp; 1 &nbsp; 2 &nbsp; 3<br>&nbsp;&nbsp; 4 &nbsp; 5 &nbsp; 6</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>P&gt; A = np.array([ [1,2,3], [4,5,6], [7,8,9] ])<br><br># 1st row<br>P&gt; A[0,:]<br>array([1, 2, 3])<br><br># 1st 2 rows<br>P&gt; A[0:2,:]<br>array([[1, 2, 3], [4, 5, 6]])</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>R&gt; A = matrix(1:9,nrow=3,byrow=T)  <br><br># 1st row<br>  R&gt; A[1,]<br>[1] 1 2 3<br><br>  # 1st 2 rows  <br>R&gt; A[1:2,]<br>     [,1] [,2] [,3]<br>[1,]    1    2    3<br>[2,]    4    5    6</font></td>
		<td style="border-left: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>J&gt; A=[1 2 3; 4 5 6; 7 8 9]; <br>#semicolon suppresses output<br><br>#1st row<br>J&gt; A[1,:]  <br>1x3 Array{Int64,2}:<br> 1  2  3<br><br>#1st 2 rows<br>J&gt; A[1:2,:]  <br>2x3 Array{Int64,2}:<br> 1  2  3<br> 4  5  6</font></td>
		<td style="border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=top bgcolor="#CFE7F5"><b><font face="Arial" size=2 color="#000000">Selecting rows&nbsp;</font></b></td>
	</tr>
	<tr>
		<td style="border-right: 1px solid #000000" height="304" align="left" valign=top bgcolor="#FFFFFF"><b><font face="Arial" size=2 color="#000000">Selecting columns</font></b></td>
		<td style="border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>M&gt; A = [1 2 3; 4 5 6; 7 8 9]<br><br>% 1st column<br>M&gt; A(:,1)<br>ans =<br>&nbsp;&nbsp; 1<br>&nbsp;&nbsp; 4<br>&nbsp;&nbsp; 7<br><br>% 1st 2 columns<br>M&gt; A(:,1:2)<br>ans =<br>&nbsp;&nbsp; 1 &nbsp; 2<br>&nbsp;&nbsp; 4 &nbsp; 5<br>&nbsp;&nbsp; 7 &nbsp; 8</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>P&gt; A = np.array([ [1,2,3], [4,5,6], [7,8,9] ])<br><br># 1st column (as row vector)<br>P&gt; A[:,0]<br>array([1, 4, 7])<br><br># 1st column (as column vector)<br>P&gt; A[:,[0]]<br>array([[1],<br>&nbsp;&nbsp; &nbsp; &nbsp; [4],<br>&nbsp;&nbsp; &nbsp; &nbsp; [7]])<br><br># 1st 2 columns<br>P&gt; A[:,0:2]<br>array([[1, 2],&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp;[4, 5],&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp;[7, 8]])</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>R&gt; A = matrix(1:9,nrow=3,byrow=T)   <br><br># 1st column as row vector <br>R&gt; t(A[,1])<br>     [,1] [,2] [,3]<br>[1,]    1    4    7  <br><br># 1st column as column vector <br>R&gt; A[,1]<br>[1] 1 4 7  <br><br># 1st 2 columns <br>R&gt; A[,1:2]<br>     [,1] [,2]<br>[1,]    1    2<br>[2,]    4    5<br>[3,]    7    8</font></td>
		<td style="border-left: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>J&gt; A=[1 2 3; 4 5 6; 7 8 9];<br><br>#1st column<br>J&gt; A[:,1] <br>3-element Array{Int64,1}:<br> 1<br> 4<br> 7<br> <br>#1st 2 columns<br>J&gt; A[:,1:2] <br>3x2 Array{Int64,2}:<br> 1  2<br> 4  5<br> 7  8</font></td>
		<td style="border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=top bgcolor="#FFFFFF"><b><font face="Arial" size=2 color="#000000">Selecting columns</font></b></td>
	</tr>
	<tr>
		<td style="border-right: 1px solid #000000" height="260" align="left" valign=top bgcolor="#CFE7F5"><b><font face="Arial" size=2 color="#000000">Extracting rows and columns by criteria<br><br>(here: get rows&nbsp;that have value 9 in column 3)</font></b></td>
		<td style="border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>M&gt; A = [1 2 3; 4 5 9; 7 8 9]<br>A =<br>&nbsp;&nbsp; 1 &nbsp; 2 &nbsp; 3<br>&nbsp;&nbsp; 4 &nbsp; 5 &nbsp; 9<br>&nbsp;&nbsp; 7 &nbsp; 8 &nbsp; 9<br><br>M&gt; A(A(:,3) == 9,:)<br>ans =<br>&nbsp;&nbsp; 4 &nbsp; 5 &nbsp; 9<br>&nbsp;&nbsp; 7 &nbsp; 8 &nbsp; 9</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>P&gt; A = np.array([ [1,2,3], [4,5,9], [7,8,9]])<br><br>P&gt; A<br>array([[1, 2, 3],<br>&nbsp;&nbsp; &nbsp; &nbsp; [4, 5, 9],<br>&nbsp;&nbsp; &nbsp; &nbsp; [7, 8, 9]])<br><br>P&gt; A[A[:,2] == 9]<br>array([[4, 5, 9],<br>&nbsp;&nbsp; &nbsp; &nbsp; [7, 8, 9]])</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>R&gt; A = matrix(1:9,nrow=3,byrow=T)  <br><br>R&gt; A<br>     [,1] [,2] [,3]<br>[1,]    1    2    3<br>[2,]    4    5    9<br>[3,]    7    8    9  <br><br>R&gt; matrix(A[A[,3]==9], ncol=3)<br>     [,1] [,2] [,3]<br>[1,]    4    5    9<br>[2,]    7    8    9</font></td>
		<td style="border-left: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>J&gt; A=[1 2 3; 4 5 9; 7 8 9]<br>3x3 Array{Int64,2}:<br> 1  2  3<br> 4  5  9<br> 7  8  9<br><br># use '.==' for<br># element-wise check<br>J&gt; A[ A[:,3] .==9, :]  <br>2x3 Array{Int64,2}:<br> 4  5  9<br> 7  8  9</font></td>
		<td style="border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=top bgcolor="#CFE7F5"><b><font face="Arial" size=2 color="#000000">Extracting rows and columns by criteria<br><br>(here: get rows&nbsp;that have value 9 in column 3)</font></b></td>
	</tr>
	<tr>
		<td style="border-right: 1px solid #000000" height="118" align="left" valign=top bgcolor="#FFFFFF"><b><font face="Arial" size=2 color="#000000">Accessing elements<br>(here: 1st element)</font></b></td>
		<td style="border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>M&gt; A = [1 2 3; 4 5 6; 7 8 9]<br><br>M&gt; A(1,1)<br>ans =&nbsp; 1</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>P&gt; A = np.array([ [1,2,3], [4,5,6], [7,8,9] ])<br><br>P&gt; A[0,0]<br>1</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>R&gt; A = matrix(c(1,2,3,4,5,9,7,8,9),nrow=3,byrow=T) <br><br> R&gt; A[1,1]<br>[1] 1</font></td>
		<td style="border-left: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>J&gt; A=[1 2 3; 4 5 6; 7 8 9];<br><br>J&gt; A[1,1]<br>1</font></td>
		<td style="border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=top bgcolor="#FFFFFF"><b><font face="Arial" size=2 color="#000000">Accessing elements<br>(here: 1st element)</font></b></td>
	</tr>
	<tr>
		<td colspan=6 height="128" align="center" valign=middle bgcolor="#FFFFFF"><b><font face="Arial" size=4 color="#000000">MANIPULATING SHAPE AND DIMENSIONS</font></b></td>
		</tr>
	<tr>
		<td style="border-right: 1px solid #000000" height="173" align="left" valign=top bgcolor="#CFE7F5"><b><font face="Arial" size=2 color="#000000">Converting&nbsp;<br>row to column vectors</font></b></td>
		<td style="border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>M&gt; b = [1 2 3] <br><br>M&gt; b = b'<br>b =<br>&nbsp;&nbsp; 1<br>&nbsp;&nbsp; 2<br>&nbsp;&nbsp; 3</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>P&gt; b = np.array([1, 2, 3])<br><br>P&gt; b = b[np.newaxis].T<br># alternatively <br>#&nbsp;b = b[:,np.newaxis]<br><br>P&gt; b<br>array([[1],<br>&nbsp;&nbsp; &nbsp; &nbsp; [2],<br>&nbsp;&nbsp; &nbsp; &nbsp; [3]])</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>R&gt; b = matrix(c(1,2,3), ncol=3)<br><br>R&gt; t(b)<br>     [,1]<br>[1,]    1<br>[2,]    2<br>[3,]    3</font></td>
		<td style="border-left: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>J&gt; b=vec([1 2 3])<br>3-element Array{Int64,1}:<br> 1<br> 2<br> 3</font></td>
		<td style="border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=top bgcolor="#CFE7F5"><b><font face="Arial" size=2 color="#000000">Converting&nbsp;<br>row to column vectors</font></b></td>
	</tr>
	<tr>
		<td style="border-right: 1px solid #000000" height="275" align="left" valign=top bgcolor="#FFFFFF"><b><font face="Arial" size=2 color="#000000">Reshaping Matrices<br><br>(here: 3x3 matrix to row vector)</font></b></td>
		<td style="border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>M&gt; A = [1 2 3; 4 5 6; 7 8 9]<br>A =<br>&nbsp;&nbsp; 1 &nbsp; 2 &nbsp; 3<br>&nbsp;&nbsp; 4 &nbsp; 5 &nbsp; 6<br>&nbsp;&nbsp; 7 &nbsp; 8 &nbsp; 9<br><br>M&gt; total_elements = numel(A)<br><br>M&gt; B = reshape(A,1,total_elements)&nbsp;<br>% or reshape(A,1,9)<br>B =<br>&nbsp;&nbsp; 1 &nbsp; 4 &nbsp; 7 &nbsp; 2 &nbsp; 5 &nbsp; 8 &nbsp; 3 &nbsp; 6 &nbsp; 9</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>P&gt; A = np.array([[1,2,3],[4,5,6],[7,8,9]])<br><br>P&gt; A<br>array([[1, 2, 3],<br>&nbsp;&nbsp; &nbsp; &nbsp; [4, 5, 9],<br>&nbsp;&nbsp; &nbsp; &nbsp; [7, 8, 9]])<br><br>P&gt; total_elements = A.shape[0] * A.shape[1]<br><br>P&gt; B = A.reshape(1, total_elements)&nbsp;<br><br># or A.reshape(1,9)<br># Alternative: A.shape = (1,9)&nbsp;<br># to&nbsp;change the array in place<br><br>P&gt; B<br>array([[1, 2, 3, 4, 5, 6, 7, 8, 9]])</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>R&gt; A = matrix(1:9,nrow=3,byrow=T)  <br><br>R&gt; A<br>     [,1] [,2] [,3]<br>[1,]    1    2    3<br>[2,]    4    5    6<br>[3,]    7    8    9 R&gt; total_elements = dim(A)[1] * dim(A)[2]<br><br>R&gt; B = matrix(A, ncol=total_elements)<br><br>R&gt; B<br>     [,1] [,2] [,3] [,4] [,5] [,6] [,7] [,8] [,9]<br>[1,]    1    4    7    2    5    8    3    6    9</font></td>
		<td style="border-left: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>J&gt; A=[1 2 3; 4 5 6; 7 8 9]<br>3x3 Array{Int64,2}:<br> 1  2  3<br> 4  5  6<br> 7  8  9<br><br>J&gt; total_elements=length(A)<br>9<br><br>J&gt;B=reshape(A,1,total_elements)<br>1x9 Array{Int64,2}:<br> 1  4  7  2  5  8  3  6  9</font></td>
		<td style="border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=top bgcolor="#FFFFFF"><b><font face="Arial" size=2 color="#000000">Reshaping Matrices<br><br>(here: 3x3 matrix to row vector)</font></b></td>
	</tr>
	<tr>
		<td style="border-right: 1px solid #000000" height="240" align="left" valign=top bgcolor="#CFE7F5"><b><font face="Arial" size=2 color="#000000">Concatenating matrices</font></b></td>
		<td style="border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>M&gt; A = [1 2 3; 4 5 6]<br><br>M&gt; B = [7 8 9; 10 11 12]<br><br>M&gt; C = [A; B]<br>&nbsp; &nbsp;&nbsp;1&nbsp; &nbsp; 2&nbsp; &nbsp; 3<br>&nbsp; &nbsp; 4&nbsp; &nbsp; 5&nbsp; &nbsp; 6<br>&nbsp; &nbsp; 7&nbsp; &nbsp; 8&nbsp; &nbsp; 9<br>&nbsp;&nbsp; 10 &nbsp; 11 &nbsp; 12</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>P&gt; A = np.array([[1, 2, 3], [4, 5, 6]])<br><br>P&gt; B = np.array([[7, 8, 9],[10,11,12]])<br><br>P&gt; C = np.concatenate((A, B), axis=0)<br><br>P&gt; C<br>array([[ 1, 2, 3],&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp;[ 4, 5, 6],&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp;[ 7, 8, 9],&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp;[10, 11, 12]])</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>R&gt; A = matrix(1:6,nrow=2,byrow=T)<br><br>R&gt; B = matrix(7:12,nrow=2,byrow=T)<br><br>R&gt; C = rbind(A,B)<br><br>R&gt; C<br>     [,1] [,2] [,3]<br>[1,]    1    2    3<br>[2,]    4    5    6<br>[3,]    7    8    9<br>[4,]   10   11   12</font></td>
		<td style="border-left: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>J&gt; A=[1 2 3; 4 5 6];<br><br>J&gt; B=[7 8 9; 10 11 12];<br><br>J&gt; C=[A; B]<br>4x3 Array{Int64,2}:<br>  1   2   3<br>  4   5   6<br>  7   8   9<br> 10  11  12</font></td>
		<td style="border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=top bgcolor="#CFE7F5"><b><font face="Arial" size=2 color="#000000">Concatenating matrices</font></b></td>
	</tr>
	<tr>
		<td style="border-right: 1px solid #000000" height="256" align="left" valign=top bgcolor="#FFFFFF"><b><font face="Arial" size=2 color="#000000">Stacking&nbsp;<br>vectors and matrices</font></b></td>
		<td style="border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>M&gt; a = [1 2 3]<br><br>M&gt; b = [4 5 6]<br><br>M&gt; c = [a' b']<br>c =<br>&nbsp;&nbsp; 1 &nbsp; 4<br>&nbsp;&nbsp; 2 &nbsp; 5<br>&nbsp;&nbsp; 3 &nbsp; 6<br><br>M&gt; c = [a; b]<br>c =<br>&nbsp;&nbsp; 1 &nbsp; 2 &nbsp; 3<br>&nbsp;&nbsp; 4 &nbsp; 5 &nbsp; 6</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>P&gt; a = np.array([1,2,3])<br>P&gt; b = np.array([4,5,6])<br><br>P&gt; np.c_[a,b]<br>array([[1, 4],<br>&nbsp;&nbsp; &nbsp; &nbsp; [2, 5],<br>&nbsp;&nbsp; &nbsp; &nbsp; [3, 6]])<br><br>P&gt; np.r_[a,b]<br>array([[1, 2, 3],<br>&nbsp;&nbsp; &nbsp; &nbsp; [4, 5, 6]])</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>R&gt; a = matrix(1:3, ncol=3)<br><br>R&gt; b = matrix(4:6, ncol=3)<br><br>R&gt; matrix(rbind(A, B), ncol=2)<br>     [,1] [,2]<br>[1,]    1    5<br>[2,]    4    3 <br><br> R&gt; rbind(A,B)<br>     [,1] [,2] [,3]<br>[1,]    1    2    3<br>[2,]    4    5    6</font></td>
		<td style="border-left: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>J&gt; a=[1 2 3];<br><br>J&gt; b=[4 5 6];<br><br>J&gt; c=[a' b']<br>3x2 Array{Int64,2}:<br> 1  4<br> 2  5<br> 3  6<br><br>J&gt; c=[a; b]<br>2x3 Array{Int64,2}:<br> 1  2  3<br> 4  5  6</font></td>
		<td style="border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=top bgcolor="#FFFFFF"><b><font face="Arial" size=2 color="#000000">Stacking&nbsp;<br>vectors and matrices</font></b></td>
	</tr>
	<tr>
		<td colspan=6 height="114" align="center" valign=middle bgcolor="#FFFFFF"><b><font face="Arial" size=4 color="#000000">BASIC MATRIX OPERATIONS</font></b></td>
		</tr>
	<tr>
		<td style="border-right: 1px solid #000000" height="253" align="left" valign=top bgcolor="#CFE7F5"><b><font face="Arial" size=2 color="#000000">Matrix-scalar<br>operations</font></b></td>
		<td style="border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>M&gt;&nbsp;A = [1 2 3; 4 5 6; 7 8 9]<br><br>M&gt; A * 2<br>ans =<br>&nbsp; &nbsp; 2&nbsp; &nbsp; 4&nbsp; &nbsp; 6<br>&nbsp; &nbsp; 8 &nbsp; 10 &nbsp; 12<br>&nbsp;&nbsp; 14 &nbsp; 16 &nbsp; 18<br><br>M&gt; A + 2<br><br>M&gt; A - 2<br><br>M&gt; A / 2</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>P&gt; A = np.array([ [1,2,3], [4,5,6], [7,8,9] ])<br><br>P&gt; A * 2<br>array([[ 2,&nbsp; 4,&nbsp; 6],<br>&nbsp;&nbsp; &nbsp; &nbsp; [ 8, 10, 12],<br>&nbsp;&nbsp; &nbsp; &nbsp; [14, 16, 18]])<br><br>P&gt; A + 2<br><br>P&gt; A - 2<br><br>P&gt; A / 2</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>R&gt; A = matrix(1:9, nrow=3, byrow=T)<br><br>R&gt; A * 2<br>     [,1] [,2] [,3]<br>[1,]    2    4    6<br>[2,]    8   10   12<br>[3,]   14   16   18 R&gt; A + 2<br><br>R&gt; A - 2<br><br>R&gt; A / 2</font></td>
		<td style="border-left: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>J&gt; A=[1 2 3; 4 5 6; 7 8 9];<br><br> # elementwise operator<br><br>J&gt; A .* 2    <br>3x3 Array{Int64,2}:<br>  2   4   6<br>  8  10  12<br> 14  16  18 <br> <br>J&gt; A .+ 2;<br><br>J&gt; A .- 2;<br><br>J&gt; A ./ 2;</font></td>
		<td style="border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=top bgcolor="#CFE7F5"><b><font face="Arial" size=2 color="#000000">Matrix-scalar<br>operations</font></b></td>
	</tr>
	<tr>
		<td style="border-right: 1px solid #000000" height="165" align="left" valign=top bgcolor="#FFFFFF"><b><font face="Arial" size=2 color="#000000">Matrix-matrix<br>multiplication</font></b></td>
		<td style="border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>M&gt;&nbsp;A = [1 2 3; 4 5 6; 7 8 9]<br><br>M&gt; A * A<br>ans =<br>&nbsp; &nbsp; 30&nbsp; &nbsp; 36&nbsp; &nbsp; 42<br>&nbsp; &nbsp; 66&nbsp; &nbsp; 81&nbsp; &nbsp; 96<br>&nbsp;&nbsp; 102 &nbsp; 126 &nbsp; 150</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>P&gt; A = np.array([ [1,2,3], [4,5,6], [7,8,9] ])<br><br>P&gt; np.dot(A,A) # or A.dot(A)<br>array([[ 30,&nbsp; 36,&nbsp; 42],<br>&nbsp;&nbsp; &nbsp; &nbsp; [ 66,&nbsp; 81,&nbsp; 96],<br>&nbsp;&nbsp; &nbsp; &nbsp; [102, 126, 150]])</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>R&gt; A = matrix(1:9, nrow=3, byrow=T)<br><br>R&gt; A %*% A<br>     [,1] [,2] [,3]<br>[1,]   30   36   42<br>[2,]   66   81   96<br>[3,]  102  126  150</font></td>
		<td style="border-left: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>J&gt; A=[1 2 3; 4 5 6; 7 8 9];<br><br>J&gt; A * A<br>3x3 Array{Int64,2}:<br>  30   36   42<br>  66   81   96<br> 102  126  150</font></td>
		<td style="border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=top bgcolor="#FFFFFF"><b><font face="Arial" size=2 color="#000000">Matrix-matrix<br>multiplication</font></b></td>
	</tr>
	<tr>
		<td style="border-right: 1px solid #000000" height="190" align="left" valign=top bgcolor="#CFE7F5"><b><font face="Arial" size=2 color="#000000">Matrix-vector<br>multiplication</font></b></td>
		<td style="border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>M&gt; A = [1 2 3; 4 5 6; 7 8 9]<br><br>M&gt; b = [ 1; 2; 3 ]<br><br>M&gt; A * b<br>ans =<br>&nbsp;&nbsp; 14<br>&nbsp;&nbsp; 32<br>&nbsp;&nbsp; 50</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>P&gt; A = np.array([ [1,2,3], [4,5,6], [7,8,9] ])<br><br>P&gt; b = np.array([ [1], [2], [3] ])<br><br>P&gt; np.dot(A,b) # or A.dot(b)<br><br>array([[14], [32], [50]])</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>R&gt; A = matrix(1:9, ncol=3)<br><br>R&gt; b = matrix(1:3, nrow=3)  R&gt; t(b %*% A)<br>     [,1]<br>[1,]   14<br>[2,]   32<br>[3,]   50</font></td>
		<td style="border-left: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>J&gt; A=[1 2 3; 4 5 6; 7 8 9];<br><br>J&gt; b=[1; 2; 3];<br><br>J&gt; A*b<br>3-element Array{Int64,1}:<br> 14<br> 32<br> 50</font></td>
		<td style="border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=top bgcolor="#CFE7F5"><b><font face="Arial" size=2 color="#000000">Matrix-vector<br>multiplication</font></b></td>
	</tr>
	<tr>
		<td style="border-right: 1px solid #000000" height="240" align="left" valign=top bgcolor="#FFFFFF"><b><font face="Arial" size=2 color="#000000">Element-wise&nbsp;<br>matrix-matrix&nbsp;operations</font></b></td>
		<td style="border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>M&gt;&nbsp;A = [1 2 3; 4 5 6; 7 8 9]<br><br>M&gt; A .* A<br>ans =<br>&nbsp; &nbsp; 1&nbsp; &nbsp; 4&nbsp; &nbsp; 9<br>&nbsp;&nbsp; 16 &nbsp; 25 &nbsp; 36<br>&nbsp;&nbsp; 49 &nbsp; 64 &nbsp; 81<br><br>M&gt; A .+ A<br><br>M&gt; A .- A<br><br>M&gt; A ./ A</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>P&gt; A = np.array([ [1,2,3], [4,5,6], [7,8,9] ])<br><br>P&gt; A * A<br>array([[ 1,&nbsp; 4,&nbsp; 9],<br>&nbsp;&nbsp; &nbsp; &nbsp; [16, 25, 36],<br>&nbsp;&nbsp; &nbsp; &nbsp; [49, 64, 81]])<br><br>P&gt; A + A<br><br>P&gt; A - A<br><br>P&gt; A / A</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>R&gt; A = matrix(1:9, nrow=3, byrow=T) R&gt; A * A<br>     [,1] [,2] [,3]<br>[1,]    1    4    9<br>[2,]   16   25   36<br>[3,]   49   64   81  <br><br>R&gt; A + A<br><br>R&gt; A - A<br><br>R&gt; A / A</font></td>
		<td style="border-left: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>J&gt; A=[1 2 3; 4 5 6; 7 8 9];<br><br>J&gt; A .* A<br>3x3 Array{Int64,2}:<br>  1   4   9<br> 16  25  36<br> 49  64  81 <br> <br>J&gt; A .+ A; <br><br>J&gt; A .- A; <br><br>J&gt; A ./ A;</font></td>
		<td style="border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=top bgcolor="#FFFFFF"><b><font face="Arial" size=2 color="#000000">Element-wise&nbsp;<br>matrix-matrix&nbsp;operations</font></b></td>
	</tr>
	<tr>
		<td style="border-right: 1px solid #000000" height="164" align="left" valign=top bgcolor="#CFE7F5"><b><font face="Arial" size=2 color="#000000">Matrix elements&nbsp;to power n <br><br>(here: individual elements squared)</font></b></td>
		<td style="border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>M&gt;&nbsp;A = [1 2 3; 4 5 6; 7 8 9]<br><br>M&gt; A.^2<br>ans =<br>&nbsp; &nbsp; 1&nbsp; &nbsp; 4&nbsp; &nbsp; 9<br>&nbsp;&nbsp; 16 &nbsp; 25 &nbsp; 36<br>&nbsp;&nbsp; 49 &nbsp; 64 &nbsp; 81</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>P&gt; A = np.array([ [1,2,3], [4,5,6], [7,8,9] ])<br><br>P&gt; np.power(A,2)<br>array([[ 1,&nbsp; 4,&nbsp; 9],<br>&nbsp;&nbsp; &nbsp; &nbsp; [16, 25, 36],<br>&nbsp;&nbsp; &nbsp; &nbsp; [49, 64, 81]])</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>R&gt; A = matrix(1:9, nrow=3, byrow=T)<br><br>R&gt; A ^ 2<br>     [,1] [,2] [,3]<br>[1,]    1    4    9<br>[2,]   16   25   36<br>[3,]   49   64   81</font></td>
		<td style="border-left: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>J&gt; A=[1 2 3; 4 5 6; 7 8 9];<br><br>J&gt; A .^ 2<br>3x3 Array{Int64,2}:<br>  1   4   9<br> 16  25  36<br> 49  64  81</font></td>
		<td style="border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=top bgcolor="#CFE7F5"><b><font face="Arial" size=2 color="#000000">Matrix elements&nbsp;to power n <br><br>(here: individual elements squared)</font></b></td>
	</tr>
	<tr>
		<td style="border-right: 1px solid #000000" height="225" align="left" valign=top bgcolor="#FFFFFF"><b><font face="Arial" size=2 color="#000000">Matrix to power n<br><br>(here: matrix-matrix&nbsp;multiplication with itself)</font></b></td>
		<td style="border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>M&gt;&nbsp;A = [1 2 3; 4 5 6; 7 8 9]<br><br>M&gt; A ^ 2<br>ans =<br>&nbsp; &nbsp; 30&nbsp; &nbsp; 36&nbsp; &nbsp; 42<br>&nbsp; &nbsp; 66&nbsp; &nbsp; 81&nbsp; &nbsp; 96<br>&nbsp;&nbsp; 102 &nbsp; 126 &nbsp; 150</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>P&gt; A = np.array([ [1,2,3], [4,5,6], [7,8,9] ])<br><br>P&gt; np.linalg.matrix_power(A,2)<br>array([[ 30,&nbsp; 36,&nbsp; 42],<br>&nbsp;&nbsp; &nbsp; &nbsp; [ 66,&nbsp; 81,&nbsp; 96],<br>&nbsp;&nbsp; &nbsp; &nbsp; [102, 126, 150]])</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>R&gt; A = matrix(1:9, ncol=3)<br><br> # requires the ‘expm’ package <br><br>R&gt; install.packages('expm') <br><br>R&gt; library(expm) <br><br> R&gt; A %^% 2<br>     [,1] [,2] [,3]<br>[1,]   30   66  102<br>[2,]   36   81  126<br>[3,]   42   96  150</font></td>
		<td style="border-left: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>J&gt; A=[1 2 3; 4 5 6; 7 8 9];<br><br>J&gt; A ^ 2<br>3x3 Array{Int64,2}:<br>  30   36   42<br>  66   81   96<br> 102  126  150</font></td>
		<td style="border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=top bgcolor="#FFFFFF"><b><font face="Arial" size=2 color="#000000">Matrix to power n<br><br>(here: matrix-matrix&nbsp;multiplication with itself)</font></b></td>
	</tr>
	<tr>
		<td style="border-right: 1px solid #000000" height="172" align="left" valign=top bgcolor="#CFE7F5"><b><font face="Arial" size=2 color="#000000">Matrix transpose</font></b></td>
		<td style="border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>M&gt;&nbsp;A = [1 2 3; 4 5 6; 7 8 9]<br><br>M&gt; A'<br>ans =<br>&nbsp;&nbsp; 1 &nbsp; 4 &nbsp; 7<br>&nbsp;&nbsp; 2 &nbsp; 5 &nbsp; 8<br>&nbsp;&nbsp; 3 &nbsp; 6 &nbsp; 9</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>P&gt; A = np.array([ [1,2,3], [4,5,6], [7,8,9] ])<br><br>P&gt; A.T<br>array([[1, 4, 7],<br>&nbsp;&nbsp; &nbsp; &nbsp; [2, 5, 8],<br>&nbsp;&nbsp; &nbsp; &nbsp; [3, 6, 9]])</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>R&gt; A = matrix(1:9, nrow=3, byrow=T) <br><br>R&gt; t(A)<br>     [,1] [,2] [,3]<br>[1,]    1    4    7<br>[2,]    2    5    8<br>[3,]    3    6    9</font></td>
		<td style="border-left: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>J&gt; A=[1 2 3; 4 5 6; 7 8 9]<br>3x3 Array{Int64,2}:<br> 1  2  3<br> 4  5  6<br> 7  8  9<br><br>J&gt; A'<br>3x3 Array{Int64,2}:<br> 1  4  7<br> 2  5  8<br> 3  6  9</font></td>
		<td style="border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=top bgcolor="#CFE7F5"><b><font face="Arial" size=2 color="#000000">Matrix transpose</font></b></td>
	</tr>
	<tr>
		<td style="border-right: 1px solid #000000" height="176" align="left" valign=top bgcolor="#FFFFFF"><b><font face="Arial" size=2 color="#000000">Determinant of a matrix:<br>&nbsp;A -&gt; |A|</font></b></td>
		<td style="border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>M&gt; A = [6 1 1; 4 -2 5; 2 8 7]<br>A =<br>&nbsp;&nbsp; 6 &nbsp; 1 &nbsp; 1<br>&nbsp;&nbsp; 4&nbsp; -2 &nbsp; 5<br>&nbsp;&nbsp; 2 &nbsp; 8 &nbsp; 7<br><br>M&gt; det(A)<br>ans = -306</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>P&gt;&nbsp;A = np.array([[6,1,1],[4,-2,5],[2,8,7]])<br><br>P&gt; A<br>array([[ 6,&nbsp; 1,&nbsp; 1],<br>&nbsp;&nbsp; &nbsp; &nbsp; [ 4, -2,&nbsp; 5],<br>&nbsp;&nbsp; &nbsp; &nbsp; [ 2,&nbsp; 8,&nbsp; 7]])<br><br>P&gt; np.linalg.det(A)<br>-306.0</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>R&gt; A = matrix(c(6,1,1,4,-2,5,2,8,7), nrow=3, byrow=T)<br><br>R&gt; A<br>     [,1] [,2] [,3]<br>[1,]    6    1    1<br>[2,]    4   -2    5<br>[3,]    2    8    7<br><br>R&gt; det(A)<br>[1] -306</font></td>
		<td style="border-left: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>J&gt; A=[6 1 1; 4 -2 5; 2 8 7]<br>3x3 Array{Int64,2}:<br> 6   1  1<br> 4  -2  5<br> 2   8  7<br><br>J&gt; det(A)<br>-306.0</font></td>
		<td style="border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=top bgcolor="#FFFFFF"><b><font face="Arial" size=2 color="#000000">Determinant of a matrix:<br>&nbsp;A -&gt; |A|</font></b></td>
	</tr>
	<tr>
		<td style="border-right: 1px solid #000000" height="202" align="left" valign=top bgcolor="#CFE7F5"><b><font face="Arial" size=2 color="#000000">Inverse of a matrix</font></b></td>
		<td style="border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>M&gt; A = [4 7; 2 6]<br>A =<br>&nbsp;&nbsp; 4 &nbsp; 7<br>&nbsp;&nbsp; 2 &nbsp; 6<br><br>M&gt; A_inv = inv(A)<br>A_inv =<br>&nbsp; &nbsp;0.60000&nbsp; -0.70000<br>&nbsp; -0.20000 &nbsp; 0.40000</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>P&gt; A = np.array([[4, 7], [2, 6]])<br><br>P&gt; A<br>array([[4, 7],&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp;[2, 6]])<br><br>P&gt; A_inverse = np.linalg.inv(A)<br><br>P&gt; A_inverse<br>array([[ 0.6, -0.7],&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp;[-0.2, 0.4]])</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>R&gt; A = matrix(c(4,7,2,6), nrow=2, byrow=T)<br><br>R&gt; A<br>     [,1] [,2]<br>[1,]    4    7<br>[2,]    2    6<br><br>R&gt; solve(A)<br>     [,1] [,2]<br>[1,]  0.6 -0.7<br>[2,] -0.2  0.4</font></td>
		<td style="border-left: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>J&gt; A=[4 7; 2 6]<br>2x2 Array{Int64,2}:<br> 4  7<br> 2  6<br><br>J&gt; A_inv=inv(A)<br>2x2 Array{Float64,2}:<br>  0.6  -0.7<br> -0.2   0.4</font></td>
		<td style="border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=top bgcolor="#CFE7F5"><b><font face="Arial" size=2 color="#000000">Inverse of a matrix</font></b></td>
	</tr>
	<tr>
		<td colspan=6 height="202" align="center" valign=middle bgcolor="#FFFFFF"><b><font face="Arial" size=4 color="#000000">ADVANCED MATRIX OPERATIONS</font></b></td>
		</tr>
	<tr>
		<td style="border-right: 1px solid #000000" height="311" align="left" valign=top bgcolor="#FFFFFF"><b><font face="Arial" size=2 color="#000000">Calculating the covariance matrix&nbsp;<br>of 3 random variables <br><br>(here: covariances of the means&nbsp;<br>of x1, x2, and x3)</font></b></td>
		<td style="border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>M&gt; x1 = [4.0000 4.2000 3.9000 4.3000 4.1000]’<br><br>M&gt; x2 = [2.0000 2.1000 2.0000 2.1000 2.2000]'<br><br>M&gt; x3 = [0.60000 0.59000 0.58000 0.62000 0.63000]’<br><br>M&gt; cov( [x1,x2,x3] )<br>ans =<br>&nbsp;&nbsp; 2.5000e-02 &nbsp; 7.5000e-03 &nbsp; 1.7500e-03<br>&nbsp;&nbsp; 7.5000e-03 &nbsp; 7.0000e-03 &nbsp; 1.3500e-03<br>&nbsp;&nbsp; 1.7500e-03 &nbsp; 1.3500e-03 &nbsp; 4.3000e-04</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>P&gt; x1 = np.array([ 4, 4.2, 3.9, 4.3, 4.1])<br><br>P&gt; x2 = np.array([ 2, 2.1, 2, 2.1, 2.2])<br><br>P&gt; x3 = np.array([ 0.6, 0.59, 0.58, 0.62, 0.63])<br><br>P&gt; np.cov([x1, x2, x3])<br>Array([[ 0.025 &nbsp;, &nbsp;0.0075 , &nbsp;0.00175],<br>&nbsp; &nbsp; &nbsp; &nbsp;[ 0.0075 , &nbsp;0.007 &nbsp;, &nbsp;0.00135],<br>&nbsp; &nbsp; &nbsp; &nbsp;[ 0.00175, &nbsp;0.00135, &nbsp;0.00043]])</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>R&gt; x1 = matrix(c(4, 4.2, 3.9, 4.3, 4.1), ncol=5)<br><br>R&gt; x2 = matrix(c(2, 2.1, 2, 2.1, 2.2), ncol=5)<br><br>R&gt; x3 = matrix(c(0.6, 0.59, 0.58, 0.62, 0.63), ncol=5)  <br><br>R&gt; cov(matrix(c(x1, x2, x3), ncol=3))<br>        [,1]    [,2]    [,3]<br>[1,] 0.02500 0.00750 0.00175<br>[2,] 0.00750 0.00700 0.00135<br>[3,] 0.00175 0.00135 0.00043</font></td>
		<td style="border-left: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>J&gt; x1=[4.0 4.2 3.9 4.3 4.1]';<br><br>J&gt; x2=[2. 2.1 2. 2.1 2.2]';<br><br>J&gt; x3=[0.6 .59 .58 .62 .63]';<br><br>J&gt; cov([x1 x2 x3])<br>3x3 Array{Float64,2}:<br> 0.025    0.0075   0.00175<br> 0.0075   0.007    0.00135<br> 0.00175  0.00135  0.00043</font></td>
		<td style="border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=top bgcolor="#FFFFFF"><b><font face="Arial" size=2 color="#000000">Calculating the covariance matrix&nbsp;<br>of 3 random variables <br><br>(here: covariances of the means&nbsp;<br>of x1, x2, and x3)</font></b></td>
	</tr>
	<tr>
		<td style="border-right: 1px solid #000000" height="309" align="left" valign=top bgcolor="#CFE7F5"><b><font face="Arial" size=2 color="#000000">Calculating&nbsp;<br>eigenvectors and&nbsp;eigenvalues</font></b></td>
		<td style="border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>M&gt; A = [3 1; 1 3]<br>A =<br>&nbsp;&nbsp; 3 &nbsp; 1<br>&nbsp;&nbsp; 1 &nbsp; 3<br><br>M&gt; [eig_vec,eig_val] = eig(A)<br>eig_vec =<br>&nbsp; -0.70711 &nbsp; 0.70711<br>&nbsp;&nbsp; 0.70711 &nbsp; 0.70711<br>eig_val =<br>Diagonal Matrix<br>&nbsp;&nbsp; 2 &nbsp; 0<br>&nbsp;&nbsp; 0 &nbsp; 4</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>P&gt; A = np.array([[3, 1], [1, 3]])<br><br>P&gt; A<br>array([[3, 1],<br>&nbsp;&nbsp; &nbsp; &nbsp; [1, 3]])<br><br>P&gt; eig_val, eig_vec = np.linalg.eig(A)<br>P&gt; eig_val<br>array([ 4.,&nbsp; 2.])<br><br>P&gt; eig_vec<br>Array([[ 0.70710678, -0.70710678],<br>&nbsp;&nbsp; &nbsp; &nbsp; [ 0.70710678,&nbsp; 0.70710678]])</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>R&gt; A = matrix(c(3,1,1,3), ncol=2)<br><br>R&gt; A<br>     [,1] [,2]<br>[1,]    3    1<br>[2,]    1    3<br>R&gt; eigen(A)<br>$values<br>[1] 4 2<br><br>$vectors<br>          [,1]       [,2]<br>[1,] 0.7071068 -0.7071068<br>[2,] 0.7071068  0.7071068</font></td>
		<td style="border-left: 1px dotted #000000" align="left" valign=top bgcolor="#CFE7F5"><font face="Andale Mono" size=2>J&gt; A=[3 1; 1 3]<br>2x2 Array{Int64,2}:<br> 3  1<br> 1  3<br><br>J&gt; (eig_vec,eig_val)=eig(a)<br>([2.0,4.0],<br>2x2 Array{Float64,2}:<br> -0.707107  0.707107<br>  0.707107  0.707107)</font></td>
		<td style="border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=top bgcolor="#CFE7F5"><b><font face="Arial" size=2 color="#000000">Calculating&nbsp;<br>eigenvectors and&nbsp;eigenvalues</font></b></td>
	</tr>
	<tr>
		<td style="border-right: 1px solid #000000" height="539" align="left" valign=top bgcolor="#FFFFFF"><b><font face="Arial" size=2 color="#000000">Generating a Gaussian dataset:<br><br>creating random vectors from the multivariate normal<br>distribution given mean and covariance matrix<br><br>(here: 5 random vectors with <br>mean 0, covariance = 0, variance = 2)</font></b></td>
		<td style="border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>% requires statistics toolbox package<br>% how to install and load it in Octave:<br><br>% download the package from:&nbsp;<br>% http://octave.sourceforge.net/packages.php<br>% pkg install&nbsp;<br>% &nbsp; &nbsp; ~/Desktop/io-2.0.2.tar.gz &nbsp;<br>% pkg install&nbsp;<br>% &nbsp; &nbsp; ~/Desktop/statistics-1.2.3.tar.gz<br><br>M&gt; pkg load statistics<br><br>M&gt; mean = [0 0]<br><br>M&gt; cov = [2 0; 0 2]<br>cov =<br>&nbsp; &nbsp;2 &nbsp; 0<br>&nbsp; &nbsp;0 &nbsp; 2<br><br>M&gt; mvnrnd(mean,cov,5)<br>&nbsp; &nbsp;2.480150 &nbsp;-0.559906<br>&nbsp; -2.933047 &nbsp; 0.560212<br>&nbsp; &nbsp;0.098206 &nbsp; 3.055316<br>&nbsp; -0.985215 &nbsp;-0.990936<br>&nbsp; &nbsp;1.122528 &nbsp; 0.686977<br>&nbsp; &nbsp;&nbsp;</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2>P&gt; mean = np.array([0,0])<br><br>P&gt; cov = np.array([[2,0],[0,2]])<br><br>P&gt; np.random.multivariate_normal(mean, cov, 5)<br><br>Array([[ 1.55432624, -1.17972629],&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp;[-2.01185294, 1.96081908],&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp;[-2.11810813, 1.45784216],&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp;[-2.93207591, -0.07369322],&nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp;[-1.37031244, -1.18408792]])</font></td>
		<td style="border-left: 1px dotted #000000; border-right: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2># requires the ‘mass’ package<br><br> R&gt; install.packages('MASS')<br><br> R&gt; library(MASS) <br><br>R&gt; mvrnorm(n=10, mean, cov)<br>            [,1]       [,2]<br> [1,] -0.8407830 -0.1882706<br> [2,]  0.8496822 -0.7889329<br> [3,] -0.1564171  0.8422177<br> [4,] -0.6288779  1.0618688<br> [5,] -0.5103879  0.1303697<br> [6,]  0.8413189 -0.1623758<br> [7,] -1.0495466 -0.4161082<br> [8,] -1.3236339  0.7755572<br> [9,]  0.2771013  1.4900494<br>[10,] -1.3536268  0.2338913</font></td>
		<td style="border-left: 1px dotted #000000" align="left" valign=top bgcolor="#FFFFFF"><font face="Andale Mono" size=2># requires the Distributions package from https://github.com/JuliaStats/Distributions.jl<br><br>J&gt; using Distributions<br><br>J&gt; mean=[0., 0.]<br>2-element Array{Float64,1}:<br> 0.0<br> 0.0<br> <br>J&gt; cov=[2. 0.; 0. 2.]<br>2x2 Array{Float64,2}:<br> 2.0  0.0<br> 0.0  2.0<br><br>J&gt; rand( MvNormal(mean, cov), 5)<br>2x5 Array{Float64,2}:<br> -0.527634  0.370725  -0.761928  -3.91747   1.47516<br> -0.448821  2.21904    2.24561    0.692063  0.390495</font></td>
		<td style="border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=top bgcolor="#FFFFFF"><b><font face="Arial" size=2 color="#000000">Generating a Gaussian dataset:<br><br>creating random vectors from the multivariate normal<br>distribution given mean and covariance matrix<br><br>(here: 5 random vectors with <br>mean 0, covariance = 0, variance = 2)</font></b></td>
	</tr>
</table>





<a id='numpy_arrays'></a>


### Alternative data structures: NumPy matrices vs. NumPy arrays

Python's NumPy library also has a dedicated "matrix" type with a syntax that is a little bit closer to the MATLAB matrix: For example, the "<code>  *  </code>" operator would perform a matrix-matrix multiplication of NumPy matrices - same operator performs element-wise multiplication on NumPy arrays.    
Vice versa, the "`.dot()`" method is used for element-wise multiplication of NumPy matrices, wheras the equivalent operation would for NumPy arrays would be achieved via the "<code>  *  </code>"-operator.  
**Most people recommend the usage of the NumPy array type over NumPy matrices, since arrays are what most of the NumPy functions return.**