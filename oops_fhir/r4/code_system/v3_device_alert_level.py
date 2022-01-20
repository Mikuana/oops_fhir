from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3DeviceAlertLevel"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3DeviceAlertLevel:
    """
    v3 Code System DeviceAlertLevel

     Domain values for the Device.Alert_levelCode

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-DeviceAlertLevel
    """

    c = CodeSystemConcept(
        {
            "code": "C",
            "definition": "Shut Down, Fix Problem and Re-initialize",
            "display": "Critical",
        }
    )
    """
    Critical

    Shut Down, Fix Problem and Re-initialize
    """

    n = CodeSystemConcept(
        {"code": "N", "definition": "No Corrective Action Needed", "display": "Normal"}
    )
    """
    Normal

    No Corrective Action Needed
    """

    s = CodeSystemConcept(
        {"code": "S", "definition": "Corrective Action Required", "display": "Serious"}
    )
    """
    Serious

    Corrective Action Required
    """

    w = CodeSystemConcept(
        {
            "code": "W",
            "definition": "Corrective Action Anticipated",
            "display": "Warning",
        }
    )
    """
    Warning

    Corrective Action Anticipated
    """

    class Meta:
        resource = _resource
