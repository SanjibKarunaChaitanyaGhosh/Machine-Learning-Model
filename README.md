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
```
# Machine-Learning-Model deployment done

###  INPUT
## 1st Input - NOT Cancerous
```bash
-0.24295555, -0.46649743, -0.13728933, -0.44421138, -0.48646498,         0.28085007,  0.04160589, -0.11146496, -0.26486866,  0.41524141,         0.13513744, -0.02091509, -0.29323907, -0.17460869, -0.2072995 ,        -0.01181432, -0.35108921, -0.1810535 , -0.24238831, -0.33731758,        -0.0842133 , -0.2632354 , -0.14784208, -0.33154752, -0.35109337,         0.48001942, -0.09649594, -0.03583041, -0.19435087,  0.17275669,         0.20372995
```

## 2nd Input - NOT Cancerous
```bash
-0.23711093, -0.4976419 ,  0.61365274, -0.49813131, -0.53102815,        -0.57694824, -0.17494424, -0.36215622, -0.284859  ,  0.43345165,         0.17818232, -0.36844966,  0.55310406, -0.31671104, -0.40524636,         0.04025752, -0.03795529, -0.18043065,  0.16478901, -0.12170969,         0.23079329, -0.50044002,  0.81940367, -0.46922838, -0.53308833,        -0.04910117, -0.04160193, -0.14913653,  0.09681787,  0.10617647,         0.49035329
```

## 3rd Input - Cancerous
```bash
-0.23712621,  1.36536344,  0.49866473,  1.30551088,  1.34147086,        -0.40653902, -0.0137241 ,  0.24063659,  0.82144876, -0.83398079,        -1.13121527,  1.36745547, -0.74874907,  1.27009847,  1.18638199,        -0.83350144, -0.49043919, -0.31559   ,  0.28726031, -0.82243534,        -0.76235747,  1.79461875,  0.17237239,  1.76366112,  1.7441412 ,        -0.53051417, -0.12362004, -0.02818105,  0.99177862, -0.561211  ,        -1.00838949
```

## 4th Input - NOT Cancerous
```bash
-0.2371001 , -0.70149659, -0.20065007, -0.68788006, -0.68220445,         1.32703326, -0.03661927, -0.22925206, -0.35324702, -0.03637245,         0.3392535 , -0.33945899,  0.83953022, -0.33991142, -0.4122402 ,         0.50792161, -0.13641493, -0.10506529,  0.33179533, -0.60315231,         0.00702008, -0.64401124,  0.61473051, -0.64770356, -0.62655473,         1.61632758,  0.08562302,  0.06074275,  0.11673994, -0.15697394,         0.39836459
```

## 5th Input - NOT Cancerous
```bash
-0.23712699, -1.44075296, -0.43531947, -1.36208497, -1.1391179 ,         0.78057331,  0.71892128,  2.82313451, -0.11914956,  1.09266219,         2.45817261, -0.26380039, -0.01605246, -0.47041357, -0.47476088,         0.83836493,  3.25102691,  8.43893667,  3.39198733,  2.62116574,         2.06120787, -1.23286131, -0.47630949, -1.24792009, -0.97396758,         0.72289445,  1.18673232,  4.67282796,  0.9320124 ,  2.09724217,         1.88645014
```

## 6th Input - Cancerous
```bash
-0.24355432,  0.38006578,  0.06921974,  0.40410139,  0.26659607,         0.96752014,  0.35641445,  0.72690205,  0.85722095,  0.43709369,        -0.66605282,  0.25555697, -0.77018483,  0.11394607,  0.17460653,        -0.24531887, -0.58082836, -0.14617367, -0.15331827, -0.80895985,        -0.48829815,  0.62940306,  0.07663816,  0.53383214,  0.49204412,         1.00046591, -0.08616295,  0.4996247 ,  0.57035018, -0.10783139,        -0.20629287
```