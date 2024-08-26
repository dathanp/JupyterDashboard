from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
  """CRUD operations for Animal collection in Mongo DB"""
  def __init__(self, USER, PASS, HOST, PORT, DB, COL):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        #USER = 'aacuser'
        #PASS = 'iamastudent'
        #HOST = 'nv-desktop-services.apporto.com'
        #PORT = 31850
        #DB = 'AAC'
        #COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
# Complete this create method to implement the C in CRUD.

# data should be a dictionary with the document info

# returns true if insert was successful, if not then false

  def create(self, data):
    if data is not None:
      result = self.collection.insert_one(data) # data should be dictionary
      return result.acknowledged # return true if insert was acknowledged
    else:
      raise Exception("Nothing to save, because data parameter is empty")
      return False

# Create method to implement the R in CRUD.
  
  # query is a dictionary representing the search criteria
  
  # returns a cursor containing the results if query worked
  # returns error message if not
  def read(self, query):
    try:
      result = list(self.collection.find(query))
      return result
    except Exception as e:
      return []
    
  # Creation of update method
  def update(self, query, update_values, multiple=False):
    # Update objects in collection
    """ query is used to match objects for updating,
        update_values is going to be the values to be updated
        multiple is a boolen so if true it will update multiple objects
        if false then it updates a single object
        
        update method will return the number of objects modified"""
    try:
      if multiple:
        result = self.collection.update_many(query, {'$set': update_values})
      else:
        result = self.collection.update_one(query, {'$set': update_values})
      
      return result.modified_count
    except Exception as e:
      return str(e)
    
  # Creation of delete method  
  def delete(self, query, multiple=False):
    """ query will match objects to delete
        multiple will delete many objects if true or one if false
        
        returns the number of objects removed"""
        
    try:
      if multiple:
        result = self.collection.delete_many(query)
      else:
        result = self.collection.delete_one(query)
        
      return result.deleted_count
    except Exception as e:
      return str(e)
