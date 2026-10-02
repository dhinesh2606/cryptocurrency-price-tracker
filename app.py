from flask import Flask, render_template_string
import pandas as pd
import webbrowser

# Create Flask app
app = Flask(__name__)


@app.route("/")
def home():

    # Read CSV file
    df = pd.read_csv("crypto_prices.csv")

    # Get latest 10 records
    latest_data = df.tail(10)

    # Convert data into HTML table
    table = latest_data.to_html(
        index=False,
        classes="crypto-table"
    )

    # Webpage HTML
    html = f"""
    <!DOCTYPE html>
    <html>

    <head>
        <title>Cryptocurrency Price Tracker</title>

        <style>

            body {{
                font-family: Arial;
                background-color: #f2f2f2;
                padding: 30px;
            }}

            h1 {{
                text-align: center;
            }}

            h2 {{
                text-align: center;
            }}

            .crypto-table {{
                width: 100%;
                border-collapse: collapse;
                background: white;
            }}

            .crypto-table th,
            .crypto-table td {{
                border: 1px solid #ddd;
                padding: 10px;
                text-align: center;
            }}

            .crypto-table th {{
                background-color: #333;
                color: white;
            }}

        </style>

    </head>

    <body>

        <h1>💰 Cryptocurrency Price Tracker</h1>

        <h2>Latest 10 Cryptocurrency Records</h2>

        {table}

    </body>

    </html>
    """

    return render_template_string(html)


# Start Flask server and open Chrome automatically
if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=True)