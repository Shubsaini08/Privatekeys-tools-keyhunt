import multiprocessing
import os

def run_script(script_name):
    os.system(f'python {script_name}')

if __name__ == "__main__":
    scripts = [
         "file.py", "file2.py", "file3.py"
    ]

    processes = []
    for script in scripts:
        p = multiprocessing.Process(target=run_script, args=(script,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
