from flask import Flask,request
def beautifulDays(i, j, k):
    # Write your code here
    beutiful = 0
    for i in range(i, j+1):
        if abs(i - (int(str(i)[::-1])))/k % 1 == 0:
            beutiful += 1
    return beutiful

app = Flask(__name__)
@app.route('/beutiful', methods=['GET','POST'])
def createAPI_beutiful():
    input_i = request.form.get('i')
    input_i = int(input_i)
    input_j = request.form.get('j')
    input_j = int(input_j)
    input_k = request.form.get('k')
    input_k = int(input_k)

    result = beautifulDays(input_i,input_j,input_k)
    return {'days_forbeutiful':result}
    
    
if __name__ == "__main__":
    app.run(debug=True)
