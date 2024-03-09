import sqlite3
from exceptions import OrderNotFound, ProductNotFound, UserNotFound
from objects import Order

conn = sqlite3.connect("product_retail.db")
cursor = conn.cursor()

def upload_order(product_id, user_id):
    if not __does_product_id_exist(product_id):
        raise ProductNotFound
    if not __does_user_id_exist(user_id):
        raise UserNotFound
    
    cursor.execute(f"insert into orders(product_id, user_id) values('{product_id}', '{user_id}')")
    conn.commit()
    return True

def retrieve_order(order_id):
    if not __does_order_exist(order_id):
        raise OrderNotFound
    
    order = cursor.execute(f"select * from orders where order_id = '{order_id}'").fetchone()
    return Order(order[0], order[1], order[2])

def update_order(order_id, n_product_id=None, n_user_id=None):
    if not __does_order_exist(order_id):
        raise OrderNotFound
    if not __does_product_id_exist(n_product_id) and n_product_id is not None:
        raise ProductNotFound
    if not __does_user_id_exist(n_user_id) and n_user_id is not None:
        raise UserNotFound
    
    if n_product_id is not None:
        cursor.execute(f"update orders set product_id = '{n_product_id}' where order_id = '{order_id}'")
        conn.commit()
    if n_user_id is not None:
        cursor.execute(f"update orders set user_id = '{n_user_id}' where order_id = '{order_id}'")
        conn.commit()
        
    return True

def delete_order(order_id):
    if not __does_order_exist(order_id):
        raise OrderNotFound
    
    cursor.execute(f"delete from orders where order_id = '{order_id}'")
    conn.commit()
    return True

def __does_user_id_exist(user_id):
    data = cursor.execute("select user_id from users").fetchall()
    for row in data:
        if row[0] == user_id:
            return True
        
    return False

def __does_product_id_exist(product_id):
    data = cursor.execute("select product_id from products").fetchall()
    for row in data:
        if row[0] == product_id:
            return True
        
    return False

def __does_order_exist(order_id):
    data = cursor.execute("select order_id from orders").fetchall()
    for row in data:
        if row[0] == order_id:
            return True
        
    return False