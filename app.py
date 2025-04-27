from flask import Flask,render_template,request

app = Flask(__name__)
@app.route('/',methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        number = int(request.form['number'])
        tonumber = int(request.form['tonumber'])
        ans = []
        for i in range(1,tonumber+1):
            r = number*i
            ans.append(r)
        return render_template('index.html',first=number,second=tonumber,ans=ans)
    
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)