import requests
from bs4 import BeautifulSoup
import re
import json
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

# Function to clean text data
def sanitize_text(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = text.strip()
    return text

# Function to extract card elements from BBC website
def extract_card_elements():
    # URL of the BBC website
    bbc_url = 'https://www.bbc.com'
    # Send a GET request to the URL
    response = requests.get(bbc_url)
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find all card elements
    return soup.find_all('div', {'data-testid': 'card-text-wrapper'})

# Function to extract data from card elements
def extract_data_from_card(card):
    headline_element = card.find('h2', {'data-testid': 'card-headline'})
    description_element = card.find('p', {'data-testid': 'card-description'})
    link_element = card.parent.find('a', {'data-testid': 'internal-link'})

    # Extract title, description, and link
    title = sanitize_text(headline_element.text) if headline_element else 'No title found'
    description = sanitize_text(description_element.text) if description_element else 'No description available'
    link = bbc_url + link_element['href'] if link_element and link_element.get('href') else 'No link available'

    return {'title': title, 'description': description, 'link': link}

# Function to extract data from BBC website
def extract_data_from_website():
    # List to store extracted data
    extracted_data = []
    # Extract card elements
    card_elements = extract_card_elements()
    index = 0
    # Loop through card elements using while loop
    while index < len(card_elements):
        card = card_elements[index]
        extracted_data.append(extract_data_from_card(card))
        index += 1
    return extracted_data

# Function to save data to a JSON file
def save_data_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    print(f"Data successfully saved to {filename}")

# Function to upload a file to Google Drive
def upload_file_to_drive(filename):
    # Authenticate with Google Drive
    google_auth = GoogleAuth()
    google_auth.LoadCredentialsFile("mycreds.txt")
    if google_auth.credentials is None:
        google_auth.LocalWebserverAuth()
    elif google_auth.access_token_expired:
        google_auth.Refresh()
    else:
        google_auth.Authorize()
    google_auth.SaveCredentialsFile("mycreds.txt")

    # Create Google Drive instance
    drive = GoogleDrive(google_auth)
    file_to_upload = drive.CreateFile({'title': os.path.basename(filename)})
    file_to_upload.SetContentFile(filename)
    file_to_upload.Upload()
    print('File uploaded to Google Drive')

# Main function
def main():
    # Extract data from the website
    extracted_data = extract_data_from_website()
    json_filename = 'extracted_data.json'
    # Save extracted data to a JSON file
    save_data_to_json(extracted_data, json_filename)
    # Upload JSON file to Google Drive
    upload_file_to_drive(json_filename)
    # Add JSON file to DVC
    os.system(f'dvc add {json_filename}')
    # Add changes to git
    os.system('git add .')
    # Commit changes
    os.system('git commit -m "Update dataset and DVC files"')
    # Push changes
    os.system('dvc push')

# Execute main function if the script is run directly
if __name__ == "__main__":
    main()
