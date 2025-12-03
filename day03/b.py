# Advent of Code 2025
# Day 03
# Part A

import requests
import os
import sys
import tracemalloc
import argparse
import time
from functools import wraps
from dotenv import load_dotenv
from itertools import combinations

load_dotenv()
BENCHMARK_ENABLED = False
DAY = 3

def args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l", "--local",
        action="store_true",
        help="Enable the use of the local input file instead of the complete online input file. (for tests)"
    )
    parser.add_argument(
        "-b", "--benchmark",
        action="store_true",
        help="Monitor the time and ressources used by the solution."
    )
    return parser.parse_args()

def input_handler(local = False):
    if local:
        with open("local.txt", "r") as f:
            return [line.strip() for line in f.readlines()]
    else:
        url = f"https://adventofcode.com/2025/day/{DAY}/input"
        cookies = {
            "session": os.getenv("AOC_SESSION_COOKIE")
        }
        response = requests.get(url, cookies=cookies)
        response.raise_for_status()
        return [line.strip() for line in response.text.splitlines()]

def benchmark(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not BENCHMARK_ENABLED:
            return func(*args, **kwargs)

        tracemalloc.start()
        start = time.perf_counter_ns()

        result = func(*args, **kwargs)

        end = time.perf_counter_ns()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(f"Exec time: {(end - start) / 1_000_000:.3f}ms.")
        print(f"Mem used: {peak / 1024:.2f}Ko.")

        return result
    return wrapper

@benchmark
def solution(content):
    result = 0
    for bank in content:
        tmp = []
        for i, c in enumerate(bank):
            while tmp and c > tmp[-1] and len(tmp) + (len(bank) - i) > 12:
                tmp.pop()
            if len(tmp) < 12:
                tmp.append(c)
        battery = ''.join(tmp)
        result += int(battery)
    return result

if __name__ == "__main__":
    args = args_parser()
    local_file = args.local
    BENCHMARK_ENABLED = args.benchmark

    content = input_handler(local_file)

    print(f"Solution: {solution(content)}")
