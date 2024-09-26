from flask import Flask, render_template, request, redirect
import search
import img_search
import vid_search
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        global search_query
        search_query = request.form['search_query']
        return redirect(f'/search?q={search_query}')
    else:
        return render_template('index.html')

@app.route('/search', methods=['POST', 'GET'])
def search_results():
    if request.method == 'POST':
        if 'search_query' in request.form.keys():
            global search_query
            search_query = request.form['search_query']
            request.method = 'GET'
            return redirect(f'/search?q={search_query}')
        elif 'img_query' in request.form.keys():
            global img_query
            img_query = request.form['img_query']
            request.method = 'GET'
            return redirect(f'/images?q={img_query}')
        elif 'vid_query' in request.form.keys():
            global vid_query
            vid_query = request.form['vid_query']
            request.method = 'GET'
            return redirect(f'/videos?q={vid_query}')
    else:
        search_links, search_titles = search.main(search_query)
        
        return render_template('search_results.html', search_query=search_query, search_titles=search_titles, search_links=search_links)
    
@app.route('/images', methods=['POST', 'GET'])
def images_search():
    if request.method == 'POST':
        if 'search_query' in request.form.keys():
            global search_query
            search_query = request.form['search_query']
            request.method = 'GET'
            return redirect(f'/search?q={search_query}')
        elif 'img_query' in request.form.keys():
            global img_query
            img_query = request.form['img_query']
            request.method = 'GET'
            return redirect(f'/images?q={img_query}')
        elif 'vid_query' in request.form.keys():
            global vid_query
            vid_query = request.form['vid_query']
            request.method = 'GET'
            return redirect(f'/videos?q={vid_query}')
    else:
        # Key-value pair of image url and description
        img_url_alt = img_search.img_search(img_query)

        # Individually stores image url and description
        img_url = []
        img_alt = []

        for image in img_url_alt:
            img_url.append(image)
            img_alt.append(img_url_alt.get(image))

        return render_template('image_results.html', img_query=img_query, img_url=img_url, img_alt=img_alt)

@app.route('/videos', methods=['POST', 'GET'])
def video_results():
    if request.method == 'POST':
        if 'search_query' in request.form.keys():
            global search_query
            search_query = request.form['search_query']
            request.method = 'GET'
            return redirect(f'/search?q={search_query}')
        elif 'img_query' in request.form.keys():
            global img_query
            img_query = request.form['img_query']
            request.method = 'GET'
            return redirect(f'/images?q={img_query}')
        elif 'vid_query' in request.form.keys():
            global vid_query
            vid_query = request.form['vid_query']
            request.method = 'GET'
            return redirect(f'/videos?q={vid_query}')
    else:
        # Key-value pair of video url and description
        vid_url_descr = vid_search.vid_search(vid_query)

        # Individually stores video url and description
        vid_url = []
        vid_descr = []

        for video in vid_url_descr:
            vid_url.append(video)
            vid_descr.append(vid_url_descr.get(video))

        return render_template('video_results.html', vid_query=vid_query, vid_url=vid_url, vid_descr=vid_descr)

if __name__ == "__main__":
    app.run(debug=True)