# Task1WebScrapping

🌐 This Python script is a web scraper that fetches job listings from a website and saves the extracted data to a local file. 💻 It utilizes the requests library to make HTTP requests and BeautifulSoup from the bs4 library to parse HTML content. 🕷️

🎯 The main function, webScrap, sends a GET request to the specified URL and checks if the response status code is 200 (OK). 📝 If successful, it parses the HTML content using BeautifulSoup, locates job listing information (title, company, and location) based on specific class names, and stores the data in a list. 📂 Finally, it writes the collected job data to a file using the writeToFile function.

🔁 The script also includes helper functions for creating the file name and writing data to the file. It runs the scraping process repeatedly every 24 hours, ensuring you have the latest job listings at your fingertips! 🕰️

⚙️ To use this script, you'll need Python 3.x and the requests and beautifulsoup4 libraries installed. Simply run the Python file, and let the scraper do its magic! 🧙‍♂️ Keep in mind that any changes to the website's HTML structure may require modifications to the code. 🛠️

Get ready to explore new job opportunities with this handy web scraper! 💼🚀
