from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["Currencies"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class Currencies(ValueSet):
    """
    CurrencyCode

    Currency codes from ISO 4217 (see https://www.iso.org/iso-4217-currency-
codes.html)

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/currencies
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
