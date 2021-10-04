import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load('model.pkl')
pipeline = joblib.load('pipeline.pkl')
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    d = request.form.to_dict()
    test = pd.DataFrame([d.values()], columns=d.keys())
    test['total_cuisines'] = test.cuisines.map(lambda x: [i.strip() for i in str(x).split(",")]).apply(len)
    test['multi_type_restuarant'] = test.rest_type.map(lambda x: [i.strip() for i in str(x).split(",")]).apply(len)
    y_pred = model.predict(pipeline.transform(test)) 
    y_pred_corrected = np.where(y_pred==1,"Success","Failure")
    return render_template('index.html', prediction_text='Restaurant wil be: {}'.format(y_pred_corrected[0]))


if __name__ == "__main__":
    app.run(debug=True)