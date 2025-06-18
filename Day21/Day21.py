# -  Scrape headlines from a news site
import requests
from bs4 import BeautifulSoup
def scrape_headlines(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all headlines (assuming they are in <h2> tags)
        headlines = soup.find_all('h2')
        return [headline.get_text(strip=True) for headline in headlines]
    
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
# Example usage
if __name__ == "__main__":
    url = "https://www.geeksforgeeks.org/" 
    headlines = scrape_headlines(url)
    if headlines:
        print("Headlines:")
        for i, headline in enumerate(headlines, start=1):
            print(f"{i}. {headline}")
    else:
        print("No headlines found or an error occurred.")