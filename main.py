'''
Part 3: REST API Development
    Objective:
        Create a REST API to serve the news articles.
        Endpoints:
            ● GET /articles: Retrieve all articles, with filtering options like by a date range, of a specific category.
            ● GET /articles/{id}: Retrieve a specific article.
            ● GET /search: Search articles by keywords.
'''


# Import required libraries
import pandas as pd
from flask import Flask, jsonify, request, abort
from datetime import datetime

# Initialize the Flask app
app = Flask(__name__)

# Load the CSV file containing the articles into a pandas DataFrame
df = pd.read_csv('news_articles.csv')

# Route to get all articles with optional filters for date range and category
@app.route("/articles")
def get_articles():
    # Create a copy of the DataFrame for filtering
    filtered_df = df.copy()

    # Get query parameters from the request
    start_date = request.args.get("start_date")  # Filter by start date
    end_date = request.args.get("end_date")  # Filter by end date
    category = request.args.get('category')  # Filter by category

    # Filter by category (if provided)
    if category:
        category = category.lower()  # Convert category to lowercase for case-insensitive comparison
        filtered_df = filtered_df[filtered_df['Category'].str.lower().str.contains(category)]

    # Filter by start date (if provided)
    if start_date:
        try:
            start_date1 = datetime.strptime(start_date, "%Y-%m-%d")  # Validate date format
            filtered_df = filtered_df[filtered_df['Date'] >= start_date]  # Filter articles after start date
        except ValueError:
            # Return a 400 error if the date format is invalid
            abort(400, description="Invalid start_date format. Use YYYY-MM-DD.")

    # Filter by end date (if provided)
    if end_date:
        try:
            end_date1 = datetime.strptime(end_date, "%Y-%m-%d")  # Validate date format
            filtered_df = filtered_df[filtered_df['Date'] <= end_date]  # Filter articles before end date
        except ValueError:
            # Return a 400 error if the date format is invalid
            abort(400, description="Invalid end_date format. Use YYYY-MM-DD.")

    # Convert the filtered DataFrame to a list of dictionaries (JSON-friendly format)
    articles = filtered_df.to_dict(orient="records")

    # Return the filtered articles as a JSON response
    return jsonify(articles), 200

# Route to get a specific article by its ID (row index)
@app.route("/articles/<int:id>")
def get_article_by_id(id):
    # Check if the provided ID is valid (in the range of article indices)
    if id < 0 or id >= len(df):
        abort(400, description="Article Not Found")  # Return a 400 error if the article is not found

    # Convert the specific row (article) to a dictionary and return it
    article = df.iloc[id].to_dict()
    return jsonify(article), 200

# Route to search for articles based on a keyword in the title, summary, or category
@app.route("/articles/search")
def search_articles():
    keyword = request.args.get('keyword')  # Get the keyword from the request query parameter

    # Validate the keyword (ensure it has at least 3 characters)
    if not keyword or len(keyword) < 3:
        abort(400, description="Please provide a valid keyword with at least 3 characters.")

    # Convert the keyword to lowercase for case-insensitive search
    keyword = keyword.lower()

    # Search for the keyword in the title, summary, or category columns
    filtered_df = df[
        df['Title'].str.lower().str.contains(keyword) |
        df['Summary'].str.lower().str.contains(keyword) |
        df['Category'].str.lower().str.contains(keyword)
    ]

    # Convert the filtered DataFrame to a list of dictionaries (JSON-friendly format)
    articles = filtered_df.to_dict(orient='records')

    # Return the matching articles as a JSON response
    return jsonify(articles), 200

# Root route for testing the server (optional)
@app.route("/")
def home():
    return "Hello, welcome to the News API!"

# Main entry point of the application
if __name__ == "__main__":
    # Run the Flask app in debug mode
    app.run(debug=True)