import pymongo as pymongo
import dns

CONN = "mongodb+srv://themis:SDGXRHVSWQGHNDZW@cluster0.o6smuif.mongodb.net/?retryWrites=true&w=majority&connectTimeoutMS=60000"

# client
client = pymongo.MongoClient(CONN)

# databases
themis_db = client["themis_db"]

# collections
opinions_col = themis_db["opinions"]

