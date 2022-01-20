from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.can_push_updates import canpushupdates as canpushupdates_


__all__ = ["canpushupdates"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class canpushupdates(canpushupdates_):
    """
    Can-push-updates

    Ability of the primary source to push updates/alerts

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/verificationresult-can-push-updates
    """

    class Meta:
        resource = _resource
