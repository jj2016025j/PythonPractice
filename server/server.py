# 不過這邊沒有網頁可以渲染
from flask import Flask, render_template
from flask_cors import CORS
import os

app = Flask(__name__, template_folder='./templates')
CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5050"}})
# 这将允许所有来源的跨域请求

# def open_browser():
#       webbrowser.open_new('http://127.0.0.1:5000/')

# if __name__ == '__main__':
#     # if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
#     #     threading.Timer(0, open_browser).start()

@app.route('/')
def home():
    print("Current working directory:", os.getcwd())
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(405)
def method_not_allowed_error(error):
    return render_template('405.html'), 405

if __name__ == '__main__':
    app.run(debug=True,port=5050)
    