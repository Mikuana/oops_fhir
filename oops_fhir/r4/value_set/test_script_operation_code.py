from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.test_script_operation_code import (
    TestScriptOperationCode as TestScriptOperationCode_,
)


__all__ = ["TestScriptOperationCode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class TestScriptOperationCode(TestScriptOperationCode_):
    """
    Test script operation code

    This value set defines a set of codes that are used to indicate the
supported operations of a testing engine or tool.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/testscript-operation-codes
    """

    class Meta:
        resource = _resource
