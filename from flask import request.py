from flask import request

app = request(__name__)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
    
@app.route('/login')
def login_post():
    return show_the_login_form()

@app.route('/login')
def login_post():
    return do_the_login()


if __name__ == "__main__":
    app.run(debug=True)
