import requests
from bs4 import BeautifulSoup
import json
from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
def scrape_stagiaires_ma(url):
    all_internships = []
    print(f"Scraping: {url}")
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve page: Status code {response.status_code}")
        return all_internships
    soup = BeautifulSoup(response.content, 'html.parser')
    cards = soup.select('div.ast-col-md-6')
    for card in cards:
        try:
            link_element = card.find('a')
            if not link_element:
                continue
            link = link_element.get('href', '')
            title_element = card.select_one('h3.title_card_offre_n')
            titre = title_element.text.strip(
            ) if title_element else "Unknown Title"
            company_element = card.select_one('span.societe_name')
            company_name = company_element.text.strip(
            ) if company_element else "Unknown Company"
            logo_element = card.select_one('div.image_entreprise_offre img')
            logo_url = logo_element.get('src', '') if logo_element else ""
            ethiques_elements = card.select('span.tooltip_ethiques')
            location = "Unknown"
            job_type = "Unknown"
            work_mode = "Unknown"
            publication_date = "Unknown"
            for element in ethiques_elements:
                tooltip = element.get('data-tooltip', '')
                text = element.get_text(strip=True)
                if tooltip == "Ville":
                    location = text.replace("Casablanca", "Casablanca")
                elif tooltip == "Type de contrat":
                    job_type = text.replace("Stage", "Stage")
                elif tooltip == "Type de lieu de travail":
                    work_mode = text.replace("Sur site", "Sur site")
                elif tooltip == "Date de publication":
                    publication_date = text
            internship_data = {
                "titre": titre,
                "entreprise": {
                    "name": company_name,
                    "logo": logo_url
                },
                "localisation": location,
                "type": job_type,
                "mode_travail": work_mode,
                "date_publication": publication_date,
                "lien": link
            }
            all_internships.append(internship_data)
        except Exception as e:
            print(f"Error processing a card: {e}")
    return all_internships
def scrape_marocannonces_com(url):
    all_jobs = []
    print(f"Scraping: {url}")
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve page: Status code {response.status_code}")
        return all_jobs
    soup = BeautifulSoup(response.content, 'html.parser')
    job_listings = soup.select('ul.cars-list > li')
    for job in job_listings:
        try:
            link_element = job.find('a')
            if not link_element:
                continue
            link = link_element.get('href', '')
            title = link_element.get('title', 'Unknown Title')
            location_element = job.select_one('span.location')
            location = location_element.text.strip(
            ) if location_element else "Unknown Location"
            img_element = job.select_one('img')
            img_url = img_element.get('src', '') if img_element else ''
            time_element = job.select_one('div.time em.date')
            pub_date = time_element.get_text(
                strip=True) if time_element else "Unknown Date"
            job_data = {
                "titre": title,
                "localisation": location,
                "image": img_url,
                "date_publication": pub_date,
                "lien": link
            }
            all_jobs.append(job_data)
        except Exception as e:
            print(f"Error processing a job: {e}")
    return all_jobs
@app.route('/api/data', methods=['GET'])
def get_data():
    stagiaires_url = "https://www.stagiaires.ma/offres-de-stages-et-premier-emploi-maroc/?query=informatique"
    marocannonces_url = "https://www.marocannonces.com/maroc/offres-emploi-domaine-informatique-multimedia-internet-b309.html?f_3=Informatique+%2F+Multim%C3%A9dia+%2F+Internet"
    internships = scrape_stagiaires_ma(stagiaires_url)
    jobs = scrape_marocannonces_com(marocannonces_url)
    all_data = {"internships": internships, "jobs": jobs}
    return jsonify(all_data)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)