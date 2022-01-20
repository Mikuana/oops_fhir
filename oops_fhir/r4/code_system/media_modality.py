from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["MediaModality"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class MediaModality:
    """
    Media Modality

    Detailed information about the type of the image - its kind, purpose, or
the kind of equipment used to generate it.

    Status: draft - Version: 4.0.1

    Copyright This resource includes content from the Digital Imaging and Communications in Medicine (DICOM) Standard, Copyright 2011 by the National Electrical Manufacturers Association

    http://terminology.hl7.org/CodeSystem/media-modality
    """

    diagram = CodeSystemConcept(
        {
            "code": "diagram",
            "definition": "A diagram. Often used in diagnostic reports",
            "display": "Diagram",
        }
    )
    """
    Diagram

    A diagram. Often used in diagnostic reports
    """

    fax = CodeSystemConcept(
        {
            "code": "fax",
            "definition": "A digital record of a fax document",
            "display": "Fax",
        }
    )
    """
    Fax

    A digital record of a fax document
    """

    scan = CodeSystemConcept(
        {
            "code": "scan",
            "definition": "A digital scan of a document. This is reserved for when there is not enough metadata to create a document reference",
            "display": "Scanned Document",
        }
    )
    """
    Scanned Document

    A digital scan of a document. This is reserved for when there is not enough metadata to create a document reference
    """

    retina = CodeSystemConcept(
        {
            "code": "retina",
            "definition": "A retinal image used for identification purposes",
            "display": "Retina Scan",
        }
    )
    """
    Retina Scan

    A retinal image used for identification purposes
    """

    fingerprint = CodeSystemConcept(
        {
            "code": "fingerprint",
            "definition": "A finger print scan used for identification purposes",
            "display": "Fingerprint",
        }
    )
    """
    Fingerprint

    A finger print scan used for identification purposes
    """

    iris = CodeSystemConcept(
        {
            "code": "iris",
            "definition": "An iris scan used for identification purposes",
            "display": "Iris Scan",
        }
    )
    """
    Iris Scan

    An iris scan used for identification purposes
    """

    palm = CodeSystemConcept(
        {
            "code": "palm",
            "definition": "A palm scan used for identification purposes",
            "display": "Palm Scan",
        }
    )
    """
    Palm Scan

    A palm scan used for identification purposes
    """

    face = CodeSystemConcept(
        {
            "code": "face",
            "definition": "A face scan used for identification purposes",
            "display": "Face Scan",
        }
    )
    """
    Face Scan

    A face scan used for identification purposes
    """

    class Meta:
        resource = _resource
