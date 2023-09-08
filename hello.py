from markupsafe import escape

app = escape(__name__)


@app.route("/<name>")
def hello(name):
    return f" Hello,{escape(name)}!"


# if __name__ == "__main__":
#     app.run(debug=True)

