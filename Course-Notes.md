# Week 1
1. Went over the basic types of statistics
  - Numerical
  - Categorical
  - Order
  - Nominal
  - Unstructured
  
2. notebooks.ai - cloud architecture all command line

3. Jupyter stands for Julia, Python and R

4. basic Unix commands

5. How to create new repositories in Github and how to use notebooks.ai

6. the book python for data analysis by wes mckinney

## Chapter 1
  - book primarily refers to *structured* data
    - tabular or spreadsheet where columns can be ifferent data types (relational databases, comma/tab delimited)
    - multidimensional arrays(matrices)
    - multiple tables of interrelated data (primary or foreign keys for SQL)
    - evenly or unevenly spaced time series
    - etc
   - part of python's success is integration with C, C++ and FORTRAN
   - Instead of writing in a specialized language and then porting to something like C++ or Java, Python is good for prototyping and building production systems
   - runs slower since it is an interpreted language (not good for low latency situations)
   - hard to build multithreaded apps b/c of the global interpreter lock (GIL) - prevents execution of more than one instruction at a time
    - can use Python C extensions to get around this 
   -Python libraries
    1. **NumPy** - numerical python. Provides data structures, algorithms, and library glue for scientific applications involving numerical data
      - fast and efficient multidemensional array object *ndarray*
      - functions for performing element-wise computations with arrays or mathematical operations between arrays
      - tools for reading and writing array-based datasets to disk
      - linear algebra operations, fourier tranfom, and random number generation
      - mature C API to enable python extensions and native C or C++ code to access MumPy's data structures and computational facilities
      - container for data to be passed between algorithms and libraries
     2. **pandas** - high level data structures and functions to make working with structured or tabular data fast, easy and expressive
      - primary objects in pandas from this books are the 
        - **DataFrame** - tabular, column oriented data structure with row and column labels
        - **Series** - one dimensional labeled array object
       - combines high performanc, array computing ideas of NumPy with the flexible data manipulation capabilities of spreadsheets and relational databases
       - sophisticated indexing functionality
      3. **matplotlib** - most popular python library for producing plots and other two dimensional data visualization
      4. **IPython and Jupyter** - Ipython is designed to maximize productivity in interactive computing and software development
        - encourages *execute-explore* workflow
        - provides easy access to OS's shell and filesystem
        - Jupyter Ipython became Jupyter - supports over 40 languages
       5. **SciPy** - collection of packages addressing stand problem domains in scientific computing
        - scipy.integrae - numerical integration routings and differential equation solvers
        - skipy.linalg - linear algebra routines and matrix decompositions extending beyond those in numpy.linalg
        - scipy.optimize - funciton optimizers (minipizers) and root finding algorithms
        - scipy.signal - signal processing tools
        - scipy.sparse - sparce matrices and sparse linear system solvers
        - scipy.special - wrapper around SPECFUN, a Fortran library implementing many common mathematical functions, such as *gamma* function
        - scipy.stats - standard continuous and discrete probability distributions, various statistical tests, adn more descriptive statistics
       6. **scikit-learn** - premier general purpose machine learning toolkit
       7. **statsmodels** - statistical analysis package
        - Regression models: Linear regression, generalized linear models, robust linear models, linear mixed effects models, etc.
        - Analysis of variance (ANOVA)
        - Time series analysis: AR, ARMA, ARIMA, VAR, and other models
        - Nonparametric methods: Kernel density estimation, kernel regression
        - Visualization of statistical model results
  - download and install Anaconda
    - type **python** into command prompt to verify Anaconda version
    - how install/update packages
    - use python 3.6 or newer
  - IDEs
      - PyDev (free), on Eclipse platform
      - Spyder (free), currently shipped with Anaconda
      - other commrecial/subscription ones
      - text editors like Atom and Sublime text 2 have Python support
  - general python help
    - pydata - google group list for questions related to python for data analysis and pandas
    - pystatsmodels - for statsmodels or pandas related questions
    - nympy-discussion 
    - scipy-user
  - jargon
    - munge/munging/wrangling - overall process of manipulating unstructured/messy data into a structured or clean form
    - pseudocode - description of algorithm or process that takes a code like form while not being actual valid source code
    - syntactic sugar - programming syntax that does not add new features but makes it convenient/easier to tyoe
    
## Chapter 2
- recommends using the official Python tutorial, python cookbook 3rd addition O'Reilly, Fluent Python O'Reilly, Effective Python Pearson

  - python is an interpreted language. The interpreter runs programs by executing one statement at a time
  - python interpreter can be invoked by typing **python**
  - >>> is th eprompt
  - type **exit()** to exit
  - type **python hellow_world.py** to execute file from PWD
  - **%run hellow_world.py** in IPython runs file
  - IPython promt is *In [1]* - can be launced just like python
  - when you type just a variable into IPython, it renders a string representation of that object
  - to start Jupyter type **jupyter** - many platforms it auto opens the web browser unless you start with --no-browser
    ~ otherwise you can go to the address that is printed when you started the notebook
  - explains how to start new notebook - like running notebooks.ai
  - author's repository on github - *wesm/pydata-book*
  
 - keyboard shortcuts IPython:
    - Ctrl-P or up-arrow	Search backward in command history for commands starting with currently entered text
    - Ctrl-N or down-arrow	Search forward in command history for commands starting with currently entered text
    - Ctrl-R	Readline-style reverse history search (partial matching)
    - Ctrl-Shift-V	Paste text from clipboard
    - Ctrl-C	Interrupt currently executing code
    - Ctrl-A	Move cursor to beginning of line
    - Ctrl-E	Move cursor to end of line
    - Ctrl-K	Delete text from cursor until end of line
    - Ctrl-U	Discard all text on current line
    - Ctrl-F	Move cursor forward one character
    - Ctrl-B	Move cursor back one character
    - Ctrl-L	Clear screen
   - Jupyter notebooks have different shortcuts
   
 - magic commands
  - IPython's special commands (not built into python itself)
  - designed to facilitate common tasks
  - prefixed by symbol %
  - %timeit - checks execution time of any Python statement
  - don't seem to work in notebooks.ai?
  - frequent commands
    - %quickref	Display the IPython Quick Reference Card
    - %magic	Display detailed documentation for all of the available magic commands
    - %debug	Enter the interactive debugger at the bottom of the last exception traceback
    - %hist	Print command input (and optionally output) history
    - %pdb	Automatically enter debugger after any exception
    - %paste	Execute preformatted Python code from clipboard
    - %cpaste	Open a special prompt for manually pasting Python code to be executed
    - %reset	Delete all variables/names defined in interactive namespace
    - %page OBJECT	Pretty-print the object and display it through a pager
    - %run script.py	Run a Python script inside IPython
    - %prun statement	Execute statement with cProfile and report the profiler output
    - %time statement	Report the execution time of a single statement
    - %timeit statement	Run a statement multiple times to compute an ensemble average execution time; useful for timing code with very short execution time
  - %who, %who_ls, %whos	Display variables defined in interactive namespace, with varying levels of information/verbosity
  - %xdel variable	Delete a variable and attempt to clear any references to the object in the IPython internals
  - %matplotlib configures its integration with the IPython shell or Jupyter notebook
    - in IPython shell, running this sets up the integration so you can create multiple plot windows without interfering with console session
    - in Jupyter it's %matplotlib inline
     
-- python language basics
  - uses whitespace to structure code instead of braces
  - using 4 spaces instead of a tab is common and suggested 
  - python statements don't need to be terminated by semicolons but they can be used to separate multiple statements on single line
  - everything is an object (number, string, data structure, function, class, module, etc)
    - each object has an associated type (string/function) and internal data
    - makes the language flexible
  - comments use #
    - also used to exclude sections of code without deleting them
  - call functions using parentheses and passing zero or more arguments, optionally assigning the returned value to a variable
  - almost every object in Python has attached functions (methods) that have access to the object's internal contents
  - functions can take both positional and keyword arguments
  
- Variables and argument passing
  - variables (names) create references to th eobject on the right side of the equals sign
    ~  In [8]: a = [1, 2, 3]
       In [9]: b = a
     ~ a and b now refer to the same object, the original list
     ~ can test by appending to a and examining b
    ~ In[10]: a.append(4)
    ~ In[11]: b
  - when you pass objects as arguments to a function, new local variables are created referencing the original objects without any copying
    ~ if you bind a new object to a variable inside a function, the change will not reflect in parent
  - object references in Python have no type associated with them
    ~ In [12]: a = 5

      In [13]: type(a)
      Out[13]: int

      In [14]: a = 'foo'

      In [15]: type(a)
      Out[15]: str
    ~ variables are names for objects in a namespace. The type of info is stored in the object itself
    ~ every object has a specific type (or class), and implicit conversions will occur onlu in certain obvious circumstances
      ~ In [17]: a = 4.5

        In [18]: b = 2

        String formatting, to be visited later
        In [19]: print('a is {0}, b is {1}'.format(type(a), type(b)))
        a is <class 'float'>, b is <class 'int'>

        In [20]: a / b
        Out[20]: 2.25
    ~ knowing the type of an object is important. Can check that an object is an instance of a type using the isinstance function
        - In [21]: a = 5

          In [22]: isinstance(a, int)
          Out[22]: True
      ~ can use isinstance with a tuple of types to check if an object's type is in the tuple
        - In [23]: a = 5; b = 4.5

          In [24]: isinstance(a, (int, float))
          Out[24]: True

          In [25]: isinstance(b, (int, float))
          Out[25]: True   
          
