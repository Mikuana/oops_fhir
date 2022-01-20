from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.test_script_profile_origin_type import (
    TestScriptProfileOriginType as TestScriptProfileOriginType_,
)


__all__ = ["TestScriptProfileOriginType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class TestScriptProfileOriginType(TestScriptProfileOriginType_):
    """
    Test script profile origin type

    This value set defines a set of codes that are used to indicate the
profile type of a test system when acting as the origin within a
TestScript.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/testscript-profile-origin-types
    """

    class Meta:
        resource = _resource
