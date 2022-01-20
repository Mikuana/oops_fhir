from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3EmployeeJobClass"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3EmployeeJobClass:
    """
    v3 Code System EmployeeJobClass

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-EmployeeJobClass
    """

    ft = CodeSystemConcept(
        {
            "code": "FT",
            "definition": "Employment in which the employee is expected to work at least a standard work week (defined by the US Bureau of Labor Statistics as 35-44 hours per week)",
            "display": "full-time",
        }
    )
    """
    full-time

    Employment in which the employee is expected to work at least a standard work week (defined by the US Bureau of Labor Statistics as 35-44 hours per week)
    """

    pt = CodeSystemConcept(
        {
            "code": "PT",
            "definition": "Employment in which the employee is expected to work less than a standard work week (defined by the US Bureau of Labor Statistics as 35-44 hours per week)",
            "display": "part-time",
        }
    )
    """
    part-time

    Employment in which the employee is expected to work less than a standard work week (defined by the US Bureau of Labor Statistics as 35-44 hours per week)
    """

    class Meta:
        resource = _resource
