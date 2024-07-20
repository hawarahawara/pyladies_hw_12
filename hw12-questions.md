## Finding the mistakes in the code

1. Line 6: "else if" is not a valid command, the right one would be "elif"
2. Line 2 and 5/7: The input from 2 is a string (standard, even if a number is put in, it will be procesed as a string), but in 5/7 an integer is needed ---> you need to convert the input into an integer
3. Line 7: I am pretty sure it is supposed to be "=" * num, i.e. the stripes should be printed num-times.
4. Line 8: after the else, there is a ":" missing.
5. (this makes the fifth mistake but I am also pretty sure it is a mistake too): after he if/else statements, the condition should not be in brackets (or at least: they do not need to be in brackets).

## Debugging Max-Value
1) What are the issues in the given script?
The script cannot handle an empty list, since it is defined over an non empty list (numbers[0]). There code is trying to access the lists index0, but it does not exists - nothing is there. 

2) How did you identify and fix them?
I ran it and got an error message, telling me which line was the offendin one.  I got a traceback error, which indicates that the code is syntactically correct but there was still an error in the code, i.e. an exepction. Python comes with built in library of exeptions, and the error message told me waht kind of error it was: "IndexError_ list index out of range", so I could deduce that the issue was with the index of the list. This list: https://www.w3schools.com/python/python_ref_exceptions.asp told me exactly what the error means - it is raised, when the index does not exist. Therefore I know where to check for waht. 


3) How would you handle an empty list in this function? Either plan and code for an error message using the try/except method or define find_max in a way that allows for empty lists - e-g- by returning "None". 

### What is a breakpoint, and how is it used in debugging?

It is is a function in the PDB - the Python De-Bugger (in the standard library). breakpoint-function is put into the code and both imports the PDB and starts it. 

# How can you handle exceptions in Python as a debugging step?

With the try/except method. 

