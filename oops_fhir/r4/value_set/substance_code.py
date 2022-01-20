from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.snomed_ct import SNOMEDCT


__all__ = ["SubstanceCode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SubstanceCode(ValueSet):
    """
    Substance Code

    This value set contains concept codes for specific substances. It
includes codes from [SNOMED](http://snomed.info/sct) where concept is-a
105590001 (Substance (substance)) and where concept is-a 373873005
(Pharmaceutical / biologic product (product))

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/substance-code
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
