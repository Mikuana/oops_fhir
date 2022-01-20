from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3AddressPartType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3AddressPartType:
    """
    v3 Code System AddressPartType

      Description:  Code that specifies whether an address part names the
street, city, country, postal code, post box, etc. Discussion: The
hierarchical nature of these concepts shows composition.  E.g. "Street
Name" is part of "Street Address Line"

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-AddressPartType
    """

    adl = CodeSystemConcept(
        {
            "code": "ADL",
            "definition": 'This can be a unit designator, such as apartment number, suite number, or floor. There may be several unit designators in an address (e.g., "3rd floor, Appt. 342"). This can also be a designator pointing away from the location, rather than specifying a smaller location within some larger one (e.g., Dutch "t.o." means "opposite to" for house boats located across the street facing houses).',
            "display": "additional locator",
            "property": [{"code": "partOf", "valueCode": "AL"}],
        }
    )
    """
    additional locator

    This can be a unit designator, such as apartment number, suite number, or floor. There may be several unit designators in an address (e.g., "3rd floor, Appt. 342"). This can also be a designator pointing away from the location, rather than specifying a smaller location within some larger one (e.g., Dutch "t.o." means "opposite to" for house boats located across the street facing houses).
    """

    al = CodeSystemConcept(
        {
            "code": "AL",
            "concept": [
                {
                    "code": "DAL",
                    "definition": "A delivery address line is frequently used instead of breaking out delivery mode, delivery installation, etc.  An address generally has only a delivery address line or a street address line, but not both.",
                    "display": "delivery address line",
                },
                {
                    "code": "SAL",
                    "definition": "Description: A street address line is frequently used instead of breaking out build number, street name, street type, etc. An address generally has only a delivery address line or a street address line, but not both.",
                    "display": "street address line",
                },
            ],
            "definition": "Description: An address line is for either an additional locator, a delivery address or a street address.",
            "display": "address line",
        }
    )
    """
    address line

    Description: An address line is for either an additional locator, a delivery address or a street address.
    """

    bnn = CodeSystemConcept(
        {
            "code": "BNN",
            "definition": "The numeric portion of a building number",
            "display": "building number numeric",
            "property": [{"code": "partOf", "valueCode": "BNR"}],
        }
    )
    """
    building number numeric

    The numeric portion of a building number
    """

    bnr = CodeSystemConcept(
        {
            "code": "BNR",
            "definition": 'The number of a building, house or lot alongside the street.  Also known as "primary street number".  This does not number the street but rather the building.',
            "display": "building number",
            "property": [{"code": "partOf", "valueCode": "SAL"}],
        }
    )
    """
    building number

    The number of a building, house or lot alongside the street.  Also known as "primary street number".  This does not number the street but rather the building.
    """

    bns = CodeSystemConcept(
        {
            "code": "BNS",
            "definition": "Any alphabetic character, fraction or other text that may appear after the numeric portion of a building number",
            "display": "building number suffix",
            "property": [{"code": "partOf", "valueCode": "BNR"}],
        }
    )
    """
    building number suffix

    Any alphabetic character, fraction or other text that may appear after the numeric portion of a building number
    """

    car = CodeSystemConcept(
        {
            "code": "CAR",
            "definition": "The name of the party who will take receipt at the specified address, and will take on responsibility for ensuring delivery to the target recipient",
            "display": "care of",
        }
    )
    """
    care of

    The name of the party who will take receipt at the specified address, and will take on responsibility for ensuring delivery to the target recipient
    """

    cen = CodeSystemConcept(
        {
            "code": "CEN",
            "definition": "A geographic sub-unit delineated for demographic purposes.",
            "display": "census tract",
        }
    )
    """
    census tract

    A geographic sub-unit delineated for demographic purposes.
    """

    cnt = CodeSystemConcept(
        {"code": "CNT", "definition": "Country", "display": "country"}
    )
    """
    country

    Country
    """

    cpa = CodeSystemConcept(
        {
            "code": "CPA",
            "definition": 'A sub-unit of a state or province. (49 of the United States of America use the term "county;" Louisiana uses the term "parish".)',
            "display": "county or parish",
        }
    )
    """
    county or parish

    A sub-unit of a state or province. (49 of the United States of America use the term "county;" Louisiana uses the term "parish".)
    """

    cty = CodeSystemConcept(
        {
            "code": "CTY",
            "definition": "The name of the city, town, village, or other community or delivery center",
            "display": "municipality",
        }
    )
    """
    municipality

    The name of the city, town, village, or other community or delivery center
    """

    del_ = CodeSystemConcept(
        {
            "code": "DEL",
            "definition": "Delimiters are printed without framing white space.  If no value component is provided, the delimiter appears as a line break.",
            "display": "delimiter",
        }
    )
    """
    delimiter

    Delimiters are printed without framing white space.  If no value component is provided, the delimiter appears as a line break.
    """

    dinst = CodeSystemConcept(
        {
            "code": "DINST",
            "definition": "Indicates the type of delivery installation (the facility to which the mail will be delivered prior to final shipping via the delivery mode.) Example: post office, letter carrier depot, community mail center, station, etc.",
            "display": "delivery installation type",
            "property": [{"code": "partOf", "valueCode": "DAL"}],
        }
    )
    """
    delivery installation type

    Indicates the type of delivery installation (the facility to which the mail will be delivered prior to final shipping via the delivery mode.) Example: post office, letter carrier depot, community mail center, station, etc.
    """

    dinsta = CodeSystemConcept(
        {
            "code": "DINSTA",
            "definition": "The location of the delivery installation, usually a town or city, and is only required if the area is different from the municipality. Area to which mail delivery service is provided from any postal facility or service such as an individual letter carrier, rural route, or postal route.",
            "display": "delivery installation area",
            "property": [{"code": "partOf", "valueCode": "DAL"}],
        }
    )
    """
    delivery installation area

    The location of the delivery installation, usually a town or city, and is only required if the area is different from the municipality. Area to which mail delivery service is provided from any postal facility or service such as an individual letter carrier, rural route, or postal route.
    """

    dinstq = CodeSystemConcept(
        {
            "code": "DINSTQ",
            "definition": "A number, letter or name identifying a delivery installation.  E.g., for Station A, the delivery installation qualifier would be 'A'.",
            "display": "delivery installation qualifier",
            "property": [{"code": "partOf", "valueCode": "DAL"}],
        }
    )
    """
    delivery installation qualifier

    A number, letter or name identifying a delivery installation.  E.g., for Station A, the delivery installation qualifier would be 'A'.
    """

    dir_ = CodeSystemConcept(
        {
            "code": "DIR",
            "definition": "Direction (e.g., N, S, W, E)",
            "display": "direction",
            "property": [{"code": "partOf", "valueCode": "SAL"}],
        }
    )
    """
    direction

    Direction (e.g., N, S, W, E)
    """

    dmod = CodeSystemConcept(
        {
            "code": "DMOD",
            "definition": "Indicates the type of service offered, method of delivery.  For example: post office box, rural route, general delivery, etc.",
            "display": "delivery mode",
            "property": [{"code": "partOf", "valueCode": "DAL"}],
        }
    )
    """
    delivery mode

    Indicates the type of service offered, method of delivery.  For example: post office box, rural route, general delivery, etc.
    """

    dmodid = CodeSystemConcept(
        {
            "code": "DMODID",
            "definition": "Represents the routing information such as a letter carrier route number.  It is the identifying number of the designator (the box number or rural route number).",
            "display": "delivery mode identifier",
            "property": [{"code": "partOf", "valueCode": "DAL"}],
        }
    )
    """
    delivery mode identifier

    Represents the routing information such as a letter carrier route number.  It is the identifying number of the designator (the box number or rural route number).
    """

    dpid = CodeSystemConcept(
        {
            "code": "DPID",
            "definition": "A value that uniquely identifies the postal address.",
            "display": "delivery point identifier",
        }
    )
    """
    delivery point identifier

    A value that uniquely identifies the postal address.
    """

    int_ = CodeSystemConcept(
        {
            "code": "INT",
            "definition": "Description:An intersection denotes that the actual address is located AT or CLOSE TO the intersection OF two or more streets.",
            "display": "intersection",
            "property": [{"code": "partOf", "valueCode": "AL"}],
        }
    )
    """
    intersection

    Description:An intersection denotes that the actual address is located AT or CLOSE TO the intersection OF two or more streets.
    """

    pob = CodeSystemConcept(
        {
            "code": "POB",
            "definition": "A numbered box located in a post station.",
            "display": "post box",
            "property": [{"code": "partOf", "valueCode": "DMODID"}],
        }
    )
    """
    post box

    A numbered box located in a post station.
    """

    pre = CodeSystemConcept(
        {
            "code": "PRE",
            "definition": "A subsection of a municipality",
            "display": "precinct",
        }
    )
    """
    precinct

    A subsection of a municipality
    """

    sta = CodeSystemConcept(
        {
            "code": "STA",
            "definition": "A sub-unit of a country with limited sovereignty in a federally organized country.",
            "display": "state or province",
        }
    )
    """
    state or province

    A sub-unit of a country with limited sovereignty in a federally organized country.
    """

    stb = CodeSystemConcept(
        {
            "code": "STB",
            "definition": "The base name of a roadway or artery recognized by a municipality (excluding street type and direction)",
            "display": "street name base",
            "property": [{"code": "partOf", "valueCode": "STR"}],
        }
    )
    """
    street name base

    The base name of a roadway or artery recognized by a municipality (excluding street type and direction)
    """

    str_ = CodeSystemConcept(
        {
            "code": "STR",
            "definition": "street name",
            "display": "street name",
            "property": [{"code": "partOf", "valueCode": "SAL"}],
        }
    )
    """
    street name

    street name
    """

    sttyp = CodeSystemConcept(
        {
            "code": "STTYP",
            "definition": "The designation given to the street.  (e.g. Street, Avenue, Crescent, etc.)",
            "display": "street type",
            "property": [{"code": "partOf", "valueCode": "STR"}],
        }
    )
    """
    street type

    The designation given to the street.  (e.g. Street, Avenue, Crescent, etc.)
    """

    unid = CodeSystemConcept(
        {
            "code": "UNID",
            "definition": "The number or name of a specific unit contained within a building or complex, as assigned by that building or complex.",
            "display": "unit identifier",
            "property": [{"code": "partOf", "valueCode": "ADL"}],
        }
    )
    """
    unit identifier

    The number or name of a specific unit contained within a building or complex, as assigned by that building or complex.
    """

    unit = CodeSystemConcept(
        {
            "code": "UNIT",
            "definition": "Indicates the type of specific unit contained within a building or complex.  E.g. Appartment, Floor",
            "display": "unit designator",
            "property": [{"code": "partOf", "valueCode": "ADL"}],
        }
    )
    """
    unit designator

    Indicates the type of specific unit contained within a building or complex.  E.g. Appartment, Floor
    """

    zip_ = CodeSystemConcept(
        {
            "code": "ZIP",
            "definition": "A postal code designating a region defined by the postal service.",
            "display": "postal code",
        }
    )
    """
    postal code

    A postal code designating a region defined by the postal service.
    """

    class Meta:
        resource = _resource
