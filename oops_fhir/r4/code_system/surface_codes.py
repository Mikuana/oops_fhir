from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["SurfaceCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class SurfaceCodes:
    """
    Surface Codes

    This value set includes a smattering of FDI tooth surface codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/FDI-surface
    """

    m = CodeSystemConcept(
        {
            "code": "M",
            "definition": "The surface of a tooth that is closest to the midline (middle) of the face.",
            "display": "Mesial",
        }
    )
    """
    Mesial

    The surface of a tooth that is closest to the midline (middle) of the face.
    """

    o = CodeSystemConcept(
        {
            "code": "O",
            "definition": "The chewing surface of posterior teeth.",
            "display": "Occlusal",
        }
    )
    """
    Occlusal

    The chewing surface of posterior teeth.
    """

    i = CodeSystemConcept(
        {
            "code": "I",
            "definition": "The biting edge of anterior teeth.",
            "display": "Incisal",
        }
    )
    """
    Incisal

    The biting edge of anterior teeth.
    """

    d = CodeSystemConcept(
        {
            "code": "D",
            "definition": "The surface of a tooth that faces away from the midline of the face.",
            "display": "Distal",
        }
    )
    """
    Distal

    The surface of a tooth that faces away from the midline of the face.
    """

    b = CodeSystemConcept(
        {
            "code": "B",
            "definition": "The surface of a posterior tooth facing the cheeks.",
            "display": "Buccal",
        }
    )
    """
    Buccal

    The surface of a posterior tooth facing the cheeks.
    """

    v = CodeSystemConcept(
        {
            "code": "V",
            "definition": "The surface of a tooth facing the lips.",
            "display": "Ventral",
        }
    )
    """
    Ventral

    The surface of a tooth facing the lips.
    """

    l = CodeSystemConcept(
        {
            "code": "L",
            "definition": "The surface of a tooth facing the tongue.",
            "display": "Lingual",
        }
    )
    """
    Lingual

    The surface of a tooth facing the tongue.
    """

    mo = CodeSystemConcept(
        {
            "code": "MO",
            "definition": "The Mesioclusal surfaces of a tooth.",
            "display": "Mesioclusal",
        }
    )
    """
    Mesioclusal

    The Mesioclusal surfaces of a tooth.
    """

    do = CodeSystemConcept(
        {
            "code": "DO",
            "definition": "The Distoclusal surfaces of a tooth.",
            "display": "Distoclusal",
        }
    )
    """
    Distoclusal

    The Distoclusal surfaces of a tooth.
    """

    di = CodeSystemConcept(
        {
            "code": "DI",
            "definition": "The Distoincisal surfaces of a tooth.",
            "display": "Distoincisal",
        }
    )
    """
    Distoincisal

    The Distoincisal surfaces of a tooth.
    """

    mod = CodeSystemConcept(
        {
            "code": "MOD",
            "definition": "The Mesioclusodistal surfaces of a tooth.",
            "display": "Mesioclusodistal",
        }
    )
    """
    Mesioclusodistal

    The Mesioclusodistal surfaces of a tooth.
    """

    class Meta:
        resource = _resource
