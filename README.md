This project is a simple/minimal REST API written in Python served using Flask which leverages a Postgres database.

To run this project, first Postgres would need to be installed, the manual migration can then be run as this project takes a database first approach.

A simple pip install should handle Python dependencies.

Run the app with: flask run


Execute curl request or any other desired method for Web Request.

curl 127.0.0.1:5000/health -> GET basic system stats as JSON
curl 127.0.0.1:5000/cod/nutrition/refresh -> integrates with an external API returning their response and loads data to a database
curl 127.0.0.1:5000/cod/nutrition/{ID} -> GET the details for a sepcific record from the previous integration from the database
