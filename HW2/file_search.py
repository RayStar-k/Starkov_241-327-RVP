import sys
import os

def search_file(filename, directory='.'):
    for root, dirs, files in os.walk(directory):
        if filename in files:
            filepath = os.path.join(root, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    lines = [f.readline() for _ in range(5)]
                    for line in lines:
                        if line:
                            print(line.rstrip())
                return True
            except:
                try:
                    with open(filepath, 'r') as f:
                        lines = [f.readline() for _ in range(5)]
                        for line in lines:
                            if line:
                                print(line.rstrip())
                    return True
                except:
                    return False
    return False

if __name__ == '__main__':
    filename = sys.argv[1]
    if not search_file(filename):
        print(f"Файл {filename} не найден")
