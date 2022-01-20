from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["FeedingDeviceCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class FeedingDeviceCodes:
    """
    Feeding Device Codes

    Materials used or needed to feed the patient.

    Status: draft - Version: 4.0.1

    Copyright This resource includes content from SNOMED Clinical Terms® (SNOMED CT®) which is copyright   of the International Health Terminology Standards Development Organisation (IHTSDO). Implementers   of these specifications must have the appropriate SNOMED CT Affiliate license - for more   information contact http://www.snomed.org/snomed-ct/get-snomed-ct or info@snomed.org

    http://hl7.org/fhir/feeding-device
    """

    standard_nipple = CodeSystemConcept(
        {
            "code": "standard-nipple",
            "definition": "Standard nipple definition:",
            "display": "Standard nipple",
        }
    )
    """
    Standard nipple

    Standard nipple definition:
    """

    preemie_nipple = CodeSystemConcept(
        {
            "code": "preemie-nipple",
            "definition": "Preemie nipple definition:",
            "display": "Preemie nipple",
        }
    )
    """
    Preemie nipple

    Preemie nipple definition:
    """

    ortho_nipple = CodeSystemConcept(
        {
            "code": "ortho-nipple",
            "definition": "Orthodontic nipple definition:",
            "display": "Orthodontic nipple",
        }
    )
    """
    Orthodontic nipple

    Orthodontic nipple definition:
    """

    sloflo_nipple = CodeSystemConcept(
        {
            "code": "sloflo-nipple",
            "definition": "Slow flow nipple definition:",
            "display": "Slow flow nipple",
        }
    )
    """
    Slow flow nipple

    Slow flow nipple definition:
    """

    midflo_nipple = CodeSystemConcept(
        {
            "code": "midflo-nipple",
            "definition": "Middle flow nipple definition:",
            "display": "Middle flow nipple",
        }
    )
    """
    Middle flow nipple

    Middle flow nipple definition:
    """

    bigcut_nipple = CodeSystemConcept(
        {
            "code": "bigcut-nipple",
            "definition": "Enlarged, cross-cut nipple definition:",
            "display": "Enlarged, cross-cut nipple",
        }
    )
    """
    Enlarged, cross-cut nipple

    Enlarged, cross-cut nipple definition:
    """

    haberman_bottle = CodeSystemConcept(
        {
            "code": "haberman-bottle",
            "definition": "Haberman bottle definition:",
            "display": "Haberman bottle",
        }
    )
    """
    Haberman bottle

    Haberman bottle definition:
    """

    sippy_valve = CodeSystemConcept(
        {
            "code": "sippy-valve",
            "definition": "Sippy cup with valve definition:",
            "display": "Sippy cup with valve",
        }
    )
    """
    Sippy cup with valve

    Sippy cup with valve definition:
    """

    sippy_no_valve = CodeSystemConcept(
        {
            "code": "sippy-no-valve",
            "definition": "Sippy cup without valve definition:",
            "display": "Sippy cup without valve",
        }
    )
    """
    Sippy cup without valve

    Sippy cup without valve definition:
    """

    provale_cup = CodeSystemConcept(
        {
            "code": "provale-cup",
            "definition": "Provale Cup definition:",
            "display": "Provale Cup",
        }
    )
    """
    Provale Cup

    Provale Cup definition:
    """

    glass_lid = CodeSystemConcept(
        {
            "code": "glass-lid",
            "definition": "Glass with lid/sippy cup definition:",
            "display": "Glass with lid/sippy cup",
        }
    )
    """
    Glass with lid/sippy cup

    Glass with lid/sippy cup definition:
    """

    handhold_cup = CodeSystemConcept(
        {
            "code": "handhold-cup",
            "definition": "Double handhold on glass/cup definition:",
            "display": "Double handhold on glass/cup",
        }
    )
    """
    Double handhold on glass/cup

    Double handhold on glass/cup definition:
    """

    rubber_mat = CodeSystemConcept(
        {
            "code": "rubber-mat",
            "definition": "Rubber matting under tray definition:",
            "display": "Rubber matting under tray",
        }
    )
    """
    Rubber matting under tray

    Rubber matting under tray definition:
    """

    straw = CodeSystemConcept(
        {"code": "straw", "definition": "Straw definition:", "display": "Straw"}
    )
    """
    Straw

    Straw definition:
    """

    nose_cup = CodeSystemConcept(
        {
            "code": "nose-cup",
            "definition": "Nose cup definition:",
            "display": "Nose cup",
        }
    )
    """
    Nose cup

    Nose cup definition:
    """

    scoop_plate = CodeSystemConcept(
        {
            "code": "scoop-plate",
            "definition": "Scoop plate definition:",
            "display": "Scoop plate",
        }
    )
    """
    Scoop plate

    Scoop plate definition:
    """

    utensil_holder = CodeSystemConcept(
        {
            "code": "utensil-holder",
            "definition": "Hand wrap utensil holder definition:",
            "display": "Hand wrap utensil holder",
        }
    )
    """
    Hand wrap utensil holder

    Hand wrap utensil holder definition:
    """

    foam_handle = CodeSystemConcept(
        {
            "code": "foam-handle",
            "definition": "Foam handle utensils definition:",
            "display": "Foam handle utensils",
        }
    )
    """
    Foam handle utensils

    Foam handle utensils definition:
    """

    angled_utensil = CodeSystemConcept(
        {
            "code": "angled-utensil",
            "definition": "Angled utensils definition:",
            "display": "Angled utensils",
        }
    )
    """
    Angled utensils

    Angled utensils definition:
    """

    spout_cup = CodeSystemConcept(
        {
            "code": "spout-cup",
            "definition": "Spout cup definition:",
            "display": "Spout cup",
        }
    )
    """
    Spout cup

    Spout cup definition:
    """

    autofeeding_device = CodeSystemConcept(
        {
            "code": "autofeeding-device",
            "definition": "Automated feeding devices definition:",
            "display": "Automated feeding devices",
        }
    )
    """
    Automated feeding devices

    Automated feeding devices definition:
    """

    rocker_knife = CodeSystemConcept(
        {
            "code": "rocker-knife",
            "definition": "Rocker knife definition:",
            "display": "Rocker knife",
        }
    )
    """
    Rocker knife

    Rocker knife definition:
    """

    class Meta:
        resource = _resource
