from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    df = pd.read_csv("../traffic_dataset.csv")
    return df.to_html()

if __name__ == "__main__":
    app.run(debug=True)