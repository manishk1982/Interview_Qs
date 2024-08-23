#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'reducePath' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING path as parameter.
#

def reducePath(path):
    # Write your code here
    output_path = []
    # Split the input path for every '/' and process it
    for item in path.split('/'):
        if item == "":
            # Hack to avoid 1st & last empty string
            continue
        elif item == ".":
            # Do nothing as single . represents current dir
            continue
        elif item == "..":
            # Pop last dir name as .. represents parent dir
            # First check if there i anyhting to pop or not - if not, then ignore
            if len(output_path) == 0:
                continue
            output_path.pop(-1)
        else:
            # Preserve the dir name
            output_path.append(item)
    
    # Frame the path to be returned - Insert '/' between every dir name and at the begining as well
    output = f'/{"/".join(output_path)}'
    return output
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    path = input()

    result = reducePath(path)

    fptr.write(result + '\n')

    fptr.close()
