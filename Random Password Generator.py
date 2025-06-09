import random
import string
passlen=8
charvalues=string.ascii_letters + string.digits + string.punctuation

password="".join([random.choice(charvalues) for i in range(passlen)])
# password=""
# for i in range(passlen):
#     password += random.choice(charvalues)
print("your random password is:",password)
