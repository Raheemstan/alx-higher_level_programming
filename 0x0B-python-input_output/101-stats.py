#!/usr/bin/python3
import sys

def print_stats(total_size, status_codes):
    """Prints file size and status code statistics."""
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        print("{}: {}".format(code, count))

def parse_line(line, status_codes):
    """Parses a log line and updates file size and status code statistics."""
    try:
        elements = line.split()
        size = int(elements[-1])
        code = elements[-2]
        
        # Update total file size
        total_size[0] += size

        # Update status code count
        status_codes[code] = status_codes.get(code, 0) + 1
    except (IndexError, ValueError):
        pass

if __name__ == "__main__":
    total_size = [0]
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            parse_line(line, status_codes)

            # Print statistics every 10 lines
            if i % 10 == 0:
                print_stats(total_size[0], status_codes)

    except KeyboardInterrupt:
        # Handle keyboard interruption
        print_stats(total_size[0], status_codes)
