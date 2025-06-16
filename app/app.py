from flask import Flask, render_template
from google.cloud import bigquery
from google.api_core import exceptions
import os

app = Flask(__name__)


@app.route('/')
def index():
    # Initialize BigQuery client
    client = bigquery.Client()

    # Define the query
    query = """
    SELECT name, COUNT(*) as count
    FROM `bigquery-public-data.usa_names.usa_1910_current`
    GROUP BY name
    ORDER BY count DESC
    LIMIT 10
    """

    try:
        # Execute the query
        query_job = client.query(query)
        results = query_job.result()  # Wait for the job to complete

        # Convert results to a list of dictionaries
        names = [{"name": row.name, "count": row.count} for row in results]

    except exceptions.GoogleAPIError as e:
        return f"An error occurred: {e}"

    return render_template('index.html', names=names)