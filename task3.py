from flask import Flask, render_template

app = Flask(__name__)

@app.route('/Justin')
def justin():
    name = "Justin"
    acronym = "idk" 
    meaning = "I don't know"
    why = "Because I often find myself unsure about things."
    return render_template("template.html", name=name, acronym=acronym, meaning=meaning, why=why)

if __name__ == '__main__':
    app.run()

