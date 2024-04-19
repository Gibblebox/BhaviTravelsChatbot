import aiohttp
import asyncio
import json
import requests
from tripsell.vo.AkasaTripSellResponseVO import APIResponse as akasaRes
import pydantic
from tripsell.tripsellutil.TripSellUtil import TripSellUtil


def lambda_handler(event, context):
    # TODO implement
    # Fetching JSON request data
    if 'body' in event:
        # Assuming request is passed as JSON string
        request_data = event['body']
        print('### Here is the request data')
        print(request_data)
    else:
        request_data = event  # If request is not wrapped in 'body'
    print('%%%%%%Here are the events ')
    print(event)

    # asyncio.run(main(request_data,authorization_token))
    #token = getToken()
   # consolidated_response = asyncio.run(main(request_data, token))

    #####
    with open('trip_sell/json/AkasaTripSellResponse.json', 'r') as akasa_response:
        consolidated_response = json.load(akasa_response)
    print(consolidated_response)


    try:
        akasaTripSellAPIRes = akasaRes.parse_obj(consolidated_response)
        print(akasaTripSellAPIRes)
        print('$$$$$$$$$$')
        scaleXDataRes = TripSellUtil.mapAkasaResToScaleXDataStructure(akasaTripSellAPIRes)
        print(scaleXDataRes.json())

    except pydantic.ValidationError as e:
        print(e.json())

    #json_string = json.dumps(scaleXDataRes.json())
    json_string = scaleXDataRes.json()
    parsed_json = json.loads(json_string)

    return parsed_json


def getToken():
    tokenResponse = requests.post('https://t-extprt-reyalrb.qp.akasaair.com/api/nsk/v2/token',
                                  json={
                                      "credentials": {
                                          "username": "QPAMD6052C_01",
                                          "password": "Mar@2024",
                                          "domain": "EXT"
                                      }
                                  }
                                  )
    print('Here is the token')
    token = tokenResponse.json().get('data').get('token')
    print(token)
    return 'Bearer '+token


async def post_request(session, url, headers, data):
    async with session.post(url, headers=headers, data=json.dumps(data)) as response:
        return await response.json()


async def fetch_all(request_data, authorization_token):
    print('@@@@@@@@final token' + authorization_token)
    async with aiohttp.ClientSession() as session:
        tasks = [

            post_request(session,
                         'https://t-extprt-reyalrb.qp.akasaair.com/api/nsk/v4/availability/search/simple',
                         headers={"Authorization": authorization_token,
                                  "Content-Type": "application/json"},
                         data=request_data
                         )

        ]
        responses = await asyncio.gather(*tasks)
        return responses


async def main(request_data, authorization_token):
    responses = await fetch_all(request_data, authorization_token)
    # Consolidate the responses. Adjust structure as needed.
    consolidated_response = responses[0]
       
   # {
    #    'api1': responses[0],
    #}
    return consolidated_response



