import random
import string

lower  = string.ascii_lowercase
upper  = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

all = lower + upper + digits + symbols

length = 16
passwords = " ".join(random.sample(all,length))

print(passwords)
