#!/bin/python

import sys
import re

def count_substring(string, sub_string):
    return len(re.findall("(?=" + sub_string + ")", string))