#!/usr/bin/env python3

"""Log parser from stdin and computes metrics"""
import sys
import re
import signal


def print_statistics(total_file_size, status_code_count):
    """Prints the log statistics of requests"""
    print(f"Total file size: {total_file_size}")
    for status_code, count in sorted(status_code_count.items()):
        if count > 0:
            print(f"{status_code}: {count}")


def signal_handler(sig, frame):
    """Handles the CTRL+C command signal"""
    print_statistics()
    sys.exit(0)


# Registering signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)


# <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
LOG_PATTERN = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(\d{2}/(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)/\d{4}:\d{2}:\d{2}:\d{2} [+-]\d{4})\] \"GET /projects/(\d+) HTTP/1\.1" (\d{3}) (\d+)$'
def read_input():
    line_count: int = 0
    total_file_size: int = 0
    status_code_count = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }
    for line in sys.stdin:
        line_count += 1
        # Remove new line
        # line = line.rstrip()
        matchedLog = re.match(LOG_PATTERN, line)
        if matchedLog:
            status_code = matchedLog.group(4)
            print(status_code)


if __name__ == "__main__":
    print(read_input())
