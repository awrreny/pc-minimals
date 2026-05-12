import argparse
import subprocess
from mirror_direct_ilp import find_minimals

SFINDER_PATH = '../existingtools/sfinder/sfinder.jar'
SFINDER_PREFIX = f'java -jar {SFINDER_PATH}'
PATH_FILE_PATH = 'temp/path.csv'

def main():
    parser = argparse.ArgumentParser(description="Find strict minimals using sfinder output")
    parser.add_argument("fumen", help="Fumen to process")
    parser.add_argument("pattern", help="Queue pattern")
    parser.add_argument("--output", nargs="?", default=None, help="Optional output file. If omitted, only prints to stdout.")
    parser.add_argument("--timeLimit", type=int, default=None, help="Time limit for the solver in seconds. Default is no limit.")
    args = parser.parse_args()

    path_cmd = f"{SFINDER_PREFIX} path -f csv -k pattern -t {args.fumen} -p {args.pattern} -o {PATH_FILE_PATH}"
    
    print(f"Running command: {path_cmd}")
    subprocess.run(path_cmd, shell=True, check=True)
    
    find_minimals(PATH_FILE_PATH, args.output, args.timeLimit)

if __name__ == "__main__":
    main()