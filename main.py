

#example database
db= {
    "alice": {"role": "admin", "email": "alice@example.com"},
    "bob": {"role": "user", "email": "bob@example.com"},
    "charlie": {"role": "user", "email": "charlie@example.com"},
    "diana": {"role": "moderator", "email": "diana@example.com"},
    "eve": {"role": "user", "email": "eve@example.com"}
}




# create new user in database with rank and login
def create(name,rank,login):


# given name, read user rank and login
def read(name):


# updates a user's rank OR login
def update(name, rank, login):


# delete all info of user
def destroy(name):


