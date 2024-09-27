import requests
from bs4 import BeautifulSoup

def vid_search(query, vid_engines):
    # Contains key-value pair of video url and description
    url_alt = {}

    # Search urls, and header (to make the search appear "human")
    urls = [
        f"https://www.google.com/search?q={query}&tbm=vid&num=100",
        f"https://www.bing.com/videos/search?q={query}"
    ]

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    if 'google_videos' not in vid_engines:
        urls.pop(0)

    if 'bing_videos' not in vid_engines:
        urls.pop(-1)
    
    for url in urls:
        # Conducts the search, and analyses content using BeautifulSoup
        r = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(r.content, "html.parser")

        # All videos extracted from page
        videos = soup.find_all("a")
        
        for video in videos:
            try:
                # Key: Video url
                # Values: Name, video length, views, publish date, creator
                url_alt[video.contents[0].attrs["ourl"]] = [
                    video.contents[0].contents[0].contents[0].contents[0].attrs["data-alt"],
                    video.contents[0].contents[0].contents[1].contents[0].contents[0].contents[0].contents[0],
                    video.contents[0].contents[1].contents[1].contents[1].contents[0].contents[0].contents[0].contents[0],
                    video.contents[0].contents[1].contents[1].contents[1].contents[0].contents[0].contents[1].contents[0],
                    video.contents[0].contents[1].contents[1].contents[1].contents[0].contents[1].contents[0].contents[0],
                    video.contents[0].contents[1].contents[1].contents[1].contents[0].contents[1].contents[1].contents[0],
                ]
            except (KeyError, AttributeError, IndexError):
                pass

    # Returns a dictionary containing video urls and their descriptions
    return url_alt

if __name__ == "__main__":
    vid_search("google", ['google_videos', 'bing_videos'])