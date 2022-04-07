from flask import Flask, render_template, request
app = Flask(__name__)

# methods is new
@app.route("/", methods={'POST', 'GET'})


def calculate():
    bmi = ''
    category = ""
    if request.method=='POST' and 'userFeet' in request.form and 'userInches' in request.form and 'userPounds':
        ft=float(request.form.get('userFeet'))
        inch=float(request.form.get('userInches'))
        weight=float(request.form.get('userPounds'))
        # total inches
        totalinches=(ft*12) + inch
        # bmi calc
        weight = weight * 0.45
        totalinches = (totalinches*0.025)**2
        bmi = float("{:.1f}".format(weight / totalinches))

        # CLASSIFICATION
        
        if(bmi < 18.5):
            category = "underweight"
        elif(bmi >= 18.5 and bmi <= 24.9):
            category = "normal"
        elif(bmi >= 25 and bmi <= 29.9):
            category = "overweight"
        elif(bmi >= 30):
            category = "obese"
        
    return render_template('bmi.html', bmi=bmi, category=category)