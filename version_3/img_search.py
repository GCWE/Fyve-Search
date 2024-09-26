import requests
from bs4 import BeautifulSoup

def img_search(query, img_engines):
    # Contains key-value pair of image url and description
    url_alt = {}

    # Search urls, and header (to make the search appear "human")
    urls = {
        f"https://unsplash.com/s/photos/{query}":"I7OuT DVW3V L1BOa", # Unsplash
        f"https://www.pexels.com/search/{query}/":"spacing_noMargin__F5u9R MediaCard_image__yVXRE" # Pexels
    }
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    if 'unsplash_search' not in img_engines:
        del urls[next(iter(urls))]

    if 'pexels_search' not in img_engines:
        del urls[next(iter(urls))]
    
    for url in urls:
        # Conducts the search, and analyses content using BeautifulSoup
        r = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(r.content, "html.parser")

        # All images extracted from page
        images = soup.find_all("img", class_=urls.get(url))
        
        # Image url and description are extracted into dictionary
        for image in images:
            # Only counts non-premium photos
            try:
                if "premium" not in image.attrs["src"]:
                    url_alt[image.attrs["src"]] = image.attrs["alt"]
            except KeyError:
                pass

    return url_alt

if __name__ == "__main__":
    img_search("google")