from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import pickle as pkl

model = pkl.load(open("model.pkl","rb"))

# flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", image_name="b-1.png")

@app.route('/predict', methods=['POST'])
def predict():
    feature = request.form["feature"]
    featurs_lst = feature.split(',')
    np_features = np.asanyarray(featurs_lst,dtype=np.float32)
    pred = model.predict(np_features.reshape(1,-1))


    output = "cancrous" if pred[0] == '1' else "not cancrous"
    
    return render_template('index.html', message=output)

# paython main
if __name__ == "__main__":
    app.run(debug=True)
