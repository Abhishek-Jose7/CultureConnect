import wikipedia
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    image = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    wikipedia_link = db.Column(db.String(200), nullable=False)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/signin')
def signin():
    return render_template("signin.html")

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route("/country/<name>")
def country(name):
    country = Country.query.filter_by(name=name).first_or_404()

    query = f"{name} culture and traditions"
    try:
        wiki_page = wikipedia.page(query)
        content = wiki_page.content

        sections = [
            section for section in content.split("\n\n") 
            if any(keyword in section.lower() for keyword in ["culture", "tradition", "heritage", "history"])
        ]
        country_info = sections[:5]  

        country_images = wiki_page.images[:10]  
    except wikipedia.exceptions.DisambiguationError as e:
        country_info = [f"Multiple entries found. Please refine your search: {e.options}"]
        country_images = []
    except wikipedia.exceptions.PageError:
        country_info = ["Could not find information for this country."]
        country_images = []
    except wikipedia.exceptions.WikipediaException as e:
        country_info = [f"An error occurred while fetching data: {e}"]
        country_images = []

    
    if not country_images:
        country_images = [url_for('static', filename='default_country.jpg')]


    return render_template(
        "country.html",
        country=country,
        country_info=country_info,
        country_images=country_images,
        wikipedia_link=wiki_page.url if 'wiki_page' in locals() else None
    )

if __name__ == "__main__":
    app.run(debug=True)
