# Interpreter for a functional language ![Python](https://img.shields.io/badge/python-%23fdc93d.svg?style=for-the-badge&logo=python&logoColor=blue)
> 185.208 Programmiersprachen (VU 2,0) 2024S
>
> Second Programming Task
>
> 

## Run Interpreter
1. add code to Exercise_2/src/interpreter/data.txt
2. 
 ```python
    python src/interpreter
```
## Run tests
 ```python
    python src/tests
```
# Basic Operations
## 1.	Printing Expressions:

The ```print``` statement is used to output the result of expressions or strings.
>
Examples:
>
```print(4 + 4 - 2);``` - Prints the result of the arithmetic operation (6).
>
```print(4 * 4 / 2);``` - Prints the result of the arithmetic operation (8).
>
```print("d" + "r");``` - Concatenates and prints strings ("dr").
>
```print("d" * 3);``` - Repeats the string "d" three times and prints the result ("ddd").
## 2.	Variable Assignment with ```input```:

The ```input``` statement allows the assignment of multiple variables in one line.
>
Syntax: ```input variable_name1 = value1, variable_name2 = value2, ... ;```
>
Examples:
>
```input x = 4, y = "ddddd", z = [1, 4], k = ["a", "b", "c"];```
>
Here,``` x ``` is an integer,```y``` is a string,```z``` is a list of integers, and ```k``` is a list of strings.
## 3.	Lambda Function Definition:

The ```lambda``` keyword is used to define anonymous functions.
>
Syntax: ```lambda parameter1, parameter2, ... : function_body ;.```
>
Example:
```input max = lambda a, b : print(if (a > b): print(a); end_if if (a < b): print(b); end_if);.```
>
This defines a lambda function max that takes two parameters a and b. It prints the larger of the two values using conditional statements ```if```.
>
## 4.	Conditional Statements:

The ```if``` statement is used to perform conditional logic.
>
Syntax: ```if (condition): action ; end_if```
>
Comparison operators:  ```>```   ```<```   ```>=```   ```<=```  ```!=```   ```==```
>
Example:
```if (a > b): print(a); end_if```   -   If ```a``` is greater than ```b```, it prints ```a```.
>
Multiple conditions can be checked sequentially as shown in the ```lambda``` function definition.

## 5.	Function Calls and Assignment:

Functions, including lambda functions, can be called and their results assigned to variables.
>
Example:
```value = max(6, 9);```   -  This calls the max function with arguments 6 and 9, assigns the result to value, and then prints value using ```print(value);```.
