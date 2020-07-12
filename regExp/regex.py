import re

pattern = re.compile(r'^([\d]{4,4})\-\d\d-\d\d,(.*),Friendly,.*$')

f = open('results.csv', 'r')

for line in f:
    res = re.match(pattern, line)
    if res:
        print(f'{res.group(2)}\n')

f.close()
