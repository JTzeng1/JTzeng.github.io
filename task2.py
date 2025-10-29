from flask import Flask

app = Flask(__name__)

@app.route('')
def class_abbreviations():
    acronyms = [
        "Hima.: PEBCAK",
        "Justin.: idk",
        "Imane.: fyi",
        "Mathew.: lmao"
    ]

    webpage = "<h1>Favorite Acronyms</h1>"
    for item in acronyms:
        webpage += f"<p>{item}</p>"
    
    return webpage

if __name__ == '__main__':
    app.run()
