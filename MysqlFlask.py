import mysql.connector as conn
from flask import Flask, request, jsonify, Response

app = Flask(__name__)


@app.route('/insertStudent', methods=['POST'])
def insertSingleRecord():
    mydb = conn.connect(host="localhost", user="root", passwd="Rohit2406", db="rohit")
    cursor = mydb.cursor()
    sno = request.json['STUNO']
    sname = request.json['STUNAME']
    smarks = request.json['STUMARKS']
    cursor.execute("insert into rohit.student VALUES(%s, %s, %s)", (sno, sname, smarks))
    mydb.commit()
    return Response(status=204)


@app.route('/deleteStudent', methods=['GET'])
def deleteSingleRecord():
    mydb = conn.connect(host="localhost", user="root", passwd="Rohit2406", db="rohit")
    cursor = mydb.cursor()
    sno = request.args.get('StudentNum')
    cursor.execute("delete from rohit.student where stdno=%s", [int(sno)])
    mydb.commit()
    return Response(status=204)


@app.route('/updateStudent', methods=['GET'])
def UpdateRecord():
    mydb = conn.connect(host="localhost", user="root", passwd="Rohit2406", db="rohit")
    cursor = mydb.cursor()
    sno = request.args.get('StudentNum')
    cursor.execute("update rohit.student set stdmarks=70 where stdno=%s", [int(sno)])
    mydb.commit()
    return Response(status=204)


@app.route('/fetchStudent', methods=['GET'])
def fetchRecords():
    mydb = conn.connect(host="localhost", user="root", passwd="Rohit2406", db="rohit")
    cursor = mydb.cursor()
    cursor.execute("select * from rohit.student")
    result = cursor.fetchall()
    return jsonify(result)


if __name__ == '__main__':
    app.run()
