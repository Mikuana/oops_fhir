from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.extension_context_type import (
    ExtensionContextType as ExtensionContextType_,
)


__all__ = ["ExtensionContextType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ExtensionContextType(ExtensionContextType_):
    """
    ExtensionContextType

    How an extension context is interpreted.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/extension-context-type
    """

    class Meta:
        resource = _resource
