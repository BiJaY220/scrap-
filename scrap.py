import requests
from bs4 import BeautifulSoup
import csv

# Send a GET request to the URL
url = 'https://www.sharesansar.com/today-share-price'
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table element
table = soup.find('table', class_='table table-striped table-bordered table-hover')

# Check if table is None
if table is not None:
    

    # Extract the table rows
    rows = []
    for tr in table.find_all('tr'):
        row = []
        for td in tr.find_all('td'):
            row.append(td.text.strip())
        if row:
            rows.append(row)

    # Write the data to a CSV file
    filename = 'sharesansar_today_share_price.csv'
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(rows)

    print(f'{filename} written successfully!')
else:
    print('Table not found on the website.')