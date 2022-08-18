#! /usr/bin/env python3
import random
from string import *

sym = ";:!@#$%^&*()[]{}"
all = ascii_uppercase + ascii_lowercase + digits + sym
r = random.sample(all, 20)
password = "".join(r)
print(f"Your password is ready: {password}")
