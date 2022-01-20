from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ExampleCoverageFinancialExceptionCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ExampleCoverageFinancialExceptionCodes:
    """
    Example Coverage Financial Exception Codes

    This value set includes Example Coverage Financial Exception Codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/ex-coverage-financial-exception
    """

    retired = CodeSystemConcept(
        {
            "code": "retired",
            "definition": "Retired persons have all copays and deductibles reduced.",
            "display": "Retired",
        }
    )
    """
    Retired

    Retired persons have all copays and deductibles reduced.
    """

    foster = CodeSystemConcept(
        {
            "code": "foster",
            "definition": "Children in the foster care have all copays and deductibles waived.",
            "display": "Foster child",
        }
    )
    """
    Foster child

    Children in the foster care have all copays and deductibles waived.
    """

    class Meta:
        resource = _resource
