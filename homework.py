import random
import string
def c(d):
    a = string.ascii_letters + string.digits
    b = ''.join(random.choices(a, k=d))
    return b
d = int(input("Enter password length: "))
print("Generated Password:", c(d))
