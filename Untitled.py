import time
import _thread
from flask import Flask, render_template,redirect

app=Flask(__name__)

@app.route('/headlines')
def enterdetail(a) -> 'html' :
    return render_template('entry.html',the_title="Welcome to the headlines",content=a)

def fun(thread,de) :
    while(1) :
        time.sleep(de)
        todos=open("news.txt",'r')
        for i in todos :
            if (len(i)<50 and i[0]!=" "):
                enterdetail(i)
        todos.close()

if __name__="__main__" :
    app.run(debug==True)
