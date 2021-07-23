from apifairy import APIFairy, response, other_responses
from flask import Flask
from marshmallow import Schema, fields

app = Flask(__name__)
apifairy = APIFairy()

app = Flask(__name__)
app.config['APIFAIRY_TITLE'] = "APIFAIRY Marshmallow Test"
app.config['APIFAIRY_VERSION'] = '1.0'
# app.config['APIFAIRY_UI'] = 'swagger_ui'
app.config['APIFAIRY_UI'] = 'redoc'
apifairy = APIFairy(app)

class MsgSchema(Schema):
    msg = fields.Str()



@app.get("/vi/api/test")
@response(MsgSchema)
@other_responses({400: 'Invalid request.', 404: 'User not found.'})
def hello():
    """Hello World

    Text attributes _italic_, *italic*, __bold__, **bold**, `monospace`.
    
    Horizontal rule:

    ---
    Bullet list:

      * apples
      * oranges
      * pears

    Numbered list:

      1. apples
      2. oranges
      3. pears

    A [link](http://example.com).

    An image:
    ![Swagger logo](https://raw.githubusercontent.com/swagger-api/swagger-ui/master/dist/favicon-32x32.png)

    Code block:

    ```
    {
      "message": "Hello, world!"
    }
    ```

    Tables:

    | Column1 | Column2 |
    | ------- | --------|
    | cell1   | cell2   |"""
    success_reponse = {"msg": "Hellow world"}
    msg_schema = MsgSchema()
    res = msg_schema.dump(success_reponse)
    return success_reponse, 200

if __name__ == "__main__":
    app.run(debug=True)