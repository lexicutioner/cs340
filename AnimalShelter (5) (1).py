from pymongo import MongoClient
class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username=None, password=None):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        if username and password:
            self.client = MongoClient('mongodb://%s:%s@localhost:46663' % (admin, Admin1))
        else:
            self.client = MongoClient('mongodb://localhost:46663')
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary 
            print('Successfully created')
            return True
        else:
            print('Failed. Data parameter is empty, nopthing to save.')           
            return False

# Create method to implement the R in CRUD.
    def read(self, data):
	  if data is not None:
            print(self.database.animals.find(data))  # data should be dictionary 
            return True
        else:
            print('No results. Data parameter is empty.')           
            return False

# Create method to implement the U in CRUD
    def update(self, keyValue, updateValue):
	  if updateValue is not None:
		self.database.animals.update(keyValue, updateValue) # data should be dictionary
		return True
	  else:
            print('Failed. Data parameter is empty, nopthing to save.')           
            return False

# Create method to implement the D in CRUD
    def delete(self, keyValue):
	  if keyValue is not None:
		self.database.animals.remove(keyValue, updateValue) # data should be dictionary
		return True
	  else:
            print('Failed. Data parameter is empty, nopthing to delete.')           
            return False