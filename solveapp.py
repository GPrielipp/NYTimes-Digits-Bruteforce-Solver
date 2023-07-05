import subprocess
import json

def batch(key, numbers, target):
    cmd_nytsolver = "C:/Python311/python.exe \"c:/Users/m265112/Desktop/Python/NYT Digits Solver/nyt_digits_solver.py\""
    cmd_findshortest = "C:/Python311/python.exe \"c:/Users/m265112/Desktop/Python/NYT Digits Solver/find_shortest.py\""
    uinput = ' '.join([str(x) for x in numbers]) + ' ' + str(target)
    subprocess.call(' '.join([cmd_nytsolver,uinput]), stdout=subprocess.DEVNULL)
    shortest = subprocess.run(cmd_findshortest, capture_output=True)
    print(f'[batch {key}]')
    print(shortest.stdout.decode())

rounds = []
with open('gamedata.json', 'r') as fd:
    rounds = json.load(fd)['rounds']

for key,round in enumerate(rounds):
    numbers = round['numbers']
    target = round['target']
    batch(key+1,numbers,target)