- attributes and methods
  - objects in python have attributes (objects stored inside the object) and methods (functions associated with an object that can have access to the object's internal data)
  - both are accessed via syntax obj.attribute_name or the getattr function
      In [1]: a = 'foo'
      In [2]: a.<Press Tab>
      
      or 
      
      In [27]: getattr(a, 'split')
      Out[27]: <function str.split>
      
- duck typing
  - don't care about the type, just whether it has certain methods or behavior
  - For example, you can verify that an object is iterable if it implemented the iterator protocol. For many objects, this means it has a __iter__ “magic method”
    ~ alternative and better way to check is to try using the iter function:
      def isiterable(obj):
    try:
        iter(obj)
        return True
    except TypeError: # not iterable
        return False
        
    In [29]: isiterable('a string')
    Out[29]: True
    
    ~ this is useful when writing functions that cna accept multiple kinds of input
      ~ writing a function that can accept any sequence (list, tuple, ndarray) or an iterator
      ~ check if object is a list (or NumPy array) and if not, convert to one
      if not isinstance(x, list) and isiterable(x):
           x = list(x)
           
 - Imports
  - modules are a file with the .py extension
  - to access variables in .py file in same directory:
    import some_module
    result = some_module.f(5)
    pi = some_module.PI
    
    or
    
    from some_module import f, g, PI
    result = g(5, PI)
 
 - can use *as* keyword to give imports different variable names
    import some_module as sm
    from some_module import PI as pi, g as gf

    r1 = sm.f(pi)
    r2 = gf(6, pi)
    
 - binary operators and comparisons
    - mostly as you'd expect
    - to check if two references refer to the same object, use the *is* keyword (or *is not*)
        In [35]: a = [1, 2, 3]

        In [36]: b = a

        In [37]: c = list(a)

        In [38]: a is b
        Out[38]: True

        In [39]: a is not c
        Out[39]: True
    - since **list** always creates new Python list, c is distint from a
    - comparing with is is not the same as the == operator because in that case a == c is true
    - common use of is and is not is to check if variable is **none** since there is only one instance of none
      In [41]: a = None

      In [42]: a is None
      Out[42]: True
  - common operators
      a + b	Add a and b
      a - b	Subtract b from a
      a * b	Multiply a by b
      a / b	Divide a by b
      a // b	Floor-divide a by b, dropping any fractional remainder
      a ** b	Raise a to the b power
      a & b	True if both a and b are True; for integers, take the bitwise AND
      a | b	True if either a or b is True; for integers, take the bitwise OR
      a ^ b	For booleans, True if a or b is True, but not both; for integers, take the bitwise EXCLUSIVE-OR
      a == b	True if a equals b
      a != b	True if a is not equal to b
      a <= b, a < b	True if a is less than (less than or equal) to b
      a > b, a >= b	True if a is greater than (greater than or equal) to b
      a is b	True if a and b reference the same Python object
      a is not b	True if a and b reference different Python objects
 
 
 - Mutable and immutable objects
  - most objects like lists, dicts, NumPy arrays, and user defined types are mutable (can be changed)
      In [43]: a_list = ['foo', 2, [4, 5]]

      In [44]: a_list[2] = (3, 4)

      In [45]: a_list
      Out[45]: ['foo', 2, (3, 4)]
  - strings and tuples are not    
      In [46]: a_tuple = (3, 5, (4, 5))

      In [47]: a_tuple[1] = 'four'
  - Just because you can mutate an object doesn't mean you should b/c of side effects
  
- Scalar types
  - built in types for handling numerical data, strings, boolean values, dates and times. "Single value" or *scalar types*
  - standard scalar types
    None	The Python “null” value (only one instance of the None object exists)
    str	String type; holds Unicode (UTF-8 encoded) strings
    bytes	Raw ASCII bytes (or Unicode encoded as bytes)
    float	Double-precision (64-bit) floating-point number (note there is no separate double type)
    bool	A True or False value
    int	Arbitrary precision signed integer
 
- numeric types 
  - primary are **int** and **float**
  - int can store arbitrary large numbers
      In [48]: ival = 17239871

      In [49]: ival ** 6
      Out[49]: 26254519291092456596965462913230729701102721  
  - floats have decimals
  - in division not resulting in whole number will yield float
  - use **//** to drop fractional part if result is not whole number
  
- strings
  - can write string literals using single or double quotes
    a = 'one way of writing a string'
    b = "another way"
  - multiple strings with line breaks use triple quotes
    c = """
    This is a longer string that
    spans multiple lines
    """
  - that actually contains 4 lines. Can count the new line caracters with the count method
    In [55]: c.count('\n')
    Out[55]: 3
  - cannot modify strings
  - can convert objects to string using str function
    In [61]: a = 5.6
    In [62]: s = str(a)
    In [63]: print(s)
    5.6
  - are a sequence of Unicode characters and can be treated like other sequences like tuples and lists.
  In [64]: s = 'python'
  In [65]: list(s)
  Out[65]: ['p', 'y', 't', 'h', 'o', 'n']
  In [66]: s[:3]
  Out[66]: 'pyt'
 - where s[:3] is called slicing 
 - backslash \ is an escape character. Used to soecify characters like newline \n or Unicode characters. Need to escape string with literal backslashes
  In [67]: s = '12\\34'
  In [68]: print(s)
  12\34
- if you need a lot of backslashes you can lead the quoted string with r to make it interpret characters as is
    In [69]: s = r'this\has\no\special\characters'
    In [70]: s
    Out[70]: 'this\\has\\no\\special\\characters'
   - the r stands for raw
- adding two strings together concatenates them and produces new string
    In [71]: a = 'this is the first half '
    In [72]: b = 'and this is the second half'
    In [73]: a + b
    Out[73]: 'this is the first half and this is the second half'
- format method can be used to substitute formated arguments into the string to produce a new string
    In [74]: template = '{0:.2f} {1:s} are worth US${2:d}'
  • {0:.2f} means to format the first argument as a floating-point number with two decimal places.
  • {1:s} means to format the second argument as a string.
  • {2:d} means to format the third argument as an exact integer.
- to substitue arguments, pass sequence of arguments to the format method
    In [75]: template.format(4.5560, 'Argentine Pesos', 1)
    Out[75]: '4.56 Argentine Pesos are worth US$1'

- Bytes and unicode 
  - Unicode used to enable consistent handling of ASCII and non-ASCII text 
  - can sometimes encounter data in different encodings and will have to convert
  
- Booleans
  - comparisons and other conditional expressions evaluate to true or false
  - boolean values combined with and and or keywords
  - Type casting 
    ~ str, bool, int, and float types are functions that can cast values to those types
    In [91]: s = '3.14159'
    In [92]: fval = float(s)
    In [93]: type(fval)
    Out[93]: float
    In [94]: int(fval)
    Out[94]: 3
    In [95]: bool(fval)
    Out[95]: True
    In [96]: bool(0)
    Out[96]: False
  - none is the python null value. If a function does not explicitly retuurn a value it returns none
    In [97]: a = None
    In [98]: a is None
    Out[98]: True
    In [99]: b = 5
    In [100]: b is not None
    Out[100]: True
  - None is also a common default value for function arguments:
    def add_and_maybe_multiply(a, b, c=None):
      result = a + b
      
      if c is not None:
        result = result * c
        
      return result
 
 - dates and times
  - datetime, date, and time types
    - datetime combines data and time and is most commonly used 
      In [102]: from datetime import datetime, date, time
      In [103]: dt = datetime(2011, 10, 29, 20, 30, 21)
      In [104]: dt.day
      Out[104]: 29
      In [105]: dt.minute
      Out[105]: 30
    - can extract equivalent date and time objects by calling methods on the datetime of the same name
      In [107]: dt.time()
      Out[107]: datetime.time(20, 30, 21)
    - lots of other datetime stuff
    
- Control Flow
  - built in keywords for conditional logic, loops, and other standard concepts
  - if, elif, and else
    ~ if checks a condition that, if True, evaluates code that follows
      if x < 0:
        print('It's negative')
      ~ can be followed by elif blocks and a catch all else if all conditions are false
      if x < 0:
        print('It's negative')
      elif x == 0:
        print('Equal to zero')
      elif 0 < x < 5:
        print('Positive but smaller than 5')
      else:
        print('Positive and larger than or equal to 5')
   - if any conditions are True, no further elif or else will be reached 
   - compound conditions using and or or are read left to life and will short circuit
    In [117]: a = 5; b = 7
    In [118]: c = 8; d = 4
    In [119]: if a < b or c > d:
    .....: print('Made it')
    Made it
      - comparison c > d never gets evaluated because the first comparison was True
      - also possible to chain comparisons
        In [120]: 4 > 3 > 2 > 1
        Out[120]: True
    - for loops - iterate over a collection (like list or tuple) or an iterator
        for value in collection:
        ###### do something with value
      ~ can advance a for loop to the next iteration, skipping remainder with the continue keyword
      ~ sums integers in list and skips none values
          sequence = [1, 2, None, 4, None, 5]
          total = 0
          for value in sequence:
            if value is None:
                continue
            total += value
     - for loop can be exited with break keyword
        sequence = [1, 2, 0, 4, 6, 5, 2, 1]
        total_until_5 = 0
        for value in sequence:
          if value == 5:
            break
          total_until_5 += value
      - break only terminates the innermost for loop. Outer will continue
- while loops specify a condition and a block of code that goes until False or ended with break
    x = 256
    total = 0
    while x > 0:
      if total > 500:
        break
      total += x
      x = x // 2
  - pass is the no-op statement. Used in blocks where no action is taken. Required becuause whitespace is a delimeter
    if x < 0:
      print('negative!')
    elif x == 0:
      ###### TODO: put something smart here
      pass
    else:
      print('positive!')
  - range - returns an iterator that yields a sequence of evenly spaced integers
      In [122]: range(10)
      Out[122]: range(0, 10)
      In [123]: list(range(10))
      Out[123]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    -start, end, and step can be given
      In [124]: list(range(0, 20, 2))
      Out[124]: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
      In [125]: list(range(5, 0, -1))
      Out[125]: [5, 4, 3, 2, 1]
    -produces integers up to but not including the endpoint. Commonly used for iterating through sequences by index
      seq = [1, 2, 3, 4]
      for i in range(len(seq)):
        val = seq[i]
    -list can store all the integers generated by range in some other data structure, often the default iterator 
    -sums all numbers from 0 to 99,999 that are multiples of 3 or 5
      sum = 0
      for i in range(100000):
        # % is the modulo operator
        if i % 3 == 0 or i % 5 == 0:
          sum += i
   - ternary expressions - combine if-else block that produces value into single line or expression
    value = true-expr if condition else false-expr
    
    In [126]: x = 5
    In [127]: 'Non-negative' if x >= 0 else 'Negative'
    Out[127]: 'Non-negative'
  - may sacrifice readability if the condition as well as the true and false are complex


# Week 2
## Chapter 3

Tuples
- fixed length immutable sequence of python objects. Should be enclosed in parentheses if more complicated
  tup = 4, 5, 6
  nested_tup = (4, 5, 6), (6, 7)
- can convert any sequence or iterator to tuple by invoking tuple
  tuple([4, 0, 2])
  tup = tuple('string') # will convert to ('s', 't', 'r', 'i', 'n', 'g')
- elements can be accessed with square brackets and are 0 indexed
- objects in stored tuple may be mutable themselves but once tuple is created it is not possible to modify which object is stored in each slot
  tup = tuple(['foo', [1, 2], True])
  tup[2] = False #### gives an error
 - if there is a list in a tuple it can be modified in place
  tup[1].append(3)
  tup 
  (out) ('foo', [1, 2, 3], True)
- can concantenate tuples using the + operator
  (3, None, 'foo') + (6, 0) + ('bar',)
- multiplying tuple by an integer concantinates that many copies of the tuple
  ('foo', 'bar') * 4
  (output) ('foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'bar')
  - the objects themselves are not copied, only the references to them
- if you try to assign to a tuple-like expression of variables, Python tries to uppack the value on the right of the equals
  tup = (4, 5, 6)
  a, b, c = tup
  b 
  (output) 5
- even nested tuples can be unpacked
  tup = 4, 5, (6, 7)
  a, b, (d, d) = tup
  d
  (out) 7
- swap variable names
  a, b, = 1, 2
  a
  (out) 1
  b
  (out) 2
  b, a = a, b
  a 
  (out) 2
  b 
  (out) 1
- common use of variable unpacking is iterating over sequences of tuples or lists
  seq = [(1, 2, 3), )4, 5, 6), (7, 8, 9)]
  for a, b, c in seq:
    print('a={0}, b={1}, c={2}'.format(a, b, c))
- another common use is returning multiple values from a function
- \*rest used to pluck elements from the beginning of a tuple
  values = 1, 2, 3, 4, 5
  a, b, \*rest = values
  a, b
  (out) (1, 2)
  rest
  (out) [3, 4, 5]
- rest is nothing special. Just references things you want to discard. Common convention is to use \*_ for unwanted variables

Tuple methods
- not many methods since contents of a tuple can't be modified
- count is useful. Counts the number of occurances of a value
  a = (1, 2, 2, 2, 3, 4, 2)
  a.count(2)
  (out) 4
  
List
- variable legth and contents can be modified. Define them with [] or *list* type function
  a_list = [2, 3, 7, None]
  tup = ('foo', 'bar', 'baz')
  b_list = list(tup)
  b_list
  b_list[1] = 'peekaboo'
 - symantically similar to tuples and can be used interchangably in many functions
 - *list* function common in data processing to materialize an iterator or generator expression
  gen = range(10)
  gen
  list(gen)
  
 Adding and removing elements
 - append method
  b_list.append('dwarf')
  b_list
 - insert at specific location
  b_list.insert(1, 'red')
  b_list
- pop to remove
  b_list.pop(2)
  b_list
- remove locates first matching value and removes
    b_list.append('foo')
    b_list
    b_list.remove('foo')
    b_list
 - check if list contains a value using *in*
  'dwarf' in b_list
- *not* to negate *in*
  'dwarf' not in b_list

Concantenating and combining lists
- similar to tuples
- append multiple elements to list using *extend*
  x = [4, None, 'foo']
  x.extend([7, 8, (2, 3)])
  x
- better to use extend than concantenating b/c less operationally expensive
  everything = []
  for chunk in list_of_lists
    everything.extend(chunk)
  
Sorting
- sort list without creating new object 
  a = [7, 2, 5, 1, 3]
  a.sort()
  a
- secondary sort key (value used to sort)
  b = ['saw', 'small', 'He', 'foxes', 'six']
  b.sort(key=len)
  b
  
  Binary search and maintaining a sorted list
  - *bisect* implements binary search and insertion into a sorted list
  - bisect.bisect finds location where elements should be inserted to keep it sorted
  - bisect.insort inserts element into that location
    import bisect
    c = [1, 2, 2, 2, 3, 4, 7]
    bisect.bisect(c, 2)
    bisect.bisect(c, 5)
    bisect.insort(c, 6)
    c
  - doesn't check if sorted first. Can use on unsorted list but might have incorrect results
  
  Slicing
  - start:stop passed to the indexing operator []
    seq = 7, 2, 3, 7, 5, 6, 0, 1]
    seq[1:5]
  - slices can be assigned to with a sequence
    seq[3:4] = [6:3]
    seq
  - start or stop could be omitted and it defaults to either beginning or end respectively
    seq[:5[
    seq[3:]
  - negative indices slice from end
    seq[-4:]
  - step can be used after a second colon 
    seq[::2]
  - using -1 as the step reverses the list or tuple
  
  Built-In Sequence Functions
  
  enumerate
 - keep track of iterations
   t = 0
   for value in collection:
   i += 1
 - python has a built in version for this
   for i, value in enumerate(collection:
 - helpful patter that uses enumerate is computing a dict mapping the values of a sequence to their locations in the sequence
   some_list = ['foo', 'bar', 'baz']
   mapping = {}
   for i, v in enumerate(some_list):
    mapping[v] = i
    mapping

sorted
- returns a new sorted list from the elements of any sequence
  sorted([7, 1, 2, 6, 0, 3, 2])
  sorted('horse race')

zip
- pairs up the elements of a number of lists, tuples, or other sequence to create a list of tuples
  seq1 = ['foo', 'bar', 'baz']
  seq2 = ['one', 'two', 'three']
  zipped = zip(seq1, seq2)
  list(zipped)
- can take arbitrary number of sequences, and the number of elements it produces is determined by the shortest sequence
  seq3 = [False, True]
  list(zip(seq1, seq2, seq3))
- common use os simultaneously iterating over multiple sequences, possibly combined with enumerate
  for i, (a, b) in enumerate(zip(seq1, seq2)):
    print('{0}: {1}, {2}'.format(i, a, b))
- given a zipped sequence, zip can unzip. Convert a list of rows to a list of columns
  pitchers = [('Nolan', 'Ryan'), {'Roger', 'Clemens'), ('Schilling', 'Curt')]
  first_names, last_names = zip(*\pitchers)
  first_names
  last_names
  
reversed
- iterates over sequence in reverse
  list(reversed(range(10)))
- is a generator so doesn't create reversed sequence until materialized

dict
- likely the most important built in data structure
- flexibly sized collection of key-value pairs, where *key* and *value* are Python objects
  empty_dict = {}
  d1 = {'a' : 'some value', 'b' : [1, 2, 3, 4]}
- can access, insert, or set elements using the same syntax as for accessing elements of a list or tuple
  d1[7] = 'an integer'
  d1
  d1['b']
- can check if a dict contains a key using the same syntax for checking whether a list or tuple contains a value
  'b' in d1
- delete with del keyword or the pop method
  d1[5] = 'some value'
  d1
  d1['dummy'] = 'another value'
  d1
  del d1[5]
  d1
  ret = d1.pop('dummy')
  ret
  d1
- gives iterators of the dict's keys and values respectively
  list(d1.keys())
- can merge one dict into another using update
  d1.update({'b' : 'foo', 'c' : 12})
  d1
-changes dicts in place s oany existing keys in the data passed to update will have their old values discarded

creating dicts from sequences
-sometimes have two sequences you wan to pair up element-wise in a dict
  mapping = {}
  for key, value in zip(key_list, value_list):
    mappying[key] = value
  since a dict is a collection of 2 tuples, the dict accepts a list of 2 tuples
    mapping = dict(zip(range(5), reversed(range(5))))
    mapping
    
default values
- common to have logic like this
  if key in some_dict:
    value = some_dict[key]
  else:
    value = default_value
- dict methods*get* and *pop* can take a default value to be returned so that the above can be written as
  value = some_dict.get(key, default_value)
- *get* by default will return None if key not present, while *pop* will raise an exception
- with setting values, a common case is for th evalues in a dict to be other collections, like list
- categorize a list of words by their first letters as a dict of lists
  words = ['apple', 'bat', 'bar', 'atom', 'book']
  by_letter = {}
  for word in words:
    letter = word[]
    if letter not in by_letter:
      by_letter[letter] = [word]
    else:
      by_letter[letter].append(word)
  by_letter
- *setdefault* dict method is used for this purpose. The above loop can be
  for word in words:
    letter = word[0]
    by_letter.setdefault(letter, []).append(word)
- built in collections module has *defaultdict* which makes it even easier. TO create, pass a type or function for generating the default value for each slot in the dict:
  from collections import defaultdict
  by_letter = defaultdict(list)
  for word in words:
    by_letter[word[0]].append(word)
    
  valid dict key types
  - values can generally be any python object
  - keys have to be immutable objects, like scalar types (int, float, string) or tuples
  - technical term is hashability
  - use hash function to check 
    hash('string')
  - need to convert list to tuple if want to use as a key
  
  set
  - unordered collection of unique elements
  - like a dict with only keys and no values
  - created with set function or set literal with curly braces
    set([2, 2, 2, 1, 3, 3])
    or
    {2, 2, 2, 1, 3, 3}
  - support mathematical set operations like union, intersection, differencce, and symmetric difference
    a = {1, 2, 3, 4, 5}
    b = {3, 4, 5, 6, 7, 8}
  - the union of the 2 sets is the set of distinct ememnts in either set. Computed with the union method or the | binary operator
    a.union(b)
    a | b
  - intersection contains the elements occurring in both sets
    a.intersection(b)
    a & b
  - all logical set operations have in-place counterparts which enable you to replace the contents of the set ont he self with the result
    c = a.copy()
    c |= b
    c
    d = a.copy()
    d &= b
  - like dicts, set elements generally must be immutable. Need to convert to tuple
    my_data = [1, 2, 3, 4]
    my_set = {tuple(my_data)}
    my_set
  - can check if set is a subset or superset of another set
    a_set = {1, 2, 3, 4, 5}
    {1, 2, 3}.issubnet(a_set)
    a_set.issuperset({1, 2, 3})
  - sets are equal if their contents are equal
    {1, 2, 3,} == {3, 2, 1}
    
list, set, and dict comprehensions
- list comprehensions are one of the most loved python features. Allow you to concisely form new list by filtering elements of a collection, transforming the elements passing the filter in one concise expression
  [expr for val in collection if condition]
- equivalent to the for loop
  result = []
  for val in collection:
    if condition:
      result.append(expr)
- filter condition can be omitted leaving only the expression. Given a list of strings, we could filter out strings with length 2 or less and convert them to uppercase
  strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
  [x.upper() for x in strings if len(x) >2]
- set and dict comprehensions are a natural extension, producing sets and dicts in an idiomatically similar way instead of lists
  dict_comp = {key-expr : value-expr for valuue in collection if condition}
- set comprehension looks like the equivalent list comprehension but with curlies
  set_comp = {expr for value in collection if condition}
- set and dict are mostly conveniences but can make code easier to write and read
- set with jsut lengths of strings in collection
  unique_lengths = {len(x) for x in strings}
  unique_lengths
- express mroe functionally with map function
  set(map(len, strings))
- create lookip map of strings to locations in list
  loc_mapping = {val : index for index, val in enumerate(strings)}
  
Nested list comprehensions
- organize by lanfuafe and make single list with all names wit 2 or more e's
  result = [name for names in all_data for name in names
            if name.count('e') >= 2]
- the got parts of the list comprehension are arranged according to the order of nesting, and any filter condition is put at the end as before
- "flatten" a list of tuples of integers into a simple lisst of integers
  some_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
  flattened = [x for tup in some_tuples for x in tup]
- the order of th efor expressions would be the same if you wrote a nested for loop instead of list comprehension
  flattened = []
  for tup in some_tuples:
    for x in tup:
      flattened.appennd(x)
- list comprehension inside a list comprehension
  [[x for x in tup] for tup in some_tuples]
  
Functions
- primary and most important method of code organization and reuse in python
- if you anticipate the need to repeat the same or similar code, make a function
- help make code more readable by giving a name to group of python statements
- declared with the def keyword and returned with return keyword
  def my_function(x, y, z=1.5):
    if z >1:
      return z * (x + y)
    else:
      return z / (x + y)
- no issue with having multiple return statements. If no return, None is returned
- each function can have positional and keyword arguments
- keyword used to specify default values or optional arguments
- x and y are positional arguments whil ez is a keyword argument. Function can be called in any of these ways:
  my_function(5, 6, z=0.7)
  my_function(3.14, 7, 3.5)
  my_function(10, 20)
- keyword arguments must follow the positional arguments but can specify keyword arguments in any order
- possible to use keywords for passing positional arguments as well
  my_function(x=5, y=6, z=7)
  my_function(y=6, x=5, z=7)
  
Namespaces, scope, and local functions
- global and local scopes (also refered to as a namespace)
- variables inside function are local. Local namespace created when function is called and immediate populated by functions arguments. When finished, local namespace is destroyed
  def func():
    a = []
    for i in range(5):
      a.append(i)
    - when func() is called, the empty list a is created, 5 elements are appended, and then a is destroyed when function exits
  a = []
   def func():
    for i in range():
      a.append(i)
- assigning variables outside function's scope is possible but hey must be decared with global keyword
  a = None
  def bind_a_variable():
    global a 
    a = []
  bind_a_variable()
  print(a)
- better to use classes instead of a lot of global variables

Returning multiple values
  def f():
    a = 5
    b = 6
    c = 7
    return a, b, c
  a, b, c = f()
- function is returning one object (a tuple) which is unpacked into the result variables. Could do this instead
  return_value = f()
- return_value would be a 3-tuple witht the three returned variables. Could also use a dict
  def f():
    a = 5
    b = 6
    c = 7
    return {'a' : a, 'b' : b, 'c' : c}

Functions are objects
- suppose need to do data cleaning and apply a bunch of transformations to list of strings
  In [171]: states = [' Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda',
.....: 'south carolina##', 'West virginia?']
- need to remove white space, punctuation symbols, standardize capitalization
- can use built-in string methods with the re standard library module for regular expressions
  import re
  def clean_strings(strings):
    result = []
    for value in strings:
      value = value.strip()
      value = re.sub('[!#?]', '', value)
      value = value.title()
      result.append(value)
    return result
  clean_strings(states)
- alternative approach is to make a list of operations you want to apply
  def remove_punctuation(value):
    return re.sub('[!#?]', '', value)
  clean_ops = [str.strip, remove_punctuation, str.title]
  def clean_strings(strings, ops)
    result = []
    for value in strings
      for function in ops:
        value = function(value)
      result.append(value)
    return result
  clean_strings(states, clean_ops)
- this is more functional and allows you to easily modify how the strings are transformed
- can use functions as arguments to other functions
  for x in map(remove_puntuation, states):
    print(x)

Anonymous (Lambda) Functions
- writing functions consisting of a single statement where result is return value
  def short_function(x):
    return x * 2
  equiv_anon = lambda x: x * 2
- convenient in data analysis where data transformation functions will take functions as arguments
- less typing and clearer to pass lambda instead of writing full funtion declaring or assigning lambda function to a local variable

Currying: Partial Argument Application
- currying means deriving new functions from existing ones by partial argument application
  def add_numbers(x, y):
    return x + y
- derive new function of one variable, add_five that adds 5 to argument
  add_five = lambda y: add_numbers(5, y)
- second argument to add_numbers is said to be curried
- built in functools module simplifies process
  from functools import partial
  add_five = partial(add_numbers, 5)
  
Generators 
- iterator protocol iterates over sequences
  some_dict = {'a': 1, 'b': 2, 'c': 3}
  for key in some_dict:
    print(key)
- python interpreter first attempts to create iterator out of some_dict
  dict_iterator = iter(some_dict)
  dict_iterator
- iterator is any object that will yield objects to the interpreter when used in a context like a for loop
- most methods expecting a list or list-like object will also accept any iterable object
  - min, max, and sum, and type constructors like list or tuple
    list(dict_iterator)
- generator is concise way to construct new iterable object
- generators return a dequence of multiple results, pausing after each until next is requested
  def squares(n=10):
    print('generating squares from 1 to {0}'.format(n **2))
    for i in range(1, n + 1):
      yield i ** 2
- when you call, no code is immediately executed:
  gen = squares()
  gen
- not until you request elements from the generator
  for x in gen:
    print(x, end=' ')
    
Generator expressions
- a more concise way to make generator is generator expressions
  gen = (x ** 2 for x in range(100))
  gen
- equivalent of this:
  def _make_gen():
    for x in range(100):
      yield x ** 2
  gen = _make_gen()
- generator expressions can be used instead of list comprehensions as function arguments
  sum(x ** 2 for x in range(100))
  dict((i, i **2) for i in range(5))
  
itertools module
- collection of generators for common data algorithms
- groupby takes any sequence and a function, grouping consecutive elements in the sequence by retun value of the function
  import itertools
  first_letter = lambda x: x[]
  names = ['Allen', 'Adam', 'Wes', 'Will', 'Albert', 'Steven']
  for letter, names in itertools,groupby(names, first_letter)"
    print(letter, list(names)) 
    - names is a generator
   
Errors and exception handling
- some functions only work with certain input
- ways to fail gracefully
  def attempt_float(x):
    try:
      return float(x)
    except:
      return x
- the code in except will only be executed if float(x) raises an exception
  attempt_float('1.2345')
  attempt_float('something')
- might want to only supress ValueError, since TypeError might indicate a program bug)
  def attempt_float(x):
    try:
      return float(x)
    except ValueError:
      return x
- catch multiple exception types
  def attempt_float(x):
    try:
      return float(x)
    except (TypeError, ValueError):
      return x
- might not want to suppress an exception, but want some code to execute regardless
  f = open(path, 'w')
  try:
    write_to_file(f)
  finally:
    f.close()
- file handle f will always get closed
- can have code that executes only if the try block succeeds using else
  f = open(path, 'w')
  try:
    write_to_file(f)
  except:
    print('Failed')
  else:
    print('Succeeded')
  finally:
    f.close()
    
Exceptions in IPython
- if an exception is raised while running script or executing any statement, IPython prints full call stack trace (gives context)

Files and Operating System
- to open file for reading or writing
  path = 'examples/segismundo.txt'
  f = open(path)
- default opens in read only. Can then treat file handle like list and iterate over lines
  for line in f:
    pass
- lines come out of file with EOL marker so use code to clean
  lines = [x.rstrip() for x in open(path)]
  lines
- when use open to create file objects, must explicitly close when done
  f.close()
- use with statement to clean open files
  with open(path) as f:
    lines = [x.rstrip() for x in f]
- most common methods for readable files
  read, seek, tell
    - read returns certain number of characters from file
    - tell gives you current position
    - seek changes file position to indicated byte
    f = open(path)
    f.read(10)
    f.tell()
    f.seek(3)
- to write to a file
  with open('tmp.txt', 'w') as handle:
    handle.writelines(x for x in open(path) if len(x) >1)
  with open('tmp.txt') as f:
    lines = f.readlines()
  lines

your_name = input("What is your name?")
print("Hello ", your_name)



# CH 4 NumPy Basics: Arrays and vectorized computation

For most data analysis applications, the main areas of functionality I’ll focus on are:

- Fast vectorized array operations for data munging and cleaning, subsetting and filtering, transformation, and any other kinds of computations
- Common array algorithms like sorting, unique, and set operations
- Efficient descriptive statistics and aggregating/summarizing data
- Data alignment and relational data manipulations for merging and joining together heterogeneous datasets
- Expressing conditional logic as array expressions instead of loops with if-elif-else branches
- Group-wise data manipulations (aggregation, transformation, function application)
- designed for efficiency on large data arrays
  - internally stores data in a contiguous block of memory
  - use less memory than built in python sequences
- numpy ops perform complex computations on entire arrays without the need for Python for loops

Numpy ndarray: A multidimensional array object
- ndarray is a fast, flexible contaner for large datasets
- allow you to perform math ops on whole blocks of data using similar sintax to the equivalent operations between scalar elements

  In [12]: import numpy as np
  Generate some random data
  In [13]: data = np.random.randn(2, 3)
  In [14]: data
  Out[14]: 
  array([[-0.2047,  0.4789, -0.5194],
       [-0.5557,  1.9658,  1.3934]])
  In [15]: data * 10
  In [16]: data + data
  
- ndarray is a generic multidimensional container for homogeneous data
  - all of the elements must be the same type
- every array has a shape, a tuple indicating the size of each dimension, and a dtype, an object describing the data type of the array
  data.dtype
  data.shape
- easiest way to create an array is the array function
  - accepts any sequence like object and produces a new NumPy array containing the passed data
  In [19]: data1 = [6, 7.5, 8, 0, 1]
  In [20]: arr1 = np.array(data1)
  In [21]: arr1
  Out[21]: array([6. , 7.5, 8. , 0. , 1. ])
- nested sequences will be converted into a multidimensional array
  In [22]: data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
  In [23]: arr2 = np.array(data2)
  In [24]: arr2
  Out[24]: 
  array([[1, 2, 3, 4],
         [5, 6, 7, 8]])
  - data 2 was a list of lists, the Numpy array arr2 has 2 dimensions with shape inferred from the data
  - can confirm by inspecting the ndim and shape attributes
    arr2.ndim
    arr2.shape
- np.array tries to infer a good data type for the array it creates. Datatype is stored in the dtype metadata object
  In [27]: arr1.dtype
  Out[27]: dtype('float64')
  In [28]: arr2.dtype
  Out[28]: dtype('int64')
- *zeros* and *ones* create arrays of 0s and 1s with a given length or shape
- *empty* creates an array without initializing its values to any particular value
- to create a higher dimensional array with these methods, pass a tuple for the shape
  In [29]: np.zeros(10)
  Out[29]: array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
  In [30]: np.zeros((3, 6))
  Out[30]: 
  array([[0., 0., 0., 0., 0., 0.],
         [0., 0., 0., 0., 0., 0.],
         [0., 0., 0., 0., 0., 0.]])
  In [31]: np.empty((2, 3, 2))
  Out[31]: 
  array([[[0., 0.],
         [0., 0.],
         [0., 0.]],
        [[0., 0.],
         [0., 0.],
          [0., 0.]]])
- np.empty might return uninitialized garbage values instead of 1s
- *arrange* is an array-valued version of the built-in Python range function
  np.arange(15)
- data type if not specified will usually be float64
- array creation functions
  - array	Convert input data (list, tuple, array, or other sequence type) to an ndarray either by inferring a dtype or explicitly specifying a dtype; copies the input data by default
  - asarray	Convert input to ndarray, but do not copy if the input is already an ndarray
  - arange	Like the built-in range but returns an ndarray instead of a list
  - ones, ones_like	Produce an array of all 1s with the given shape and dtype; ones_like takes another array and produces a ones array of the same shape and dtype
  - zeros, zeros_like	Like ones and ones_like but producing arrays of 0s instead
  - empty, empty_like	Create new arrays by allocating new memory, but do not populate with any values like ones and zeros
  - full, full_like	Produce an array of the given shape and dtype with all values set to the indicated “fill value” full_like takes another array and produces a filled array of the same shape and dtype
  - eye, identity	Create a square N × N identity matrix (1s on the diagonal and 0s elsewhere) 
  
Data types for ndarrays
- dtype is a special object containing metadata 
  In [33]: arr1 = np.array([1, 2, 3], dtype=np.float64)
  In [34]: arr2 = np.array([1, 2, 3], dtype=np.int32)
  In [35]: arr1.dtype
  Out[35]: dtype('float64')
  In [36]: arr2.dtype
  Out[36]: dtype('int32') 
- dtypes are a source of Numpy's flexibility for interacting with data coming from other systems
- in most cases they provide a mapping directly onto an underlying disk or memory representation
- cast float to int dtype
  In [41]: arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
  In [42]: arr
  Out[42]: array([ 3.7, -1.2, -2.6,  0.5, 12.9, 10.1])
  In [43]: arr.astype(np.int32)
  Out[43]: array([ 3, -1, -2,  0, 12, 10], dtype=int32)
- astype - array of strings representing numbers converted to numeric
  In [44]: numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
  In [45]: numeric_strings.astype(float)
  Out[45]: array([ 1.25, -9.6 , 42.  ])
- numpy.string_type may truncate input without warning b/c string data is fixed sized in NumPy. Use panda
- can also use another's array dtype attribute
  In [46]: int_array = np.arange(10)
  In [47]: calibers = np.array([.22, .270, .357, .380, .44, .50], dtype=np.float64)
  In [48]: int_array.astype(calibers.dtype)
  Out[48]: array([0., 1., 2., 3., 4., 5., 6., 7., 8., 9.])
- shorthand type code strings you can use to refer to a dtype
  In [49]: empty_uint32 = np.empty(8, dtype='u4')
  In [50]: empty_uint32
  Out[50]: 
  array([         0, 1075314688,          0, 1075707904,          0,
         1075838976,          0, 1072693248], dtype=uint32)
- calling astype always creates a new array, even if the new dtype is the same as the old dtype

Arithmetic with NumPy arrays
- arrays enable you to express batch operations on data without writing for loops
- called vectorization
- any arithmetic operations between equal-size arrays applies th eoperation element-wise
  In [51]: arr = np.array([[1., 2., 3.], [4., 5., 6.]])
  In [52]: arr
  Out[52]: 
  array([[1., 2., 3.],
        [4., 5., 6.]])
  In [53]: arr * arr
  Out[53]: 
  array([[ 1.,  4.,  9.],
        [16., 25., 36.]])
  In [54]: arr - arr
  Out[54]: 
  array([[0., 0., 0.],
        [0., 0., 0.]])
- arithmetic operations with scalars propagate the scalar argument to each element in the array
  In [55]: 1 / arr
  Out[55]: 
  array([[1.    , 0.5   , 0.3333],
        [0.25  , 0.2   , 0.1667]])
  In [56]: arr ** 0.5
  Out[56]: 
  array([[1.    , 1.4142, 1.7321],
        [2.    , 2.2361, 2.4495]])
- comparisons between arrays of the same size yield boolean arrays
  In [57]: arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
  In [58]: arr2
  Out[58]: 
  array([[ 0.,  4.,  1.],
        [ 7.,  2., 12.]])
  In [59]: arr2 > arr
  Out[59]: 
  array([[False,  True, False],
        [ True, False,  True]])
- evaluating operations between different sized arrays is called broadcasting

Basic indexing and slicing
- one-dimensional arrays
  In [60]: arr = np.arange(10)
  In [61]: arr
  Out[61]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
  In [62]: arr[5]
  Out[62]: 5
  In [63]: arr[5:8]
  Out[63]: array([5, 6, 7])
  In [64]: arr[5:8] = 12
  In [65]: arr
  Out[65]: array([ 0,  1,  2,  3,  4, 12, 12, 12,  8,  9])
- if you assign a scalar value to a slice (ar[5:9] = 12) the value is propagated (or broadcasted) to the entire selection
- data is not copied. Any modifications to the view will be reflected in the source array
  In [66]: arr_slice = arr[5:8]
  In [67]: arr_slice
  Out[67]: array([12, 12, 12])
  In [68]: arr_slice[1] = 12345
  In [69]: arr
  Out[69]: 
  array([    0,     1,     2,     3,     4,    12, 12345,    12,     8,
             9])
  In [70]: arr_slice[:] = 64
  In [71]: arr
  Out[71]: array([ 0,  1,  2,  3,  4, 64, 64, 64,  8,  9])
- two dimensional array, the elements at each index are no longer scalars, but one dimensional arrays
  In [72]: arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
  In [73]: arr2d[2]
  Out[73]: array([7, 8, 9])
- individual elements can be accessed recursively
- can pass a comma separated list of indices to select individual elements
- these are equivalent:
  In [74]: arr2d[0][2]
  Out[74]: 3
  In [75]: arr2d[0, 2]
  Out[75]: 3
- if you omit later indices, the returned object will be a lower dimensional ndarray consisting of all the data along the higher dimensions
- tx2x3 array arr3d
  In [76]: arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
  In [77]: arr3d
  Out[77]: 
  array([[[ 1,  2,  3],
          [ 4,  5,  6]],
        [[ 7,  8,  9],
          [10, 11, 12]]])
- arr3d[0] is a 2x3 array
  In [78]: arr3d[0]
  Out[78]: 
  array([[1, 2, 3],
        [4, 5, 6]])
- both scalar values and arraus can be assigned to arr3d[0]
  In [79]: old_values = arr3d[0].copy()
  In [80]: arr3d[0] = 42
  In [81]: arr3d
  Out[81]: 
  array([[[42, 42, 42],
          [42, 42, 42]],
        [[ 7,  8,  9],
          [10, 11, 12]]])
  In [82]: arr3d[0] = old_values
  In [83]: arr3d
  Out[83]: 
  array([[[ 1,  2,  3],
          [ 4,  5,  6]],
        [[ 7,  8,  9],
          [10, 11, 12]]])
- arr3d1[1, 0] fives all the values whose indices start with (1, 0), forming a 1 dimensional array
  In [84]: arr3d[1, 0]
  Out[84]: array([7, 8, 9])
- this expression is the same as though we had indexed in two steps
  In [85]: x = arr3d[1]

  In [86]: x
  Out[86]: 
  array([[ 7,  8,  9],
        [10, 11, 12]])

  In [87]: x[0]
  Out[87]: array([7, 8, 9])

Indexing with slices
- like one dimensional objects (lists), ndarrays can be sliced
  In [88]: arr
  Out[88]: array([ 0,  1,  2,  3,  4, 64, 64, 64,  8,  9])
  In [89]: arr[1:6]
  Out[89]: array([ 1,  2,  3,  4, 64])
- twp dimensional arrays
  In [90]: arr2d
  Out[90]: 
  array([[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]])

  In [91]: arr2d[:2]
  Out[91]: 
  array([[1, 2, 3],
        [4, 5, 6]])
- sliced alone axis 0. A slice selects a range of elements along an axis
- arr2d[:] reads as "select the first two rows of arr2d"
- can pass multiple slices like indexes
  In [92]: arr2d[:2, 1:]
  Out[92]: 
  array([[2, 3],
        [5, 6]])
- always obtain array views of the same number dimensions. By mixing intefer indexes and slices, you get lower dimensional slices
- select second row, first 2 columns
  In [93]: arr2d[1, :2]
  Out[93]: array([4, 5]) 
- third column, first two rows
  In [94]: arr2d[:2, 2]
  Out[94]: array([3, 6])
- a colon by itself means take the entire axis, so you can only slice higher dimensional axes by doing
  In [95]: arr2d[:, :1]
  Out[95]: 
  array([[1],
        [4],
        [7]])
- assigning to a slice expression assigns to the whole selection         
- In [96]: arr2d[:2, 1:] = 0
  In [97]: arr2d
  Out[97]: 
  array([[1, 0, 0],
         [4, 0, 0],
        [7, 8, 9]]) 
Boolean Indexing
  In [98]: names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
  In [99]: data = np.random.randn(7, 4)
  In [100]: names
  Out[100]: array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'], dtype='<U4')
  In [101]: data
  Out[101]: 
  array([[ 0.0929,  0.2817,  0.769 ,  1.2464],
        [ 1.0072, -1.2962,  0.275 ,  0.2289],
        [ 1.3529,  0.8864, -2.0016, -0.3718],
        [ 1.669 , -0.4386, -0.5397,  0.477 ],
        [ 3.2489, -1.0212, -0.5771,  0.1241],
        [ 0.3026,  0.5238,  0.0009,  1.3438],
        [-0.7135, -0.8312, -2.3702, -1.8608]])
- use randn function in numpy.random to generate random normally distributed data
- array of names with duplicates, array of some data
- suppose each name corresponds to a row in the data array and you want to select all the rows corresponding to Bob
- comparisons with arrays are vectorized
- comparing names with the string 'Bob' yield boolean array
  In [102]: names == 'Bob'
  Out[102]: array([ True, False, False,  True, False, False, False])
- this boolean array can be passed when indexing the array
  In [103]: data[names == 'Bob']
  Out[103]: 
  array([[ 0.0929,  0.2817,  0.769 ,  1.2464],
        [ 1.669 , -0.4386, -0.5397,  0.477 ]])
- the boolean array must be of the same length as the array axis it's indexing
- can mix and match boolean arrays with slices or integers
- select from rows where names == 'bob' and index columns
  In [104]: data[names == 'Bob', 2:]
  Out[104]: 
  array([[ 0.769 ,  1.2464],
        [-0.5397,  0.477 ]])
  In [105]: data[names == 'Bob', 3]
  Out[105]: array([1.2464, 0.477 ])
- To select everything but 'Bob', can use != or negate the condition using ~
  In [106]: names != 'Bob'
  Out[106]: array([False,  True,  True, False,  True,  True,  True])
  In [107]: data[~(names == 'Bob')]
  Out[107]: 
  array([[ 1.0072, -1.2962,  0.275 ,  0.2289],
        [ 1.3529,  0.8864, -2.0016, -0.3718],
         [ 3.2489, -1.0212, -0.5771,  0.1241],
         [ 0.3026,  0.5238,  0.0009,  1.3438],
         [-0.7135, -0.8312, -2.3702, -1.8608]])
- ~ operator can be useful when you want to invert a general condition
  In [108]: cond = names == 'Bob'
  In [109]: data[~cond]
  Out[109]: 
  array([[ 1.0072, -1.2962,  0.275 ,  0.2289],
        [ 1.3529,  0.8864, -2.0016, -0.3718],
        [ 3.2489, -1.0212, -0.5771,  0.1241],
        [ 0.3026,  0.5238,  0.0009,  1.3438],
        [-0.7135, -0.8312, -2.3702, -1.8608]])
- selecting two of the three names to combine multiple conditions, use boolean arithmentic operators like & and |
  In [110]: mask = (names == 'Bob') | (names == 'Will')
  In [111]: mask
  Out[111]: array([ True, False,  True,  True,  True, False, False])
  In [112]: data[mask]
  Out[112]: 
  array([[ 0.0929,  0.2817,  0.769 ,  1.2464],
        [ 1.3529,  0.8864, -2.0016, -0.3718],
        [ 1.669 , -0.4386, -0.5397,  0.477 ],
        [ 3.2489, -1.0212, -0.5771,  0.1241]])
- selecting data from an array by boolean indexing always creates copy of data, even if returned array is unchanged
- set all negative values of data to 0 
  In [113]: data[data < 0] = 0
  In [114]: data
  Out[114]: 
  array([[0.0929, 0.2817, 0.769 , 1.2464],
        [1.0072, 0.    , 0.275 , 0.2289],
        [1.3529, 0.8864, 0.    , 0.    ],
        [1.669 , 0.    , 0.    , 0.477 ],
        [3.2489, 0.    , 0.    , 0.1241],
        [0.3026, 0.5238, 0.0009, 1.3438],
        [0.    , 0.    , 0.    , 0.    ]])
- set whole rows or columns using one dimensional boolean array
  In [115]: data[names != 'Joe'] = 7
  In [116]: data
  Out[116]: 
  array([[7.    , 7.    , 7.    , 7.    ],
        [1.0072, 0.    , 0.275 , 0.2289],
         [7.    , 7.    , 7.    , 7.    ],
        [7.    , 7.    , 7.    , 7.    ],
        [7.    , 7.    , 7.    , 7.    ],
        [0.3026, 0.5238, 0.0009, 1.3438],
        [0.    , 0.    , 0.    , 0.    ]])

Fancy Indexing
- describes indexing using integer arrays
- suppose we had an 8x4 array
  In [117]: arr = np.empty((8, 4))
  In [118]: for i in range(8):
    .....:     arr[i] = i
  In [119]: arr
  Out[119]: 
  array([[0., 0., 0., 0.],
         [1., 1., 1., 1.],
        [2., 2., 2., 2.],
        [3., 3., 3., 3.],
        [4., 4., 4., 4.],
        [5., 5., 5., 5.],
        [6., 6., 6., 6.],
        [7., 7., 7., 7.]])
- to select a subset of rows in a particular order, pass a list or ndarray of integers specifying the desired order 
  In [120]: arr[[4, 3, 0, 6]]
  Out[120]: 
  array([[4., 4., 4., 4.],
        [3., 3., 3., 3.],
        [0., 0., 0., 0.],
        [6., 6., 6., 6.]]) 
- using negative indices selects rows from the end
  In [121]: arr[[-3, -5, -7]]
  Out[121]: 
  array([[5., 5., 5., 5.],
        [3., 3., 3., 3.],
        [1., 1., 1., 1.]])
- passing multiple index arrays selects a one dimensional array of elements correspinding to each tuple of indices 
  In [122]: arr = np.arange(32).reshape((8, 4))
  In [123]: arr
  Out[123]: 
  array([[ 0,  1,  2,  3],
        [ 4,  5,  6,  7],
        [ 8,  9, 10, 11],
        [12, 13, 14, 15],
        [16, 17, 18, 19],
        [20, 21, 22, 23],
        [24, 25, 26, 27],
        [28, 29, 30, 31]])
  In [124]: arr[[1, 5, 7, 2], [0, 3, 1, 2]]
  Out[124]: array([ 4, 23, 29, 10])
- here the elements (1, 0), (5, 3), (7, 1) and (2, 2) were selected
- regardless o fhow many dimensions the array has, the result of fancy indexing with multiple integer arrays is always one-dimensional
- rectangular region formed by selecting a subset of the matrix's rows and columns:
  In [125]: arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]]
  Out[125]: 
  array([[ 4,  7,  5,  6],
         [20, 23, 21, 22],
        [28, 31, 29, 30],
        [ 8, 11,  9, 10]])
- fancy indexing always copies the data into a new array 

Transposing Arrays and swapping axes
- transposing is a special form of reshaping that retuns a view on the underlying data without copying
- arrays have the transpose method and the special T attribute
  In [126]: arr = np.arange(15).reshape((3, 5))
  In [127]: arr
  Out[127]: 
  array([[ 0,  1,  2,  3,  4],
        [ 5,  6,  7,  8,  9],
        [10, 11, 12, 13, 14]])
  In [128]: arr.T
  Out[128]: 
  array([[ 0,  5, 10],
        [ 1,  6, 11],
        [ 2,  7, 12],
        [ 3,  8, 13],
        [ 4,  9, 14]])
- may do this when computing the inner matrix product using np.dot
  In [129]: arr = np.random.randn(6, 3)
  In [130]: arr
  Out[130]: 
  array([[-0.8608,  0.5601, -1.2659],
        [ 0.1198, -1.0635,  0.3329],
        [-2.3594, -0.1995, -1.542 ],
        [-0.9707, -1.307 ,  0.2863],
        [ 0.378 , -0.7539,  0.3313],
        [ 1.3497,  0.0699,  0.2467]])
  In [131]: np.dot(arr.T, arr)
  Out[131]: 
  array([[ 9.2291,  0.9394,  4.948 ],
        [ 0.9394,  3.7662, -1.3622],
        [ 4.948 , -1.3622,  4.3437]])
- for higher dimensional arrays, transpose will accept a tuple of axis numbers to permute the axes
  In [132]: arr = np.arange(16).reshape((2, 2, 4))
  In [133]: arr
  Out[133]: 
  array([[[ 0,  1,  2,  3],
          [ 4,  5,  6,  7]],
        [[ 8,  9, 10, 11],
          [12, 13, 14, 15]]])
  In [134]: arr.transpose((1, 0, 2))
  Out[134]: 
  array([[[ 0,  1,  2,  3],
          [ 8,  9, 10, 11]],
        [[ 4,  5,  6,  7],
          [12, 13, 14, 15]]])
- the axes have been reprdered with the second axis first, the first axis second, and the last unchanged
- transposing with.T is a special case of swapping axes. ndarray has the method swapaxes which takes a pair of axis numbers and switches the indicated axes to rearrange the data
  In [135]: arr
  Out[135]: 
  array([[[ 0,  1,  2,  3],
          [ 4,  5,  6,  7]],
        [[ 8,  9, 10, 11],
          [12, 13, 14, 15]]])

  In [136]: arr.swapaxes(1, 2)
  Out[136]: 
  array([[[ 0,  4],
          [ 1,  5],
          [ 2,  6],
          [ 3,  7]],
         [[ 8, 12],
          [ 9, 13],
          [10, 14],
          [11, 15]]])
- swapexes similarily returns a view on the data without making a copy 

Universal Functions: Fast element-wise Array Functions
- universal functions (ufunc) are functions that perform element-wise operations on data in ndarrays
- like fast vectorized wrappers for simple functions that take one or more scalar values and produce one or more scalar results
- sqrt or exp
  In [137]: arr = np.arange(10)
  In [138]: arr
  Out[138]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
  In [139]: np.sqrt(arr)
  Out[139]: 
  array([0.    , 1.    , 1.4142, 1.7321, 2.    , 2.2361, 2.4495, 2.6458,
        2.8284, 3.    ])
  In [140]: np.exp(arr)
  Out[140]: 
  array([   1.    ,    2.7183,    7.3891,   20.0855,   54.5982,  148.4132,
          403.4288, 1096.6332, 2980.958 , 8103.0839])
- referred to as unary ufuncs
- add or maximum take two arrays (binary ufuncs) and return a single array
  In [141]: x = np.random.randn(8)
  In [142]: y = np.random.randn(8)
  In [143]: x
  Out[143]: 
  array([-0.0119,  1.0048,  1.3272, -0.9193, -1.5491,  0.0222,  0.7584,
        -0.6605])
  In [144]: y
  Out[144]: 
  array([ 0.8626, -0.01  ,  0.05  ,  0.6702,  0.853 , -0.9559, -0.0235,
        -2.3042])
  In [145]: np.maximum(x, y)
  Out[145]: 
  array([ 0.8626,  1.0048,  1.3272,  0.6702,  0.853 ,  0.0222,  0.7584,
        -0.6605])
- numpy.maximum computes the element-wise maximum of the elements in x and y
- ufunc can return multiple arrays
- modf is a vectorized version of the built in divmod. it reutns the fractional and integral parts of a float array
  In [146]: arr = np.random.randn(7) * 5
  In [147]: arr
  Out[147]: array([-3.2623, -6.0915, -6.663 ,  5.3731,  3.6182,  3.45  ,  5.0077])
  In [148]: remainder, whole_part = np.modf(arr)
  In [149]: remainder
  Out[149]: array([-0.2623, -0.0915, -0.663 ,  0.3731,  0.6182,  0.45  ,  0.0077])
  In [150]: whole_part
  Out[150]: array([-3., -6., -6.,  5.,  3.,  3.,  5.])
- ufuncs accept an optional out argument that allows them to operate in place on arrays
  In [151]: arr
  Out[151]: array([-3.2623, -6.0915, -6.663 ,  5.3731,  3.6182,  3.45  ,  5.0077])
  In [152]: np.sqrt(arr)
  Out[152]: array([   nan,    nan,    nan, 2.318 , 1.9022, 1.8574, 2.2378])
  In [153]: np.sqrt(arr, arr)
  Out[153]: array([   nan,    nan,    nan, 2.318 , 1.9022, 1.8574, 2.2378])
  In [154]: arr
  Out[154]: array([   nan,    nan,    nan, 2.318 , 1.9022, 1.8574, 2.2378])
- unary ufuncs
  - abs, fabs	Compute the absolute value element-wise for integer, floating-point, or complex values
  - sqrt	Compute the square root of each element (equivalent to arr ** 0.5)
  - square	Compute the square of each element (equivalent to arr ** 2)
  - exp	Compute the exponent ex of each element
  - log, log10, log2, log1p	Natural logarithm (base e), log base 10, log base 2, and log(1 + x), respectively
  - sign	Compute the sign of each element: 1 (positive), 0 (zero), or –1 (negative)
  - ceil	Compute the ceiling of each element (i.e., the smallest integer greater than or equal to that number)
  - floor	Compute the floor of each element (i.e., the largest integer less than or equal to each element)
  - rint	Round elements to the nearest integer, preserving the dtype
  - modf	Return fractional and integral parts of array as a separate array
  - isnan	Return boolean array indicating whether each value is NaN (Not a Number)
  - isfinite, isinf	Return boolean array indicating whether each element is finite (non-inf, non-NaN) or infinite, respectively
  - cos, cosh, sin, sinh, tan, tanh	Regular and hyperbolic trigonometric functions
  - arccos, arccosh, arcsin, arcsinh, arctan, arctanh	Inverse trigonometric functions
  - logical_not	Compute truth value of not x element-wise (equivalent to ~arr).
- binary ufuncs
  - add	Add corresponding elements in arrays
  - subtract	Subtract elements in second array from first array
  - multiply	Multiply array elements
  - divide, floor_divide	Divide or floor divide (truncating the remainder)
  - power	Raise elements in first array to powers indicated in second array
  - maximum, fmax	Element-wise maximum; fmax ignores NaN
  - minimum, fmin	Element-wise minimum; fmin ignores NaN
  - mod	Element-wise modulus (remainder of division)
  - copysign	Copy sign of values in second argument to values in first argument
  - greater, greater_equal, less, less_equal, equal, not_equal	Perform element-wise comparison, yielding boolean array (equivalent   to infix operators >, >=, <, <=, ==, !=)
  - logical_and, logical_or, logical_xor	Compute element-wise truth value of logical operation (equivalent to infix operators & |, ^)

Array-Oriented Programming with Arrays
- NumPy arrays enable you to express many kinds of data processing tasks as a concise array instead of loops
- referred to as vectorization
- will often be 1 or 2 orders of magnitude faster 
- np.meshgrid function takes 2 1D arrays and produces two 2D matrices correspinding to all pairs of (x, y)
  In [155]: points = np.arange(-5, 5, 0.01) # 1000 equally spaced points
  In [156]: xs, ys = np.meshgrid(points, points)
  In [157]: ys
  Out[157]: 
  array([[-5.  , -5.  , -5.  , ..., -5.  , -5.  , -5.  ],
        [-4.99, -4.99, -4.99, ..., -4.99, -4.99, -4.99],
        [-4.98, -4.98, -4.98, ..., -4.98, -4.98, -4.98],
        ...,
        [ 4.97,  4.97,  4.97, ...,  4.97,  4.97,  4.97],
        [ 4.98,  4.98,  4.98, ...,  4.98,  4.98,  4.98],
        [ 4.99,  4.99,  4.99, ...,  4.99,  4.99,  4.99]])
- evaluating the function is a matter of writing the same expression you would with 2 points
  In [158]: z = np.sqrt(xs ** 2 + ys ** 2)
  In [159]: z
  Out[159]: 
  array([[7.0711, 7.064 , 7.0569, ..., 7.0499, 7.0569, 7.064 ],
        [7.064 , 7.0569, 7.0499, ..., 7.0428, 7.0499, 7.0569],
        [7.0569, 7.0499, 7.0428, ..., 7.0357, 7.0428, 7.0499],
        ...,
        [7.0499, 7.0428, 7.0357, ..., 7.0286, 7.0357, 7.0428],
        [7.0569, 7.0499, 7.0428, ..., 7.0357, 7.0428, 7.0499],
        [7.064 , 7.0569, 7.0499, ..., 7.0428, 7.0499, 7.0569]])
- use matplotlib to create visualizations of this two-dimensional array
  In [160]: import matplotlib.pyplot as plt
  In [161]: plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()
  Out[161]: <matplotlib.colorbar.Colorbar at 0x7f8520cd1b38>
  In [162]: plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
  Out[162]: Text(0.5,1,'Image plot of $\\sqrt{x^2 + y^2}$ for a grid of values')
- omshow creates an image plot from a two dimensional array of function values

Expressing conditional logic as array operations
- numpy .where function is a vectorized version of if/else statement
- have boolean array and two arrays of values. Want to take value from xarr whenever the corresponding value in cond is True, and otherwise take the value from yarr
  In [165]: xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
  In [166]: yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
  In [167]: cond = np.array([True, False, True, True, False])
  In [168]: result = [(x if c else y)
    .....:           for x, y, c in zip(xarr, yarr, cond)]
  In [169]: result
  Out[169]: [1.1, 2.2, 1.3, 1.4, 2.5]
  - this is not fast for large arrays and will not work for multidimensional arrays
- .where version 
  In [168]: result = [(x if c else y)
    .....:           for x, y, c in zip(xarr, yarr, cond)]
  In [169]: result
  Out[169]: [1.1, 2.2, 1.3, 1.4, 2.5]
- typical use of where is to produce a new array of values based on another aray
- matrix of rand data and you want to replace all positive values with 2 and all negative with -2
  In [172]: arr = np.random.randn(4, 4)
  In [173]: arr
  Out[173]: 
  array([[-0.5031, -0.6223, -0.9212, -0.7262],
        [ 0.2229,  0.0513, -1.1577,  0.8167],
        [ 0.4336,  1.0107,  1.8249, -0.9975],
        [ 0.8506, -0.1316,  0.9124,  0.1882]])
  In [174]: arr > 0
  Out[174]: 
  array([[False, False, False, False],
        [ True,  True, False,  True],
        [ True,  True,  True, False],
        [ True, False,  True,  True]])
  In [175]: np.where(arr > 0, 2, -2)
  Out[175]: 
  array([[-2, -2, -2, -2],
        [ 2,  2, -2,  2],
        [ 2,  2,  2, -2],
        [ 2, -2,  2,  2]])
- can combine scalars and arrays with np.where
- replace all positive values in arr with the constant 2
  In [176]: np.where(arr > 0, 2, arr) # set only positive values to 2
  Out[176]: 
  array([[-0.5031, -0.6223, -0.9212, -0.7262],
        [ 2.    ,  2.    , -1.1577,  2.    ],
        [ 2.    ,  2.    ,  2.    , -0.9975],
        [ 2.    , -0.1316,  2.    ,  2.    ]])

Mathematical and statistical methods
- can use aggregations like sum, mean, and std by calling th earray instance method or using the top-level NumPy function
  In [177]: arr = np.random.randn(5, 4)
  In [178]: arr
  Out[178]: 
  array([[ 2.1695, -0.1149,  2.0037,  0.0296],
        [ 0.7953,  0.1181, -0.7485,  0.585 ],
        [ 0.1527, -1.5657, -0.5625, -0.0327],
        [-0.929 , -0.4826, -0.0363,  1.0954],
        [ 0.9809, -0.5895,  1.5817, -0.5287]])
  In [179]: arr.mean()
  Out[179]: 0.19607051119998253
  In [180]: np.mean(arr)
  Out[180]: 0.19607051119998253
  In [181]: arr.sum()
  Out[181]: 3.9214102239996507
- functions like mean and sum take an optional axis argument that computes the statistic over the given axis, resulting in an array with one fewer dimension
  In [182]: arr.mean(axis=1)
  Out[182]: array([ 1.022 ,  0.1875, -0.502 , -0.0881,  0.3611])
  In [183]: arr.sum(axis=0)
  Out[183]: array([ 3.1693, -2.6345,  2.2381,  1.1486])
  - arr.mean(1) means "compute mean across the columns" where arr.sum(o) means "compute the sum down the rows"
- cumsum and cumprod do not aggregate (produce array of intermediate results
  In [184]: arr = np.array([0, 1, 2, 3, 4, 5, 6, 7])
  In [185]: arr.cumsum()
  Out[185]: array([ 0,  1,  3,  6, 10, 15, 21, 28])
- in multidemensional arrays, accumulation functions like cumsum return an array of the same size but with partial aggregates computed along the indicated axis according to each lower dimensional slice
  In [186]: arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
  In [187]: arr
  Out[187]: 
  array([[0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]])
  In [188]: arr.cumsum(axis=0)
  Out[188]: 
  array([[ 0,  1,  2],
        [ 3,  5,  7],
        [ 9, 12, 15]])
  In [189]: arr.cumprod(axis=1)
  Out[189]: 
  array([[  0,   0,   0],
        [  3,  12,  60],
        [  6,  42, 336]])
- basic array statistical methods
  - sum	Sum of all the elements in the array or along an axis; zero-length arrays have sum 0
  - mean	Arithmetic mean; zero-length arrays have NaN mean
  - std, var	Standard deviation and variance, respectively, with optional degrees of freedom adjustment (default denominator n)
  - min, max	Minimum and maximum
  - argmin, argmax	Indices of minimum and maximum elements, respectively
  - cumsum	Cumulative sum of elements starting from 0
  - cumprod	Cumulative product of elements starting from 1

Methods for Boolean Arrays
- sum is often used to count true values in a boolean array 
  In [190]: arr = np.random.randn(100)
  In [191]: (arr > 0).sum() # Number of positive values
  Out[191]: 42
- two additional methods, any and all, useful especially boolean arrays
- any tests whether one or more values in an array is true, whole all checks if every value is true
  In [192]: bools = np.array([False, False, True, False])
  In [193]: bools.any()
  Out[193]: True
  In [194]: bools.all()
  Out[194]: False

Sorting
- sort in place witht he sort method 
  In [195]: arr = np.random.randn(6)
  In [196]: arr
  Out[196]: array([ 0.6095, -0.4938,  1.24  , -0.1357,  1.43  , -0.8469])
  In [197]: arr.sort()
  In [198]: arr
  Out[198]: array([-0.8469, -0.4938, -0.1357,  0.6095,  1.24  ,  1.43  ])
- can sort each one-dimensional section of values in a multidimensional array in place along an axis by passing the axis number to sort
  In [195]: arr = np.random.randn(6)
  In [196]: arr
  Out[196]: array([ 0.6095, -0.4938,  1.24  , -0.1357,  1.43  , -0.8469])
  In [197]: arr.sort()
  In [198]: arr
  Out[198]: array([-0.8469, -0.4938, -0.1357,  0.6095,  1.24  ,  1.43  ])
- the top-level method np.sort retuns a sorted cioy if an array instead of modifying the array in place. Can sort and select th evalue at a particular rank
  In [203]: large_arr = np.random.randn(1000)
  In [204]: large_arr.sort()
  In [205]: large_arr[int(0.05 * len(large_arr))] # 5% quantile
  Out[205]: -1.5311513550102103

Unique and other set logic
- basic set operations for one-dimensional ndarrays
- np.unique which returns the sorted unique values in an array
  In [206]: names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
  In [207]: np.unique(names)
  Out[207]: array(['Bob', 'Joe', 'Will'], dtype='<U4')
  In [208]: ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
  In [209]: np.unique(ints)
  Out[209]: array([1, 2, 3, 4])
- np.in1d tests membershjip of values in one array to another, returning a boolean array 
  In [211]: values = np.array([6, 0, 0, 3, 2, 5, 6])
  In [212]: np.in1d(values, [2, 3, 6])
  Out[212]: array([ True, False, False,  True,  True, False,  True])
- Array set operations
  - unique(x)	Compute the sorted, unique elements in x
  - intersect1d(x, y)	Compute the sorted, common elements in x and y
  - union1d(x, y)	Compute the sorted union of elements
  - in1d(x, y)	Compute a boolean array indicating whether each element of x is contained in y
  - setdiff1d(x, y)	Set difference, elements in x that are not in y
  - setxor1d(x, y)	Set symmetric differences; elements that are in either of the arrays, but not both
  
File Input and Output with Arrays
- save and load data to and from desk in text or binary format
- np.save and np.load 
- arrays are saved by default in an uncompressed raw binary format with the file extension.npy
  In [213]: arr = np.arange(10)
  In [214]: np.save('some_array', arr)
- if file path does not already end in .npy, the extension will be appended. Array on disk can then be loaded with np.load
  In [215]: np.load('some_array.npy')
  Out[215]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
- save multiple arrays arrays in an uncompressed archive using np.savez and passing the arrays as keyword arguments
  In [216]: np.savez('array_archive.npz', a=arr, b=arr)
- when loading an .npz file, you get back a dickt-like object that loads the individual arrays lazily 
  In [217]: arch = np.load('array_archive.npz')
  In [218]: arch['b']
  Out[218]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
- if your data compresses well, you may wish to use numpy.savez_compressed instead
  In [219]: np.savez_compressed('arrays_compressed.npz', a=arr, b=arr)

Linear Algebra
- multiplying two two dimesional arrays with * is an element-wise product instead of a matrix dot product
- there is a function dot, bot an array method and a function for matrix multiplication
  In [223]: x = np.array([[1., 2., 3.], [4., 5., 6.]])
  In [224]: y = np.array([[6., 23.], [-1, 7], [8, 9]])
  In [225]: x
  Out[225]: 
  array([[1., 2., 3.],
        [4., 5., 6.]])
  In [226]: y
  Out[226]: 
  array([[ 6., 23.],
        [-1.,  7.],
        [ 8.,  9.]])
  In [227]: x.dot(y)
  Out[227]: 
  array([[ 28.,  64.],
        [ 67., 181.]])
-x.dot(y) is equivalent to np.dot(x, y)
  In [228]: np.dot(x, y)
  Out[228]: 
  array([[ 28.,  64.],
        [ 67., 181.]])
- a matrix product between a two dimensional array and a suitable sized one-timensional array results in a one dimensional array
  In [229]: np.dot(x, np.ones(3))
  Out[229]: array([ 6., 15.])
- the @ also works as an infix operator that performs matrix multiplication
  In [230]: x @ np.ones(3)
  Out[230]: array([ 6., 15.])
- numpy.linalg has standard set of matrix decompositions and things like inverse and determinant
- implemented under the hood
  In [231]: from numpy.linalg import inv, qr
  In [232]: X = np.random.randn(5, 5)
  In [233]: mat = X.T.dot(X)
  In [234]: inv(mat)
  Out[234]: 
  array([[  933.1189,   871.8258, -1417.6902, -1460.4005,  1782.1391],
        [  871.8258,   815.3929, -1325.9965, -1365.9242,  1666.9347],
        [-1417.6902, -1325.9965,  2158.4424,  2222.0191, -2711.6822],
        [-1460.4005, -1365.9242,  2222.0191,  2289.0575, -2793.422 ],
        [ 1782.1391,  1666.9347, -2711.6822, -2793.422 ,  3409.5128]])
  In [235]: mat.dot(inv(mat))
  Out[235]: 
  array([[ 1.,  0.,  0.,  0.,  0.],
        [ 0.,  1., -0., -0., -0.],
        [-0., -0.,  1.,  0., -0.],
        [ 0.,  0.,  0.,  1.,  0.],
        [ 0.,  0., -0., -0.,  1.]])
  In [236]: q, r = qr(mat)
  In [237]: r
  Out[237]: 
  array([[-1.6914,  4.38  ,  0.1757,  0.4075, -0.7838],
        [ 0.    , -2.6436,  0.1939, -3.072 , -1.0702],
        [ 0.    ,  0.    , -0.8138,  1.5414,  0.6155],
        [ 0.    ,  0.    ,  0.    , -2.6445, -2.1669],
        [ 0.    ,  0.    ,  0.    ,  0.    ,  0.0002]])
- the expression X.T.dot(X) computes the dot product of X with its transpose X.T
- common linear algebra functions
  - diag	Return the diagonal (or off-diagonal) elements of a square matrix as a 1D array, or convert a 1D array into a square    matrix with zeros on the off-diagonal
  - dot	Matrix multiplication
  - trace	Compute the sum of the diagonal elements
  - det	Compute the matrix determinant
  - eig	Compute the eigenvalues and eigenvectors of a square matrix
  - inv	Compute the inverse of a square matrix
  - pinv	Compute the Moore-Penrose pseudo-inverse of a matrix
  - qr	Compute the QR decomposition
  - svd	Compute the singular value decomposition (SVD)
  - solve	Solve the linear system Ax = b for x, where A is a square matrix
  - lstsq	Compute the least-squares solution to Ax = b

Pseudorandom Number Generation
- numpy.random mod supplements built in random with functions to generate whol arrays of sample values from many kinds of probability distributions
- 4x4 array of samples from the standard normal distribution using normal
  In [238]: samples = np.random.normal(size=(4, 4))
  In [239]: samples
  Out[239]: 
  array([[ 0.5732,  0.1933,  0.4429,  1.2796],
        [ 0.575 ,  0.4339, -0.7658, -1.237 ],
        [-0.5367,  1.8545, -0.92  , -0.1082],
        [ 0.1525,  0.9435, -1.0953, -0.144 ]])
- built in only sample sone value at a time
- numpy is faster
- called pseudorandom numbers because generated by algorithm with deterministic behavior based ont he seed of the generator
- can change the seed with np.random.seed(1234)
- data gen functions in numpy.random use a global random seed. To avoid global state, use numpy.random.RandomState to creat random generator isolated from others
  In [245]: rng = np.random.RandomState(1234)
  In [246]: rng.randn(10)
  Out[246]: 
  array([ 0.4714, -1.191 ,  1.4327, -0.3127, -0.7206,  0.8872,  0.8596,
        -0.6365,  0.0157, -2.2427])
- some functions from mumpy.random
  - seed	Seed the random number generator
  - permutation	Return a random permutation of a sequence, or return a permuted range
  - shuffle	Randomly permute a sequence in-place
  - rand	Draw samples from a uniform distribution
  - randint	Draw random integers from a given low-to-high range
  - randn	Draw samples from a normal distribution with mean 0 and standard deviation 1 (MATLAB-like interface)
  - binomial	Draw samples from a binomial distribution
  - normal	Draw samples from a normal (Gaussian) distribution
  - beta	Draw samples from a beta distribution
  - chisquare	Draw samples from a chi-square distribution
  - gamma	Draw samples from a gamma distribution
  - uniform	Draw samples from a uniform [0, 1) distribution

Example: Random Walks
- simulation of random walks provides illustrative application of utilizing array operations
- random walk starting at 0 with steps of 1 and -1 occuring with equal probablility
  - pure python way
    In [247]: import random
      .....: position = 0
      .....: walk = [position]
      .....: steps = 1000
      .....: for i in range(steps):
      .....:     step = 1 if random.randint(0, 1) else -1
      .....:     position += step
      .....:     walk.append(position)
      .....:
   - walk is the cumulative sum of the random steps and could be evaluated as an array expression
  - ise np.random mod to draw 1000 coin flips at once, set these to 1 and -1 an dcompute cumsum
    In [251]: nsteps = 1000
    In [252]: draws = np.random.randint(0, 2, size=nsteps
    In [253]: steps = np.where(draws > 0, 1, -1)
    In [254]: walk = steps.cumsum()
- can extract stats like min and max value along the walk's trajectory
  In [255]: walk.min()
  Out[255]: -3
  In [256]: walk.max()
  Out[256]: 31
- mor ecomplicated stat is first crossing time, the step at which the rand walk reaches a certain value
- might want to know how long it took the rand wal kto get at least 10 steps from the origin in eithr direction
- np.abs(walk) >= 10 gives boolean array indicating where the walk has reached or exceeded 10, but we want the index of th efirst 10 or -10
- can compute using argmax, which returns the first index of the maximum value in the boolean array (True)
    In [257]: (np.abs(walk) >= 10).argmax()
    Out[257]: 37
  - argmax always makes full scan of th earray

Simulating many random walks at once
- if goal is to simulate many wlaks, can generate with minor modifications
- if passed a 2-tuple, numpy.random functions will generate a 2 dimensional array of draws, and we can compute cumsum across the rows 
  n [258]: nwalks = 5000
  In [259]: nsteps = 1000
  In [260]: draws = np.random.randint(0, 2, size=(nwalks, nsteps)) # 0 or 1
  In [261]: steps = np.where(draws > 0, 1, -1)
  In [262]: walks = steps.cumsum(1)
  In [263]: walks
  Out[263]: 
  array([[  1,   0,   1, ...,   8,   7,   8],
        [  1,   0,  -1, ...,  34,  33,  32],
        [  1,   0,  -1, ...,   4,   5,   4],
        ...,
        [  1,   2,   1, ...,  24,  25,  26],
        [  1,   2,   3, ...,  14,  13,  14],
        [ -1,  -2,  -3, ..., -24, -23, -22]])
- now can compute max and min values obtained over all the walks 
  In [264]: walks.max()
  Out[264]: 138
  In [265]: walks.min()
  Out[265]: -133
- compute minimum crossing time to 30 or -30. Tricky because not all 5000 of them reach 30. Can check using the any method
  In [266]: hits30 = (np.abs(walks) >= 30).any(1)
  In [267]: hits30
  Out[267]: array([False,  True, False, ..., False,  True, False])
  In [268]: hits30.sum() # Number that hit 30 or -30
  Out[268]: 3410
- can use this boolean array to select out the rows of walks that actually cross the absolute 30 level and call argmax across axis 1 to get the crossing times
  In [269]: crossing_times = (np.abs(walks[hits30]) >= 30).argmax(1)
  In [270]: crossing_times
  Out[270]: array([735, 409, 253, ..., 327, 453, 447])
- compute average minimum crossing time
  In [271]: crossing_times.mean()
  Out[271]: 498.8897360703812



# Chapter 5: Getting Started with pandas
- pandas contains data structures and manipulation tools for data cleansinng and analysis
- used for tabular or heterogeneous data

  import pandas as pd
  from pandas import Series, DataFrame
  
- series is a one-dimensional array-like object containing a sequence of values and an associated array of data labels called an index
  obj = pd.Series([4, 7, -5, 3])
- string representation of a Series displayed interactively shows the index on the left and the values on the right
- if you don't specify and index, default is 0 through N - 1 where N is the length of data
  obj.values
  obj.index (like range)
- can create Series with an index identifying each data point with label
  obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
- can use labels in the index when selecting single values or a set of values
  obj2['a']
  obj2['d'] = 6
  obj2[['c', 'a', 'd']]
- here ['c', 'a', 'd'] is interpreted as a lsit of indices even though it contains strings instead of integers
- using NumPy operations will preserve the index-value link
  obj2[obj2 > 0]
  obj2 * 2
  np.exp(obj2)
- Series is a fixed-length, ordered dict that maps index values to data values
  'b' in obj2
  'e' in obj2
- can create a Series using a dict by passing it 
    sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon: 16000, 'Utah': 5000}
    obj3 = pd.Series(sdata)
- when passing a dict, the index is the resulting Series will have the dicts keys in sorted order. Can override by passing keys in the order you want
  states = ['California', 'Ohio', 'Oregon', 'Texas']
  obj4 = pd.Series(sdata, index=states)
- California has NaN because it does not exist
  pd.isnull(obj4)
- used to detect missing data
- can also use
  obj4.isnull()
- both the Series object and index have a *name* attribute 
  obj4.name = 'population'
  onj4.index.name = 'state'
- a series' index can be altered in-place by assignment
  obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
  
- DataFrame represents a rectangular table of data and contains an ordered collection of columns, each of which can be a different value type
- has both a row and column index - like a dict of Series all sharing the same index
- data is stored as one or more two-dimensional arrays
- create a DF from a dict of equal length dicts or NumPy arrays
  data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
  'year': [2000, 2001, 2002, 2001, 2002, 2003],
  'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
  frame = pd.DataFrame(data)
- the resulting DF has index assigned automatically and columns in sorted order 
- head method selects only first 5 rows
  frame.head()
- can specify a sequence of columns to be displayed in that order
  pd.DataFrame(data, columns=['year', 'state', 'pop'])
- if you pass a column that isn't in the dict, appears with missing values
  frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index = ['one', 'two', 'three', 'four', 'five', 'six'])
  frame2.columns
- a column can be retrieved as a series either by dict-like notation or by attribute
  frame2['state']
  frame2.year
- rows can be retieved by position or name with the special loc attribute
  frame2.loc['three']
- columns can be modified by assignment using a scalar value or an array of values
  frame2['debt'] = 16.5
  frame2['debt'] = np.arrange(6.)
- when assigning lists or arrays to a column, the value's length must mach the length of the DF. If you assign a Series, its labels will be realigned exactly to the DF's index, inserting missing values in any holes
  val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
  frame2['debt'] = val
- assigning column that doesn't exist will create a new column. The del keyword deletes columns as with a dict
  frame2['estern'] = frame2.state == 'Ohio'
  frame2
  del frame2['eastern']
  frame2.columns
- nested dicts are common
  pop = {'Nevada': {2001: 2.4, 2002: 2.9},
  ....: 'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
- if nested dict is passed to the DF, pandas will interpret outer dict keys as columns and inner keys as row indices
  frame3 = pd.DataFrame(pop)
- can transpose the DF (swap rows and columns) with similar to NumPy
  frame3.T
- keys in the inner dicts are combined and sorted to form the index in the result. This isn't true if an explicit index is specified
  pd.DataFrame(pop, index=[2001, 2002, 2003])
- dicts of Series are treated in much the same way
  pdata = {'Ohio': frame3['Ohio'][:-1],
  ....: 'Nevada': frame3['Nevada'][:2]}
  pd.DataFrame(pdata)
- if a DataFrame's index and columns have theri name attributes set, these will also be displayed
  frame3.index.name = 'year'; frame3.columns.name = 'state'
- as with Series, the values attribute returns the data contained in the DF as a two-dimensional ndarray
  frame3.values
- if the DF columns are different dtypes, the dtype of the values array will be chosen to accomodate all of the columns
  frame2.values
- possible data inputs to DF constructor
  -2D ndarray   A matrix of data, passing optional row and column labels
  - dict of arrays, lists, or tuples Each sequence becomes a column in the DataFrame; all -sequences must be the same length
- NumPy structured/record array   Treated as the “dict of arrays” case
- dict of Series   Each value becomes a column; indexes from each Series are unioned together to form the result’s row index if no explicit index is passed
- dict of dicts    Each inner dict becomes a column; keys are unioned to form the row index as in the “dict of Series” case
- List of dicts or Series Each item becomes a row in the DataFrame; union of dict keys or Series indexes become the DataFrame’s column labels
- List of lists or tuples   Treated as the “2D ndarray” case
- Another DataFrame The DataFrame’s indexes are used unless different ones are passed
- NumPy MaskedArray Like the “2D ndarray” case except masked values become NA/missing in the DataFrame result


#### Index Objects
- responsible for holding the axis labels and other metadata (like the axis name or names)
- any array or other sequence of labels you use when constructing a Series or DF is internally converted to an index
  obj = pd.Series(range(3), index=['a', 'b', 'c'])
  obj = pd.Series(range(3), index=['a', 'b', 'c'])
  index
  index[1:]
- index objects are immutable and thus can't be modified by the user
  index[1] = 'd' # TypeError
- immutability makes it safer to share index objects among data structures
  labels = pd.Index(np.arange(3))
  labels
  obj2 = pd.Series([1.5, -2.5, 0], index=labels)
  obj2.index is labels
- an index behaves like a fixed-sized set
  frame3
  frame3.columns
  'Ohio' in frame3.columns
  2003 in frame3.index
- unlike python sets, pandas index can contain duplicate labels
  dup_labels = pd.Index(['foo', 'foo', 'bar', 'bar'])
- selections with duplicate labels will select all occurances of that label
- each index has a nnumber of methods and properties for set logic, which answer other common questions about the data it contains
- some index methods and properties
  - append Concatenate with additional Index objects, producing a new Index
  - difference Compute set difference as an Index
  - intersection Compute set intersection
  - union Compute set union
  - isin Compute boolean array indicating whether each value is contained in the passed collection
  - delete Compute new Index with element at index i deleted
  - drop Compute new Index by deleting passed values
  - insert Compute new Index by inserting element at index i
  - is_monotonic Returns True if each element is greater than or equal to the previous element
  - is_unique Returns True if the Index has no duplicate values
  - unique Compute the array of unique values in the Index

#### Essential Functionality
##### Reindexing
- create a new object with the data conformed to a new index
  obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
- calling reindex on this series rearranges the data according to the new index, introducing missing values if any index values were not already present 
  obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
- for ordered data like time seies, it may be desirable to do some interpolation or filling of values when reindexing
- the method option allows this using methods such as ffill
  obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
  obj3.reindex(range(6), method='ffill')
- with DF, reindex can alter the (row) index and/or columns 
- when passed only a sequence. reindexes rows
  frame = pd.DataFrame(np.arange(9).reshape((3, 3)),
  ....: index=['a', 'c', 'd'],
  ....: columns=['Ohio', 'Texas', 'California'])
  frame2 = frame.reindex(['a', 'b', 'c', 'd'])
- the columns can be reindexed with the columns keyword
  states = ['Texas', 'Utah', 'California']
  frame.reindex(columns=states)
- can reindex more succintly by label-indexing with loc
  frame.loc[['a', 'b', 'c', 'd'], states]
- reindex function arguments
  - index New sequence to use as index. Can be Index instance or any other sequence-like Python data structure. An Index will be used exactly as is without any copying.
  - method Interpolation (fill) method; 'ffill' fills forward, while 'bfill' fills backward.
  - fill_value Substitute value to use when introducing missing data by reindexing.
  - limit When forward- or backfilling, maximum size gap (in number of elements) to fill.
  - tolerance When forward- or backfilling, maximum size gap (in absolute numeric distance) to fill for inexact matches.
  - level Match simple Index on level of MultiIndex; otherwise select subset of.
  - copy If True, always copy underlying data even if new index is equivalent to old index; if False, do not copy the data when the indexes are equivalent.
  
##### Dropping entries from an axis
- drop method will retun a new object with the indicated value or values deleted from an axis
  obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
  new_obj = obj.drop('c')
  obj.drop(['d', 'c'])
- with DF, index calues can be deleted from either axis
  data = pd.DataFrame(np.arange(16).reshape((4, 4)),
  .....: index=['Ohio', 'Colorado', 'Utah', 'New York'],
  .....: columns=['one', 'two', 'three', 'four'])
- calling drop with a sequence of labels will drop values fromt he row labels (axis 0)
  data.drop(['Colorado', 'Ohio'])
- can drop values from columns by passing axis=1 or axis='columns'
  data.drop('two', axis=1)
  data.drop(['two', 'four'], axis='columns')
- many functions, like drop, which modify the size or shape of a series or DF, can manipulate an object in place without returning a new object
  obj.drop('c', inplace=True)
- inplace destroys any data that is dropped

###### Indexing, selection, and filtering
- series indexing (obj[...]) works analogously to NumPy array indexing, except you can use the series's index values instead of only integers
  obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
  obj['b']
  obj[1]
  obj[2:4]
  obj[['b', 'a', 'd']]
  obj[[1, 3]]
  obj[obj < 2]
- slicing with labels behaves different than normal python. End point is inclusive
  obj['b':'c']
- setting using these methods modifies the corresponding section of the series
  obj['b':'c'] = 5
- indexing into a DF is for retrieving one or more columns either with a single value or sequence
  data = pd.DataFrame(np.arange(16).reshape((4, 4)),
  .....: index=['Ohio', 'Colorado', 'Utah', 'New York'],
  .....: columns=['one', 'two', 'three', 'four'])
  data['two']
  data[['three', 'one']]
- indexing like this has a few special cases. Slicing or selecting with a boolean array
  data[:2]
  data[data['three'] > 5]
- the row selection syntax data[:2] is provided as a convenience
- passing a single element or a list to the [] operator selects columns
- another use case is indexing with a boolean DF, such as one produced by a scalar comparison
  data < 5
  data[data < 5] = 0
- this makes DF syntactically more like a two-dimensional NumPy array in this particular case

##### selection with loc and iloc
- for DF label-indexing on rows
- enable selection of subset of the rows and columns from a DF with NumPy-like notation using axis labels (loc) or integers (iloc)
- select single row and multiple columns by label
  data.loc['Colorado', ['two', 'three']]
- perform similar selection with integers
  data.iloc[2, [3, 0, 1]]
  data.iloc[2]
  data.iloc[[1, 2], [3, 0, 1]]
- both idexing functions work with slices in addition to single labels or lists of labels
  data.loc[:'Utah', 'two']
  data.iloc[:, :3][data.three > 5]
- indexing options with DF
  - df[val] Select single column or sequence of columns from the DataFrame; special case
conveniences: boolean array (filter rows), slice (slice rows), or boolean DataFrame (set values based on some criterion)
  - df.loc[val] Selects single row or subset of rows from the DataFrame by label
  - df.loc[:, val] Selects single column or subset of columns by label
  - df.loc[val1, val2] Select both rows and columns by label
  - df.iloc[where] Selects single row or subset of rows from the DataFrame by integer position
  - df.iloc[:, where] Selects single column or subset of columns by integer position
  - df.iloc[where_i, where_j] Select both rows and columns by integer position
  - df.at[label_i, label_j] Select a single scalar value by row and column label
  - df.iat[i, j] Select a single scalar value by row and column position (integers)
  - reindex method Select either rows or columns by labels
  - get_value, set_value methods Select single value by row and column label
  
##### integer indexes
- if you have an axis index containing integers, data selection will always be label-oriented. loc for labels, iloc for integers
  ser.loc[:1]
  ser.iloc[:1]
  
##### arithmetic and data alignment
- when adding objects together. if index pairs are not the same, the respective index in
the result will be the untion of the index pairs
  s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
  s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1],
  .....: index=['a', 'c', 'e', 'f', 'g'])
  s1 + s2
