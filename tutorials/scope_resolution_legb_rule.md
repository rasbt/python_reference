# A Beginner's Guide to Python's Namespaces, Scope Resolution, and the LEGB Rule #


This is a short tutorial about Python's namespaces and the scope resolution for variable names using the LEGB-rule. The following sections will provide short example code blocks that should illustrate the problem followed by short explanations. You can simply read this tutorial from start to end, but I'd like to encourage you to execute the code snippets - you can either copy & paste them, or for your convenience, simply [download it as IPython notebook](https://raw.githubusercontent.com/rasbt/python_reference/master/tutorials/scope_resolution_legb_rule.ipynb).

<br>
<br>

## Objectives
- Namespaces and scopes - where does Python look for variable names?
- Can we define/reuse variable names for multiple objects at the same time?
- In which order does Python search different namespaces for variable names?

<br>
<br>

## Sections  
- [Introduction to namespaces and scopes](#introduction)  
- [1. LG - Local and Global scopes](#section_1)  
- [2. LEG - Local, Enclosed, and Global scope](#section_2)  
- [3. LEGB - Local, Enclosed, Global, Built-in](#section_3)  
- [Self-assessment exercise](#assessment)
- [Conclusion](#conclusion)  
- [Solutions](#solutions)
- [Warning: For-loop variables "leaking" into the global namespace](#for_loop)

<a name="introduction"></a>
<br>
<br>

##Introduction to Namespaces and Scopes

<br>

###Namespaces
<br>

Roughly speaking, namespaces are just containers for mapping names to objects. As you might have already heard, everything in Python - literals, lists, dictionaries, functions, classes, etc. - is an object.  
Such a "name-to-object" mapping allows us to access an object by a name that we've assigned to it. E.g., if we make a simple string assignment via `a_string = "Hello string"`, we created a reference to the `"Hello string"` object, and henceforth we can access via its variable name `a_string`.

We can picture a namespace as a Python dictionary structure, where the dictionary keys represent the names and the dictionary values the object itself (and this is also how namespaces are currently implemented in Python), e.g., 

<pre>a_namespace = {'name_a':object_1, 'name_b':object_2, ...}</pre>  


Now, the tricky part is that we have multiple independent namespaces in Python, and names can be reused for different namespaces (only the objects are unique, for example:

<pre>a_namespace = {'name_a':object_1, 'name_b':object_2, ...}
b_namespace = {'name_a':object_3, 'name_b':object_4, ...}</pre>

For example, every time we call a `for-loop` or define a function, it will create its own namespace. Namespaces also have different levels of hierarchy (the so-called "scope"), which we will discuss in more detail in the next section.

<br>
<br>

### Scope


In the section above, we have learned that namespaces can exist independently from each other and that they are structured in a certain hierarchy, which brings us to the concept of "scope". The "scope" in Python defines the "hierarchy level" in which we search namespaces for certain "name-to-object" mappings.  
For example, let us consider the following code:

`Input:`
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">i <span style="color: #333333">=</span> <span style="color: #0000DD; font-weight: bold">1</span>

<span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">foo</span>():
    i <span style="color: #333333">=</span> <span style="color: #0000DD; font-weight: bold">5</span>
    <span style="color: #007020">print</span>(i, <span style="background-color: #fff0f0">&#39;in foo()&#39;</span>)
<span style="color: #007020">print</span>(i, <span style="background-color: #fff0f0">&#39;global&#39;</span>)

foo()
</pre></div>

`Output:`
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #888888">1 global</span>
<span style="color: #888888">5 in foo()</span>
</pre></div>

<br>
<br>
Here, we just defined the variable name `i` twice, once on the `foo` function.

- `foo_namespace = {'i':object_3, ...}`  
- `global_namespace = {'i':object_1, 'name_b':object_2, ...}`

So, how does Python now which namespace it has to search if we want to print the value of the variable `i`? This is where Python's LEGB-rule comes into play, which we will discuss in the next section.

<br>
### Tip:
If we want to print out the dictionary mapping of the global and local variables, we can use the
the functions `global()` and `local()

`Input:`
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #888888">#print(globals()) # prints global namespace</span>
<span style="color: #888888">#print(locals()) # prints local namespace</span>

glob <span style="color: #333333">=</span> <span style="color: #0000DD; font-weight: bold">1</span>

<span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">foo</span>():
    loc <span style="color: #333333">=</span> <span style="color: #0000DD; font-weight: bold">5</span>
    <span style="color: #007020">print</span>(<span style="background-color: #fff0f0">&#39;loc in foo():&#39;</span>, <span style="background-color: #fff0f0">&#39;loc&#39;</span> <span style="color: #000000; font-weight: bold">in</span> <span style="color: #007020">locals</span>())

foo()
<span style="color: #007020">print</span>(<span style="background-color: #fff0f0">&#39;loc in global:&#39;</span>, <span style="background-color: #fff0f0">&#39;loc&#39;</span> <span style="color: #000000; font-weight: bold">in</span> <span style="color: #007020">globals</span>())    
<span style="color: #007020">print</span>(<span style="background-color: #fff0f0">&#39;glob in global:&#39;</span>, <span style="background-color: #fff0f0">&#39;foo&#39;</span> <span style="color: #000000; font-weight: bold">in</span> <span style="color: #007020">globals</span>())
</pre></div>

`Output:`
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #888888">loc in foo(): True</span>
<span style="color: #888888">loc in global: False</span>
<span style="color: #888888">glob in global: True</span>
</pre></div>

<br>
<br>

### Scope resolution for variable names via the LEGB rule.

We have seen that multiple namespaces can exist independently from each other and that they can contain the same variable names on different hierachy levels. The "scope" defines on which hierarchy level Python searches for a particular "variable name" for its associated object. Now, the next question is: "In which order does Python search the different levels of namespaces before it finds the name-to-object' mapping?"  
To answer is: It uses the LEGB-rule, which stands for

**Local -> Enclosed -> Global -> Built-in**, 

where the arrows should denote the direction of the namespace-hierarchy search order.  

- *Local* can be inside a function or class method, for example.  
- *Enclosed* can be its `enclosing` function, e.g., if a function is wrapped inside another function.  
- *Global* refers to the uppermost level of the executing script itself, and  
- *Built-in* are special names that Python reserves for itself.  

So, if a particular name:object mapping cannot be found in the local namespaces, the namespaces of the enclosed scope are being searched next. If the search in the enclosed scope is unsuccessful, too, Python moves on to the global namespace, and eventually, it will search the global namespaces (side note: if a name cannot found in any of the namespaces, a *NameError* will is raised).

**Note**:  
Namespaces can also be further nested, for example if we import modules, or if we are defining new classes. In those cases we have to use prefixes to access those nested namespaces. Let me illustrate this concept in the following code block:

`Input:`
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">import</span> <span style="color: #0e84b5; font-weight: bold">numpy</span>
<span style="color: #008800; font-weight: bold">import</span> <span style="color: #0e84b5; font-weight: bold">math</span>
<span style="color: #008800; font-weight: bold">import</span> <span style="color: #0e84b5; font-weight: bold">scipy</span>

<span style="color: #007020">print</span>(math<span style="color: #333333">.</span>pi, <span style="background-color: #fff0f0">&#39;from the math module&#39;</span>)
<span style="color: #007020">print</span>(numpy<span style="color: #333333">.</span>pi, <span style="background-color: #fff0f0">&#39;from the numpy package&#39;</span>)
<span style="color: #007020">print</span>(scipy<span style="color: #333333">.</span>pi, <span style="background-color: #fff0f0">&#39;from the scipy package&#39;</span>)
</pre></div>

`Output:`
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #888888">3.141592653589793 from the math module</span>
<span style="color: #888888">3.141592653589793 from the numpy package</span>
<span style="color: #888888">3.141592653589793 from the scipy package</span>
</pre></div>
<br>
<br>
(This is also why we have to be careful if we import modules via "`from a_module import *`", since it loads the variable names into the global namespace and could potentially overwrite already existing variable names)

<br>
<a name='section1'></a>
<br>
<br>
![LEGB figure](../Images/scope_resolution_1.png)
<br>
<br>

<a name="section_1"></a>
<br>
<br>

## 1. LG - Local and Global scopes

<a name='example1.1'></a>
**Example 1.1**  
As a warm-up exercise, let us first forget about the enclosed (E) and built-in (B) scopes in the LEGB rule and only take a look at LG - the local and global scopes.  
What does the following code print?

<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">a_var <span style="color: #333333">=</span> <span style="background-color: #fff0f0">&#39;global variable&#39;</span>

<span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">a_func</span>():
    <span style="color: #007020">print</span>(a_var, <span style="background-color: #fff0f0">&#39;[ a_var inside a_func() ]&#39;</span>)

a_func()
<span style="color: #007020">print</span>(a_var, <span style="background-color: #fff0f0">&#39;[ a_var outside a_func() ]&#39;</span>)
</pre></div>

**a)**
<pre>raises an error</pre>

**b)** 
<pre>
global value [ a_var outside a_func() ]</pre>

**c)** 
<pre>global value [ a_var in a_func() ]  
global value [ a_var outside a_func() ]</pre>

[[go to solution](#solutions)]

### Here is why:

We call `a_func()` first, which is supposed to print the value of `a_var`. According to the LEGB rule, the function will first look in its own local scope (L) if `a_var` is defined there. Since `a_func()` does not define its own `a_var`, it will look one-level above in the global scope (G) in which `a_var` has been defined previously.
<br>
<br>

<a name='example1.2'></a>
**Example 1.2**  
Now, let us define the variable `a_var` in the global and the local scope.  
Can you guess what the following code will produce?

<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">a_var <span style="color: #333333">=</span> <span style="background-color: #fff0f0">&#39;global value&#39;</span>

<span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">a_func</span>():
    a_var <span style="color: #333333">=</span> <span style="background-color: #fff0f0">&#39;local value&#39;</span>
    <span style="color: #007020">print</span>(a_var, <span style="background-color: #fff0f0">&#39;[ a_var inside a_func() ]&#39;</span>)

a_func()
<span style="color: #007020">print</span>(a_var, <span style="background-color: #fff0f0">&#39;[ a_var outside a_func() ]&#39;</span>)
</pre></div>

**a)**
<pre>raises an error</pre>

**b)** 
<pre>local value [ a_var in a_func() ]
global value [ a_var outside a_func() ]</pre>

**c)** 
<pre>global value [ a_var in a_func() ]  
global value [ a_var outside a_func() ]</pre>


[[go to solution](#solutions)]

### Here is why:

When we call `a_func()`, it will first look in its local scope (L) for `a_var`, since `a_var` is defined in the local scope of `a_func`, its assigned value `local variable` is printed. Note that this doesn't affect the global variable, which is in a different scope.

<br>
However, it is also possible to modify the global by, e.g., re-assigning a new value to it if we use the global keyword as the following example will illustrate:

`Input:`
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">a_var <span style="color: #333333">=</span> <span style="background-color: #fff0f0">&#39;global value&#39;</span>

<span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">a_func</span>():
    <span style="color: #008800; font-weight: bold">global</span> a_var
    a_var <span style="color: #333333">=</span> <span style="background-color: #fff0f0">&#39;local value&#39;</span>
    <span style="color: #007020">print</span>(a_var, <span style="background-color: #fff0f0">&#39;[ a_var inside a_func() ]&#39;</span>)

<span style="color: #007020">print</span>(a_var, <span style="background-color: #fff0f0">&#39;[ a_var outside a_func() ]&#39;</span>)
a_func()
<span style="color: #007020">print</span>(a_var, <span style="background-color: #fff0f0">&#39;[ a_var outside a_func() ]&#39;</span>)
</pre></div>

`Output:`
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #888888">**a)**</span>
<span style="color: #888888">&lt;pre&gt;raises an error&lt;/pre&gt;</span>

<span style="color: #888888">**b)** </span>
<span style="color: #888888">&lt;pre&gt;</span>
<span style="color: #888888">global value [ a_var outside a_func() ]&lt;/pre&gt;</span>

<span style="color: #888888">**c)** </span>
<span style="color: #888888">&lt;pre&gt;global value [ a_var in a_func() ]  </span>
<span style="color: #888888">global value [ a_var outside a_func() ]&lt;/pre&gt;</span>
</pre></div>

But we have to be careful about the order: it is easy to raise an `UnboundLocalError` if we don't explicitly tell Python that we want to use the global scope and try to modify a variable's value (remember, the right side of an assignment operation is executed first):

`Input:`
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">a_var <span style="color: #333333">=</span> <span style="color: #0000DD; font-weight: bold">1</span>

<span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">a_func</span>():
    a_var <span style="color: #333333">=</span> a_var <span style="color: #333333">+</span> <span style="color: #0000DD; font-weight: bold">1</span>
    <span style="color: #007020">print</span>(a_var, <span style="background-color: #fff0f0">&#39;[ a_var inside a_func() ]&#39;</span>)

<span style="color: #007020">print</span>(a_var, <span style="background-color: #fff0f0">&#39;[ a_var outside a_func() ]&#39;</span>)
a_func()
</pre></div>
`Output:`
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #333333">---------------------------------------------------------------------------</span>
<span style="color: #FF0000; font-weight: bold">UnboundLocalError</span>                         Traceback (most recent call last)
<span style="color: #333333">&lt;</span>ipython<span style="color: #333333">-</span><span style="color: #007020">input</span><span style="color: #333333">-</span><span style="color: #0000DD; font-weight: bold">4</span><span style="color: #333333">-</span>a6cdd0ee9a55<span style="color: #333333">&gt;</span> <span style="color: #000000; font-weight: bold">in</span> <span style="color: #333333">&lt;</span>module<span style="color: #333333">&gt;</span>()
      <span style="color: #0000DD; font-weight: bold">6</span> 
      <span style="color: #0000DD; font-weight: bold">7</span> <span style="color: #007020">print</span>(a_var, <span style="background-color: #fff0f0">&#39;[ a_var outside a_func() ]&#39;</span>)
<span style="color: #333333">----&gt;</span> <span style="color: #0000DD; font-weight: bold">8</span> a_func()

<span style="color: #333333">&lt;</span>ipython<span style="color: #333333">-</span><span style="color: #007020">input</span><span style="color: #333333">-</span><span style="color: #0000DD; font-weight: bold">4</span><span style="color: #333333">-</span>a6cdd0ee9a55<span style="color: #333333">&gt;</span> <span style="color: #000000; font-weight: bold">in</span> a_func()
      <span style="color: #0000DD; font-weight: bold">2</span> 
      <span style="color: #0000DD; font-weight: bold">3</span> <span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">a_func</span>():
<span style="color: #333333">----&gt;</span> <span style="color: #0000DD; font-weight: bold">4</span>     a_var <span style="color: #333333">=</span> a_var <span style="color: #333333">+</span> <span style="color: #0000DD; font-weight: bold">1</span>
      <span style="color: #0000DD; font-weight: bold">5</span>     <span style="color: #007020">print</span>(a_var, <span style="background-color: #fff0f0">&#39;[ a_var inside a_func() ]&#39;</span>)
      <span style="color: #0000DD; font-weight: bold">6</span> 

<span style="color: #FF0000; font-weight: bold">UnboundLocalError</span>: local variable <span style="background-color: #fff0f0">&#39;a_var&#39;</span> referenced before assignment

<span style="color: #0000DD; font-weight: bold">1</span> [ a_var outside a_func() ]
</pre></div>

<br>
<br>

<a name="section_2"></a>
<br>
<br>

## 2. LEG - Local, Enclosed, and Global scope



Now, let us introduce the concept of the enclosed (E) scope. Following the order "Local -> Enclosed -> Global", can you guess what the following code will print?

<a name='example2'></a>
**Example 2.1**

<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">a_var <span style="color: #333333">=</span> <span style="background-color: #fff0f0">&#39;global value&#39;</span>

<span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">outer</span>():
    a_var <span style="color: #333333">=</span> <span style="background-color: #fff0f0">&#39;enclosed value&#39;</span>
    
    <span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">inner</span>():
        a_var <span style="color: #333333">=</span> <span style="background-color: #fff0f0">&#39;local value&#39;</span>
        <span style="color: #007020">print</span>(a_var)
    
    inner()

outer()
</pre></div>
**a)**
<pre>global value</pre>

**b)** 
<pre>enclosed value</pre>

**c)** 
<pre>local value</pre>

[[go to solution](#solutions)]

### Here is why:

Let us quickly recapitulate what we just did: We called `outer()`, which defined the variable `a_var` locally (next to an existing `a_var` in the global scope). Next, the `outer()` function called `inner()`, which in turn defined a variable with of name `a_var` as well. The `print()` function inside `inner()` searched in the local scope first (L->E) before it went up in the scope hierarchy, and therefore it printed the value that was assigned in the local scope.

Similar to the concept of the `global` keyword, which we have seen in the section above, we can use the keyword `nonlocal` inside the inner function to explicitly access a variable from the outer (enclosed) scope in order to modify its value.  
Note that the `nonlocal` keyword was added in Python 3.x and is not implemented in Python 2.x (yet).

`Input:`
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">a_var <span style="color: #333333">=</span> <span style="background-color: #fff0f0">&#39;global value&#39;</span>

<span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">outer</span>():
       a_var <span style="color: #333333">=</span> <span style="background-color: #fff0f0">&#39;local value&#39;</span>
       <span style="color: #007020">print</span>(<span style="background-color: #fff0f0">&#39;outer before:&#39;</span>, a_var)
       <span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">inner</span>():
           <span style="color: #008800; font-weight: bold">nonlocal</span> a_var
           a_var <span style="color: #333333">=</span> <span style="background-color: #fff0f0">&#39;inner value&#39;</span>
           <span style="color: #007020">print</span>(<span style="background-color: #fff0f0">&#39;in inner():&#39;</span>, a_var)
       inner()
       <span style="color: #007020">print</span>(<span style="background-color: #fff0f0">&quot;outer after:&quot;</span>, a_var)
outer()
</pre></div>
`Output:`
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #888888">outer before: local value</span>
<span style="color: #888888">in inner(): inner value</span>
<span style="color: #888888">outer after: inner value</span>
</pre></div>

<a name="section_3"></a>
<br>
<br>
<br>


## 3. LEGB - Local, Enclosed, Global, Built-in

To wrap up the LEGB rule, let us come to the built-in scope. Here, we will define our "own" length-function, which happens to bear the same name as the in-built `len()` function. What outcome do you expect if we'd execute the following code?

<a name='example3'></a>

**Example 3**

<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">a_var <span style="color: #333333">=</span> <span style="background-color: #fff0f0">&#39;global variable&#39;</span>

<span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">len</span>(in_var):
    <span style="color: #007020">print</span>(<span style="background-color: #fff0f0">&#39;called my len() function&#39;</span>)
    l <span style="color: #333333">=</span> <span style="color: #0000DD; font-weight: bold">0</span>
    <span style="color: #008800; font-weight: bold">for</span> i <span style="color: #000000; font-weight: bold">in</span> in_var:
        l <span style="color: #333333">+=</span> <span style="color: #0000DD; font-weight: bold">1</span>
    <span style="color: #008800; font-weight: bold">return</span> l

<span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">a_func</span>(in_var):
    len_in_var <span style="color: #333333">=</span> <span style="color: #007020">len</span>(in_var)
    <span style="color: #007020">print</span>(<span style="background-color: #fff0f0">&#39;Input variable is of length&#39;</span>, len_in_var)

a_func(<span style="background-color: #fff0f0">&#39;Hello, World!&#39;</span>)
</pre></div>

**a)**
<pre>raises an error (conflict with in-built `len()` function)</pre>

**b)** 
<pre>called my len() function
Input variable is of length 13</pre>

**c)** 
<pre>Input variable is of length 13</pre>

[[go to solution](#solutions)]

### Here is why:

Since the exact same names can be used to map names to different objects - as long as the names are in different name spaces - there is no problem of reusing the name `len` to define our own length function (this is just for demonstration purposes, it is NOT recommended). As we go up in Python's L -> E -> G -> B hierarchy, the function `a_func()` finds `len()` already in the global scope first before it attempts


<a name ="assessment"></a>
<br>
<br>

# Self-assessment exercise

Now, after we went through a couple of exercises, let us quickly check where we are. So, one more time: What would the following code print out?

<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">a <span style="color: #333333">=</span> <span style="background-color: #fff0f0">&#39;global&#39;</span>

<span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">outer</span>():
    
    <span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">len</span>(in_var):
        <span style="color: #007020">print</span>(<span style="background-color: #fff0f0">&#39;called my len() function: &#39;</span>, end<span style="color: #333333">=</span><span style="background-color: #fff0f0">&quot;&quot;</span>)
        l <span style="color: #333333">=</span> <span style="color: #0000DD; font-weight: bold">0</span>
        <span style="color: #008800; font-weight: bold">for</span> i <span style="color: #000000; font-weight: bold">in</span> in_var:
            l <span style="color: #333333">+=</span> <span style="color: #0000DD; font-weight: bold">1</span>
        <span style="color: #008800; font-weight: bold">return</span> l
    
    a <span style="color: #333333">=</span> <span style="background-color: #fff0f0">&#39;local&#39;</span>
    
    <span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">inner</span>():
        <span style="color: #008800; font-weight: bold">global</span> <span style="color: #007020">len</span>
        <span style="color: #008800; font-weight: bold">nonlocal</span> a
        a <span style="color: #333333">+=</span> <span style="background-color: #fff0f0">&#39; variable&#39;</span>
    inner()
    <span style="color: #007020">print</span>(<span style="background-color: #fff0f0">&#39;a is&#39;</span>, a)
    <span style="color: #007020">print</span>(<span style="color: #007020">len</span>(a))

outer()

<span style="color: #007020">print</span>(<span style="color: #007020">len</span>(a))
<span style="color: #007020">print</span>(<span style="background-color: #fff0f0">&#39;a is&#39;</span>, a)
</pre></div>

<a name="conclusion"
<br>
<br>

[[go to solution](#solutions)]

# Conclusion

I hope this short tutorial was helpful to understand the basic concept of Python's scope resolution order using the LEGB rule. I want to encourage you (as a little self-assessment exercise) to look at the code snippets again tomorrow and check if you can correctly predict all their outcomes.

#### A rule of thumb

In practice, **it is usually a bad idea to modify global variables inside the function scope**, since it often be the cause of confusion and weird errors that are hard to debug.  
If you want to modify a global variable via a function, it is recommended to pass it as an argument and reassign the return-value.  
For example:

`Input:`
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">a_var <span style="color: #333333">=</span> <span style="color: #0000DD; font-weight: bold">2</span>

<span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">a_func</span>(some_var):
    <span style="color: #008800; font-weight: bold">return</span> <span style="color: #0000DD; font-weight: bold">2</span><span style="color: #333333">**</span><span style="color: #0000DD; font-weight: bold">3</span>

a_var <span style="color: #333333">=</span> a_func(a_var)
<span style="color: #007020">print</span>(a_var)
</pre></div>
`Output:`
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #888888">8</span>
</pre></div>


<a name = "solutions"></a>
<br>
<br>

## Solutions

In order to prevent you from unintentional spoilers, I have written the solutions in binary format. In order to display the character representation, you just need to execute the following lines of code:

<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #007020">print</span>(<span style="background-color: #fff0f0">&#39;Example 1.1:&#39;</span>, <span style="color: #007020">chr</span>(<span style="color: #007020">int</span>(<span style="background-color: #fff0f0">&#39;01100011&#39;</span>,<span style="color: #0000DD; font-weight: bold">2</span>)))
</pre></div>

[[back to example 1.1](#example1.1)]

<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #007020">print</span>(<span style="background-color: #fff0f0">&#39;Example 1.2:&#39;</span>, <span style="color: #007020">chr</span>(<span style="color: #007020">int</span>(<span style="background-color: #fff0f0">&#39;01100001&#39;</span>,<span style="color: #0000DD; font-weight: bold">2</span>)))
</pre></div>

[[back to example 1.2](#example1.2)]

<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #007020">print</span>(<span style="background-color: #fff0f0">&#39;Example 2:&#39;</span>, <span style="color: #007020">chr</span>(<span style="color: #007020">int</span>(<span style="background-color: #fff0f0">&#39;01100011&#39;</span>,<span style="color: #0000DD; font-weight: bold">2</span>)))
</pre></div>

[[back to example 2](#example2)]

<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #007020">print</span>(<span style="background-color: #fff0f0">&#39;Example 3:&#39;</span>, <span style="color: #007020">chr</span>(<span style="color: #007020">int</span>(<span style="background-color: #fff0f0">&#39;01100010&#39;</span>,<span style="color: #0000DD; font-weight: bold">2</span>)))
</pre></div>

[[back to example 3](#example3)]

<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #888888"># Solution to the self-assessment exercise</span>
sol <span style="color: #333333">=</span> <span style="background-color: #fff0f0">&quot;000010100110111101110101011101000110010101110010001010&quot;</span>\
<span style="background-color: #fff0f0">&quot;0000101001001110100000101000001010011000010010000001101001011100110&quot;</span>\
<span style="background-color: #fff0f0">&quot;0100000011011000110111101100011011000010110110000100000011101100110&quot;</span>\
<span style="background-color: #fff0f0">&quot;0001011100100110100101100001011000100110110001100101000010100110001&quot;</span>\
<span style="background-color: #fff0f0">&quot;1011000010110110001101100011001010110010000100000011011010111100100&quot;</span>\
<span style="background-color: #fff0f0">&quot;1000000110110001100101011011100010100000101001001000000110011001110&quot;</span>\
<span style="background-color: #fff0f0">&quot;1010110111001100011011101000110100101101111011011100011101000100000&quot;</span>\
<span style="background-color: #fff0f0">&quot;0011000100110100000010100000101001100111011011000110111101100010011&quot;</span>\
<span style="background-color: #fff0f0">&quot;0000101101100001110100000101000001010001101100000101001100001001000&quot;</span>\
<span style="background-color: #fff0f0">&quot;0001101001011100110010000001100111011011000110111101100010011000010&quot;</span>\
<span style="background-color: #fff0f0">&quot;1101100&quot;</span>

sol_str <span style="color: #333333">=</span><span style="background-color: #fff0f0">&#39;&#39;</span><span style="color: #333333">.</span>join(<span style="color: #007020">chr</span>(<span style="color: #007020">int</span>(sol[i:i<span style="color: #333333">+</span><span style="color: #0000DD; font-weight: bold">8</span>], <span style="color: #0000DD; font-weight: bold">2</span>)) <span style="color: #008800; font-weight: bold">for</span> i <span style="color: #000000; font-weight: bold">in</span> <span style="color: #007020">range</span>(<span style="color: #0000DD; font-weight: bold">0</span>, <span style="color: #007020">len</span>(sol), <span style="color: #0000DD; font-weight: bold">8</span>))
<span style="color: #008800; font-weight: bold">for</span> line <span style="color: #000000; font-weight: bold">in</span> sol_str<span style="color: #333333">.</span>split(<span style="background-color: #fff0f0">&#39;</span><span style="color: #666666; font-weight: bold; background-color: #fff0f0">\n</span><span style="background-color: #fff0f0">&#39;</span>):
    <span style="color: #007020">print</span>(line)
</pre></div>

[[back to self-assessment exercise](#assessment)]




<br>
<br>
<a name="for_loop"></a>

## Warning: For-loop variables "leaking" into the global namespace

In contrast to some other programming languages, `for-loops` will use the scope they exist in and leave their defined loop-variable behind.

`Input:`
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">for</span> a <span style="color: #000000; font-weight: bold">in</span> <span style="color: #007020">range</span>(<span style="color: #0000DD; font-weight: bold">5</span>):
    <span style="color: #008800; font-weight: bold">if</span> a <span style="color: #333333">==</span> <span style="color: #0000DD; font-weight: bold">4</span>:
        <span style="color: #007020">print</span>(a, <span style="background-color: #fff0f0">&#39;-&gt; a in for-loop&#39;</span>)
<span style="color: #007020">print</span>(a, <span style="background-color: #fff0f0">&#39;-&gt; a in global&#39;</span>)
</pre></div>
`Output:`
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #888888">4 -&gt; a in for-loop</span>
<span style="color: #888888">4 -&gt; a in global</span>
</pre></div>

**This also applies if we explicitely defined the `for-loop` variable in the global namespace before!** In this case it will rebind the existing variable:

`Input:`
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">b <span style="color: #333333">=</span> <span style="color: #0000DD; font-weight: bold">1</span>
<span style="color: #008800; font-weight: bold">for</span> b <span style="color: #000000; font-weight: bold">in</span> <span style="color: #007020">range</span>(<span style="color: #0000DD; font-weight: bold">5</span>):
    <span style="color: #008800; font-weight: bold">if</span> b <span style="color: #333333">==</span> <span style="color: #0000DD; font-weight: bold">4</span>:
        <span style="color: #007020">print</span>(b, <span style="background-color: #fff0f0">&#39;-&gt; b in for-loop&#39;</span>)
<span style="color: #007020">print</span>(b, <span style="background-color: #fff0f0">&#39;-&gt; b in global&#39;</span>)
</pre></div>

`Output:`
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #888888">4 -&gt; b in for-loop</span>
<span style="color: #888888">4 -&gt; b in global</span>
</pre></div>

However, in **Python 3.x**, we can use closures to prevent the for-loop variable to cut into the global namespace. Here is an example (exectuted in Python 3.4):

`Input:`
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">i <span style="color: #333333">=</span> <span style="color: #0000DD; font-weight: bold">1</span>
<span style="color: #007020">print</span>([i <span style="color: #008800; font-weight: bold">for</span> i <span style="color: #000000; font-weight: bold">in</span> <span style="color: #007020">range</span>(<span style="color: #0000DD; font-weight: bold">5</span>)])
<span style="color: #007020">print</span>(i, <span style="background-color: #fff0f0">&#39;-&gt; i in global&#39;</span>)
</pre></div>
`Output:`
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #888888">[0, 1, 2, 3, 4]</span>
<span style="color: #888888">1 -&gt; i in global</span>
</pre></div>

Why did I mention "Python 3.x"? Well, as it happens, the same code executed in Python 2.x would print:

<pre>
4 -> i in global
</pre>

This goes back to a change that was made in Python 3.x and is described in [What’s New In Python 3.0](https://docs.python.org/3/whatsnew/3.0.html) as follows:

"List comprehensions no longer support the syntactic form `[... for var in item1, item2, ...]`. Use `[... for var in (item1, item2, ...)]` instead. Also note that list comprehensions have different semantics: they are closer to syntactic sugar for a generator expression inside a `list()` constructor, and in particular the loop control variables are no longer leaked into the surrounding scope."