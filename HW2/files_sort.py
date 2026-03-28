import sys
import os

if __name__ == '__main__':
    directory = sys.argv[1]
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    files_with_ext = [(f, os.path.splitext(f)) for f in files]
    files_with_ext.sort(key=lambda x: (x[1][1], x[1][0]))
    for f, _ in files_with_ext:
        print(f)
