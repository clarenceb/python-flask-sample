Demo Script
===========

Install dependencies on Ubuntu
-------------------------------

```sh
sudo apt install python3-venv
python -m venv .venv

source .venv/bin/activate
pip install -r requirements.txt
```

Run the app locally
-------------------

```sh
flask run
```

Deploy to Azure App Service on Linux
------------------------------------

```sh
RESOURCE_GROUP_NAME="helloazureflask"
APP_SERVICE_NAME="helloazureflask2"

az group create --name $RESOURCE_GROUP_NAME --location "Australia East"

az webapp up --runtime PYTHON:3.9 --sku B1 --logs --name $APP_SERVICE_NAME --resource-group $RESOURCE_GROUP_NAME
```

Stream logs
-----------

```sh
az webapp log config --web-server-logging 'filesystem' --name $APP_SERVICE_NAME --resource-group $RESOURCE_GROUP_NAME

az webapp log tail --name $APP_SERVICE_NAME --resource-group $RESOURCE_GROUP_NAME
```

(Optional) requires GitHub Copilot - simple load test
-----------------------------------------------------

Install `k6` load testing tool.

Create a file called k6-script.js with the following contents:

```javascript
// K6 script to hit endpoint https://helloazureflask.azurewebsites.net/ for 30s with 10 VUs
```

Press ENTER and TAB (line-by-line) to prompt GitHub Copilot to generate a script.

Run the script:

```sh
k6 run k6-script.js
```

Logs and metrics check:

* Check the log stream for the load test results.
* Check the Azure Monitor Metrics for web app - Requests and Response Time.

Add code to the app Azure OpenAPI Studio's Chat Playground:

* Go to Azure OpenAPI Studio
* Make sure you have deployed a ChatGPT 3.5 Turbo model
* Go to Playground / Chat
* Type a sample conversation:

```
Write a text greeting and a short joke for the user named Fred and try to make it rhyme.  Always mention the person's name in the response.
```

* Change the system prompt to:

```
You are an AI assistant that provides cheerful greetings to people.
```

* Click the enter button to generate a repsponse.

* Click View Code and copy and paste into `app.py` - name hardcoded name to the name variable using string interpolation.
* Deploy the app again
* Set the app settings on the web app:

```sh
# Set AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_KEY in openai-vars.sh
source ./openai-vars.sh

az webapp config appsettings set \
    -g $RESOURCE_GROUP_NAME \
    -n $APP_SERVICE_NAME \
    --settings AZURE_OPENAI_KEY=$AZURE_OPENAI_KEY AZURE_OPENAI_ENDPOINT=$AZURE_OPENAI_ENDPOINT

unset AZURE_OPENAI_KEY
unset AZURE_OPENAI_ENDPOINT
```

Test the deployed app works with a generated greeting using Azure Open AI.

Cleanup
-------

```sh
az group delete --name $RESOURCE_GROUP_NAME --no-wait
```

Resources
---------

* https://learn.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=flask
