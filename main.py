from flask import Flask, request
from caesar import rotate_string
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True



form = """
    <form method="post">

    <!DOCTYPE html>

    <html>
        <head>
            <style>
                form {
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }
                textarea {
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }
            </style>
        </head>
        <body>
            
                <label>Rotate by:
                    <input type="text" name="rot" value=0 />
                </label>
                <textarea name="text"> </textarea>
                <input type="submit" value="Submit" />  
        </body>
    </html>
</form>
"""

@app.route("/", methods=['POST'])
def encrypt():
    text = request.form['text']
    rot = request.form['rot']
    rot = int(rot)
    new_string = rotate_string(text, rot)

    return "<h1>" + cgi.escape(new_string) + "</h1>"


@app.route("/")
def index():
    return form

app.run()