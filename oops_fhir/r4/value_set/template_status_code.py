from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["TemplateStatusCode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class TemplateStatusCode(ValueSet):
    """
    TemplateStatusCode

    The status indicates the level of maturity of the design and may be used
to manage the use of the design.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/template-status-code
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
