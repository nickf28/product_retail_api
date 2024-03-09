import sqlite3
from exceptions import ReviewExistsForProduct, ReviewRatingOutOfRange, ReviewNotFound, UserNotFound
from objects import Review

conn = sqlite3.connect("product_retail.db")
cursor = conn.cursor()

def submit_review(product_id, rating, user_id):
    if __did_customer_already_review_said_product(user_id, product_id):
        raise ReviewExistsForProduct
    
    if rating not in range(1, 11):
        raise ReviewRatingOutOfRange
    
    if not __does_user_exist(user_id):
        raise UserNotFound
    
    cursor.execute(f"insert into reviews(product_id, rating, user_id) values ('{product_id}', '{rating}', '{user_id}')")
    conn.commit()
    return True

def retrieve_review(review_id):
    if not __does_review_exist(review_id):
        raise ReviewNotFound
    
    review = cursor.execute(f"select * from reviews where review_id = '{review_id}'").fetchone()
    return Review(review[0], review[1], review[2], review[3])

def change_rating(review_id, n_rating):
    if not __does_review_exist(review_id):
        raise ReviewNotFound
    
    if n_rating not in range(1, 11):
        raise ReviewRatingOutOfRange
    
    cursor.execute(f"update reviews set rating = '{n_rating}' where review_id = '{review_id}'")
    conn.commit()
    return True

def delete_review(review_id):
    if not __does_review_exist(review_id):
        raise ReviewNotFound
    
    cursor.execute(f"delete from reviews where review_id = '{review_id}'")
    conn.commit()
    return True
    
def __does_user_exist(user_id):
    data = cursor.execute("select user_id from users").fetchall()
    for row in data:
        if row[0] == user_id:
            return True
        
    return False

def __does_review_exist(review_id):
    data = cursor.execute("select review_id from reviews").fetchall()
    for row in data:
        if row[0] == review_id:
            return True
        
    return False

def __did_customer_already_review_said_product(user_id, product_id):
    data = cursor.execute("select user_id, product_id from reviews").fetchall()
    for row in data:
        if row[0] == user_id and row[1] == product_id:
            return True
        
    return False