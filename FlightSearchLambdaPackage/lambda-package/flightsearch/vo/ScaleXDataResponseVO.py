import typing # import List, Optional, Dict
import pydantic #import BaseModel
import json


class Segment(pydantic.BaseModel):
    segmentKey: str
    flightIdentifier: str
    origin: str
    destination: str
    dateOfDeparture: str
    dateOfArrival: str
    timeOfDeparture: str
    timeOfArrival: str


class Journey(pydantic.BaseModel):
    journeyKey: str
    dateOfDeparture: str
    dateOfArrival: str
    timeOfDeparture: str
    timeOfArrival: str
    stops: str
    totalDurationOfJourney: str
    segments: typing.List[Segment] 
    
    ecFareTotal: str
    ecFareDiscountedTotal: str
    ecADTFarePerADT: str
    ecADTTaxesPerADT: str
    ecADTmultiplier: str
    ecCHDFarePerADT: str
    ecCHDTaxesPerADT: str
    ecCHDmultiplier: str
    avFareTotal: str
    avFareDiscountedTotal: str
    avADTFarePerADT: str
    avADTTaxesPerADT: str
    avADTmultiplier: str
    avCHDFarePerCHD: str
    avCHDTaxesPerCHD: str
    avCHDmultiplier: str


class TravelPlan(pydantic.BaseModel):
    origin: str
    destination: str
    dateOfDeparture: str
    journeys: typing.List[Journey] 


segment1 = Segment(
    segmentKey="Segment001",
    flightIdentifier="FlightA",
    origin="CityX",
    destination="CityY",
    dateOfDeparture="2024-04-01",
    dateOfArrival="2024-04-02",
    timeOfDeparture="08:00",
    timeOfArrival="12:00"
)

journey1 = Journey(
    journeyKey="Journey001",
    dateOfDeparture="2024-04-01",
    dateOfArrival="2024-04-02",
    timeOfDeparture="08:00",
    timeOfArrival="12:00",
    stops="0",
    totalDurationOfJourney="4 hours",
    segments=[segment1],
    ecFareTotal="100",
    ecFareDiscountedTotal="95",
    ecADTFarePerADT="100",
    ecADTTaxesPerADT="20",
    ecADTmultiplier="1",
    ecCHDFarePerADT="75",
    ecCHDTaxesPerADT="15",
    ecCHDmultiplier="0.75",
    avFareTotal="120",
    avFareDiscountedTotal="110",
    avADTFarePerADT="120",
    avADTTaxesPerADT="25",
    avADTmultiplier="1",
    avCHDFarePerCHD="90",
    avCHDTaxesPerCHD="20",
    avCHDmultiplier="0.75"
)

travelPlan = TravelPlan(
    origin="CityX",
    destination="CityY",
    dateOfDeparture="2024-04-01",
    journeys=[journey1]
)


print(travelPlan.json())
