from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ProcedureDeviceActionCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ProcedureDeviceActionCodes:
    """
    Procedure Device Action Codes

    Example codes indicating the change that happened to the device during
the procedure.  Note that these are in no way complete and might not
even be appropriate for some uses.

    Status: draft - Version: 4.0.1

    Copyright This resource includes content from SNOMED Clinical Terms® (SNOMED CT®) which is copyright of the International Health Terminology Standards Development Organisation (IHTSDO). Implementers of these specifications must have the appropriate SNOMED CT Affiliate license - for more information contact http://www.snomed.org/snomed-ct/get-snomed-ct or info@snomed.org

    http://hl7.org/fhir/device-action
    """

    implanted = CodeSystemConcept(
        {
            "code": "implanted",
            "definition": "The device was implanted in the patient during the procedure.",
            "display": "Implanted",
        }
    )
    """
    Implanted

    The device was implanted in the patient during the procedure.
    """

    explanted = CodeSystemConcept(
        {
            "code": "explanted",
            "definition": "The device was explanted from the patient during the procedure.",
            "display": "Explanted",
        }
    )
    """
    Explanted

    The device was explanted from the patient during the procedure.
    """

    manipulated = CodeSystemConcept(
        {
            "code": "manipulated",
            "definition": "The device remains in the patient, but its location, settings, or functionality was changed.",
            "display": "Manipulated",
        }
    )
    """
    Manipulated

    The device remains in the patient, but its location, settings, or functionality was changed.
    """

    class Meta:
        resource = _resource