- internal data alignment introduces missing values in the label locations that don't overlap
- in the case of SF, alignment is performed on both rows and columns
  df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'),
  .....: index=['Ohio', 'Texas', 'Colorado'])
  df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
  .....: index=['Utah', 'Ohio', 'Texas', 'Oregon'])
  df1 + df2
- since the 'c' and 'e' columns are not in both, they appear as all missing in the result. Same for rows whose labels are not common to both objects
- if you add DF objects with no column or row labels in common, all nulls

##### Arithmetic methods with fill values
- fill with special value when axis label is in one but not the other
  In [165]: df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)),
  .....: columns=list('abcd'))
  In [166]: df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)),
  .....: columns=list('abcde'))
  In [167]: df2.loc[1, 'b'] = np.nan
  In [170]: df1 + df2
- using the add method on df1 pases df2 an argument of fill_value
  In [171]: df1.add(df2, fill_value=0)
- flexible arithmetic methods
  - add, radd Methods for addition (+)
  - sub, rsub Methods for subtraction (-)
  - div, rdiv Methods for division (/)
  - floordiv, rfloordiv Methods for floor division (//)
  - mul, rmul Methods for multiplication (*)
  - pow, rpow Methods for exponentiation (**)
- as with numpy arrays of different dimensions, arithmetic between df and series is defined
  In [175]: arr = np.arange(12.).reshape((3, 4))
  In [176]: arr
  Out[176]:
  array([[ 0., 1., 2., 3.],
        [ 4., 5., 6., 7.],
        [ 8., 9., 10., 11.]])
  In [177]: arr[0]
  Out[177]: array([ 0., 1., 2., 3.])
  In [178]: arr - arr[0]
  Out[178]:
  array([[ 0., 0., 0., 0.],
        [ 4., 4., 4., 4.],
        [ 8., 8., 8., 8.]])
- subtract arr[0] from arr, the subtraction is performed once for each row
- referred to as broadcasting 
- similar with SF and series
  In [179]: frame = pd.DataFrame(np.arange(12.).reshape((4, 3)),
  .....: columns=list('bde'),
  .....: index=['Utah', 'Ohio', 'Texas', 'Oregon'])
  In [180]: series = frame.iloc[0]
  In [181]: frame
  Out[181]:
           b d e
  Utah 0.0 1.0 2.0
  Ohio 3.0 4.0 5.0
  Texas 6.0 7.0 8.0
  Oregon 9.0 10.0 11.0
  In [182]: series
  Out[182]:
  b 0.0
  d 1.0
  e 2.0
  Name: Utah, dtype: float64



















  
