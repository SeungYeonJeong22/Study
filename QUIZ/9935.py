input_string = input()
bomb = input()
lenbomb = len(bomb)
last_char = bomb[-1]
stack = []

for char in input_string:
    stack.append(char)
    if last_char == char and ''.join(stack[-lenbomb:]) == bomb:
        del(stack[-lenbomb:])

if stack:
    print(stack)
else:
    print('FRULA')