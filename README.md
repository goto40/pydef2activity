# pydef2activity

Small example how to transform a 

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
 
 All other code elements are rendered as activity directly.
 
## Install

get the red baron full-AST-parser: ```pip3 install redbaron```
