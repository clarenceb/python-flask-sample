Demo Script
===========

Install dependencies on Windows
-------------------------------

```powershell
py -m venv .venv
.venv\scripts\activate
pip install -r requirements.txt
```

Run the app locally
-------------------

```powershell
flask run
```

Deploy to Azure App Service on Linux
------------------------------------

```powershell
$RESOURCE_GROUP_NAME = "helloazureflask"
$APP_SERVICE_NAME = "helloazureflask"

az group create --name $RESOURCE_GROUP_NAME --location "Australia East"

az webapp up --runtime PYTHON:3.9 --sku B1 --logs --name $APP_SERVICE_NAME --resource-group $RESOURCE_GROUP_NAME
```

Stream logs
-----------

```powershell
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

```powershell
k6 run k6-script.js
```

Logs and metrics check:

* Check the log stream for the load test results.
* Check the Azure Monitor Metrics for web app - Requests and Response Time.

```powershell

Cleanup
-------

```powershell
az group delete --name $RESOURCE_GROUP_NAME --no-wait
```

Resources
---------

* https://learn.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=flask
