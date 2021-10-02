from user import User
from privilege import Privilege
class Admin(User):
    
    def __init__(self, first_name, last_name, address, telephone):
        self.privileges = Privilege()
        super().__init__( first_name, last_name, address, telephone)
