#!/usr/bin/env python3
# The above allows us to run this without python
# Make sure to import 
# Below are two types of imports, os lets us use terminal commands, sys allows us to take inputs
import os
import sys
name = sys.argv[1]

if __name__ == "__main__":
    print(f"The name is {name}")
    #os.system('ls -l')
    