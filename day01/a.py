# Advent of Code 2025
# Day 01
# Part A

import requests
import os
import sys
from dotenv import load_dotenv

load_dotenv()

# Input handling
if "-t" in sys.argv:
    with open("test.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
else:
    day = 1
    url = f"https://adventofcode.com/2025/day/{day}/input"
    cookies = {
        "session": os.getenv("AOC_SESSION_COOKIE")
    }
    response = requests.get(url, cookies=cookies)
    response.raise_for_status()
    lines = [line.strip() for line in response.text.splitlines()]

# Solution
pos = 50
password = 0

for line in lines:
    direction, value = line[0], int(line[1:]) % 100
    pos = (pos - value) if direction == "L" else (pos + value)
    pos %= 100
    if pos == 0: password += 1
print(password)