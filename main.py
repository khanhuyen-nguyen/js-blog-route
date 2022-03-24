from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template('')

@app.route('/history')
def history():
    return render_template('')

@app.route('/structure')
def structure():
    return render_template('')

@app.route('/activities')
def activities():
    return render_template('')

@app.route('/japan')
def japan():
    return render_template('')

@app.route('/stories')
def stories():
    return render_template('')    

if __name__ == "__main__":
    app.run(debug= True)
