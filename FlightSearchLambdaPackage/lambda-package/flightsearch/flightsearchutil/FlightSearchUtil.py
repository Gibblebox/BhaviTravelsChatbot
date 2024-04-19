from ..vo.AkasaResponseVO import APIResponse as akasaRes
from ..vo.ScaleXDataResponseVO import TravelPlan as sxdTravelPlan
from ..vo.ScaleXDataResponseVO import Journey as sxdJourney
from ..vo.ScaleXDataResponseVO import Segment as sxdSegment
import json


class FlightSearchUtil:

    def mapAkasaResToScaleXDataStructure(akasaFlightSearchAPIRes) -> sxdTravelPlan:
        originDestinationCodes = str(list(
            akasaFlightSearchAPIRes.data.results[0].trips[0].journeysAvailableByMarket.keys())[0])

        origin, destination = originDestinationCodes.split('|')

        journeysFromAkasaAPI = akasaFlightSearchAPIRes.data.results[0].trips[0].journeysAvailableByMarket.get(
            originDestinationCodes)
        
        travelPlan = sxdTravelPlan(
            origin=origin,
            destination=destination,
            dateOfDeparture=akasaFlightSearchAPIRes.data.results[0].trips[0].date,
            journeys=FlightSearchUtil.populateJourneys(journeysFromAkasaAPI)
        )

        return travelPlan
    
    
    # method map journeys data from Akasa AIR API response to our ScaleXdata response
    def populateJourneys(journeysFromAkasaAPI) -> list[sxdJourney]:

        scaleXDataJourneys = []
        for i in range(len(journeysFromAkasaAPI)):
            print(journeysFromAkasaAPI[i])

            departureDateTime = journeysFromAkasaAPI[i].designator.departure
            departureDate, departureTime = departureDateTime.split('T')
            arrivalDateTime = journeysFromAkasaAPI[i].designator.arrival
            arrivalDate, arrivalTime = arrivalDateTime.split('T')

            scaleXdataJourney = sxdJourney(
                journeyKey=journeysFromAkasaAPI[i].journeyKey,
                dateOfDeparture=departureDate,
                dateOfArrival=arrivalDate,
                timeOfDeparture=departureTime,
                timeOfArrival=arrivalTime,
                stops=str(journeysFromAkasaAPI[i].stops),
                totalDurationOfJourney="",

                # write method to populate segments
                segments=FlightSearchUtil.populateSegments(journeysFromAkasaAPI[i]),

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

            scaleXDataJourneys.append(scaleXdataJourney)

        return scaleXDataJourneys


    def populateSegments(journeyFromAkasaAPI) -> list[sxdSegment]:
        scaleXDataSegments = []
        for j in range(len(journeyFromAkasaAPI.segments)):
            segment = journeyFromAkasaAPI.segments[j]

            departureDateTime = segment.designator.departure
            departureDate, departureTime = departureDateTime.split('T')
            arrivalDateTime = segment.designator.arrival
            arrivalDate, arrivalTime = arrivalDateTime.split('T')

            scaleXDataSegment = sxdSegment(
                segmentKey=segment.segmentKey,
                flightIdentifier=segment.identifier.carrierCode+segment.identifier.identifier,
                origin=segment.designator.origin,
                destination=segment.designator.destination,
                dateOfDeparture=departureDate,
                dateOfArrival=arrivalDate,
                timeOfDeparture=departureTime,
                timeOfArrival=arrivalTime)

            scaleXDataSegments.append(scaleXDataSegment)

        return scaleXDataSegments
