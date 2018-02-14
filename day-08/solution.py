import sys

n = int(sys.stdin.readline().strip())
phoneBook = dict()

for i in range(0, n):
    entry = sys.stdin.readline().strip().split(' ')
    phoneBook[entry[0]] = entry[1]

query = sys.stdin.readline().strip()
while query:
    phoneNumber = phoneBook.get(query)
    if phoneNumber:
        print(query + '=' + phoneNumber)
    else:
        print('Not found')
    query = sys.stdin.readline().strip()
