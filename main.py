from flask import Flask
from caesar import rotate_string

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


@app.route("/")

def index():
    return form

app.run()