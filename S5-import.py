# Importing, creating modules and packages 
import math 
print(math.sqrt(16))

# or use from math import *
from math import sqrt,pi
print(sqrt(25))
print(pi)

# importing numpy library
import numpy as np

# importing custom package 
from Package import maths
print(maths.addition(2,3))

# importing subpackage
from Package.subpackage import mult
result = mult.multiply(5,8)
print(result)
# or 
from Package.subpackage.mult import multiply
result = multiply(4,5)
print(result)

# Standard libraries or packages overview

# import re --regular expression
# import random
# import datetime  
# import time 
# import os
# import json
# import shutil
# import csv
