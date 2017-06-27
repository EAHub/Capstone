from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/Page1')

@app.route('/Page1', methods=['GET','POST'])
def Page1():
  return render_template('Page1.html')

@app.route('/Page2', methods=['GET','POST'])
def Page2():
	return render_template('Page2.html')

@app.route('/Page3', methods=['GET','POST'])
def Page3():
	return render_template('Page3.html')

if __name__ == '__main__':
  app.run(port=33507)
