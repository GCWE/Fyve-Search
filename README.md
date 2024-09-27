# Fyve Search 👋
A metasearch engine built with Python and Docker.

## Introduction
Fyve Search is a metasearch engine - that is, it collates the search results from multiple different search engines (e.g. Google, Bing, Yahoo) and outputs them to you, the user.

It works through the process of web scraping (BeautifulSoup4), which involves a HTML parser that effectively conducts a "search" on the many different search engines for unique links.

This then all gets wrapped up in a Docker container, for added security (see below).

## Installation
Make sure you have Docker and Docker Compose installed on your system - refer to the Docker website for setup instructions.

Proceed by running the following in your terminal:
```
pip install PyQt5 PyQtWebEngine
```

Download the folder containing the latest version of Fyve Search (Version 4).

Open the folder as your working directory.

Execute the following:
```
python /path/to/disposable_chromium/run_chromium.py
```

This will prompt the program to begin building a Chromium Browser webtop, along with the Fyve Search metasearch engine. Once done, simply kill the program and retype the same "run_chromium.py" command as before.
Voila! Fyve Search should now be working in the Chromium browser.

## Why Use Fyve Search?
There are a few reasons why you might want to use Fyve Search as opposed to one of your standard search engines.

1. Search Efficiency: Did you know that search engines like Google only index about 5% of the entirety of the internet? By utilizing numerous different search engines in outputting search results, Fyve Search therefore ensures that you don't miss out on that one search link you need, and thereby saves you heaps of time from aimlessly scouring through pages of search results (you know what I mean!).

2. Privacy: In our modern age, and with more and more of our personal information getting stored online, it has become more important than ever that there are means for us to stay safe online. And yet it seems that the search engines of today not only fail to properly protect users from online hackers, but contribute to the issue through selling user information to thirdy-party services!
With Fyve Search, you don't have to worry about these issues - through means of Docker containers that separate the metasearch engine (as well as a dedicated browser) from your local machine, you can rest assured that any hacker who taps into your system will be kept isolated within the Docker container, and have no access to your personal files/folders. What's more, as soon as you close your browser session the Docker container self-destructs, thereby disconnecting the hacker entirely from your device.
The integration of a Tor proxy also aims to shield your IP address/location by tunneling it through a series of proxy servers (and constantly changing the IP address) and thereby preventing those pesky third-party organizations from building a database of information about you.

3. Royalty-Free Images: All "image engines" used in Fyve Search provide completely free-to-use images/graphics. Never again will you have to worry about violating copyright issues when using online photos for commercial purposes.

4. AI Search Results: Fyve Search allows you to connect Fyve search to a Groq API key, which in turn grants you access to
As of the time of writing these Docs, Groq AI is completely free to use. 🥳

5. Maximum Customization: I believe that you can only be most efficient when you work in an environment tailor-made for you. That is precisely what Fyve Search offers: be it colour schemes, or search engine selection, you're in full control.

6. We also have sweet themes for special holidays 😎

## Troubleshooting

**Why am I receiving errors when running Fyve Search?**

One possibility is that Docker may not have been properly installed - if you're sure it has been, check to see if the Docker Engine is running properly.


**How do I enable AI Search (Groq)?**

You can enable AI Search by first setting the "AI Search" toggle on the Settings page.

To get your Groq API key, head over to the "GroqCloud" site and create an account. Doing so should grant you access to the "API Keys" tab, where you can then generate a connection token. Paste this into the input box in the Fyve Search Settings page, and voila! You're all set.

Test it out by searching something!


**Do I have to use the Dockerized Chromium wrapper?**

Although it is not compulsory to run Fyve Search in the dedicated Chromium wrapper, I very much encourage it - this is because most common browsers also involve some tracking services that sell user data to third-party organizations (for monetization purposes); a problem which the Chromium browser aims to resolve through integration with the Tor proxy.

However, if you simply want to run Fyve Search in another web browser, there are some additional steps you will need to take to set it up:

Replace the entire "run_chromium.py" with the following:

```
import os
os.system("docker-compose -f docker-compose.yml up -d")
```

Run the program as normal. Go to your browser and type "0.0.0.0:8080" - the Fyve Search homepage should appear.
