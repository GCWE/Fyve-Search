import requests
from bs4 import BeautifulSoup
import re

# Function to fetch search results from a search engine
def search(query, num_results, search_engine="google"):
    search_url = {
        "google": f"https://www.google.com/search?q={query}&num={num_results}",
        "bing": f"https://www.bing.com/search?q={query}&count={num_results}",
        "brave": f"https://search.brave.com/search?q={query}&source=web",
        # "yahoo": f"https://search.yahoo.com/search?p={query}",
        # "duckduckgo": f"https://duckduckgo.com/?q={query}",
    }
    
    # Adding a User-Agent header to the HTTP request makes it appear as if the request is coming from a human
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    response = requests.get(search_url.get(search_engine, search_url["google"]), headers=headers)

    soup = BeautifulSoup(response.text, "lxml")
    links = []  # Use a list to store unique links
    titles = [] # Use a list to store page title for links
    seen = [] # Contains all repeated urls
    url_title = {} # A page's url as key, its title as the value
    
    for link in soup.find_all("a", href=True):
        href = link.get("href") 
        anchor_text = link.text
        url_title[href] = anchor_text # Webpage title as key, url as value

        # we need to parse a complex (and very messy) page of results and filter only the relevant links
        if href and anchor_text:
            # print(search_engine.lower())
            # Check if anchor text doesn't contain the search engine name
            if search_engine.lower() not in anchor_text.lower():
                # Use a regular expression to extract URLs that start with "https"
                url_match = re.search(r"https:\/\/\S+", href)
                if url_match:
                    url = url_match.group(0)
                    title = url_title.get(url) # Gets the title for a given url

                    # Check if the URL does not contain the search engine name (case-insensitive), and the page has a title
                    if (not re.search(fr"{search_engine.lower()}\.\w+", url, re.I)) and title not in [None, ' ', '  ']:
                        # Each url repeats twice - the first one with the wrong title, and the other with the right one
                        # So, only the second title is appended
                        if url not in seen:
                            seen.append(url)
                        else:
                            links.append(url)
                            titles.append(title)

    return links, titles

def main(query, search_engines):
    num_results = 100

    url_results = []
    titles = []

    for engine in search_engines:
        engine_urls, engine_titles = search(query, num_results, engine)
        url_results.extend(engine_urls)
        titles.extend(engine_titles)

    return url_results, titles

if __name__ == "__main__":
    query = input('Search input: ')
    main(query, ['google', 'bing', 'brave', 'yahoo', 'duckduckgo'])