n = int(input().strip())
phoneBook = dict()

for i in range(0, n):
    entry = input().strip().split(' ')
    phoneBook[entry[0]] = entry[1]

query = input().strip()
while query:
    phoneNumber = phoneBook.get(query)
    if phoneNumber:
        print(query + '=' + phoneNumber)
    else:
        print('Not found')
    query = input().strip()
