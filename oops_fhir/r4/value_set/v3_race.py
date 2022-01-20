from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_race import v3Race as v3Race_


__all__ = ["v3Race"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3Race(v3Race_):
    """
    v3 Code System Race

     In the United States, federal standards for classifying data on race
determine the categories used by federal agencies and exert a strong
influence on categorization by state and local agencies and private
sector organizations.  The federal standards do not conceptually define
race, and they recognize the absence of an anthropological or scientific
basis for racial classification.  Instead, the federal standards
acknowledge that race is a social-political construct in which an
individual's own identification with one more race categories is
preferred to observer identification. The standards use a variety of
features to define five minimum race categories. Among these features
are descent from "the original peoples" of a specified region or nation.
The minimum race categories are American Indian or Alaska Native, Asian,
Black or African American, Native Hawaiian or Other Pacific Islander,
and White.  The federal standards stipulate that race data need not be
limited to the five minimum categories, but any expansion must be
collapsible to those categories.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-Race
    """

    class Meta:
        resource = _resource
