from dotenv import load_dotenv
from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    load_dotenv()
    app.run()