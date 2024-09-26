from flask import Flask, render_template, request, redirect
import search
import img_search
import vid_search
from datetime import datetime
import os
from groq import Groq

app = Flask(__name__)

def check_theme():
    if 'dark_mode' in settings_data:
        theme = 'filter: invert(1) hue-rotate(180deg);'
    else:
        theme = ''

    return theme

def get_groq_key():
    with open('groq_key.txt', 'r') as file:
        groq_key = file.read()
    
    return groq_key

def ai_result(message):
    client = Groq(
        api_key=os.environ.get('GROQ_API_KEY'),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': f'Explain: {message}',
            }
        ],
        model='llama3-8b-8192'
    )

    ai_output = chat_completion.choices[0].message.content
    ai_output = ai_output.replace('\n','<br>')
    
    return ai_output

with open('settings.txt', 'r') as file:
    settings_data = file.read()

setting_toggs = ['dark_mode', 'ai_search', 'google', 'bing', 'brave', 'yahoo', 'duckduckgo', 'unsplash_search', 'pexels_search', 'google_videos', 'bing_videos']

if 'ai_search' in settings_data:
    groq_key = get_groq_key()

    os.environ['GROQ_API_KEY'] = groq_key

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        global search_query
        search_query = request.form['search_query']
        return redirect(f'/search?q={search_query}')
    else:
        theme = check_theme()

        return render_template('index.html', theme=theme)

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
        elif 'toggle_state' in request.form.keys():
            global settings_data
            settings_data = request.form.getlist('toggle_state')
            groq_key = request.form.get('ai-key')

            os.environ['GROQ_API_KEY'] = groq_key

            with open('settings.txt', 'w') as file:
                file.write(str(settings_data))

            with open('groq_key.txt', 'w') as file:
                file.write(str(groq_key))

            request.method = 'GET'

            return redirect('/settings')
    else:
        theme = check_theme()

        active_engines = []

        for toggle in setting_toggs[2:7]:
            if toggle in settings_data:
                active_engines.append(toggle)

        ai_results = ''
        if 'ai_search' in settings_data:
            ai_results = f'''
            <div class="ai_results">
                <h4>AI Says...</h4>
                <br>
                {ai_result(search_query)}
            </div>
            <br><br>'''

        search_links, search_titles = search.main(search_query, active_engines)
        
        return render_template('search_results.html', search_query=search_query, search_titles=search_titles, search_links=search_links, theme=theme, ai_results=ai_results)
    
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
        elif 'toggle_state' in request.form.keys():
            global settings_data
            settings_data = request.form.getlist('toggle_state')
            groq_key = request.form.get('ai-key')

            os.environ['GROQ_API_KEY'] = groq_key

            with open('settings.txt', 'w') as file:
                file.write(str(settings_data))

            with open('groq_key.txt', 'w') as file:
                file.write(str(groq_key))

            request.method = 'GET'

            return redirect('/settings')
    else:
        theme = check_theme()

        active_engines = []

        for toggle in setting_toggs[7:9]:
            if toggle in settings_data:
                active_engines.append(toggle)

        # Key-value pair of image url and description
        img_url_alt = img_search.img_search(img_query, active_engines)

        # Individually stores image url and description
        img_url = []
        img_alt = []

        for image in img_url_alt:
            img_url.append(image)
            img_alt.append(img_url_alt.get(image))

        return render_template('image_results.html', img_query=img_query, img_url=img_url, img_alt=img_alt, theme=theme)

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
        elif 'toggle_state' in request.form.keys():
            global settings_data
            settings_data = request.form.getlist('toggle_state')
            groq_key = request.form.get('ai-key')

            os.environ['GROQ_API_KEY'] = groq_key

            with open('settings.txt', 'w') as file:
                file.write(str(settings_data))

            with open('groq_key.txt', 'w') as file:
                file.write(str(groq_key))

            request.method = 'GET'

            return redirect('/settings')
    else:
        theme = check_theme()

        active_engines = []

        for toggle in setting_toggs[9:11]:
            if toggle in settings_data:
                active_engines.append(toggle)

        # Key-value pair of video url and description
        vid_url_descr = vid_search.vid_search(vid_query, active_engines)

        # Individually stores video url and description
        vid_url = []
        vid_descr = []

        for video in vid_url_descr:
            vid_url.append(video)
            vid_descr.append(vid_url_descr.get(video))

        return render_template('video_results.html', vid_query=vid_query, vid_url=vid_url, vid_descr=vid_descr, theme=theme)

@app.route('/settings', methods=['POST', 'GET'])
def settings():
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
        elif 'toggle_state' in request.form.keys():
            global settings_data
            settings_data = request.form.getlist('toggle_state')
            groq_key = request.form.get('ai-key')

            os.environ['GROQ_API_KEY'] = groq_key

            with open('settings.txt', 'w') as file:
                file.write(str(settings_data))

            with open('groq_key.txt', 'w') as file:
                file.write(str(groq_key))

            request.method = 'GET'

            return redirect('/settings')
    else:
        theme = check_theme()

        togg_states = {}

        for toggle in setting_toggs:
            if toggle in settings_data:
                togg_states[toggle] = 'checked'
            else:
                togg_states[toggle] = None

        groq_key = get_groq_key()

        return render_template('settings.html',
            dark_mode_state=togg_states['dark_mode'],
            ai_search_state=togg_states['ai_search'],
            google_state=togg_states['google'],
            bing_state=togg_states['bing'],
            brave_state=togg_states['brave'],
            yahoo_state=togg_states['yahoo'],
            duckduckgo_state=togg_states['duckduckgo'],
            unsplash_search_state=togg_states['unsplash_search'],
            pexels_search_state=togg_states['pexels_search'],
            google_videos_state=togg_states['google_videos'],
            bing_videos_state=togg_states['bing_videos'],
            groq_key=groq_key,
            theme=theme
        )

if __name__ == "__main__":
    app.run(debug=True)
