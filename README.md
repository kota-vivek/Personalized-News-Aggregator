# News Aggregator

This project is a Flask-based news aggregator that scrapes articles from various news sources, categorizes them using NLP, and provides access via a REST API.

## Table of Contents
- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)

## Introduction

This project is a news aggregator that scrapes articles from multiple news websites, categorizes them into different topics, and provides a REST API to retrieve and search for articles. The project also uses NLP to automatically classify articles into categories such as World News, Sports, Business, etc.

## Technologies Used

- **Python3** (e.g., version 3.8 or 3.9)
- **Flask** (for the API)
- **Selenium & BeautifulSoup** (for web scraping)
- **pandas** (for data manipulation)
- **spacy** (for NLP)

## Prerequisites

Before running this project, you need to have:
- **Python 3.x** installed.
- **pip** for package management. Ensure `pip` is available to install dependencies.
- **ChromeDriver** installed for Selenium (if scraping dynamic websites).


## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/news-aggregator.git
cd news-aggregator
```

2. Install Dependencies

Install all the required dependencies using the requirements.txt file:

```bash
pip install -r requirements.txt
```

This will install Flask, Selenium, BeautifulSoup, pandas, spacy, and other necessary packages.

## Running the Application

1. Start the Flask server:
```bash
python main.py
```

Visit http://127.0.0.1:5000/ to see the API in action.

## API Endpoints

- **GET /articles**
    Retrieves all articles.
    Query parameters: category, start_date, end_date.
- **GET /articles/{id}**
    Retrieves a specific article by ID.
- **GET /articles/search**
    Searches for articles by a keyword.

## Project Structure

```bash
news-aggregator/
│
├── main.py                # Flask application
├── assignment.ipynb       # Web scraper for news articles
├── news_articles.csv      # CSV file containing scraped articles
├── requirements.txt       # Dependencies
├── README.md              # Documentation
```