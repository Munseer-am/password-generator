# bin/env python3
# importing modules
import random 

import array 

# maximum length of password
max_len = 30


# digits used for creating password
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']   

# locase characters
locase_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  

                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 

                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 

                     'z'] 

  
# upcase characters
upcase_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',  

                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 

                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 

                     'Z'] 

  
# symbols
symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  

           '*', '(', ')', '<'] 

  

# combining all characters, numbers and symbols
combined_list = digits + upcase_characters + locase_characters + symbols 

  

# randomising digits
rand_digit = random.choice(digits) 

# randomising upper case characters
rand_upper = random.choice(upcase_characters) 

rand_lower = random.choice(locase_characters) 

rand_symbol = random.choice(symbols) 

  

temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol 

for x in range(max_len - 4): 

    temp_pass = temp_pass + random.choice(combined_list) 

    temp_pass_list = array.array('u', temp_pass) 

    random.shuffle(temp_pass_list)

password = "" 

for x in temp_pass_list: 

        password = password + x 

print("""  __  __
 |  \/  |_   _ _ __  ___  ___  ___ _ __
 | |\/| | | | | '_ \/ __|/ _ \/ _ \ '__|
 | |  | | |_| | | | \__ \  __/  __/ |
 |_|  |_|\__,_|_| |_|___/\___|\___|_|""")

print("\n THIS SCRIPT IS CREATED BY MUNSEER")

print("\n you password is ready:",password)
