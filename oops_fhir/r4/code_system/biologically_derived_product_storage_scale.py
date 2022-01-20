from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["BiologicallyDerivedProductStorageScale"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class BiologicallyDerivedProductStorageScale:
    """
    BiologicallyDerivedProductStorageScale

    BiologicallyDerived Product Storage Scale.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/product-storage-scale
    """

    farenheit = CodeSystemConcept(
        {
            "code": "farenheit",
            "definition": "Fahrenheit temperature scale.",
            "display": "Fahrenheit",
        }
    )
    """
    Fahrenheit

    Fahrenheit temperature scale.
    """

    celsius = CodeSystemConcept(
        {
            "code": "celsius",
            "definition": "Celsius or centigrade temperature scale.",
            "display": "Celsius",
        }
    )
    """
    Celsius

    Celsius or centigrade temperature scale.
    """

    kelvin = CodeSystemConcept(
        {
            "code": "kelvin",
            "definition": "Kelvin absolute thermodynamic temperature scale.",
            "display": "Kelvin",
        }
    )
    """
    Kelvin

    Kelvin absolute thermodynamic temperature scale.
    """

    class Meta:
        resource = _resource
