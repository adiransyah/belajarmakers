from flask import Flask,request

def viralAdvertising(n):
    # Write your code here
    people = 5
    likes = 0
    for i in range(n):
        people = int(people/2)
        likes += people
        people *= 3
    return likes

app = Flask(__name__)
@app.route('/advers', methods=['GET','POST'])
def creatAPI():
    input_n = request.headers.get('n')
    input_n = int(input_n)

    result =  viralAdvertising(input_n)
    return {'number_for_viral': result}

if __name__ == "__main__":
    app.run(debug=True)
