from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3AcknowledgementDetailType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3AcknowledgementDetailType:
    """
    v3 Code System AcknowledgementDetailType

     A code identifying the specific message to be provided.  Discussion:  A
textual value may be specified as the print name, or for non-coded
messages, as the original text.  Examples:  'Required attribute xxx is
missing', 'System will be unavailable March 19 from 0100 to 0300'

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-AcknowledgementDetailType
    """

    e = CodeSystemConcept(
        {
            "code": "E",
            "definition": "Definition:An issue which has prevented, or will prevent (unless a management is provided for the issue by the sender), the successful processing of an interaction.  Response interactions which include an issue which is an Error are a 'rejection', indicating that the request was not successfully processed. \r\n\n                        \n                           Example:Unable to find specified patient.",
            "display": "Error",
        }
    )
    """
    Error

    Definition:An issue which has prevented, or will prevent (unless a management is provided for the issue by the sender), the successful processing of an interaction.  Response interactions which include an issue which is an Error are a 'rejection', indicating that the request was not successfully processed. 

                        
                           Example:Unable to find specified patient.
    """

    i = CodeSystemConcept(
        {
            "code": "I",
            "definition": "Definition: The message relates to an issue which has no bearing on the successful processing of the request.  Information issues cannot be overridden by specifying a management.\r\n\n                        \n                           Example: A Patient's coverage will expire in 5 days.",
            "display": "Information",
        }
    )
    """
    Information

    Definition: The message relates to an issue which has no bearing on the successful processing of the request.  Information issues cannot be overridden by specifying a management.

                        
                           Example: A Patient's coverage will expire in 5 days.
    """

    w = CodeSystemConcept(
        {
            "code": "W",
            "definition": "Definition: The message relates to an issue which cannot prevent the successful processing of a request, but which could result in the processing not having the ideal or intended effect.  Managing a warning issue is not required for successful processing, but will suppress the warning from being raised. \r\n\n                        \n                           Example:\n                        \r\n\n                        Unexpected additional repetitions of phone number have been ignored.",
            "display": "Warning",
        }
    )
    """
    Warning

    Definition: The message relates to an issue which cannot prevent the successful processing of a request, but which could result in the processing not having the ideal or intended effect.  Managing a warning issue is not required for successful processing, but will suppress the warning from being raised. 

                        
                           Example:
                        

                        Unexpected additional repetitions of phone number have been ignored.
    """

    err = CodeSystemConcept(
        {"code": "ERR", "property": [{"code": "status", "valueCode": "retired"}]}
    )
    """
    None

    
    """

    info = CodeSystemConcept(
        {"code": "INFO", "property": [{"code": "status", "valueCode": "retired"}]}
    )
    """
    None

    
    """

    warn = CodeSystemConcept(
        {"code": "WARN", "property": [{"code": "status", "valueCode": "retired"}]}
    )
    """
    None

    
    """

    class Meta:
        resource = _resource
