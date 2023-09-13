#webScrapper
import requests
from bs4 import BeautifulSoup
import json

# Set the URL for LinkedIn job listings
url = 'https://www.linkedin.com/jobs/search/?keywords=software%20engineer&location=New%20York'

# Send an HTTP GET request to the URL
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    job_listings = soup.find_all('li', class_='result-card')

    job_data = []

    for job in job_listings:
        job_title = job.find('h3').text.strip()
        job_company = job.find('a', class_='result-card__subtitle-link').text.strip()
        job_location = job.find('span', class_='job-result-card__location').text.strip()
        job_link = job.find('a', class_='result-card__full-card-link')['href']

        job_info = {
            'title': job_title,
            'company': job_company,
            'location': job_location,
            'link': job_link
        }

        job_data.append(job_info)

    # Print or save the job data as needed (in this case, we'll print it as JSON)
    print(json.dumps(job_data, indent=2))
else:
    print("Failed to retrieve the web page.")
