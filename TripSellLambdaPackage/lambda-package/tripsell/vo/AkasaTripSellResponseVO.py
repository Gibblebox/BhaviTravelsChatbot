from typing import List, Optional, Dict
from pydantic import BaseModel, Field

class LegInfo(BaseModel):
    arrivalTerminal: Optional[str] = None
    departureTerminal: Optional[str] = None
    arrivalTime: Optional[str] = None
    departureTime: Optional[str] = None

class Leg(BaseModel):
    legKey: str
    legInfo: LegInfo
    # Add other fields as necessary

class Segment(BaseModel):
    segmentKey: str
    legs: List[Leg]
    # Include other segment-related fields here

class Journey(BaseModel):
    journeyKey: str
    segments: List[Segment]
    # Other journey-specific fields

class PassengerInfo(BaseModel):
    gender: Optional[int] = None
    dateOfBirth: Optional[str] = None
    # Extend with more passenger info fields as needed

class Passenger(BaseModel):
    passengerKey: str
    info: PassengerInfo
    # Other fields related to a passenger

class SalesDetail(BaseModel):
    agentCode: str
    domainCode: str
    locationCode: str
    organizationCode: str
    # Additional sales-related fields

class Sales(BaseModel):
    created: SalesDetail
    source: SalesDetail
    modified: Optional[SalesDetail] = None

class Payment(BaseModel):
    amount: float
    currencyCode: str
    # Other payment details

class Contact(BaseModel):
    email: Optional[str] = None
    phone: Optional[str] = None
    # Additional contact details



class ServiceCharge(BaseModel):
    amount: float
    code: Optional[str] = None
    detail: Optional[str] = None
    type: int
    collectType: int
    currencyCode: str
    foreignCurrencyCode: Optional[str] = None
    foreignAmount: Optional[float] = None
    ticketCode: Optional[str] = None

class PassengerTotal(BaseModel):
    services: Optional[List[ServiceCharge]] = None
    specialServices: Optional[List[ServiceCharge]] = None
    seats: Optional[List[ServiceCharge]] = None
    upgrades: Optional[List[ServiceCharge]] = None
    spoilage: Optional[List[ServiceCharge]] = None
    nameChanges: Optional[List[ServiceCharge]] = None
    convenience: Optional[List[ServiceCharge]] = None
    infant: Optional[List[ServiceCharge]] = None

class JourneyTotal(BaseModel):
    totalAmount: float
    totalPoints: int
    totalTax: float
    totalDiscount: float

class Breakdown(BaseModel):
    balanceDue: float
    pointsBalanceDue: int
    authorizedBalanceDue: float
    totalAmount: float
    totalPoints: int
    totalToCollect: float
    totalPointsToCollect: int
    totalCharged: float
    passengerTotals: Dict[str, PassengerTotal]
    passengers: Dict[str, PassengerTotal]  # Assuming similar structure to passengerTotals for simplification
    journeyTotals: Dict[str, JourneyTotal]
    addOnTotals: Optional[Dict[str, List[ServiceCharge]]] = None  # If there's more specific structure, it needs to be defined


class Data(BaseModel):
    selfServiceMoveAvailable: bool
    bookingKey: Optional[str] = None
    currencyCode: str
    journeys: List[Journey]
    passengers: Dict[str, Passenger]
    sales: Sales
    contacts: Dict[str, Contact]
    payments: List[Payment]
    breakdown: Breakdown
    # Include other top-level fields as necessary


class TripSellResponse(BaseModel):
    data: Data
