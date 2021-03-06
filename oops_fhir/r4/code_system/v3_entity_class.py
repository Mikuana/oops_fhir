from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3EntityClass"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3EntityClass:
    """
    v3 Code System EntityClass

     Classifies the Entity class and all of its subclasses.  The terminology
is hierarchical.  At the top is this  HL7-defined domain of high-level
categories (such as represented by the Entity subclasses). Each of these
terms must be harmonized and is specializable. The value sets beneath
are drawn from multiple, frequently external, domains that reflect much
more fine-grained typing.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-EntityClass
    """

    ent = CodeSystemConcept(
        {
            "code": "ENT",
            "concept": [
                {
                    "code": "HCE",
                    "definition": "A health chart included to serve as a document receiving entity in the management of medical records.",
                    "display": "health chart entity",
                },
                {
                    "code": "LIV",
                    "concept": [
                        {
                            "code": "NLIV",
                            "concept": [
                                {
                                    "code": "ANM",
                                    "definition": "A living subject from the animal kingdom.",
                                    "display": "animal",
                                },
                                {
                                    "code": "MIC",
                                    "definition": "All single celled living organisms including protozoa, bacteria, yeast, viruses, etc.",
                                    "display": "microorganism",
                                },
                                {
                                    "code": "PLNT",
                                    "definition": "A living subject from the order of plants.",
                                    "display": "plant",
                                },
                            ],
                            "definition": "A subtype of living subject that includes all living things except the species Homo Sapiens.",
                            "display": "non-person living subject",
                        },
                        {
                            "code": "PSN",
                            "definition": "A living subject of the species homo sapiens.",
                            "display": "person",
                        },
                    ],
                    "definition": "Anything that essentially has the property of life, independent of current state (a dead human corpse is still essentially a living subject).",
                    "display": "living subject",
                },
                {
                    "code": "MAT",
                    "concept": [
                        {
                            "code": "CHEM",
                            "definition": "A substance that is fully defined by an organic or inorganic chemical formula, includes mixtures of other chemical substances. Refine using, e.g., IUPAC codes.",
                            "display": "chemical substance",
                        },
                        {
                            "code": "FOOD",
                            "definition": "Naturally occurring, processed or manufactured entities that are primarily used as food for humans and animals.",
                            "display": "food",
                        },
                        {
                            "code": "MMAT",
                            "concept": [
                                {
                                    "code": "CONT",
                                    "concept": [
                                        {
                                            "code": "HOLD",
                                            "definition": "A type of container that can hold other containers or other holders.",
                                            "display": "holder",
                                        }
                                    ],
                                    "definition": "A container of other entities.",
                                    "display": "container",
                                },
                                {
                                    "code": "DEV",
                                    "concept": [
                                        {
                                            "code": "CER",
                                            "definition": "A physical artifact that stores information about the granting of authorization.",
                                            "display": "certificate representation",
                                        },
                                        {
                                            "code": "MODDV",
                                            "definition": "Class to contain unique attributes of diagnostic imaging equipment.",
                                            "display": "imaging modality",
                                        },
                                    ],
                                    "definition": "A subtype of ManufacturedMaterial used in an activity, without being substantially changed through that activity.  The kind of device is identified by the code attribute inherited from Entity.\r\n\n                        \n                           Usage: This includes durable (reusable) medical equipment as well as disposable equipment.",
                                    "display": "device",
                                },
                            ],
                            "definition": "Corresponds to the ManufacturedMaterial class",
                            "display": "manufactured material",
                        },
                    ],
                    "definition": "Any thing that has extension in space and mass, may be of living or non-living origin.",
                    "display": "material",
                },
                {
                    "code": "ORG",
                    "concept": [
                        {
                            "code": "PUB",
                            "definition": "An agency of the people of a state often assuming some authority over a certain matter. Includes government, governmental agencies, associations.",
                            "display": "public institution",
                        },
                        {
                            "code": "STATE",
                            "concept": [
                                {
                                    "code": "NAT",
                                    "definition": "A politically organized body of people bonded by territory and known as a nation.",
                                    "display": "Nation",
                                }
                            ],
                            "definition": "A politically organized body of people bonded by territory, culture, or ethnicity, having sovereignty (to a certain extent) granted by other states (enclosing or neighboring states). This includes countries (nations), provinces (e.g., one of the United States of America or a French departement), counties or municipalities. Refine using, e.g., ISO country codes, FIPS-PUB state codes, etc.",
                            "display": "state",
                        },
                    ],
                    "definition": "A social or legal structure formed by human beings.",
                    "display": "organization",
                },
                {
                    "code": "PLC",
                    "concept": [
                        {
                            "code": "CITY",
                            "definition": "The territory of a city, town or other municipality.",
                            "display": "city or town",
                        },
                        {
                            "code": "COUNTRY",
                            "definition": "The territory of a sovereign nation.",
                            "display": "country",
                        },
                        {
                            "code": "COUNTY",
                            "definition": "The territory of a county, parish or other division of a state or province.",
                            "display": "county or parish",
                        },
                        {
                            "code": "PROVINCE",
                            "definition": "The territory of a state, province, department or other division of a sovereign country.",
                            "display": "state or province",
                        },
                    ],
                    "definition": "A physical place or site with its containing structure. May be natural or man-made. The geographic position of a place may or may not be constant.",
                    "display": "place",
                },
                {
                    "code": "RGRP",
                    "definition": "A grouping of resources (personnel, material, or places) to be used for scheduling purposes.  May be a pool of like-type resources, a team, or combination of personnel, material and places.",
                    "display": "group",
                },
            ],
            "definition": "Corresponds to the Entity class",
            "display": "entity",
        }
    )
    """
    entity

    Corresponds to the Entity class
    """

    class Meta:
        resource = _resource
