from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

# Fonction pour charger les données depuis un fichier Excel
def charger_donnees():
    # Chargez votre fichier Excel (mettez le chemin correct du fichier)
    df = pd.read_excel('robes.xlsx')

    # Conversion des données en format JSON adapté pour l'API
    robes = []
    for _, row in df.iterrows():
        robe = {
            'Nom': row['Nom'],
            'Description': row['Description'],
            'Descriptiondetaillee': row['DescriptionDetaillee'],
            'Images': row['Images'].split(',')
        }
        robes.append(robe)
    
    return robes

# Route principale pour afficher la page web
@app.route('/')
def index():
    return render_template('index.html')

# API pour récupérer les robes au format JSON
@app.route('/api/robes')
def api_robes():
    robes = charger_donnees()
    return jsonify(robes)

if __name__ == '__main__':
    app.run(debug=True)


