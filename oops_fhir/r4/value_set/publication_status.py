from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.publication_status import (
    PublicationStatus as PublicationStatus_,
)


__all__ = ["PublicationStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class PublicationStatus(PublicationStatus_):
    """
    PublicationStatus

    The lifecycle status of an artifact.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/publication-status
    """

    class Meta:
        resource = _resource
