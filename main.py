from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime
from data import Data

app = Flask(__name__)

# Connect to the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sample.db'
db = SQLAlchemy(app)


# Define your model class
class Insight(db.Model):
    __tablename__ = "insights"
    id = db.Column(db.Integer, primary_key=True)
    end_year = db.Column(db.Integer, nullable=True)
    intensity = db.Column(db.Integer, nullable=True)
    sector = db.Column(db.String, nullable=True)
    topic = db.Column(db.String, nullable=True)
    insight = db.Column(db.String, nullable=True)
    url = db.Column(db.String, nullable=True)
    region = db.Column(db.String, nullable=True)
    start_year = db.Column(db.Integer, nullable=True)
    impact = db.Column(db.String, nullable=True)
    added = db.Column(db.DateTime, nullable=True)  # Allow NULL values for added
    published = db.Column(db.DateTime, nullable=True)  # Allow NULL values for published
    country = db.Column(db.String, nullable=True)
    relevance = db.Column(db.Integer, nullable=True)
    pestle = db.Column(db.String, nullable=True)
    source = db.Column(db.String, nullable=True)
    title = db.Column(db.String, nullable=True)
    likelihood = db.Column(db.Integer, nullable=True)


# Read data from the JSON file
with open('jsondata.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(len(data))

# Add data to the database within application context
with app.app_context():
    db.create_all()
    # Check if there is data in the 'insights' table
    if Insight.query.count() == 0:
        for item in data:
            end_year = int(item.get('end_year')) if item['end_year'] else None
            intensity = item.get('intensity') if item['intensity'] else None
            sector = item.get('sector') if item['sector'] else None
            topic = item.get('topic') if item['topic'] else None
            insight = item.get('insight') if item['insight'] else None
            url = item.get('url') if item['url'] else None
            region = item.get('region') if item['region'] else None
            start_year = int(item.get('start_year')) if item['start_year'] else None
            impact = item.get('impact') if item['impact'] else None
            # Parse added and published datetime strings if they are not empty
            added_str = item.get('added', '')
            published_str = item.get('published', '')

            # Check if added and published fields are not empty
            added = datetime.strptime(added_str, '%B, %d %Y %H:%M:%S') if added_str else None
            published = datetime.strptime(published_str, '%B, %d %Y %H:%M:%S') if published_str else None

            country = item.get('country') if item['country'] else None
            relevance = item.get('relevance') if item['relevance'] else None
            pestle = item.get('pestle') if item['pestle'] else None
            source = item.get('source') if item['source'] else None
            title = item.get('title') if item['title'] else None
            likelihood = item.get('likelihood') if item['likelihood'] else None

            insight = Insight(
                end_year=end_year,
                intensity=intensity,
                sector=sector,
                topic=topic,
                insight=insight,
                url=url,
                region=region,
                start_year=start_year,
                impact=impact,
                added=added,
                published=published,
                country=country,
                relevance=relevance,
                pestle=pestle,
                source=source,
                title=title,
                likelihood=likelihood
            )
            db.session.add(insight)

    # Commit the changes
    db.session.commit()

    # Close the session
    db.session.close()


@app.route('/')
def dashboard():
    intensity_data = Data.get_data("intensity", db.session.query(Insight.intensity, db.func.count()).group_by(Insight.intensity).all())
    likelihood_data = Data.get_data("likelihood", db.session.query(Insight.likelihood, db.func.count()).group_by(Insight.likelihood).all())
    region_data = Data.get_data("region", db.session.query(Insight.region, db.func.count()).group_by(Insight.region).all())
    topic_data = Data.get_data("topic", db.session.query(Insight.topic, db.func.count()).group_by(Insight.topic).all())
    country_data = Data.get_data("country", db.session.query(Insight.country, db.func.count()).group_by(Insight.country).all())
    relevance_data = Data.get_data("relevance", db.session.query(Insight.relevance, db.func.count()).group_by(Insight.relevance).all())
    return render_template('index.html', intensity=intensity_data, likelihood=likelihood_data,
                           region=region_data, topic=topic_data, country=country_data, relevance=relevance_data)


if __name__ == '__main__':
    app.run(debug=True)
