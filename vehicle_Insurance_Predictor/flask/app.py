from flask import Flask, request, render_template
import pickle
import numpy as np

# creating a Flask app
app = Flask(__name__)

# loading the model
model = pickle.load(open('model.pkl','rb'))


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods = ['POST'])
def predict():
    if request.method == 'POST':
        output_msg = ''

        float_features = [float(x) for x in request.form.values()]
        final_features = np.array(float_features)

        predict_target = model.predict([final_features])

        if predict_target == 1:
            output_msg = 'Congratulations! You are eligible for a vehicle insurance. You will be contacted shortly by ' \
                         'our executive!'

        elif predict_target == 0:
            output_msg = 'We are so sorry, We can not proceed with vehicle insurance in your case!'

    return render_template('home.html', prediction_value=output_msg)


if __name__=='__main__':
    app.run(debug=True)
