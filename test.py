import main


#example database
db= {
    "alice": {"role": "admin", "email": "alice@example.com"},
    "bob": {"role": "user", "email": "bob@example.com"},
}


# Creation test
# "charlie": {"role": "user", "email": "charlie@example.com"},
main.create(db, "charlie", "user", "charlie@example.com")

print(db["charlie"],db["charlie"] == {"role": "user", "email": "charlie@example.com"})


# reading test
alice_read = main.read(db,"alice")
bob_read = main.read(db,"bob")
char_read = main.read(db,"charlie")

print("alice test: ", alice_read == db["alice"])
print("bob test: ", bob_read == db["bob"])
print("charlie test: ", char_read == db["charlie"])


