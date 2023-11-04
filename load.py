import subprocess
import sys


if __name__ == "__main__":
    
    file_path=sys.argv[1:] # recive the file path argument
    
    if len(file_path)> 1:
        print("Error! please add quotation between the file path")
    else:
        print(file_path[0])
        subprocess.call(['python', 'eda.py', f'{file_path[0]}']) # call the eda.py file and parse to it the filepath
    
