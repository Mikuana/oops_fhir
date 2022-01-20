from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3ExposureMode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3ExposureMode:
    """
    v3 Code System ExposureMode

     Code for the mechanism by which the exposure agent was exchanged or
potentially exchanged by the participants involved in the exposure.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-ExposureMode
    """

    underscore_exposure_mode = CodeSystemConcept(
        {
            "code": "_ExposureMode",
            "concept": [
                {
                    "code": "AIRBORNE",
                    "definition": "Description: Communication of an agent from a living subject or environmental source to a living subject through indirect contact via oral or nasal inhalation.",
                    "display": "airborne",
                },
                {
                    "code": "CONTACT",
                    "definition": "Description: Communication of an agent from a living subject or environmental source to a living subject through direct physical contact.",
                    "display": "contact",
                },
                {
                    "code": "FOODBORNE",
                    "definition": "Description: Communication of an agent from a food source to a living subject via oral consumption.",
                    "display": "foodborne",
                },
                {
                    "code": "WATERBORNE",
                    "definition": "Description: Communication of an agent to a living subject by contact and/or consumption via an aqueous medium",
                    "display": "waterborne",
                },
            ],
            "definition": "Code for the mechanism by which the exposure agent was exchanged or potentially exchanged by the participants involved in the exposure.",
            "display": "ExposureMode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ExposureMode

    Code for the mechanism by which the exposure agent was exchanged or potentially exchanged by the participants involved in the exposure.
    """

    class Meta:
        resource = _resource
