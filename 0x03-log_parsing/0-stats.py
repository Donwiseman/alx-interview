#!/usr/bin/python3
"""Parses a log file from stdin following a given format"""

import sys

for line in sys.stdin:
    line.strip()
    print(line)