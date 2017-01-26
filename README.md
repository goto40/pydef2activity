# pydef2activity

Small example script to demonstrate how to transform a python function to an activity diagram. 

## Run

Usage: ```./pydef2activity <file> <function name>```

## Example

 * Command: ```./pydef2activity demo.py foo```
 * Input: [Example input demo.py](demo.py)
 * Output: ![Example output for demo.py](foo.png?raw=true)

## Features

 * ```if/elif/else```
 * ```# activity xy``` ... ```# end activiy```
 * ```# comment for last activity```
 * simple for loops (for a in b)
 
 All other code elements are rendered as activity directly.
 
## Install and preconditions 
 * get the red baron full-AST-parser: ```pip3 install redbaron```
 * bash 
 * plantuml (as command)
 
 
