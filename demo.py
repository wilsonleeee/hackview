#coding=utf8

#Author: wilsonleeee
#Email: 773560195@qq.com

import time
import datetime
import MySQLdb
from flask import Flask,render_template
import json

app = Flask(__name__)

@app.route('/get',methods=['GET','POST'])
def get_time():

    db=MySQLdb.connect(host='10.1.12.45', port=3306, user='dog', passwd='123456', db='demo', connect_timeout=100)
    cur = db.cursor()
    localTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    cur.execute("select clock, value from history_uint where itemid = 25438 order by clock asc limit 100")
    datas = cur.fetchall()
    table_data = []
    for data in datas:
        timeStamp = data[0]
        dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
        otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
        tmp = [str(otherStyleTime),int(data[1])]
        table_data.append(tmp)
    return json.dumps(table_data)

@app.route('/', methods=['GET','POST'])
def get():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()