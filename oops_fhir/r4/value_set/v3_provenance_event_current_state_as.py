from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["v3ProvenanceEventCurrentStateAS"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ProvenanceEventCurrentStateAS(ValueSet):
    """
    V3 Value SetProvenanceEventCurrentState-AS

     Specifies the state change of a target Act, using ActStatus codes, from
its previous state as a predecessor Act. For example, if the target Act
is the result of a predecessor Act being "obsoleted" and replaced with
the target Act, the source ProvenanceEventCurrentState Act code would be
"obsoleted".

    Status: active - Version: 2014-08-07

    http://terminology.hl7.org/ValueSet/v3-ProvenanceEventCurrentState-AS
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
