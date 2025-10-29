from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

# create an instance of Flask
app = Flask(__name__) 

boostrap = Bootstrap5(app)

# route decorator binds a function to a URL

@app.route('')
def t_test():
    return render_template('template2.html')

if __name__ == '__main__':
    app.run()
