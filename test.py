from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/result",methods=['POST'])
def result():
    n1=request.form['a']
    n1=int(n1)
    n2=request.form['b']
    n2=int(n2)
    op=request.form['operation']
    data=0
    if op=='add':
        data=n1+n2
    elif op=='sub':
        data=n1-n2
    elif op=='muliply':
        data=n1*n2
    else :
        data=n1/n2
    return render_template('result.html',data=data)
if __name__=="__main__":
    app.run()
