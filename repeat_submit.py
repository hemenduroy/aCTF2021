from datetime import datetime
import time
import sys
import os

folderpath = sys.argv[1]
tickinterval = 1 

def do_submit(folderpath):
    files = os.listdir(folderpath)
    for file in files:
        if file.endswith('.py'):
            print(f'[INFO][{datetime.now()}] Executing exploit in {file}!')
            os.system(f'python3 {os.path.join(folderpath, file)}')


print(f'[INFO] Folder path set to {folderpath}')

i = 0
while True:
    print(f'[INFO] Submitting for tick {i}')
    do_submit(folderpath)

    i += 1
    print(f'[SLEEP] Sleeping...')
    time.sleep(tickinterval)
    print('\n\n')
