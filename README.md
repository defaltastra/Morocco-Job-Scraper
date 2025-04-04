

```markdown
# 🧑‍💻 Internship & Job Scraper API (Morocco)

This project is a lightweight Flask API that scrapes internship and job postings from two popular Moroccan websites: [Stagiaires.ma](https://www.stagiaires.ma) and [MarocAnnonces.com](https://www.marocannonces.com). It returns the results in a clean JSON format, ideal for frontend integration or analysis.

## 🚀 Features

- Scrapes internship data from **Stagiaires.ma**
- Scrapes IT job listings from **MarocAnnonces.com**
- Exposes a single API endpoint to fetch and serve combined data
- CORS-enabled Flask API for cross-origin access

## 📦 Tech Stack

- Python 3
- Flask
- BeautifulSoup (bs4)
- Requests
- Flask-CORS

## 📂 Project Structure

```
.
├── app.py             # Main application script with scraping logic & Flask API
├── requirements.txt   # Python dependencies
└── README.md          # You're here!
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/defaltastra/morocco-job-scraper.git
cd morocco-job-scraper
```

### 2. Create virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> Make sure your `requirements.txt` contains:
>
> ```
> flask
> flask-cors
> requests
> beautifulsoup4
> ```

### 4. Run the server

```bash
python app.py
```

The API will be accessible at:  
📍 `http://localhost:3000/api/data`

## 📥 API Usage

### Endpoint: `/api/data`

Returns JSON containing:

```json
{
  "internships": [
    {
      "titre": "Stage en développement web",
      "entreprise": {
        "name": "Startup XYZ",
        "logo": "https://..."
      },
      "localisation": "Casablanca",
      "type": "Stage",
      "mode_travail": "Sur site",
      "date_publication": "2024-03-30",
      "lien": "https://..."
    }
  ],
  "jobs": [
    {
      "titre": "Développeur PHP",
      "localisation": "Rabat",
      "image": "https://...",
      "date_publication": "2024-03-29",
      "lien": "https://..."
    }
  ]
}
```

## 📌 Notes

- The scraper simulates a browser using `User-Agent` headers to avoid blocking.
- Any scraping structure change on the websites may require updates to the selectors.
- Logging is printed to the console for debug visibility.

## 🧑‍💻 Author

Made with ❤️ by [Defaltastra](https://github.com/defaltastra)  
Feel free to contribute or fork!

## 📃 License

MIT License – use freely for personal or commercial projects.
```

