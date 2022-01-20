from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.basic_resource_types import (
    BasicResourceTypes as BasicResourceTypes_,
)


__all__ = ["BasicResourceTypes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class BasicResourceTypes(BasicResourceTypes_):
    """
    Basic Resource Types

    This value set defines codes for resources not yet supported by (or
which will never be supported by) FHIR.  Many of the codes listed here
will eventually be turned into official resources.  However, there is no
guarantee that any particular resource will be created nor that the
scope will be exactly as defined by the codes presented here.  Codes in
this set will be deprecated if/when formal resources are defined that
encompass these concepts.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/basic-resource-type
    """

    class Meta:
        resource = _resource
