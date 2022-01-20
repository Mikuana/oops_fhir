from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3Ethnicity"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3Ethnicity:
    """
    v3 Code System Ethnicity

     In the United States, federal standards for classifying data on
ethnicity determine the categories used by federal agencies and exert a
strong influence on categorization by state and local agencies and
private sector organizations. The federal standards do not conceptually
define ethnicity, and they recognize the absence of an anthropological
or scientific basis for ethnicity classification.  Instead, the federal
standards acknowledge that ethnicity is a social-political construct in
which an individual's own identification with a particular ethnicity is
preferred to observer identification.  The standards specify two minimum
ethnicity categories: Hispanic or Latino, and Not Hispanic or Latino.
The standards define a Hispanic or Latino as a person of "Mexican,
Puerto Rican, Cuban, South or Central America, or other Spanish culture
or origin, regardless of race." The standards stipulate that ethnicity
data need not be limited to the two minimum categories, but any
expansion must be collapsible to those categories.  In addition, the
standards stipulate that an individual can be Hispanic or Latino or can
be Not Hispanic or Latino, but cannot be both.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-Ethnicity
    """

    two135_2 = CodeSystemConcept(
        {
            "code": "2135-2",
            "concept": [
                {
                    "code": "2137-8",
                    "concept": [
                        {
                            "code": "2138-6",
                            "definition": "Andalusian",
                            "display": "Andalusian",
                        },
                        {
                            "code": "2139-4",
                            "definition": "Asturian",
                            "display": "Asturian",
                        },
                        {
                            "code": "2140-2",
                            "definition": "Castillian",
                            "display": "Castillian",
                        },
                        {
                            "code": "2141-0",
                            "definition": "Catalonian",
                            "display": "Catalonian",
                        },
                        {
                            "code": "2142-8",
                            "definition": "Belearic Islander",
                            "display": "Belearic Islander",
                        },
                        {
                            "code": "2143-6",
                            "definition": "Gallego",
                            "display": "Gallego",
                        },
                        {
                            "code": "2144-4",
                            "definition": "Valencian",
                            "display": "Valencian",
                        },
                        {
                            "code": "2145-1",
                            "definition": "Canarian",
                            "display": "Canarian",
                        },
                        {
                            "code": "2146-9",
                            "definition": "Spanish Basque",
                            "display": "Spanish Basque",
                        },
                    ],
                    "definition": "Spaniard",
                    "display": "Spaniard",
                },
                {
                    "code": "2148-5",
                    "concept": [
                        {
                            "code": "2149-3",
                            "definition": "Mexican American",
                            "display": "Mexican American",
                        },
                        {
                            "code": "2150-1",
                            "definition": "Mexicano",
                            "display": "Mexicano",
                        },
                        {
                            "code": "2151-9",
                            "definition": "Chicano",
                            "display": "Chicano",
                        },
                        {
                            "code": "2152-7",
                            "definition": "La Raza",
                            "display": "La Raza",
                        },
                        {
                            "code": "2153-5",
                            "definition": "Mexican American Indian",
                            "display": "Mexican American Indian",
                        },
                    ],
                    "definition": "Mexican",
                    "display": "Mexican",
                },
                {
                    "code": "2155-0",
                    "concept": [
                        {
                            "code": "2156-8",
                            "definition": "Costa Rican",
                            "display": "Costa Rican",
                        },
                        {
                            "code": "2157-6",
                            "definition": "Guatemalan",
                            "display": "Guatemalan",
                        },
                        {
                            "code": "2158-4",
                            "definition": "Honduran",
                            "display": "Honduran",
                        },
                        {
                            "code": "2159-2",
                            "definition": "Nicaraguan",
                            "display": "Nicaraguan",
                        },
                        {
                            "code": "2160-0",
                            "definition": "Panamanian",
                            "display": "Panamanian",
                        },
                        {
                            "code": "2161-8",
                            "definition": "Salvadoran",
                            "display": "Salvadoran",
                        },
                        {
                            "code": "2162-6",
                            "definition": "Central American Indian",
                            "display": "Central American Indian",
                        },
                        {
                            "code": "2163-4",
                            "definition": "Canal Zone",
                            "display": "Canal Zone",
                        },
                    ],
                    "definition": "Central American",
                    "display": "Central American",
                },
                {
                    "code": "2165-9",
                    "concept": [
                        {
                            "code": "2166-7",
                            "definition": "Argentinean",
                            "display": "Argentinean",
                        },
                        {
                            "code": "2167-5",
                            "definition": "Bolivian",
                            "display": "Bolivian",
                        },
                        {
                            "code": "2168-3",
                            "definition": "Chilean",
                            "display": "Chilean",
                        },
                        {
                            "code": "2169-1",
                            "definition": "Colombian",
                            "display": "Colombian",
                        },
                        {
                            "code": "2170-9",
                            "definition": "Ecuadorian",
                            "display": "Ecuadorian",
                        },
                        {
                            "code": "2171-7",
                            "definition": "Paraguayan",
                            "display": "Paraguayan",
                        },
                        {
                            "code": "2172-5",
                            "definition": "Peruvian",
                            "display": "Peruvian",
                        },
                        {
                            "code": "2173-3",
                            "definition": "Uruguayan",
                            "display": "Uruguayan",
                        },
                        {
                            "code": "2174-1",
                            "definition": "Venezuelan",
                            "display": "Venezuelan",
                        },
                        {
                            "code": "2175-8",
                            "definition": "South American Indian",
                            "display": "South American Indian",
                        },
                        {
                            "code": "2176-6",
                            "definition": "Criollo",
                            "display": "Criollo",
                        },
                    ],
                    "definition": "South American",
                    "display": "South American",
                },
                {
                    "code": "2178-2",
                    "definition": "Latin American",
                    "display": "Latin American",
                },
                {
                    "code": "2180-8",
                    "definition": "Puerto Rican",
                    "display": "Puerto Rican",
                },
                {"code": "2182-4", "definition": "Cuban", "display": "Cuban"},
                {"code": "2184-0", "definition": "Dominican", "display": "Dominican"},
            ],
            "definition": "Hispanic or Latino",
            "display": "Hispanic or Latino",
        }
    )
    """
    Hispanic or Latino

    Hispanic or Latino
    """

    two186_5 = CodeSystemConcept(
        {
            "code": "2186-5",
            "definition": 'Note that this term remains in the table for completeness, even though within HL7, the notion of "not otherwise coded" term is deprecated.',
            "display": "Not Hispanic or Latino",
        }
    )
    """
    Not Hispanic or Latino

    Note that this term remains in the table for completeness, even though within HL7, the notion of "not otherwise coded" term is deprecated.
    """

    class Meta:
        resource = _resource
