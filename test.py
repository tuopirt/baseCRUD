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