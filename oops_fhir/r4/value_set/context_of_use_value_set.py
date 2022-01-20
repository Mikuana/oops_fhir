from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.snomed_ct import SNOMEDCT


__all__ = ["ContextofUseValueSet"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ContextofUseValueSet(ValueSet):
    """
    ConformanceUseContext

    This value set defines a base set of codes that can be used to indicate
that the content in a resource was developed with a focus and intent of
supporting use within particular contexts.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/use-context
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
