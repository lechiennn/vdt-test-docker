from flask import Flask
from pymongo import MongoClient
app = Flask(__name__)
print('start')
@app.route('/')
def hello():
    client = MongoClient('mongodb://db:27017')
    db = client.attendee
    counter =  db.counter.find_one({'_id': 1})
    if counter is None:
        counter = {'_id': 1, 'count': 0}
        db.counter.insert_one(counter)
    else:
        db.counter.update_one({'_id': 1}, {'$inc': {'count': 1}})
    #db = client.testDMBS
    #customer = db.Customer.find_one({'customerId':8})
    
    return 'Hello, World! You have visited this page {} time'.format(counter['count'])
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
