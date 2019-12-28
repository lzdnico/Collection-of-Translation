# coding=utf-8
import sys
import flask_restful
import  requests
import urllib3
import urllib
import urllib.parse
import api.trans
from flask import Flask,render_template,request


urllib3.disable_warnings()


app = Flask(__name__)


@app.route('/',methods=['GET', 'POST'])
def login():
    try:
        if request.method == "POST":
            if request.form['submit'] == '🔥 点击翻译 🍩':
                s = request.form['trans']
                ans = api.trans.translate(s)
                google = ans[0]
                baidu  = ans[1]
                youdao = ans[2]           
                return render_template('index.html',ori=s,to1=google,to2=baidu,to3=youdao)
            if request.form['submit'] == '🔥 点击翻译定义 🍩':
                s = request.form['trans']
                ans = api.trans.cnki(s)        
                return render_template('cnki.html',ori=s,to1=ans)
        return render_template('index.html')
    except:
        return render_template('index.html')

  
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False,port=10068)            #自定义端口