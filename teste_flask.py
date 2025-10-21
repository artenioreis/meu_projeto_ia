from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "✅ Flask está funcionando!"

@app.route('/teste')
def teste():
    return "🎉 Tudo OK com o Flask!"

if __name__ == '__main__':
    print("🚀 Servidor Flask de teste...")
    app.run(debug=True, port=5000)