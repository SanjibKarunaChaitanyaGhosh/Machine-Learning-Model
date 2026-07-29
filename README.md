# machine-Learning
conda activate myenv
conda install flask
conda install pandas
conda install numpy
conda install pickle

## create app.py

from flask import Flask,request,render_template

## Step 1: Create a new Conda environment

I recommend Python 3.11 because it's compatible with most deep learning libraries.
```bash
conda create -n breast_cancer python=3.11
```
Press y when prompted.

```bash
conda activate breast_cancer
conda deactivate
```
## step 2 :
```bash
ls
```
* output should be something like that
```bash
app.py
model.h5
requirements.txt
templates/
static/
```
## Step 3: Open requirements.txt
```bash
cat requirements.txt
```
* or
```bash
nano requirements.txt
```
## Step 4: If the file looks fine

Install everything:
```bash
pip install -r requirements.txt
```

## Step-5: if you want to use conda then 
conda install flask=3.0.3
conda install pandas=2.2.3
conda install numpy=1.26.4

and install TensorFlow (if your project needs it):

pip install tensorflow==2.17.0
Which approach should you use?

Since you're using Conda, I recommend:

Use Conda for packages available on Conda (numpy, pandas, flask).
Use pip only for packages that are not available or are newer (such as some TensorFlow versions).

Run:
```bash
cat requirements.txt
```# Machine-Learning-Model
