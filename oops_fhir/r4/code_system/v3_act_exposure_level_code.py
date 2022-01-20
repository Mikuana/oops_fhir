from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3ActExposureLevelCode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3ActExposureLevelCode:
    """
    v3 Code System ActExposureLevelCode

     A qualitative measure of the degree of exposure to the causative agent.
This includes concepts such as "low", "medium" and "high".  This
quantifies how the quantity that was available to be administered to the
target differs from typical or background levels of the substance.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-ActExposureLevelCode
    """

    underscore_act_exposure_level_code = CodeSystemConcept(
        {
            "code": "_ActExposureLevelCode",
            "concept": [
                {
                    "code": "HIGH",
                    "definition": "Description: Exposure to an agent at a relatively high level above background.",
                    "display": "high",
                },
                {
                    "code": "LOW",
                    "definition": "Description: Exposure to an agent at a relatively low level above background.",
                    "display": "low",
                },
                {
                    "code": "MEDIUM",
                    "definition": "Description: Exposure to an agent at a relatively moderate level above background.A",
                    "display": "medium",
                },
            ],
            "definition": 'A qualitative measure of the degree of exposure to the causative agent.  This includes concepts such as "low", "medium" and "high".  This quantifies how the quantity that was available to be administered to the target differs from typical or background levels of the substance.',
            "display": "ActExposureLevelCode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActExposureLevelCode

    A qualitative measure of the degree of exposure to the causative agent.  This includes concepts such as "low", "medium" and "high".  This quantifies how the quantity that was available to be administered to the target differs from typical or background levels of the substance.
    """

    class Meta:
        resource = _resource
