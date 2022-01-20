from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["COSMIC"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class COSMIC(ValueSet):
    """
    C o s m i c

    COSMIC : Catalogue Of Somatic Mutations In Cancer

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/cosmic
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
