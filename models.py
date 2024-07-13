from werkzeug.security import generate_password_hash, check_password_hash


#i have written it to create a new user in the database
def create_user(email, password, collection):
    hashed_password = generate_password_hash(password)
    user = {'email': email, 'password': hashed_password}
    collection.insert_one(user)

def find_user_by_email(email, collection):
    return collection.find_one({'email': email})

def verify_password(stored_password, provided_password):
    return check_password_hash(stored_password, provided_password)