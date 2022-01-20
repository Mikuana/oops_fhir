from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.expression_language import (
    ExpressionLanguage as ExpressionLanguage_,
)


__all__ = ["ExpressionLanguage"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ExpressionLanguage(ExpressionLanguage_):
    """
    ExpressionLanguage

    The media type of the expression language.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/expression-language
    """

    class Meta:
        resource = _resource
