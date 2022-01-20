from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_ethnicity import v3Ethnicity as v3Ethnicity_


__all__ = ["v3Ethnicity"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3Ethnicity(v3Ethnicity_):
    """
    v3 Code System Ethnicity

     In the United States, federal standards for classifying data on
ethnicity determine the categories used by federal agencies and exert a
strong influence on categorization by state and local agencies and
private sector organizations. The federal standards do not conceptually
define ethnicity, and they recognize the absence of an anthropological
or scientific basis for ethnicity classification.  Instead, the federal
standards acknowledge that ethnicity is a social-political construct in
which an individual's own identification with a particular ethnicity is
preferred to observer identification.  The standards specify two minimum
ethnicity categories: Hispanic or Latino, and Not Hispanic or Latino.
The standards define a Hispanic or Latino as a person of "Mexican,
Puerto Rican, Cuban, South or Central America, or other Spanish culture
or origin, regardless of race." The standards stipulate that ethnicity
data need not be limited to the two minimum categories, but any
expansion must be collapsible to those categories.  In addition, the
standards stipulate that an individual can be Hispanic or Latino or can
be Not Hispanic or Latino, but cannot be both.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-Ethnicity
    """

    class Meta:
        resource = _resource
