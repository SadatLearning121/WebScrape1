from bs4 import BeautifulSoup
import requests

url= 'https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=python&cboWorkExp1=-1&txtLocation='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')

# Find all job listings
jobs = soup.find_all('div', class_='srp-listing')

for job in jobs:
    try:

        #Extract company name
        comp_name = job.find('span', class_='srp-comp-name').text.strip()

        job_title = job.find('h3').text.strip()
        # Extract skills
        skills = [skill.text.strip() for skill in job.find_all('a', class_='srphglt')]
        #Extract location, experience and salary
        location =  job.find('div', class_='srp-loc').text.strip()
        experience = job.find('div', class_='srp-exp').text.strip()
        salary =  job.find('div', class_='srp-sal').text.strip()

        print(f"Company:{comp_name}")
        print(f"Job title:{job_title}")
        print(f"Skills:{skills}")
        print(f"Location:{location}")
        print(f"Experience:{experience}")
        print(f"Salary:{salary}")
        print("-" * 50)



    except AttributeError as e:
        print(f"Error processing a job listing: {e}")
        continue







