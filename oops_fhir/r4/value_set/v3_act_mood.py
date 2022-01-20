from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_mood import v3ActMood as v3ActMood_


__all__ = ["v3ActMood"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ActMood(v3ActMood_):
    """
    v3 Code System ActMood

     OpenIssue:  In Ballot 2009May, a strong Negative vote was lodged
against several of the concept definitions in the vocabulary used for
Act.moodCode. The vote was found "Persuasive With Mod", with the
understanding that M and M would undertake a detailed review of these
concept definitions for a future release of the RIM.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ActMood
    """

    class Meta:
        resource = _resource
