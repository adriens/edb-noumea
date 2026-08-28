import requests
import pandas as pd
import io

from ._http import get_with_retry

# URL de la page à scraper
URL = "https://www.noumea.nc/noumea-pratique/salubrite-publique/qualite-eaux-baignade"

def get_water_quality():
    """
    Récupère les données sur la qualité de l'eau de baignade depuis le site de la ville de Nouméa
    et les retourne dans un DataFrame pandas en lisant directement les tables HTML.
    """
    try:
        # Ajouter un header User-Agent pour simuler un navigateur
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        response = get_with_retry(URL, headers=headers)
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête HTTP : {e}")
        return None

    try:
        # pandas.read_html retourne une liste de tous les DataFrames trouvés dans le HTML
        tables = pd.read_html(io.BytesIO(response.content), flavor='lxml')
    except ValueError:
        print("Aucune table n'a été trouvée sur la page.")
        return None

    if not tables:
        print("Aucune table n'a été trouvée sur la page.")
        return None

    # En supposant que le tableau que nous voulons est le premier trouvé
    df = tables[0]

    # Renommer les colonnes pour qu'elles soient plus claires
    # Nous nous attendons à deux colonnes : Plage et État
    if df.shape[1] == 2:
        df.columns = ["plage", "etat_sanitaire"]
    else:
        print(f"La table trouvée n'a pas le format attendu (2 colonnes). Colonnes trouvées : {df.shape[1]}")
        return None

    return df

if __name__ == "__main__":
    # Appeler la fonction pour obtenir le DataFrame
    water_quality_df = get_water_quality()

    # Afficher le DataFrame s'il a été créé avec succès
    if water_quality_df is not None:
        print("📊 État sanitaire des eaux de baignade à Nouméa 📊")
        print(water_quality_df.to_string())