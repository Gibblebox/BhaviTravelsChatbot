import typing #List, Optional, Dict
import pydantic 

class Designator(pydantic.BaseModel):
    destination: str
    origin: str
    arrival: str
    departure: str

class Identifier(pydantic.BaseModel):
    identifier: str
    carrierCode: str
    opSuffix: typing.Optional[str] = None

class LegInfo(pydantic.BaseModel):
    departureTimeUtc: str
    arrivalTimeUtc: str
    adjustedCapacity: int
    arrivalTerminal: str
    arrivalTimeVariant: int
    backMoveDays: int
    capacity: int
    changeOfDirection: bool
    codeShareIndicator: int
    departureTerminal: typing.Optional[str] = None
    departureTimeVariant: int
    equipmentType: str
    equipmentTypeSuffix: typing.Optional[str] = None
    eTicket: bool
    irop: bool
    lid: int
    marketingCode: typing.Optional[str] = None
    marketingOverride: bool
    operatedByText: typing.Optional[str] = None
    operatingCarrier: typing.Optional[str] = None
    operatingFlightNumber: typing.Optional[str] = None
    operatingOpSuffix: typing.Optional[str] = None
    outMoveDays: int
    arrivalTime: str
    departureTime: str
    prbcCode: str
    scheduleServiceType: str
    sold: int
    status: int
    subjectToGovtApproval: bool

class Leg(pydantic.BaseModel):
    legKey: str
    operationsInfo: typing.Optional[typing.Dict] = None
    designator: Designator
    legInfo: LegInfo
    nests: typing.List[typing.Dict] = []
    ssrs: typing.List[typing.Dict] = []
    seatmapReference: str
    flightReference: str

class Segment(pydantic.BaseModel):
    isChangeOfGauge: bool
    isBlocked: bool
    isHosted: bool
    designator: Designator
    isSeatmapViewable: bool
    segmentKey: str
    identifier: Identifier
    cabinOfService: typing.Optional[str] = None
    externalIdentifier: typing.Optional[str] = None
    international: bool
    segmentType: int
    legs: typing.List[Leg]

class FareDetail(pydantic.BaseModel):
    availableCount: int
    status: int
    reference: str
    serviceBundleSetCode: typing.Optional[str] = None
    bundleReferences: typing.Optional[str] = None
    ssrReferences: typing.Optional[str] = None

class Fare(pydantic.BaseModel):
    fareAvailabilityKey: str
    details: typing.List[FareDetail]
    isSumOfSector: bool

class Journey(pydantic.BaseModel):
    flightType: int
    stops: int
    designator: Designator
    journeyKey: str
    segments: typing.List[Segment]
    fares: typing.List[Fare]
    notForGeneralUser: bool

class Trip(pydantic.BaseModel):
    multipleOriginStations: bool
    multipleDestinationStations: bool
    date: str
    journeysAvailableByMarket: typing.Dict[str, typing.List[Journey]]

class Result(pydantic.BaseModel):
    trips: typing.List[Trip]
    #faresAvailable: Dict[str, Dict]
    #currencyCode: str
    #includeTaxesAndFees: bool
    #bundleOffers: Optional[Dict] = None

class Data(pydantic.BaseModel):
    results: typing.List[Result]
    faresAvailable: typing.Dict[str, typing.Dict]

class APIResponse(pydantic.BaseModel):
    data: Data
