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
 

az webapp log tail --name $APP_SERVICE_NAME --resource-group $RESOURCE_GROUP_NAME
```

Cleanup
-------

```powershell
az group delete --name $RESOURCE_GROUP_NAME --no-wait
```

Resources
---------

* https://learn.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=flask
