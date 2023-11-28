import requests
from bs4 import BeautifulSoup

# Function to fetch HTML content from a URL
def get_html(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve HTML. Status code: {response.status_code}")
        return None

# Function to scrape book titles and ratings from HTML
def scrape_books(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    # Extracting book titles and ratings
    titles = soup.find_all('h3')  # Assuming book titles are under h3 tags
    ratings = soup.find_all('p', class_='star-rating')  # Assuming ratings are under p tags with class 'star-rating'

    for title, rating in zip(titles, ratings):
        book_title = title.a['title']
        book_rating = rating['class'][1]  # Extracting the rating from the class attribute
        print(f"Title: {book_title}, Rating: {book_rating}")

# Main function
def main():
    url = 'https://books.toscrape.com/'
    html = get_html(url)
    
    if html:
        scrape_books(html)

if __name__ == "__main__":
    main()