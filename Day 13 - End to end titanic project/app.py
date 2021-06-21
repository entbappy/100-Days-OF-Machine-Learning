from flask import Flask, request, jsonify, render_template
import pickle

pipe = pickle.load(open('pipe.pkl', 'rb'))


app = Flask(__name__)


@app.route('/', methods=['GET']) # Rendering hompage
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])  #For calling the API from webapp
def execute():
    if (request.method == 'POST'):
        pclass = int(request.form['pclass'])
        sex = request.form['sex']
        age = float(request.form['age'])
        fare = float(request.form['fare'])
        embarked = request.form['embarked']
        family_type = request.form['family_type']

        list_data = [[pclass, sex,age,fare, embarked, family_type ]]

        prediction = pipe.predict(list_data)
        print(prediction)

        return render_template('show.html', prediction = prediction)


if __name__ == '__main__':
    app.run(debug=True)

