from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page where you input marks
@app.route('/')
def index():
    return render_template('result.html')

# Route to check the result
@app.route('/result/<int:marks>')
def result(marks):
    # Set the passing marks
    passing_marks = 40
    # Check if the marks are enough to pass
    if marks >= passing_marks:
        result = 'Pass'
    else:
        result = 'Fail'
    
    return render_template('result.html', marks=marks, result=result)

if __name__ == '__main__':
    app.run(debug=True)
