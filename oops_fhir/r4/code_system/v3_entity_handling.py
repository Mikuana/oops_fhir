from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3EntityHandling"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3EntityHandling:
    """
    v3 Code System EntityHandling

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-EntityHandling
    """

    amb = CodeSystemConcept(
        {
            "code": "AMB",
            "definition": "Keep at ambient temperature, 22 +/- 2C",
            "display": "Ambient Temperature",
        }
    )
    """
    Ambient Temperature

    Keep at ambient temperature, 22 +/- 2C
    """

    c37 = CodeSystemConcept(
        {
            "code": "C37",
            "definition": "Critical to keep at body temperature 36-38C",
            "display": "Body Temperature",
        }
    )
    """
    Body Temperature

    Critical to keep at body temperature 36-38C
    """

    camb = CodeSystemConcept(
        {
            "code": "CAMB",
            "definition": "Critical ambient - must not be refrigerated or frozen.",
            "display": "Critical Ambient temperature",
        }
    )
    """
    Critical Ambient temperature

    Critical ambient - must not be refrigerated or frozen.
    """

    catm = CodeSystemConcept(
        {
            "code": "CATM",
            "definition": "Critical. Do not expose to atmosphere.  Do not uncap.",
            "display": "Protect from Air",
        }
    )
    """
    Protect from Air

    Critical. Do not expose to atmosphere.  Do not uncap.
    """

    cfrz = CodeSystemConcept(
        {
            "code": "CFRZ",
            "definition": "Critical frozen. Specimen must not be allowed to thaw until immediately prior to testing.",
            "display": "Critical frozen",
        }
    )
    """
    Critical frozen

    Critical frozen. Specimen must not be allowed to thaw until immediately prior to testing.
    """

    cref = CodeSystemConcept(
        {
            "code": "CREF",
            "definition": "Critical refrigerated - must not be allowed to freeze or warm until imediately prior to testing.",
            "display": "Critical refrigerated temperature",
        }
    )
    """
    Critical refrigerated temperature

    Critical refrigerated - must not be allowed to freeze or warm until imediately prior to testing.
    """

    dfrz = CodeSystemConcept(
        {
            "code": "DFRZ",
            "definition": "Deep Frozen -16 to -20C.",
            "display": "Deep Frozen",
        }
    )
    """
    Deep Frozen

    Deep Frozen -16 to -20C.
    """

    dry = CodeSystemConcept(
        {"code": "DRY", "definition": "Keep in a dry environment", "display": "dry"}
    )
    """
    dry

    Keep in a dry environment
    """

    frz = CodeSystemConcept(
        {"code": "FRZ", "definition": "Keep frozen below 0 ?C", "display": "frozen"}
    )
    """
    frozen

    Keep frozen below 0 ?C
    """

    mtlf = CodeSystemConcept(
        {
            "code": "MTLF",
            "definition": "Container is free of heavy metals, including lead.",
            "display": "Metal Free",
        }
    )
    """
    Metal Free

    Container is free of heavy metals, including lead.
    """

    ntr = CodeSystemConcept(
        {"code": "NTR", "definition": "Keep in liquid nitrogen", "display": "nitrogen"}
    )
    """
    nitrogen

    Keep in liquid nitrogen
    """

    prtl = CodeSystemConcept(
        {
            "code": "PRTL",
            "definition": "Protect from light (eg. Wrap in aluminum foil).",
            "display": "Protect from Light",
        }
    )
    """
    Protect from Light

    Protect from light (eg. Wrap in aluminum foil).
    """

    psa = CodeSystemConcept(
        {"code": "PSA", "definition": "Do not shake", "display": "do not shake"}
    )
    """
    do not shake

    Do not shake
    """

    pso = CodeSystemConcept(
        {"code": "PSO", "definition": "Protect against shock", "display": "no shock"}
    )
    """
    no shock

    Protect against shock
    """

    ref = CodeSystemConcept(
        {
            "code": "REF",
            "definition": "Keep at refrigerated temperature:4-8C Accidental warming or freezing is of little consequence.",
            "display": "Refrigerated temperature",
        }
    )
    """
    Refrigerated temperature

    Keep at refrigerated temperature:4-8C Accidental warming or freezing is of little consequence.
    """

    sbu = CodeSystemConcept(
        {
            "code": "SBU",
            "definition": "Shake thoroughly before using",
            "display": "Shake before use",
        }
    )
    """
    Shake before use

    Shake thoroughly before using
    """

    ufrz = CodeSystemConcept(
        {
            "code": "UFRZ",
            "definition": "Ultra cold frozen -75 to -85C.  Ultra cold freezer is typically at temperature of dry ice.",
            "display": "Ultra frozen",
        }
    )
    """
    Ultra frozen

    Ultra cold frozen -75 to -85C.  Ultra cold freezer is typically at temperature of dry ice.
    """

    upr = CodeSystemConcept(
        {
            "code": "UPR",
            "definition": "Keep upright, do not turn upside down",
            "display": "upright",
        }
    )
    """
    upright

    Keep upright, do not turn upside down
    """

    class Meta:
        resource = _resource
