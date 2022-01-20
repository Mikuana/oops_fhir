from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3QueryParameterValue"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3QueryParameterValue:
    """
    v3 Code System QueryParameterValue

     The domain of coded values used as parameters within QueryByParameter
queries.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-QueryParameterValue
    """

    underscore_dispense_query_filter_code = CodeSystemConcept(
        {
            "code": "_DispenseQueryFilterCode",
            "concept": [
                {
                    "code": "ALLDISP",
                    "definition": "Description:Returns all dispenses to date for a prescription.",
                    "display": "all dispenses",
                },
                {
                    "code": "LASTDISP",
                    "definition": "Description:Returns the most recent dispense for a prescription.",
                    "display": "last dispense",
                },
                {
                    "code": "NODISP",
                    "definition": "Description:Returns no dispense for a prescription.",
                    "display": "no dispense",
                },
            ],
            "definition": "Description:Filter codes used to manage volume of dispenses returned by  a parameter-based queries.",
            "display": "dispense query filter code",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    dispense query filter code

    Description:Filter codes used to manage volume of dispenses returned by  a parameter-based queries.
    """

    underscore_order_filter_code = CodeSystemConcept(
        {
            "code": "_OrderFilterCode",
            "concept": [
                {
                    "code": "AO",
                    "definition": "Return all orders.",
                    "display": "all orders",
                },
                {
                    "code": "ONR",
                    "definition": "Return only those orders that do not have results.",
                    "display": "orders without results",
                },
                {
                    "code": "OWR",
                    "definition": "Return only those orders that have results.",
                    "display": "orders with results",
                },
            ],
            "definition": "Filter codes used to manage types of orders being returned by a parameter-based query.",
            "display": "_OrderFilterCode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    _OrderFilterCode

    Filter codes used to manage types of orders being returned by a parameter-based query.
    """

    underscore_prescription_dispense_filter_code = CodeSystemConcept(
        {
            "code": "_PrescriptionDispenseFilterCode",
            "concept": [
                {
                    "code": "C",
                    "definition": "Filter to only include SubstanceAdministration orders which have no remaining quantity authorized to be dispensed.",
                    "display": "Completely dispensed",
                },
                {
                    "code": "N",
                    "definition": "Filter to only include SubstanceAdministration orders which have no fulfilling supply events performed.",
                    "display": "Never Dispensed",
                },
                {
                    "code": "R",
                    "definition": "Filter to only include SubstanceAdministration orders which have had at least one fulfilling supply event, but which still have outstanding quantity remaining to be authorized.",
                    "display": "Dispensed with remaining fills",
                },
            ],
            "definition": 'A "helper" vocabulary used to construct complex query filters based on how and whether a prescription has been dispensed.',
            "display": "Prescription Dispense Filter Code",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    Prescription Dispense Filter Code

    A "helper" vocabulary used to construct complex query filters based on how and whether a prescription has been dispensed.
    """

    underscore_query_parameter_value = CodeSystemConcept(
        {
            "code": "_QueryParameterValue",
            "concept": [
                {
                    "code": "ISSFA",
                    "definition": "Description:Result set should not be filtered based on the presence of issues.",
                    "display": "all",
                },
                {
                    "code": "ISSFI",
                    "definition": "Description:Result set should be filtered to only include records with associated issues.",
                    "display": "with issues",
                },
                {
                    "code": "ISSFU",
                    "definition": "Description:Result set should be filtered to only include records with associated unmanaged issues.",
                    "display": "with unmanaged issues",
                },
            ],
            "definition": "Description:Indicates how result sets should be filtered based on whether they have associated issues.",
            "display": "QueryParameterValue",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    QueryParameterValue

    Description:Indicates how result sets should be filtered based on whether they have associated issues.
    """

    class Meta:
        resource = _resource
