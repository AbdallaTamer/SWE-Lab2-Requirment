from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get data from form
        user_input = request.form['user_input']
        # Process data
        processed_data = f"{user_input} ashtr katkot!"
        return render_template('result.html', data=processed_data)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
