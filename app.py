from flask import Flask, render_template, request, redirect

app=Flask(__name__)

posts=[]

@app.route('/')
def index():
	return render_template('index.html', posts=posts)

@app.route('/post', methods=['POST'])
def post():
	print(request.form)
	if 'message' in request.form:
		message = request.form['message']
		posts.append(message)
	else:
		return "oshibka soosbshenie ne bilo otpr", 400
	return redirect('/')

if __name__ == '__main__':
	app.run(debug=True)
