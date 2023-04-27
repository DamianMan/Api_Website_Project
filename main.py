from flask import Flask, render_template
import requests


app = Flask(__name__)


url = 'https://restcountries.com/v3.1/all?fields=name,capital,currencies'


response = requests.get(url)
data = response.json()

capitals = [lang['capital'] for lang in data][:50]


currencies = [lang['currencies'] for lang in data][:50]

cur = []
for n in range(len(currencies)):
    for l in currencies[n]:
        cur.append(l)
names = [name['name']['official'] for name in data][:50]



dict = dict(zip(names,cur))








@app.route("/")
def home():
    print(dict)

    return render_template("index.html", name_cur=dict, capitals=capitals)




if "__main__" == __name__:
    app.run(debug=True)
