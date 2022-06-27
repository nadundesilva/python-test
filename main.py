from fastapi import FastAPI
import http.client
import json
import requests
import httpx

app = FastAPI()


@app.get("/http-client")
async def getUsingHttpClient():
    con = http.client.HTTPSConnection("postman-echo.com")
    con.request("GET", "/get?foo1=bar1&foo2=bar2")
    resp = con.getresponse()
    respBody = resp.read().decode()
    con.close()

    print("Status: {} and reason: {}".format(resp.status, resp.reason))
    return {"clientType": "http.client", "statusCode": resp.status, "body": json.loads(respBody)}

@app.get("/requests")
async def getUsingRequests():
    resp = requests.get("https://postman-echo.com/get?foo1=bar1&foo2=bar2")
    print(resp)
    return {"clientType": "requests", "statusCode": resp.status_code, "body": json.loads(resp.text)}

@app.get("/httpx")
async def getUsingRequests():
    resp = httpx.get("https://postman-echo.com/get?foo1=bar1&foo2=bar2")
    print(resp)
    return {"clientType": "requests", "statusCode": resp.status_code, "body": json.loads(resp.text)}

@app.get("/httpx/2")
async def getUsingRequests():
    client = httpx.AsyncClient(http2=True)
    resp = await client.get("https://postman-echo.com/get?foo1=bar1&foo2=bar2")
    print(resp)
    return {"clientType": "requests", "statusCode": resp.status_code, "body": json.loads(resp.text)}
