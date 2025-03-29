# CatAPI - API de Imagens Aleatórias

Este é um projeto Flask que fornece imagens aleatórias de gatos, cachorros, imagens do espaço via API da NASA e um easter egg do Pikachu. Utiliza HTMX para carregar dinamicamente as imagens sem recarregar a página.

## Tecnologias Utilizadas

- **Python + Flask** - Backend
- **HTMX** - Manipulação dinâmica da página
- **DaisyUI + TailwindCSS** - Estilização
- **The Cat API, Dog CEO API, NASA API, PokeAPI** - Fornecem as imagens

## Como Executar o Projeto

### 1. Clonar o Repositório
```sh
git clone https://github.com/SEU_USUARIO/SEU_REPO.git
cd SEU_REPO
```

### 2. Criar e Ativar o Ambiente Virtual
```sh
python -m venv venv
# No Windows
venv\Scripts\activate
# No Mac/Linux
source venv/bin/activate
```

### 3. Instalar as Dependências
```sh
pip install -r requirements.txt
```

### 4. Executar o Servidor Flask
```sh
python main.py
```

O servidor rodará em `http://127.0.0.1:5000/`.

## Estrutura do Projeto
```
catapi/
│── templates/         # HTMLs com HTMX
│   ├── index.html
│── static/            # Arquivos CSS e JS
│── main.py            # Backend Flask
│── requirements.txt   # Dependências do projeto
│── .gitignore         # Arquivos ignorados no Git
│── README.md          # Documentação
```

## Funcionalidades
- **Botão Gato 🐱** - Carrega uma imagem aleatória de gato
- **Botão Cachorro 🐶** - Carrega uma imagem aleatória de cachorro
- **Botão Espaço 👽** - Carrega a imagem do dia da NASA
- **Botão Pikachu ⚡🐹** - Mostra um easter egg do Pikachu

## Exemplo de Uso (HTMX)
```html
<button hx-get="/cat_image" hx-target="#day-image" hx-swap="outerHTML" class="btn btn-primary">🐱 Gato</button>
```
