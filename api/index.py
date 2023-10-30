from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    shownews = True
    card_header = 'Latest News'
    card_time = "30/10/2023"
    card_title = 'Flume V3.0.3 Release'
    card_text = 'This update comes with new Sever Utility Command!'
    card_link = '/'
    card_button_text = 'Go somewhere'
    
    return render_template('home.html', shownews=shownews, card_header=card_header,card_time = card_time , card_title=card_title, card_text=card_text, card_link=card_link, card_button_text=card_button_text)

@app.route('/docs')
def documentation():
    return render_template('docs.html')

# Custom 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
