from flask import Flask, render_template, json
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/test')
def test():
    my_dict = {'name':'Canadiens','city':'Montréal','sport':'Hockey'}
    return json.dumps(my_dict, encoding='utf-8')

if __name__ == '__main__':
    app.run(debug=True)
