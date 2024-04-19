import aiohttp
import asyncio
import json



async def post_request(session, url, headers, data):
    async with session.post(url, headers=headers, data=json.dumps(data)) as response:
        return await response.json()


async def fetch_all():
    async with aiohttp.ClientSession() as session:
        tasks = [
            post_request(session,
                         'https://t-extprt-reyalrb.qp.akasaair.com/api/nsk/v4/availability/search/simple',
                         headers={"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJVbmtub3duIiwianRpIjoiYmM1YTEwY2YtNmVjZC03NjI1LTg3YWUtYjVhN2YzMmRkODFjIiwiaXNzIjoiZG90UkVaIEFQSSJ9.q-mSvSss4SrxX2Rw0ozYIvsI0LhGCH81WatCOoY44uE",
                                  "Content-Type": "application/json"},
                         data={
                             "origin": "DEL",
                             "destination": "HYD",
                             "searchDestinationMacs": True,
                             "searchOriginMacs": True,
                             "beginDate": "2024-03-28",
                             "endDate": "",
                             "getAllDetails": True,
                             "taxesAndFees": "TaxesAndFees",
                             "passengers": {
                                 "types": [
                                     {
                                         "type": "ADT",
                                         "count": 2
                                     },
                                     {
                                         "type": "CHD",
                                         "count": 1
                                     },
                                     {
                                         "type": "INFT",
                                         "count": 1
                                     }
                                 ]
                             },
                             "codes": {
                                 "currencyCode": "INR",
                                 "promotionCode": ""
                             },
                             "numberOfFaresPerJourney": 4,
                             "filters": {
                                 "compressionType": 1,
                                 "groupByDate": False,
                                 "carrierCode": "QP",
                                 "type": "ALL",
                                 "maxConnections": 4,
                                 "productClasses": [
                                     "EC",
                                     "AV",
                                     "SP"
                                 ],
                                 "sortOptions": [
                                     "NoSort"
                                 ],
                                 "fareTypes": [
                                     "R",
                                     "V",
                                     "S"
                                 ]
                             }
                         }),
             # Uncomment the below code when other apis need to be integrated.            

            #post_request(session, 
             #            'https://api2.example.com/data', 
              #           headers={"X-API-Key": "api-key-2"},
               #          data={"param1": "value1", "param2": "value2"}),
            #post_request(session, 
             #            'https://api3.example.com/data', 
              #           headers={"Authorization": "Basic base64credentials"},
               #          data={"field1": "value1"})'''
        ]
        responses = await asyncio.gather(*tasks)
        return responses


async def main():
    responses = await fetch_all()
    # Consolidate the responses. Adjust structure as needed.
    consolidated_response = {
        'api1': responses[0],

    }
    return consolidated_response


