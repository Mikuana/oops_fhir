from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_sequencing import v3Sequencing as v3Sequencing_


__all__ = ["v3Sequencing"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3Sequencing(v3Sequencing_):
    """
    v3 Code System Sequencing

     Specifies sequence of sort order.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-Sequencing
    """

    class Meta:
        resource = _resource
