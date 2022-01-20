from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3triggerEventID"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3triggerEventID:
    """
    v3 Code System triggerEventID

      Description:  This code system contains all HL7 artifacts of type TE
(Trigger Event) that are created by HL7 or its affiliates or their
designates using the realm namespacing rules approved by HL7.  Local
implementations who create trigger events outside of these namespacing
rules, (e.g. using the ZZ realm code) must register their own code
system.  The specific list of legal codes can be found by consulting the
HL7 publications (editions, ballots, implementation guides, etc.)
published by HL7 Inc. and by the various HL7 affiliates and their
designates.  Codes shall be expressed in upper case, with separator as
shown in HL7 publications with no version id.  E.g. PORX_TE123456UV.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-triggerEventID
    """

    polb_te004000_uv = CodeSystemConcept(
        {
            "code": "POLB_TE004000UV",
            "definition": "Description:",
            "display": "Result Status",
        }
    )
    """
    Result Status

    Description:
    """

    polb_te004001_uv = CodeSystemConcept(
        {
            "code": "POLB_TE004001UV",
            "definition": "Description:",
            "display": "Result Confirm",
        }
    )
    """
    Result Confirm

    Description:
    """

    polb_te004002_uv = CodeSystemConcept(
        {
            "code": "POLB_TE004002UV",
            "definition": "Description:",
            "display": "Result Reject",
        }
    )
    """
    Result Reject

    Description:
    """

    polb_te004007_uv = CodeSystemConcept(
        {
            "code": "POLB_TE004007UV",
            "definition": "Description:",
            "display": "Result Tracking",
        }
    )
    """
    Result Tracking

    Description:
    """

    polb_te004100_uv = CodeSystemConcept(
        {
            "code": "POLB_TE004100UV",
            "definition": "Description:",
            "display": "Result in Progress",
        }
    )
    """
    Result in Progress

    Description:
    """

    polb_te004102_uv = CodeSystemConcept(
        {
            "code": "POLB_TE004102UV",
            "definition": "Description:",
            "display": "Result Activate",
        }
    )
    """
    Result Activate

    Description:
    """

    polb_te004200_uv = CodeSystemConcept(
        {
            "code": "POLB_TE004200UV",
            "definition": "Description:",
            "display": "Result Complete with Fulfillment",
        }
    )
    """
    Result Complete with Fulfillment

    Description:
    """

    polb_te004201_uv = CodeSystemConcept(
        {
            "code": "POLB_TE004201UV",
            "definition": "Description:",
            "display": "Result Corrected",
        }
    )
    """
    Result Corrected

    Description:
    """

    polb_te004202_uv = CodeSystemConcept(
        {
            "code": "POLB_TE004202UV",
            "definition": "Description:",
            "display": "Result Complete",
        }
    )
    """
    Result Complete

    Description:
    """

    polb_te004301_uv = CodeSystemConcept(
        {
            "code": "POLB_TE004301UV",
            "definition": "Description:",
            "display": "Result Abort",
        }
    )
    """
    Result Abort

    Description:
    """

    polb_te004500_uv = CodeSystemConcept(
        {
            "code": "POLB_TE004500UV",
            "definition": "Description:",
            "display": "Result Nullify",
        }
    )
    """
    Result Nullify

    Description:
    """

    class Meta:
        resource = _resource
