from flask import Flask,request
app=Flask(__name__)

@app.route('/news')
def news():
	return "All the latest news will be made available to all the students"
if __name__=='__main__':
	app.run(debug=True)