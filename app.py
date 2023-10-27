import os
import requests
import json
import openai
from dotenv import load_dotenv

load_dotenv()

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)

@app.route('/')
def index():
    print('Request for index page received')
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
    name = request.form.get('name').strip()

    if name:
        print('Request for hello page received with name=%s' % name)
       
        # Paste code from Azure OpenAI Studio Chat Playground or uncomment code below
        # ---------------------------------------------------------------------------

        # openai.api_key = os.getenv("AZURE_OPENAI_KEY")
        # openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
        # openai.api_type = 'azure'
        # openai.api_version = '2023-07-01-preview'

        # response = openai.ChatCompletion.create(
        #     engine="gpt-35-turbo",
        #     messages = [
        #         {"role":"system","content":"You are an AI assistant that provides cheerful greetings to people."},
        #         {"role":"user","content":"Write a text greeting and a short joke for the user named %s and try to make it rhyme.  Always mention the person's name in the response." % name},
        #         {"role":"assistant","content":"Hello %s, it's nice to see\nThat you've come to chat with me\nI'm here to help with all you seek\nSo ask away, don't be meek!" % name}],
        #     temperature=0.7,
        #     max_tokens=50,
        #     top_p=0.95,
        #     frequency_penalty=0,
        #     presence_penalty=0,
        #     stop=None)

        # print(response)

        # greeting_text = response.choices[0].message.content.replace('\n', ' ').replace(' .', '.').strip()

        # Comment out line below if using code above
        greeting_text = name

        print('greeting_text=%s' % greeting_text)

        return render_template('hello.html', name = greeting_text)
    else:
        print('Request for hello page received with no name or blank name -- redirecting')
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
