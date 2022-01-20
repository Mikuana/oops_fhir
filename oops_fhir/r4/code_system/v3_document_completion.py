from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3DocumentCompletion"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3DocumentCompletion:
    """
    v3 Code System DocumentCompletion

     Identifies the current completion state of a clinical document.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-DocumentCompletion
    """

    au = CodeSystemConcept(
        {
            "code": "AU",
            "definition": "A completion status in which a document has been signed manually or electronically by one or more individuals who attest to its accuracy.  No explicit determination is made that the assigned individual has performed the authentication.  While the standard allows multiple instances of authentication, it would be typical to have a single instance of authentication, usually by the assigned individual.",
            "display": "authenticated",
        }
    )
    """
    authenticated

    A completion status in which a document has been signed manually or electronically by one or more individuals who attest to its accuracy.  No explicit determination is made that the assigned individual has performed the authentication.  While the standard allows multiple instances of authentication, it would be typical to have a single instance of authentication, usually by the assigned individual.
    """

    di = CodeSystemConcept(
        {
            "code": "DI",
            "definition": "A completion status in which information has been orally recorded but not yet transcribed.",
            "display": "dictated",
        }
    )
    """
    dictated

    A completion status in which information has been orally recorded but not yet transcribed.
    """

    do = CodeSystemConcept(
        {
            "code": "DO",
            "definition": "A completion status in which document content, other than dictation, has been received but has not been translated into the final electronic format.  Examples include paper documents, whether hand-written or typewritten, and intermediate electronic forms, such as voice to text.",
            "display": "documented",
        }
    )
    """
    documented

    A completion status in which document content, other than dictation, has been received but has not been translated into the final electronic format.  Examples include paper documents, whether hand-written or typewritten, and intermediate electronic forms, such as voice to text.
    """

    in_ = CodeSystemConcept(
        {
            "code": "IN",
            "definition": "A completion status in which information is known to be missing from a transcribed document.",
            "display": "incomplete",
        }
    )
    """
    incomplete

    A completion status in which information is known to be missing from a transcribed document.
    """

    ip = CodeSystemConcept(
        {
            "code": "IP",
            "definition": "A workflow status where the material has been assigned to personnel to perform the task of transcription. The document remains in this state until the document is transcribed.",
            "display": "in progress",
        }
    )
    """
    in progress

    A workflow status where the material has been assigned to personnel to perform the task of transcription. The document remains in this state until the document is transcribed.
    """

    la = CodeSystemConcept(
        {
            "code": "LA",
            "definition": "A completion status in which a document has been signed manually or electronically by the individual who is legally responsible for that document. This is the most mature state in the workflow progression.",
            "display": "legally authenticated",
        }
    )
    """
    legally authenticated

    A completion status in which a document has been signed manually or electronically by the individual who is legally responsible for that document. This is the most mature state in the workflow progression.
    """

    nu = CodeSystemConcept(
        {
            "code": "NU",
            "definition": "A completion status in which a document was created in error or was placed in the wrong chart. The document is no longer available.",
            "display": "nullified document",
        }
    )
    """
    nullified document

    A completion status in which a document was created in error or was placed in the wrong chart. The document is no longer available.
    """

    pa = CodeSystemConcept(
        {
            "code": "PA",
            "definition": "A completion status in which a document is transcribed but not authenticated.",
            "display": "pre-authenticated",
        }
    )
    """
    pre-authenticated

    A completion status in which a document is transcribed but not authenticated.
    """

    uc = CodeSystemConcept(
        {
            "code": "UC",
            "definition": "A completion status where the document is complete and there is no expectation that the document will be signed.",
            "display": "unsigned completed document",
        }
    )
    """
    unsigned completed document

    A completion status where the document is complete and there is no expectation that the document will be signed.
    """

    class Meta:
        resource = _resource
