from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ExampleDiagnosisOnAdmissionCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ExampleDiagnosisOnAdmissionCodes:
    """
    Example Diagnosis on Admission Codes

    This value set includes example Diagnosis on Admission codes.

    Status: draft - Version: 4.0.1

    Copyright These codes have been appropriated from the [UB04 code set](http://www.nubc.org/) owned and managed by the [AHA](http://www.aha.org/). Users require a [license from the AHA](http://www.nubc.org/licensing/index.dhtml) in order to use these codes. **Note: the codes have been withdrawn in a later version**

    http://terminology.hl7.org/CodeSystem/ex-diagnosis-on-admission
    """

    y = CodeSystemConcept(
        {
            "code": "y",
            "definition": "Diagnosis was present at time of inpatient admission.",
            "display": "Yes",
        }
    )
    """
    Yes

    Diagnosis was present at time of inpatient admission.
    """

    n = CodeSystemConcept(
        {
            "code": "n",
            "definition": "Diagnosis was not present at time of inpatient admission.",
            "display": "No",
        }
    )
    """
    No

    Diagnosis was not present at time of inpatient admission.
    """

    u = CodeSystemConcept(
        {
            "code": "u",
            "definition": "Documentation insufficient to determine if condition was present at the time of inpatient admission.",
            "display": "Unknown",
        }
    )
    """
    Unknown

    Documentation insufficient to determine if condition was present at the time of inpatient admission.
    """

    w = CodeSystemConcept(
        {
            "code": "w",
            "definition": "Clinically undetermined. Provider unable to clinically determine whether the condition was present at the time of inpatient admission.",
            "display": "Undetermined",
        }
    )
    """
    Undetermined

    Clinically undetermined. Provider unable to clinically determine whether the condition was present at the time of inpatient admission.
    """

    class Meta:
        resource = _resource
