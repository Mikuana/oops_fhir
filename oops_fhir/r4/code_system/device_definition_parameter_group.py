from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["DeviceDefinitionParameterGroup"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class DeviceDefinitionParameterGroup:
    """
    DeviceDefinitionParameterGroup

    Codes identifying groupings of parameters; e.g. Cardiovascular.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/parameter-group
    """

    haemodynamic = CodeSystemConcept(
        {
            "code": "haemodynamic",
            "definition": "Haemodynamic Parameter Group - MDC_PGRP_HEMO.",
            "display": "Haemodynamic Parameter Group",
        }
    )
    """
    Haemodynamic Parameter Group

    Haemodynamic Parameter Group - MDC_PGRP_HEMO.
    """

    ecg = CodeSystemConcept(
        {
            "code": "ecg",
            "definition": "ECG Parameter Group - MDC_PGRP_ECG.",
            "display": "ECG Parameter Group",
        }
    )
    """
    ECG Parameter Group

    ECG Parameter Group - MDC_PGRP_ECG.
    """

    respiratory = CodeSystemConcept(
        {
            "code": "respiratory",
            "definition": "Respiratory Parameter Group - MDC_PGRP_RESP.",
            "display": "Respiratory Parameter Group",
        }
    )
    """
    Respiratory Parameter Group

    Respiratory Parameter Group - MDC_PGRP_RESP.
    """

    ventilation = CodeSystemConcept(
        {
            "code": "ventilation",
            "definition": "Ventilation Parameter Group - MDC_PGRP_VENT.",
            "display": "Ventilation Parameter Group",
        }
    )
    """
    Ventilation Parameter Group

    Ventilation Parameter Group - MDC_PGRP_VENT.
    """

    neurological = CodeSystemConcept(
        {
            "code": "neurological",
            "definition": "Neurological Parameter Group - MDC_PGRP_NEURO.",
            "display": "Neurological Parameter Group",
        }
    )
    """
    Neurological Parameter Group

    Neurological Parameter Group - MDC_PGRP_NEURO.
    """

    drug_delivery = CodeSystemConcept(
        {
            "code": "drug-delivery",
            "definition": "Drug Delivery Parameter Group - MDC_PGRP_DRUG.",
            "display": "Drug Delivery Parameter Group",
        }
    )
    """
    Drug Delivery Parameter Group

    Drug Delivery Parameter Group - MDC_PGRP_DRUG.
    """

    fluid_chemistry = CodeSystemConcept(
        {
            "code": "fluid-chemistry",
            "definition": "Fluid Chemistry Parameter Group - MDC_PGRP_FLUID.",
            "display": "Fluid Chemistry Parameter Group",
        }
    )
    """
    Fluid Chemistry Parameter Group

    Fluid Chemistry Parameter Group - MDC_PGRP_FLUID.
    """

    blood_chemistry = CodeSystemConcept(
        {
            "code": "blood-chemistry",
            "definition": "Blood Chemistry Parameter Group - MDC_PGRP_BLOOD_CHEM.",
            "display": "Blood Chemistry Parameter Group",
        }
    )
    """
    Blood Chemistry Parameter Group

    Blood Chemistry Parameter Group - MDC_PGRP_BLOOD_CHEM.
    """

    miscellaneous = CodeSystemConcept(
        {
            "code": "miscellaneous",
            "definition": "Miscellaneous Parameter Group - MDC_PGRP_MISC.",
            "display": "Miscellaneous Parameter Group",
        }
    )
    """
    Miscellaneous Parameter Group

    Miscellaneous Parameter Group - MDC_PGRP_MISC.
    """

    class Meta:
        resource = _resource
