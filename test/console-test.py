import time

print('Hello World')

for i in range(20):
    print(f'i = {i}', end='\r')
    time.sleep(0.1)
print()

LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'

for i in range(20):
    for row in range(4):
        for col in range(4):
            print(f'{i} ', end='')
        print('')
    
    time.sleep(0.1)
    for i in range(4):
        print(LINE_UP, end=LINE_CLEAR)

for i in range(4):
    print('-')