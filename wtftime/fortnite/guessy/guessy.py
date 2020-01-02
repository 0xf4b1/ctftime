
print(open(__file__).read())

flag = open("/opt/flag.txt").read()
print flag
guess = input("Guess the flag: ")
print guess
if guess == flag:
    print("Correct!")
