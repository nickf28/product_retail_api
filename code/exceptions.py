

# USER EXCEPTIONS
class UserAlreadyExists(Exception):
    def __init__(self, message="User already exists in table, cannot have users with a duplicate username or email."):
        self.message = message
        super().__init__(self.message)
        
class UserNotFound(Exception):
    def __init__(self, message="User not found."):
        self.message = message
        super().__init__(self.message)
        
class InvalidSignIn(Exception):
    def __init__(self, message="User is not found in the system or credentials are incorrect, try again."):
        self.message = message
        super().__init__(self.message)
        
# PRODUCT EXCEPTIONS
class ProductAlreadyExists(Exception):
    def __init__(self, message="Product with same title name already exists in the database."):
        self.message = message
        super().__init__(self.message)
        
class ProductNotFound(Exception):
    def __init__(self, message="Product with title not found within the table."):
        self.message = message
        super().__init__(self.message)
        
# ORDER EXCEPTIONS
class OrderNotFound(Exception):
    def __init__(self, message="Order not found in the table."):
        self.message = message
        super().__init__(self.message)
        
# REVIEW EXCEPTIONS
class ReviewExistsForProduct(Exception):
    def __init__(self, message="Said customer has already reviewed this product."):
        self.message = message
        super().__init__(self.message)
        
class ReviewRatingOutOfRange(Exception):
    def __init__(self, message="Rating must be from 1 - 10."):
        self.message = message
        super().__init__(self.message)
        
class ReviewNotFound(Exception):
    def __init__(self, message="Review does not exist."):
        self.message = message
        super().__init__(self.message)