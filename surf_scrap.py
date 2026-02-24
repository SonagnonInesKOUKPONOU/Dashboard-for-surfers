# surf_scrap.py c'est le scrip python pour exécuter la librairie surf_scrap
import requests
import pandas as pd
from bs4 import BeautifulSoup


def scrape_surf_report(url, output_path):
    """
    Scrape surf weather data from surf-report.com
    and save it as a CSV file.

    Parameters
    ----------
    url : str
        URL of the surf report page
    output_path : str
        Path where the CSV file will be saved
    """

    # --- request ---
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")


    bloc_jours_meteo = soup.find_all('div', class_='forecast-tab')

    donnees = []

    for bloc in bloc_jours_meteo:

        date = bloc.find('div', class_='title').get_text(strip=True)
        lignes = bloc.find_all('div', class_='line')

        for ligne in lignes[1:]:

            if 'tides' in ligne.get('class', []):
                continue

            hour = ligne.find('div', class_='date').get_text(strip=True)
            waves_size = ligne.find('div', class_='waves').get_text(strip=True)
            wind_speed = ligne.find('div', class_='wind').find('span').get_text(strip=True)
            wind_direction = ligne.find('div', class_='wind img').find('img')['alt']
            wind_direction = wind_direction.replace("Orientation vent ", "")

            donnees.append({
                "date": date,
                "hour": hour,
                "waves_size": waves_size,
                "wind_speed": wind_speed,
                "wind_direction": wind_direction
            })

    df = pd.DataFrame(donnees)

    # --- save CSV ---
    df.to_csv(output_path, index=False, encoding="utf-8")

    return df