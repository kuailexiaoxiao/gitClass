import sys
import time

poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
use Python!
'''
f = open('poem.txt')
line = f.readline()
if len(line) == 0:
    f = open('poem.txt', 'w')
    f.write(poem)
    f.close()

try:
    f = open('poem.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end=" ")
        sys.stdout.flush()
        print("Press ctrl+c now")
        time.sleep(2)
except IOError:
    print("Could not find file poem.txt")
except KeyboardInterrupt:
    print("!! You cancelled the reading from the file.")
finally:
    if f:
        f.close()
    print("Cleaning up : closed the file")
#