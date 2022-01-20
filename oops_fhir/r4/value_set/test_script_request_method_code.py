from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.test_script_request_method_code import (
    TestScriptRequestMethodCode as TestScriptRequestMethodCode_,
)


__all__ = ["TestScriptRequestMethodCode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class TestScriptRequestMethodCode(TestScriptRequestMethodCode_):
    """
    TestScriptRequestMethodCode

    The allowable request method or HTTP operation codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/http-operations
    """

    class Meta:
        resource = _resource
