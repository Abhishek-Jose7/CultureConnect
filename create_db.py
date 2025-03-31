from app import app, db, Country

# Ensure the Flask application context is active when performing DB operations
with app.app_context():
    # Create all tables in the database
    db.create_all()

    # Delete all existing countries to reset the table
    db.session.query(Country).delete()

    # Define the countries to be added to the database
    countries = [
         Country(name="India", image="india.jpg", description="Description of India", wikipedia_link="https://en.wikipedia.org/wiki/India"),
            Country(name="Japan", image="japan.jpg", description="Description of Japan", wikipedia_link="https://en.wikipedia.org/wiki/Japan"),
            Country(name="China", image="china.jpg", description="Description of China", wikipedia_link="https://en.wikipedia.org/wiki/China")
    ]
    
    # Add each country to the session
    for country in countries:
        db.session.add(country)

    db.session.commit()

    print("Database initialized with sample data!")
