import random
import string
import time


letter = string.ascii_lowercase + " "
result = ""
target = "hello"
for letter in target:
    while True:
        i = random.choice(letter)
        print(result + i)
        if(i == letter):
            result += i
            break
    time.sleep(0.1)
print(result)