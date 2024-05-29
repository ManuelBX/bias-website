from flask import Flask, render_template, request, redirect, url_for
import sys
from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

def analysisResult(url):
    if len(url) == 0:
        return ""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Give the following URL a bias score followed by a brief explanation. The result should be formatted as follows [score] Bias Score, explaination."
            },
            {
                "role": "user",
                "content": url
            },
        ],
        temperature=1,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    res = str(response.choices[0])
    try:
        k = res.index("[")
        j = res.rindex(".") + 1

    except ValueError:
        return res

    return res[k:j]

app = Flask(__name__)


'''
@app.route('/')
def index():  # put application's code here
    return render_template("test.html")


@app.route('/#', methods=["POST"])
def result():
    if request.method == "POST":
       search = request.form["search"]
       return redirect(url_for("result", search=search))
    else:
       return render_template("index.html")
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        url = request.form.get('url')
        result = analysisResult(url)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run()
