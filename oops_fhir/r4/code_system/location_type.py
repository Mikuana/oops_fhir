from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["LocationType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class LocationType:
    """
    Location type

    This example value set defines a set of codes that can be used to
indicate the physical form of the Location.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/location-physical-type
    """

    si = CodeSystemConcept(
        {
            "code": "si",
            "definition": "A collection of buildings or other locations such as a site or a campus.",
            "display": "Site",
        }
    )
    """
    Site

    A collection of buildings or other locations such as a site or a campus.
    """

    bu = CodeSystemConcept(
        {
            "code": "bu",
            "definition": "Any Building or structure. This may contain rooms, corridors, wings, etc. It might not have walls, or a roof, but is considered a defined/allocated space.",
            "display": "Building",
        }
    )
    """
    Building

    Any Building or structure. This may contain rooms, corridors, wings, etc. It might not have walls, or a roof, but is considered a defined/allocated space.
    """

    wi = CodeSystemConcept(
        {
            "code": "wi",
            "definition": "A Wing within a Building, this often contains levels, rooms and corridors.",
            "display": "Wing",
        }
    )
    """
    Wing

    A Wing within a Building, this often contains levels, rooms and corridors.
    """

    wa = CodeSystemConcept(
        {
            "code": "wa",
            "definition": "A Ward is a section of a medical facility that may contain rooms and other types of location.",
            "display": "Ward",
        }
    )
    """
    Ward

    A Ward is a section of a medical facility that may contain rooms and other types of location.
    """

    lvl = CodeSystemConcept(
        {
            "code": "lvl",
            "definition": "A Level in a multi-level Building/Structure.",
            "display": "Level",
        }
    )
    """
    Level

    A Level in a multi-level Building/Structure.
    """

    co = CodeSystemConcept(
        {
            "code": "co",
            "definition": "Any corridor within a Building, that may connect rooms.",
            "display": "Corridor",
        }
    )
    """
    Corridor

    Any corridor within a Building, that may connect rooms.
    """

    ro = CodeSystemConcept(
        {
            "code": "ro",
            "definition": "A space that is allocated as a room, it may have walls/roof etc., but does not require these.",
            "display": "Room",
        }
    )
    """
    Room

    A space that is allocated as a room, it may have walls/roof etc., but does not require these.
    """

    bd = CodeSystemConcept(
        {
            "code": "bd",
            "definition": "A space that is allocated for sleeping/laying on. This is not the physical bed/trolley that may be moved about, but the space it may occupy.",
            "display": "Bed",
        }
    )
    """
    Bed

    A space that is allocated for sleeping/laying on. This is not the physical bed/trolley that may be moved about, but the space it may occupy.
    """

    ve = CodeSystemConcept(
        {"code": "ve", "definition": "A means of transportation.", "display": "Vehicle"}
    )
    """
    Vehicle

    A means of transportation.
    """

    ho = CodeSystemConcept(
        {
            "code": "ho",
            "definition": "A residential dwelling. Usually used to reference a location that a person/patient may reside.",
            "display": "House",
        }
    )
    """
    House

    A residential dwelling. Usually used to reference a location that a person/patient may reside.
    """

    ca = CodeSystemConcept(
        {
            "code": "ca",
            "definition": "A container that can store goods, equipment, medications or other items.",
            "display": "Cabinet",
        }
    )
    """
    Cabinet

    A container that can store goods, equipment, medications or other items.
    """

    rd = CodeSystemConcept(
        {
            "code": "rd",
            "definition": "A defined path to travel between 2 points that has a known name.",
            "display": "Road",
        }
    )
    """
    Road

    A defined path to travel between 2 points that has a known name.
    """

    area = CodeSystemConcept(
        {
            "code": "area",
            "definition": "A defined physical boundary of something, such as a flood risk zone, region, postcode",
            "display": "Area",
        }
    )
    """
    Area

    A defined physical boundary of something, such as a flood risk zone, region, postcode
    """

    jdn = CodeSystemConcept(
        {
            "code": "jdn",
            "definition": "A wide scope that covers a conceptual domain, such as a Nation (Country wide community or Federal Government - e.g. Ministry of Health),  Province or State (community or Government), Business (throughout the enterprise), Nation with a business scope of an agency (e.g. CDC, FDA etc.) or a Business segment (UK Pharmacy), not just an physical boundary",
            "display": "Jurisdiction",
        }
    )
    """
    Jurisdiction

    A wide scope that covers a conceptual domain, such as a Nation (Country wide community or Federal Government - e.g. Ministry of Health),  Province or State (community or Government), Business (throughout the enterprise), Nation with a business scope of an agency (e.g. CDC, FDA etc.) or a Business segment (UK Pharmacy), not just an physical boundary
    """

    class Meta:
        resource = _resource
