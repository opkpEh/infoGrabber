from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def root():
    data = request.json['info']

    with open('info.txt', 'w') as file:
        file.write(data)

    return "ok"
    
if __name__=='__main__':
    app.run(port=300, debug=True)
