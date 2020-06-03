import bcrypt

password = '123xyz'

hashed01 = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
hashed02 = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

print("That's first hushed password: ", hashed01)
print("That's second hushed password:", hashed02)

test_password = '123xyz '

if bcrypt.hashpw(test_password.encode('utf-8'), hashed01) == hashed01:
    print("It's OK")
else:
    print("NG")
