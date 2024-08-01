pip install transformers torch flask

from flask import Flask, request, render_template
from transformers import pipeline

app = Flask(__name__)

# Load the summarization pipeline
summarizer = pipeline("summarization")

# Function to summarize text
def summarize_text(text):
    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    if request.method == "POST":
        text = request.form["text"]
        summary = summarize_text(text)
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
