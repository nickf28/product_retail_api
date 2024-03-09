import sqlite3
from objects import Game
from exceptions import ProductAlreadyExists, ProductNotFound

conn = sqlite3.connect("product_retail.db")
cursor = conn.cursor()

def upload_product(product: Game):
    if not isinstance(product, Game):
        raise TypeError
    
    if __does_product_exist(product.title):
        raise ProductAlreadyExists

    cursor.execute(f"insert into products (title, genre, release_date, price) values ('{product.title}', '{product.genre}', '{product.release_date}', '{product.price}')")
    conn.commit()
    return True

def retrieve_product(title):
    if not __does_product_exist(title):
        raise ProductNotFound
    
    product = cursor.execute(f"select title, genre, release_date, price from products where title = '{title}'").fetchone()
    return Game(product[0], product[1], product[2], product[3])

def modify_product(title, n_title=None, n_genre=None, n_rel_date=None, n_price=None):
    if not __does_product_exist(title):
        raise ProductNotFound
    
    actual_product = retrieve_product(title)
    
    if n_title is not None:
        cursor.execute(f"update products set title = '{n_title}' where title = '{actual_product.title}'")
        conn.commit()
    if n_genre is not None:
        cursor.execute(f"update products set genre = '{n_genre}' where title = '{title}'")
        conn.commit()
    if n_rel_date is not None:
        cursor.execute(f"update products set release_date = '{n_rel_date}' where title = '{title}'")
        conn.commit()
    if n_price is not None:
        cursor.execute(f"update products set price = '{n_price}' where title = '{title}'")
        conn.commit()
        
    return True
    
def delete_product(title):
    if not __does_product_exist(title):
        raise ProductNotFound
    
    cursor.execute(f"delete from products where title = '{title}'")
    conn.commit()
    return True

def __does_product_exist(title):
    data = cursor.execute("select title from products").fetchall()
    for row in data:
        if row[0] == title:
            return True
        
    return False