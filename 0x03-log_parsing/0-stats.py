#!/usr/bin/python3
import sys
import re

def print_stats(total_size, status_count):
    """Print the current statistics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_count.keys()):
        if status_count[code] > 0:
            print("{}: {}".format(code, status_count[code]))

if __name__ == "__main__":
    total_size = 0
    status_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            # Parse the line using a regular expression
            match = re.search(r'(\S+) - \[(.*?)\] "GET /projects/\d+ HTTP/1\.1" (\d{3}) (\d+)', line)
            if match:
                status_code = int(match.group(3))
                file_size = int(match.group(4))
                
                # Accumulate file size
                total_size += file_size
                
                # Count the status code
                if status_code in status_count:
                    status_count[status_code] += 1

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_count)

    except KeyboardInterrupt:
        # On keyboard interrupt, print the final stats
        print_stats(total_size, status_count)
        raise

    # Final stats after all input
    print_stats(total_size, status_count)
