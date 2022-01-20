from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.indicator import Indicator as Indicator_


__all__ = ["Indicator"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class Indicator(Indicator_):
    """
    CDSHooksIndicator

    This value set captures the set of indicator codes defined by the CDS
Hooks specification.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/cdshooks-indicator
    """

    class Meta:
        resource = _resource
