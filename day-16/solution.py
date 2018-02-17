S = input().strip()

try:
    integer_value = int(S)
    print(integer_value)
except ValueError:
    print('Bad String')
