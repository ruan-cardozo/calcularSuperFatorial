from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/superfatorial/<int:number>', methods=['GET'])
def calcular_superfatorial(number):
    def calcular_fatorial(n):
        if n == 0 or n == 1:
            return 1
        return n * calcular_fatorial(n - 1)

    result = 1
    for i in range(1, number + 1):
        result *= calcular_fatorial(i)

    return jsonify({'superfatorial': result})


if __name__ == '__main__':
    app.run()
