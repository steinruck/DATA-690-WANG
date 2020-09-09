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





















 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
