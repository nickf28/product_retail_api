import sqlite3
from objects import User
from exceptions import UserAlreadyExists, UserNotFound, InvalidSignIn

conn = sqlite3.connect("product_retail.db")
cursor = conn.cursor()

def create_new_user(username, email, password):
    if __does_user_exist(username, email):
        raise UserAlreadyExists
    
    cursor.execute(f"insert into users(username, email, password) values ('{username}', '{email}', '{password}')")
    conn.commit()
    return True
    
def sign_in_user(username, email, password):
    if not __does_user_exist2(username, email, password):
        raise InvalidSignIn
    
    return True

def retrieve_user(username, email, password):
    if not __does_user_exist2(username, email, password):
        raise UserNotFound
    
    return User(username, email, password)

def reset_password(username, email, password, new_password):
    if not __does_user_exist2(username, email, password):
        raise UserNotFound
    
    cursor.execute(f"update users set password = '{new_password}' where username = '{username}'")
    conn.commit()
    return True

def delete_account(username, email, password):
    if not __does_user_exist2(username, email, password):
        raise UserNotFound
    
    cursor.execute(f"delete from users where username = '{username}'")
    conn.commit()
    return True

def __does_user_exist(username, email):
    data = cursor.execute("select username, email from users").fetchall()
    for row in data:
        if row[0] == username or row[1] == email:
            return True
        
    return False
        
def __does_user_exist2(username, email, password):
    data = cursor.execute("select username, email, password from users").fetchall()
    for row in data:
        if row[0] == username and row[1] == email and row[2] == password:
            return True
        
    return False