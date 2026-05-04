#!/usr/bin/env python3

import subprocess
import sys
import os

def main():
    # Determine the base directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to gifsicle.exe
    # Assuming gifsicle-1.95-win64/gifsicle.exe is relative to the script's directory
    gifsicle_path = os.path.join(script_dir, 'gifsicle-1.95-win64', 'gifsicle.exe')

    # Check if gifsicle.exe exists
    if not os.path.exists(gifsicle_path):
        print(f"Error: gifsicle.exe not found at {gifsicle_path}", file=sys.stderr)
        sys.exit(1)

    # Prepare the command to run gifsicle.exe
    # sys.argv[0] is the script name itself, so we slice from 1 to get actual arguments
    command = [gifsicle_path] + sys.argv[1:]

    try:
        # Execute gifsicle.exe and capture its output
        # text=True decodes stdout/stderr as text
        # check=False means we handle non-zero exit codes ourselves
        result = subprocess.run(command, capture_output=True, text=True, check=False)

        # Print stdout and stderr from gifsicle.exe
        if result.stdout:
            print(result.stdout, end='')
        if result.stderr:
            print(result.stderr, end='', file=sys.stderr)

        # Exit with the same exit code as gifsicle.exe
        sys.exit(result.returncode)

    except FileNotFoundError:
        print(f"Error: The gifsicle executable was not found at {gifsicle_path}. "
              "Please ensure it's correctly placed.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
