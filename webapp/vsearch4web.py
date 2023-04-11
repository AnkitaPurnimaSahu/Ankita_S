import html
from flask import Flask, render_template, request, redirect, escape
from vowels_function_module import search4letters

app = Flask(__name__)

# @app.route('/') #this is a function decorator
# def hello() -> '302':
#     return redirect('/entry')


# @app.route('/search4', methods=['POST'])
# def do_search() -> str:
#     # return str(search4letters('life, the universe, and everything!', 'eiru,!'))
#     phrase = request.form['phrase']
#     letters = request.form['letters']
#     return str(search4letters(phrase, letters))

def log_request(req: 'flask_request', res: str) -> None:
    with open ('webapp\\vsearch.log', 'a') as log:
        # print(str(dir(req)), res, file = log)
        # print(req.form, file = log, end='|')
        # print(req.remote_addr, file = log, end='|')
        # print(req.user_agent, file = log,  end='|')
        # print(res.form, file = log)
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    # return str(search4letters('life, the universe, and everything!', 'eiru,!'))
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html', the_phrase = phrase, the_letters = letters, the_title = title, the_results = results,)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title = 'Welcome to search4letters on the web')


@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with open('webapp\\vsearch.log') as log:
    #     contents = log.readlines()
    # return escape(''.join(contents))
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    # return str(contents)
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html', the_title='View Log', the_row_titles=titles, the_data=contents,) 
        
if __name__ =='__main__':
    app.run(debug=True)