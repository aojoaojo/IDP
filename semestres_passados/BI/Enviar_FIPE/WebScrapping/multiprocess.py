from concurrent.futures import ProcessPoolExecutor
import subprocess

def execute_main_script(argument):
    command = ['python3', 'extract.py', argument]
    result = subprocess.run(command)

if __name__ == '__main__':
    index_list = ['1', '2', '3', '4']
    with ProcessPoolExecutor() as executor:
        executor.map(execute_main_script, index_list)
