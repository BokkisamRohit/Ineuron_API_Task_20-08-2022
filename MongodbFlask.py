import pymongo
from flask import Flask, request, jsonify, Response

app = Flask(__name__)
client = pymongo.MongoClient(
    "mongodb+srv://BRohit:Rohit2406@bokkisam-rohit.tcdrz.mongodb.net/?retryWrites=true&w=majority")
database = client['student']
collection = database["table"]


@app.route('/insertData', methods=['POST'])
def insertRecords():
    res = request.json
    collection.insert_many(res)
    return Response(status=204)


@app.route('/fetchData', methods=['GET'])
def fetchStudentRecords():
    d = collection.find()
    sl = list()
    for i in d:
        sl.append(i)
    return jsonify(str(sl))


@app.route('/deleteData', methods=['GET'])
def deleteRecord():
    collection.delete_one({'studentName': "Rohit"})
    return Response(status=204)


@app.route('/updateData', methods=['GET'])
def updateRecord():
    collection.update_one({'studentName': "Rohit"}, {'$set': {'studentMarks': 93}})
    return Response(status=204)


if __name__ == '__main__':
    app.run()
