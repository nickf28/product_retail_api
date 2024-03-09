

class Game:
    def __init__(self, title, genre, release_date, price):
        self.title = title
        self.genre = genre
        self.release_date = release_date
        self.price = price
        
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Game):
            return False
        
        return (self.title == __value.title and self.genre == __value.genre and self.release_date == __value.release_date and self.price == __value.price)
        
    def __str__(self):
        return display(self.title, self.genre, self.release_date, self.price)
        
class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, User):
            return False
        
        return (self.username == __value.username and self.email == __value.email and self.password == __value.password)
        
    def __str__(self):
        return display(self.username, self.email, self.password)
        
class Order:
    def __init__(self, order_id, product_id, user_id):
        self.order_id = order_id
        self.product_id = product_id
        self.user_id = user_id
        
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Order):
            return False
        
        return (self.order_id == __value.order_id and self.product_id == __value.product_id and self.user_id == __value.user_id)
        
    def __str__(self):
        return display(f"Order ID: {self.order_id}", f"Product ID: {self.product_id}", f"User ID: {self.user_id}")
        
class Review:
    def __init__(self, review_id, product_id, rating, user_id):
        self.review_id = review_id
        self.product_id = product_id
        self.rating = rating
        self.user_id = user_id
        
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Review):
            return False
        
        return (self.review_id == __value.review_id and self.product_id == __value.product_id and self.rating == __value.rating and self.user_id == __value.user_id)
        
    def __str__(self):
        return display(f"Review ID: {self.review_id}",f"Product ID: {self.product_id}", f"Rating: {self.rating}", f"User ID: {self.user_id}")

def display(*args):
    out = ""
    
    for arg in args:
        out += str(arg) + "\n"
        
    return out