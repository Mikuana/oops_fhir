from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.spdxlicense import SPDXLicense as SPDXLicense_


__all__ = ["SPDXLicense"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SPDXLicense(SPDXLicense_):
    """
    SPDXLicense

    The license that applies to an Implementation Guide (using an SPDX
license Identifiers, or 'not-open-source'). The binding is required but
new SPDX license Identifiers are allowed to be used
(https://spdx.org/licenses/).

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/spdx-license
    """

    class Meta:
        resource = _resource
