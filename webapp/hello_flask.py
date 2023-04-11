from flask import Flask
import vowels_function_module

app = Flask(__name__)

@app.route('/') #this is a function decorator
def hello() -> str:
    return 'Hello world from Flask!'

@app.route('/search4')
def do_search() -> str:
    return str(vowels_function_module.search4letters('life, the universe, and everything!', 'eiru,!'))


app.run()