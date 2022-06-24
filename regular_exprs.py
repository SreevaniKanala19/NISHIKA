import re

print(re.findall(r'[Gg]eeks', 'GeeksforGeeks:A computer1 science portal for 99 geeks'))
print(re.findall(r'\d\d', 'GeeksforGeeks:A computer1 science portal for 99 geeks'))
print(re.findall(r'\d{2}', 'GeeksforGeeks:A computer1 science portal for 99 geeks'))
print(re.findall(r'\w+', 'GeeksforGeeks:A computer1 science portal for 99 geeks'))
print(re.findall(r'\s+', 'GeeksforGeeks:A computer1 science portal for 99 geeks'))
print(re.findall(r'[com]puter', 'GeeksforGeeks:A computer1 computer1 computer1 science portal for 99 geeks'))
print(re.findall(r'[\w . _ \d]+', 'k.sreevani@gmail.com sreevani964@gmail.com noorbasha.py@gmail.com noor.py@yahoo.com'))
print(re.findall('[\d{4}\s-]+', '4444 5555 6666 1122 , 4784-7898-7410-123'))


