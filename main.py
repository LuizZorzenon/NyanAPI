from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cat_image')
def get_cat_image():
    try:
        r = requests.get("https://api.thecatapi.com/v1/images/search")
        data = r.json()
        print(data)
        url = data[0].get("url")
        return f'<img id="day-image" src="{url}" alt="Imagem de gato" width="450px" height="450" class="max-w-full rounded-lg shadow-lg">'
    except Exception as e:
        return "<p>Erro ao carregar imagem</p>"

@app.route('/dog_image')
def get_dog_image():  
    try:
        r = requests.get("https://dog.ceo/api/breeds/image/random")
        print(r)
        data = r.json()
        print(data)
        url = data["message"]
        print(url)
        return f'<img id="day-image" src="{url}" alt="Imagem Cachorro" width="450px" height="450" class="max-w-full rounded-lg shadow-lg">'
    except Exception as e:
            return "<p>Erro ao carregar imagem</p>"

@app.route('/space_image')
def get_space_image():
    api_demo = "OSmBujutbKJfM0Eo2bBVlrBffgi9cwlFpg5178rl"
    try:
        response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api_demo}")
        data = response.json()
        url = data["url"]
        return f'<img id="day-image" src="{url}" alt="Imagem Cachorro" width="450px" height="450" class="max-w-full rounded-lg shadow-lg">'  # Retorna todos os dados da APOD
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/pikachu_image')
def easter_egg():
    try:
        response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
        response.raise_for_status()
        data = response.json()
        url = data["sprites"]["front_default"]
        return f'<img id="day-image" src="{url}" alt="Imagem pikachu" width="450px" height="450" class="max-w-full rounded-lg shadow-lg">'
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
    


if __name__ == '__main__':
    app.run(debug=True)