from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ChargeItemCode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ChargeItemCode:
    """
    ChargeItemCode

    Example set of codes that can be used for billing purposes.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/chargeitem-billingcodes
    """

    one100 = CodeSystemConcept(
        {
            "code": "1100",
            "definition": "From German EBM billing system:\nUnvorhergesehene Inanspruchnahme des Vertragsarztes durch einen Patienten;zwischen 19:00 und 22:00 Uhr;an Samstagen, Sonntagen und gesetzlichen Feiertagen, am 24.12. und 31.12. zwischen 07:00 und 19:00 Uhr.",
            "display": "Unvorhergesehene Inanspruchnahme",
        }
    )
    """
    Unvorhergesehene Inanspruchnahme

    From German EBM billing system:
Unvorhergesehene Inanspruchnahme des Vertragsarztes durch einen Patienten;zwischen 19:00 und 22:00 Uhr;an Samstagen, Sonntagen und gesetzlichen Feiertagen, am 24.12. und 31.12. zwischen 07:00 und 19:00 Uhr.
    """

    one210 = CodeSystemConcept(
        {
            "code": "1210",
            "definition": "From German EBM billing system:\nNotfallpauschale im organisierten Not(-fall)dienst und für nicht an der vertragsärztlichen Versorgung teilnehmende Ärzte, Institute und Krankenhäuser bei Inanspruchnahme;zwischen 07:00 und 19:00 Uhr.",
            "display": "Notfallpauschale",
        }
    )
    """
    Notfallpauschale

    From German EBM billing system:
Notfallpauschale im organisierten Not(-fall)dienst und für nicht an der vertragsärztlichen Versorgung teilnehmende Ärzte, Institute und Krankenhäuser bei Inanspruchnahme;zwischen 07:00 und 19:00 Uhr.
    """

    one320 = CodeSystemConcept(
        {
            "code": "1320",
            "definition": "From German EBM billing system:\nGrundpauschale für Ärzte, Institute und Krankenhäuser, die zur Erbringung von Leistungen innerhalb mindestens eines der Fachgebiete Anästhesiologie, Frauenheilkunde und Geburtshilfe, Haut- und Geschlechtskrankheiten, Mund-, Kiefer- und Gesichtschirurgie und Humangenetik ermächtigt sind.",
            "display": "Grundpauschale",
        }
    )
    """
    Grundpauschale

    From German EBM billing system:
Grundpauschale für Ärzte, Institute und Krankenhäuser, die zur Erbringung von Leistungen innerhalb mindestens eines der Fachgebiete Anästhesiologie, Frauenheilkunde und Geburtshilfe, Haut- und Geschlechtskrankheiten, Mund-, Kiefer- und Gesichtschirurgie und Humangenetik ermächtigt sind.
    """

    class Meta:
        resource = _resource
