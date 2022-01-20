from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.chromosome_human import (
    chromosomehuman as chromosomehuman_,
)


__all__ = ["chromosomehuman"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class chromosomehuman(chromosomehuman_):
    """
    chromosome-human

    Chromosome number for human.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/chromosome-human
    """

    class Meta:
        resource = _resource
