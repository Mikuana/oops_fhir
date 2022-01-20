from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.consent_data_meaning import (
    ConsentDataMeaning as ConsentDataMeaning_,
)


__all__ = ["ConsentDataMeaning"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ConsentDataMeaning(ConsentDataMeaning_):
    """
    ConsentDataMeaning

    How a resource reference is interpreted when testing consent
restrictions.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/consent-data-meaning
    """

    class Meta:
        resource = _resource
