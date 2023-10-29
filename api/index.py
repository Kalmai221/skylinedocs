from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    shownews = True
    card_header = 'Latest News'
    card_title = 'Flume V3.0.3 Release'
    card_text = 'This update comes with new Sever Utility Command!'
    card_link = '/'
    card_button_text = 'Go somewhere'
    
    return render_template('home.html', shownews=shownews, card_header=card_header, card_title=card_title, card_text=card_text, card_link=card_link, card_button_text=card_button_text)

@app.route('/documentation')
def documentation():
    return render_template('documentation.html')

if __name__ == '__main__':
    app.run(debug=True)
