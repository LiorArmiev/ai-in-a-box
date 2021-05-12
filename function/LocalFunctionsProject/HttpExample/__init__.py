import logging

import azure.functions as func
import pyodbc
import requests
import json 

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
   
    server = 'localhost'
    database = 'master'
    username = 'sa'
    password = 'Aa123456789'   
    driver= '{ODBC Driver 17 for SQL Server}'
    
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')
    
    if name:
        sentiment = "SAD"

        headers = {
           'Content-type': 'application/json',
           'accept': 'application/json'
            }
        data = '{"documents":[{"id":"1-en","text":"' + name + '"}]}"'
        response = requests.post('http://localhost:5002/text/analytics/v3.0/sentiment?model-version=latest', headers=headers, data=data)
        res = response.json()
        sentiment = res['documents'][0]['sentiment']
        
        with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
            with conn.cursor() as cursor:
                cursor.execute("select count(*) from Inventory")
                row = cursor.fetchone()
        
        with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
            with conn.cursor() as cursor:
                cursor.execute("INSERT INTO Inventory VALUES ({}, '{}', '{}');".format(row[0]+1,name,sentiment))

        return func.HttpResponse(f"Runing on a Contianer! \n\nYour query was: '{name}'.\nThe sentiment is '{sentiment}'.\n\n{str(res['documents'][0]['confidenceScores'])}")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
