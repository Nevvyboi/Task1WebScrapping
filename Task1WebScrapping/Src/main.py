import requests
from bs4 import BeautifulSoup
import os
import time

def webScrap(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        job_listings = soup.find_all('div', class_='card-content')
        dataToSave = []
        for job in job_listings:
            title_element = job.find('h2', class_='title')
            company_element = job.find('h3', class_='company')
            location_element = job.find('p', class_='location')
            
            title = title_element.text.strip() if title_element else 'No Title'
            company = company_element.text.strip() if company_element else 'No Company'
            location = location_element.text.strip() if location_element else 'No Location'
            
            dataToSave.append(f"Job Title: {title}\nCompany: {company}\nLocation: {location}\n---\n")
        writeToFile(dataToSave)
    else:
        print(f"Failed to retrieve data: status code {response.status_code}")

def createNameofFile2Save():
    current_working_directory = os.getcwd()
    fileName = f"{current_working_directory}\PythonFakeJobs.txt"
    return fileName

def writeToFile(data):
    data = "\n".join(data)
    with open(createNameofFile2Save(), 'w') as file:
        file.write(data)
    print("File created/updated with job data")

def main():
    url = 'https://realpython.github.io/fake-jobs/'
    webScrap(url)
    while True:
        time.sleep(86400)  
        webScrap()

if __name__ == "__main__":
    main()