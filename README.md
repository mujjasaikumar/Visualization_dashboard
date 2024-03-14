
# Data Visualization Dashboard

This project is a Data Visualization Dashboard built using Flask, JavaScript, and Google Charts. It provides visualizations for various variables extracted from a SQLite database. The dashboard allows users to interact with the data and gain insights into different aspects.

## Features

- **Dynamic Visualizations**: Visualizations are dynamically generated based on the data stored in the SQLite database.
- **Interactive Charts**: Charts are interactive, allowing users to explore the data by zooming, panning, and hovering over data points.
- **Responsive Design**: The dashboard is designed to be responsive, ensuring optimal viewing experience across different devices and screen sizes.
- **Multiple Variable Visualizations**: Users can visualize multiple variables including Intensity, Likelihood, Relevance, Country, Topics, and Region.
- **Data Filtering**: The dashboard supports filtering of data based on different criteria, enabling users to focus on specific subsets of data.

## Setup Instructions

1. **Clone the Repository**:
   ```
   git clone https://github.com/mujjasaikumar/Visualization_dashboard.git
   ```

2. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. **Run the Flask App**:
   ```
   python main.py
   ```

4. **Access the Dashboard**:
   Open a web browser and navigate to `http://localhost:5000` to access the dashboard.

## Project Structure

- **main.py**: Contains the Flask application logic, including routes and database setup.
- **data.py**: Provides functions for data processing and querying the database.
- **templates/index.html**: HTML template file for the dashboard frontend.

## Database

- **Database File**: The SQLite database file (`sample.db`) is automatically created and populated with data from the provided JSON file (`jsondata.json`).
- **Schema Definition**: The database schema is defined using SQLAlchemy ORM in the `Insight` model class.

## Visualizations

The dashboard provides visualizations for the following variables:

1. **Intensity Distribution**: Shows the distribution of intensity values.
2. **Likelihood Distribution**: Displays the distribution of likelihood values.
3. **Relevance Distribution**: Visualizes the distribution of relevance values.
4. **Country Distribution**: Shows the distribution of data across different countries.
5. **Topic Distribution**: Displays the distribution of data across different topics.
6. **Region Distribution**: Visualizes the distribution of data across different regions.

---
- Saikumar Mujja

