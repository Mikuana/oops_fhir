from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ResourceType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ResourceType:
    """
    ResourceType

    One of the resource types defined as part of this version of FHIR.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/resource-types
    """

    account = CodeSystemConcept(
        {
            "code": "Account",
            "definition": "A financial tool for tracking value accrued for a particular purpose.  In the healthcare field, used to track charges for a patient, cost centers, etc.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Account",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Cuenta",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "账户",
                },
            ],
            "display": "Account",
        }
    )
    """
    Account

    A financial tool for tracking value accrued for a particular purpose.  In the healthcare field, used to track charges for a patient, cost centers, etc.
    """

    activity_definition = CodeSystemConcept(
        {
            "code": "ActivityDefinition",
            "definition": "This resource allows for the definition of some activity to be performed, independent of a particular patient, practitioner, or other performance context.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ActivityDefinition",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "DefinizioneAttivita",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "DefinicionDeActividad",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "活动定义",
                },
            ],
            "display": "ActivityDefinition",
        }
    )
    """
    ActivityDefinition

    This resource allows for the definition of some activity to be performed, independent of a particular patient, practitioner, or other performance context.
    """

    adverse_event = CodeSystemConcept(
        {
            "code": "AdverseEvent",
            "definition": "Actual or  potential/avoided event causing unintended physical injury resulting from or contributed to by medical care, a research study or other healthcare setting factors that requires additional monitoring, treatment, or hospitalization, or that results in death.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "AdverseEvent",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "EventoAvverso",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "EventoAdverso",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "不良事件",
                },
            ],
            "display": "AdverseEvent",
        }
    )
    """
    AdverseEvent

    Actual or  potential/avoided event causing unintended physical injury resulting from or contributed to by medical care, a research study or other healthcare setting factors that requires additional monitoring, treatment, or hospitalization, or that results in death.
    """

    allergy_intolerance = CodeSystemConcept(
        {
            "code": "AllergyIntolerance",
            "definition": "Risk of harmful or undesirable, physiological response which is unique to an individual and associated with exposure to a substance.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "AllergyIntolerance",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "AllergiaIntolleranza",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "IntoléranceAllergique",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "AllergiaIntolerancia",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "变态反应与不耐性",
                },
            ],
            "display": "AllergyIntolerance",
        }
    )
    """
    AllergyIntolerance

    Risk of harmful or undesirable, physiological response which is unique to an individual and associated with exposure to a substance.
    """

    appointment = CodeSystemConcept(
        {
            "code": "Appointment",
            "definition": "A booking of a healthcare event among patient(s), practitioner(s), related person(s) and/or device(s) for a specific date/time. This may result in one or more Encounter(s).",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Appointment",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Appuntamento",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "RendezVous",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Cita",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "预约",
                },
            ],
            "display": "Appointment",
        }
    )
    """
    Appointment

    A booking of a healthcare event among patient(s), practitioner(s), related person(s) and/or device(s) for a specific date/time. This may result in one or more Encounter(s).
    """

    appointment_response = CodeSystemConcept(
        {
            "code": "AppointmentResponse",
            "definition": "A reply to an appointment request for a patient and/or practitioner(s), such as a confirmation or rejection.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "AppointmentResponse",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "RispostaAppuntamento",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "RéponseRendezVous",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "CitaRespuesta",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "预约响应",
                },
            ],
            "display": "AppointmentResponse",
        }
    )
    """
    AppointmentResponse

    A reply to an appointment request for a patient and/or practitioner(s), such as a confirmation or rejection.
    """

    audit_event = CodeSystemConcept(
        {
            "code": "AuditEvent",
            "definition": "A record of an event made for purposes of maintaining a security log. Typical uses include detection of intrusion attempts and monitoring for inappropriate usage.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "AuditEvent",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ÉvènementSécurité",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "EventoSeguridad",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "审计事件",
                },
            ],
            "display": "AuditEvent",
        }
    )
    """
    AuditEvent

    A record of an event made for purposes of maintaining a security log. Typical uses include detection of intrusion attempts and monitoring for inappropriate usage.
    """

    basic = CodeSystemConcept(
        {
            "code": "Basic",
            "definition": "Basic is used for handling concepts not yet defined in FHIR, narrative-only resources that don't map to an existing resource, and custom resources not appropriate for inclusion in the FHIR specification.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Basic",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Basique",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Basico",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "初级资源",
                },
            ],
            "display": "Basic",
        }
    )
    """
    Basic

    Basic is used for handling concepts not yet defined in FHIR, narrative-only resources that don't map to an existing resource, and custom resources not appropriate for inclusion in the FHIR specification.
    """

    binary = CodeSystemConcept(
        {
            "code": "Binary",
            "definition": "A resource that represents the data of a single raw artifact as digital content accessible in its native format.  A Binary resource can contain any content, whether text, image, pdf, zip archive, etc.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Binary",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Binario",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Binaire",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Binario",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "二进制资源",
                },
            ],
            "display": "Binary",
        }
    )
    """
    Binary

    A resource that represents the data of a single raw artifact as digital content accessible in its native format.  A Binary resource can contain any content, whether text, image, pdf, zip archive, etc.
    """

    biologically_derived_product = CodeSystemConcept(
        {
            "code": "BiologicallyDerivedProduct",
            "definition": "A material substance originating from a biological entity intended to be transplanted or infused\ninto another (possibly the same) biological entity.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "BiologicallyDerivedProduct",
                }
            ],
            "display": "BiologicallyDerivedProduct",
        }
    )
    """
    BiologicallyDerivedProduct

    A material substance originating from a biological entity intended to be transplanted or infused
into another (possibly the same) biological entity.
    """

    body_structure = CodeSystemConcept(
        {
            "code": "BodyStructure",
            "definition": "Record details about an anatomical structure.  This resource may be used when a coded concept does not provide the necessary detail needed for the use case.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "BodyStructure",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "StrutturaDelCorpo",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "MorphologieDeCorps",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "EstructuraDelCuerpo",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "身体结构",
                },
            ],
            "display": "BodyStructure",
        }
    )
    """
    BodyStructure

    Record details about an anatomical structure.  This resource may be used when a coded concept does not provide the necessary detail needed for the use case.
    """

    bundle = CodeSystemConcept(
        {
            "code": "Bundle",
            "definition": "A container for a collection of resources.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Bundle",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Paquet",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Paquete",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "捆束",
                },
            ],
            "display": "Bundle",
        }
    )
    """
    Bundle

    A container for a collection of resources.
    """

    capability_statement = CodeSystemConcept(
        {
            "code": "CapabilityStatement",
            "definition": "A Capability Statement documents a set of capabilities (behaviors) of a FHIR Server for a particular version of FHIR that may be used as a statement of actual server functionality or a statement of required or desired server implementation.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "CapabilityStatement",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "DeclaracionDeCapacidad",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "能力声明",
                },
            ],
            "display": "CapabilityStatement",
        }
    )
    """
    CapabilityStatement

    A Capability Statement documents a set of capabilities (behaviors) of a FHIR Server for a particular version of FHIR that may be used as a statement of actual server functionality or a statement of required or desired server implementation.
    """

    care_plan = CodeSystemConcept(
        {
            "code": "CarePlan",
            "definition": "Describes the intention of how one or more practitioners intend to deliver care for a particular patient, group or community for a period of time, possibly limited to care for a specific condition or set of conditions.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "CarePlan",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "PianoDiCura",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "PlanDeSoins",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "PlanDeCuidado",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "照护计划",
                },
            ],
            "display": "CarePlan",
        }
    )
    """
    CarePlan

    Describes the intention of how one or more practitioners intend to deliver care for a particular patient, group or community for a period of time, possibly limited to care for a specific condition or set of conditions.
    """

    care_team = CodeSystemConcept(
        {
            "code": "CareTeam",
            "definition": "The Care Team includes all the people and organizations who plan to participate in the coordination and delivery of care for a patient.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "CareTeam",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "EquipoDeCuidado",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "照护团队",
                },
            ],
            "display": "CareTeam",
        }
    )
    """
    CareTeam

    The Care Team includes all the people and organizations who plan to participate in the coordination and delivery of care for a patient.
    """

    catalog_entry = CodeSystemConcept(
        {
            "code": "CatalogEntry",
            "definition": "Catalog entries are wrappers that contextualize items included in a catalog.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "CatalogEntry",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "EntradaDeCatalogo",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "条目定义",
                },
            ],
            "display": "CatalogEntry",
        }
    )
    """
    CatalogEntry

    Catalog entries are wrappers that contextualize items included in a catalog.
    """

    charge_item = CodeSystemConcept(
        {
            "code": "ChargeItem",
            "definition": "The resource ChargeItem describes the provision of healthcare provider products for a certain patient, therefore referring not only to the product, but containing in addition details of the provision, like date, time, amounts and participating organizations and persons. Main Usage of the ChargeItem is to enable the billing process and internal cost allocation.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ChargeItem",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "CargoDeItem",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "收费项目",
                },
            ],
            "display": "ChargeItem",
        }
    )
    """
    ChargeItem

    The resource ChargeItem describes the provision of healthcare provider products for a certain patient, therefore referring not only to the product, but containing in addition details of the provision, like date, time, amounts and participating organizations and persons. Main Usage of the ChargeItem is to enable the billing process and internal cost allocation.
    """

    charge_item_definition = CodeSystemConcept(
        {
            "code": "ChargeItemDefinition",
            "definition": "The ChargeItemDefinition resource provides the properties that apply to the (billing) codes necessary to calculate costs and prices. The properties may differ largely depending on type and realm, therefore this resource gives only a rough structure and requires profiling for each type of billing code system.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ChargeItemDefinition",
                }
            ],
            "display": "ChargeItemDefinition",
        }
    )
    """
    ChargeItemDefinition

    The ChargeItemDefinition resource provides the properties that apply to the (billing) codes necessary to calculate costs and prices. The properties may differ largely depending on type and realm, therefore this resource gives only a rough structure and requires profiling for each type of billing code system.
    """

    claim = CodeSystemConcept(
        {
            "code": "Claim",
            "definition": "A provider issued list of professional services and products which have been provided, or are to be provided, to a patient which is sent to an insurer for reimbursement.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Claim",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Réclamation",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Reclamación / Factura",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "赔单",
                },
            ],
            "display": "Claim",
        }
    )
    """
    Claim

    A provider issued list of professional services and products which have been provided, or are to be provided, to a patient which is sent to an insurer for reimbursement.
    """

    claim_response = CodeSystemConcept(
        {
            "code": "ClaimResponse",
            "definition": "This resource provides the adjudication details from the processing of a Claim resource.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ClaimResponse",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "RéponseARéclamation",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "赔单请求",
                },
            ],
            "display": "ClaimResponse",
        }
    )
    """
    ClaimResponse

    This resource provides the adjudication details from the processing of a Claim resource.
    """

    clinical_impression = CodeSystemConcept(
        {
            "code": "ClinicalImpression",
            "definition": 'A record of a clinical assessment performed to determine what problem(s) may affect the patient and before planning the treatments or management strategies that are best to manage a patient\'s condition. Assessments are often 1:1 with a clinical consultation / encounter,  but this varies greatly depending on the clinical workflow. This resource is called "ClinicalImpression" rather than "ClinicalAssessment" to avoid confusion with the recording of assessment tools such as Apgar score.',
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ClinicalImpression",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ImpressioneClinica",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ImpressionClinique",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "HallazgoClinico",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "临床印象",
                },
            ],
            "display": "ClinicalImpression",
        }
    )
    """
    ClinicalImpression

    A record of a clinical assessment performed to determine what problem(s) may affect the patient and before planning the treatments or management strategies that are best to manage a patient's condition. Assessments are often 1:1 with a clinical consultation / encounter,  but this varies greatly depending on the clinical workflow. This resource is called "ClinicalImpression" rather than "ClinicalAssessment" to avoid confusion with the recording of assessment tools such as Apgar score.
    """

    code_system = CodeSystemConcept(
        {
            "code": "CodeSystem",
            "definition": "The CodeSystem resource is used to declare the existence of and describe a code system or code system supplement and its key properties, and optionally define a part or all of its content.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "CodeSystem",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "SistemaDiCodifica",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "SistemaDeCodigos",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "代码系统",
                },
            ],
            "display": "CodeSystem",
        }
    )
    """
    CodeSystem

    The CodeSystem resource is used to declare the existence of and describe a code system or code system supplement and its key properties, and optionally define a part or all of its content.
    """

    communication = CodeSystemConcept(
        {
            "code": "Communication",
            "definition": "An occurrence of information being transmitted; e.g. an alert that was sent to a responsible provider, a public health agency that was notified about a reportable condition.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Communication",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Comunicazione",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Communication",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Comunicación",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "通讯",
                },
            ],
            "display": "Communication",
        }
    )
    """
    Communication

    An occurrence of information being transmitted; e.g. an alert that was sent to a responsible provider, a public health agency that was notified about a reportable condition.
    """

    communication_request = CodeSystemConcept(
        {
            "code": "CommunicationRequest",
            "definition": "A request to convey information; e.g. the CDS system proposes that an alert be sent to a responsible provider, the CDS system proposes that the public health agency be notified about a reportable condition.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "CommunicationRequest",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "RichiestaDiComunicazione",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "DemandeDeCommunication",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ComunicaciónRequerimiento",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "通讯请求",
                },
            ],
            "display": "CommunicationRequest",
        }
    )
    """
    CommunicationRequest

    A request to convey information; e.g. the CDS system proposes that an alert be sent to a responsible provider, the CDS system proposes that the public health agency be notified about a reportable condition.
    """

    compartment_definition = CodeSystemConcept(
        {
            "code": "CompartmentDefinition",
            "definition": "A compartment definition that defines how resources are accessed on a server.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "CompartmentDefinition",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "DefinicionDeCompartimento",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "逻辑区块定义",
                },
            ],
            "display": "CompartmentDefinition",
        }
    )
    """
    CompartmentDefinition

    A compartment definition that defines how resources are accessed on a server.
    """

    composition = CodeSystemConcept(
        {
            "code": "Composition",
            "definition": "A set of healthcare-related information that is assembled together into a single logical package that provides a single coherent statement of meaning, establishes its own context and that has clinical attestation with regard to who is making the statement. A Composition defines the structure and narrative content necessary for a document. However, a Composition alone does not constitute a document. Rather, the Composition must be the first entry in a Bundle where Bundle.type=document, and any other resources referenced from Composition must be included as subsequent entries in the Bundle (for example Patient, Practitioner, Encounter, etc.).",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Composition",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Composizione",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Composition",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Composición",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "组合式文书",
                },
            ],
            "display": "Composition",
        }
    )
    """
    Composition

    A set of healthcare-related information that is assembled together into a single logical package that provides a single coherent statement of meaning, establishes its own context and that has clinical attestation with regard to who is making the statement. A Composition defines the structure and narrative content necessary for a document. However, a Composition alone does not constitute a document. Rather, the Composition must be the first entry in a Bundle where Bundle.type=document, and any other resources referenced from Composition must be included as subsequent entries in the Bundle (for example Patient, Practitioner, Encounter, etc.).
    """

    concept_map = CodeSystemConcept(
        {
            "code": "ConceptMap",
            "definition": "A statement of relationships from one set of concepts to one or more other concepts - either concepts in code systems, or data element/data element concepts, or classes in class models.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ConceptMap",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "MappaDiConcetti",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "CarteDeConcepts",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "MapaDeConceptos",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "概念映射",
                },
            ],
            "display": "ConceptMap",
        }
    )
    """
    ConceptMap

    A statement of relationships from one set of concepts to one or more other concepts - either concepts in code systems, or data element/data element concepts, or classes in class models.
    """

    condition = CodeSystemConcept(
        {
            "code": "Condition",
            "definition": "A clinical condition, problem, diagnosis, or other event, situation, issue, or clinical concept that has risen to a level of concern.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Condition",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Condizione",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Condition",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Condición",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "情况",
                },
            ],
            "display": "Condition",
        }
    )
    """
    Condition

    A clinical condition, problem, diagnosis, or other event, situation, issue, or clinical concept that has risen to a level of concern.
    """

    consent = CodeSystemConcept(
        {
            "code": "Consent",
            "definition": "A record of a healthcare consumer’s  choices, which permits or denies identified recipient(s) or recipient role(s) to perform one or more actions within a given policy context, for specific purposes and periods of time.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Consent",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Consenso",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Consentimiento",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "同意书",
                },
            ],
            "display": "Consent",
        }
    )
    """
    Consent

    A record of a healthcare consumer’s  choices, which permits or denies identified recipient(s) or recipient role(s) to perform one or more actions within a given policy context, for specific purposes and periods of time.
    """

    contract = CodeSystemConcept(
        {
            "code": "Contract",
            "definition": "Legally enforceable, formally recorded unilateral or bilateral directive i.e., a policy or agreement.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Contract",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Contratto",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Contrat",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Contato",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "合同",
                },
            ],
            "display": "Contract",
        }
    )
    """
    Contract

    Legally enforceable, formally recorded unilateral or bilateral directive i.e., a policy or agreement.
    """

    coverage = CodeSystemConcept(
        {
            "code": "Coverage",
            "definition": "Financial instrument which may be used to reimburse or pay for health care products and services. Includes both insurance and self-payment.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Coverage",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Copertura",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Couverture",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Cobertura",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "保险责任",
                },
            ],
            "display": "Coverage",
        }
    )
    """
    Coverage

    Financial instrument which may be used to reimburse or pay for health care products and services. Includes both insurance and self-payment.
    """

    coverage_eligibility_request = CodeSystemConcept(
        {
            "code": "CoverageEligibilityRequest",
            "definition": "The CoverageEligibilityRequest provides patient and insurance coverage information to an insurer for them to respond, in the form of an CoverageEligibilityResponse, with information regarding whether the stated coverage is valid and in-force and optionally to provide the insurance details of the policy.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "CoverageEligibilityRequest",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "RichiestaEleggibilitaCopertura",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "CouvertureDemandeEligibilité",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "资格请求",
                },
            ],
            "display": "CoverageEligibilityRequest",
        }
    )
    """
    CoverageEligibilityRequest

    The CoverageEligibilityRequest provides patient and insurance coverage information to an insurer for them to respond, in the form of an CoverageEligibilityResponse, with information regarding whether the stated coverage is valid and in-force and optionally to provide the insurance details of the policy.
    """

    coverage_eligibility_response = CodeSystemConcept(
        {
            "code": "CoverageEligibilityResponse",
            "definition": "This resource provides eligibility and plan details from the processing of an CoverageEligibilityRequest resource.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "CoverageEligibilityResponse",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "RispostaEleggibilitaCopertura",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "RéponseEligibilitéCouverture",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "资格响应",
                },
            ],
            "display": "CoverageEligibilityResponse",
        }
    )
    """
    CoverageEligibilityResponse

    This resource provides eligibility and plan details from the processing of an CoverageEligibilityRequest resource.
    """

    detected_issue = CodeSystemConcept(
        {
            "code": "DetectedIssue",
            "definition": "Indicates an actual or potential clinical issue with or between one or more active or proposed clinical actions for a patient; e.g. Drug-drug interaction, Ineffective treatment frequency, Procedure-condition conflict, etc.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "DetectedIssue",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ProblemaRilevato",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Problème Détecté",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Problema-Detectado /ProblemaDetectado",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "已发现问题",
                },
            ],
            "display": "DetectedIssue",
        }
    )
    """
    DetectedIssue

    Indicates an actual or potential clinical issue with or between one or more active or proposed clinical actions for a patient; e.g. Drug-drug interaction, Ineffective treatment frequency, Procedure-condition conflict, etc.
    """

    device = CodeSystemConcept(
        {
            "code": "Device",
            "definition": "A type of a manufactured item that is used in the provision of healthcare without being substantially changed through that activity. The device may be a medical or non-medical device.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Device",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Dispositivo",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Dispositif",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Dispositivo",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "装置",
                },
            ],
            "display": "Device",
        }
    )
    """
    Device

    A type of a manufactured item that is used in the provision of healthcare without being substantially changed through that activity. The device may be a medical or non-medical device.
    """

    device_definition = CodeSystemConcept(
        {
            "code": "DeviceDefinition",
            "definition": "The characteristics, operational status and capabilities of a medical-related component of a medical device.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "DeviceDefinition",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "DéfinitionDeDispositif",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "DefiniciónDeDispositivo",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "装置组件",
                },
            ],
            "display": "DeviceDefinition",
        }
    )
    """
    DeviceDefinition

    The characteristics, operational status and capabilities of a medical-related component of a medical device.
    """

    device_metric = CodeSystemConcept(
        {
            "code": "DeviceMetric",
            "definition": "Describes a measurement, calculation or setting capability of a medical device.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "DeviceMetric",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "MétriqueDispositif",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "MetricaDeDispositivo",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "装置指标",
                },
            ],
            "display": "DeviceMetric",
        }
    )
    """
    DeviceMetric

    Describes a measurement, calculation or setting capability of a medical device.
    """

    device_request = CodeSystemConcept(
        {
            "code": "DeviceRequest",
            "definition": "Represents a request for a patient to employ a medical device. The device may be an implantable device, or an external assistive device, such as a walker.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "DeviceRequest",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "RichiestaDispositivo",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "DemandeUtilisationDispositif",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "SolicitudDeDispositivo",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "装置请求",
                },
            ],
            "display": "DeviceRequest",
        }
    )
    """
    DeviceRequest

    Represents a request for a patient to employ a medical device. The device may be an implantable device, or an external assistive device, such as a walker.
    """

    device_use_statement = CodeSystemConcept(
        {
            "code": "DeviceUseStatement",
            "definition": "A record of a device being used by a patient where the record is the result of a report from the patient or another clinician.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "DeviceUseStatement",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "装置使用声明",
                },
            ],
            "display": "DeviceUseStatement",
        }
    )
    """
    DeviceUseStatement

    A record of a device being used by a patient where the record is the result of a report from the patient or another clinician.
    """

    diagnostic_report = CodeSystemConcept(
        {
            "code": "DiagnosticReport",
            "definition": "The findings and interpretation of diagnostic  tests performed on patients, groups of patients, devices, and locations, and/or specimens derived from these. The report includes clinical context such as requesting and provider information, and some mix of atomic results, images, textual and coded interpretations, and formatted representation of diagnostic reports.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "DiagnosticReport",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "RefertoDiagnostico",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "RapportDiagnostique",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "诊断报告",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "InformeDiagnostico",
                },
            ],
            "display": "DiagnosticReport",
        }
    )
    """
    DiagnosticReport

    The findings and interpretation of diagnostic  tests performed on patients, groups of patients, devices, and locations, and/or specimens derived from these. The report includes clinical context such as requesting and provider information, and some mix of atomic results, images, textual and coded interpretations, and formatted representation of diagnostic reports.
    """

    document_manifest = CodeSystemConcept(
        {
            "code": "DocumentManifest",
            "definition": "A collection of documents compiled for a purpose together with metadata that applies to the collection.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "DocumentManifest",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Manifeste",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "文档清单",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ManifestoDocumento",
                },
            ],
            "display": "DocumentManifest",
        }
    )
    """
    DocumentManifest

    A collection of documents compiled for a purpose together with metadata that applies to the collection.
    """

    document_reference = CodeSystemConcept(
        {
            "code": "DocumentReference",
            "definition": "A reference to a document of any kind for any purpose. Provides metadata about the document so that the document can be discovered and managed. The scope of a document is any seralized object with a mime-type, so includes formal patient centric documents (CDA), cliical notes, scanned paper, and non-patient specific documents like policy text.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "DocumentReference",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "RiferimentoDocumento",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "RéférenceDocument",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ReferenciaDocumento",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "文档引用",
                },
            ],
            "display": "DocumentReference",
        }
    )
    """
    DocumentReference

    A reference to a document of any kind for any purpose. Provides metadata about the document so that the document can be discovered and managed. The scope of a document is any seralized object with a mime-type, so includes formal patient centric documents (CDA), cliical notes, scanned paper, and non-patient specific documents like policy text.
    """

    domain_resource = CodeSystemConcept(
        {
            "code": "DomainResource",
            "definition": "A resource that includes narrative, extensions, and contained resources.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "DomainResource",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "RecursoDeDominio",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "领域资源",
                },
            ],
            "display": "DomainResource",
        }
    )
    """
    DomainResource

    A resource that includes narrative, extensions, and contained resources.
    """

    effect_evidence_synthesis = CodeSystemConcept(
        {
            "code": "EffectEvidenceSynthesis",
            "definition": "The EffectEvidenceSynthesis resource describes the difference in an outcome between exposures states in a population where the effect estimate is derived from a combination of research studies.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "EffectEvidenceSynthesis",
                }
            ],
            "display": "EffectEvidenceSynthesis",
        }
    )
    """
    EffectEvidenceSynthesis

    The EffectEvidenceSynthesis resource describes the difference in an outcome between exposures states in a population where the effect estimate is derived from a combination of research studies.
    """

    encounter = CodeSystemConcept(
        {
            "code": "Encounter",
            "definition": "An interaction between a patient and healthcare provider(s) for the purpose of providing healthcare service(s) or assessing the health status of a patient.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Encounter",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Venue",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "就医过程",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Encuentro",
                },
            ],
            "display": "Encounter",
        }
    )
    """
    Encounter

    An interaction between a patient and healthcare provider(s) for the purpose of providing healthcare service(s) or assessing the health status of a patient.
    """

    endpoint = CodeSystemConcept(
        {
            "code": "Endpoint",
            "definition": "The technical details of an endpoint that can be used for electronic services, such as for web services providing XDS.b or a REST endpoint for another FHIR server. This may include any security context information.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Endpoint",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Endpoint",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "端点",
                },
            ],
            "display": "Endpoint",
        }
    )
    """
    Endpoint

    The technical details of an endpoint that can be used for electronic services, such as for web services providing XDS.b or a REST endpoint for another FHIR server. This may include any security context information.
    """

    enrollment_request = CodeSystemConcept(
        {
            "code": "EnrollmentRequest",
            "definition": "This resource provides the insurance enrollment details to the insurer regarding a specified coverage.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "EnrollmentRequest",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "RichiestaIscrizione",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "DemandeInscription",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "SolicitudDeEnrolamiento",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "保险注册请求",
                },
            ],
            "display": "EnrollmentRequest",
        }
    )
    """
    EnrollmentRequest

    This resource provides the insurance enrollment details to the insurer regarding a specified coverage.
    """

    enrollment_response = CodeSystemConcept(
        {
            "code": "EnrollmentResponse",
            "definition": "This resource provides enrollment and plan details from the processing of an EnrollmentRequest resource.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "EnrollmentResponse",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "RispostaIscrizione",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "RéponseInscription",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "RespuestaDeEnrolamiento",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "保险注册响应",
                },
            ],
            "display": "EnrollmentResponse",
        }
    )
    """
    EnrollmentResponse

    This resource provides enrollment and plan details from the processing of an EnrollmentRequest resource.
    """

    episode_of_care = CodeSystemConcept(
        {
            "code": "EpisodeOfCare",
            "definition": "An association between a patient and an organization / healthcare provider(s) during which time encounters may occur. The managing organization assumes a level of responsibility for the patient during this time.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "EpisodeOfCare",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "EpisodioDiCura",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ÉpisodeDeSoins",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "EpisodioDeCuidado",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "照护服务节段",
                },
            ],
            "display": "EpisodeOfCare",
        }
    )
    """
    EpisodeOfCare

    An association between a patient and an organization / healthcare provider(s) during which time encounters may occur. The managing organization assumes a level of responsibility for the patient during this time.
    """

    event_definition = CodeSystemConcept(
        {
            "code": "EventDefinition",
            "definition": "The EventDefinition resource provides a reusable description of when a particular event can occur.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "EventDefinition",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "DefinizioneEvento",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "DefinitionDeEvento",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "事件定义",
                },
            ],
            "display": "EventDefinition",
        }
    )
    """
    EventDefinition

    The EventDefinition resource provides a reusable description of when a particular event can occur.
    """

    evidence = CodeSystemConcept(
        {
            "code": "Evidence",
            "definition": "The Evidence resource describes the conditional state (population and any exposures being compared within the population) and outcome (if specified) that the knowledge (evidence, assertion, recommendation) is about.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Evidence",
                }
            ],
            "display": "Evidence",
        }
    )
    """
    Evidence

    The Evidence resource describes the conditional state (population and any exposures being compared within the population) and outcome (if specified) that the knowledge (evidence, assertion, recommendation) is about.
    """

    evidence_variable = CodeSystemConcept(
        {
            "code": "EvidenceVariable",
            "definition": 'The EvidenceVariable resource describes a "PICO" element that knowledge (evidence, assertion, recommendation) is about.',
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "EvidenceVariable",
                }
            ],
            "display": "EvidenceVariable",
        }
    )
    """
    EvidenceVariable

    The EvidenceVariable resource describes a "PICO" element that knowledge (evidence, assertion, recommendation) is about.
    """

    example_scenario = CodeSystemConcept(
        {
            "code": "ExampleScenario",
            "definition": "Example of workflow instance.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ExampleScenario",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ScenarioDiEsempio",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "EjemploDeEscenario",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "示例场景",
                },
            ],
            "display": "ExampleScenario",
        }
    )
    """
    ExampleScenario

    Example of workflow instance.
    """

    explanation_of_benefit = CodeSystemConcept(
        {
            "code": "ExplanationOfBenefit",
            "definition": "This resource provides: the claim details; adjudication details from the processing of a Claim; and optionally account balance information, for informing the subscriber of the benefits provided.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ExplanationOfBenefit",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ExplicationDuBénéfice",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "赔付说明",
                },
            ],
            "display": "ExplanationOfBenefit",
        }
    )
    """
    ExplanationOfBenefit

    This resource provides: the claim details; adjudication details from the processing of a Claim; and optionally account balance information, for informing the subscriber of the benefits provided.
    """

    family_member_history = CodeSystemConcept(
        {
            "code": "FamilyMemberHistory",
            "definition": "Significant health conditions for a person related to the patient relevant in the context of care for the patient.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "FamilyMemberHistory",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "HistoireMembreFamille",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "HistorialMiembroFamiliar",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "家族史",
                },
            ],
            "display": "FamilyMemberHistory",
        }
    )
    """
    FamilyMemberHistory

    Significant health conditions for a person related to the patient relevant in the context of care for the patient.
    """

    flag = CodeSystemConcept(
        {
            "code": "Flag",
            "definition": "Prospective warnings of potential issues when providing care to the patient.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Flag",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Drapeau",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Bandera",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "标记",
                },
            ],
            "display": "Flag",
        }
    )
    """
    Flag

    Prospective warnings of potential issues when providing care to the patient.
    """

    goal = CodeSystemConcept(
        {
            "code": "Goal",
            "definition": "Describes the intended objective(s) for a patient, group or organization care, for example, weight loss, restoring an activity of daily living, obtaining herd immunity via immunization, meeting a process improvement objective, etc.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Goal",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "But",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Objetivo",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "目标",
                },
            ],
            "display": "Goal",
        }
    )
    """
    Goal

    Describes the intended objective(s) for a patient, group or organization care, for example, weight loss, restoring an activity of daily living, obtaining herd immunity via immunization, meeting a process improvement objective, etc.
    """

    graph_definition = CodeSystemConcept(
        {
            "code": "GraphDefinition",
            "definition": "A formal computable definition of a graph of resources - that is, a coherent set of resources that form a graph by following references. The Graph Definition resource defines a set and makes rules about the set.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "GraphDefinition",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "DefinitionGrafico",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "图形定义",
                },
            ],
            "display": "GraphDefinition",
        }
    )
    """
    GraphDefinition

    A formal computable definition of a graph of resources - that is, a coherent set of resources that form a graph by following references. The Graph Definition resource defines a set and makes rules about the set.
    """

    group = CodeSystemConcept(
        {
            "code": "Group",
            "definition": "Represents a defined collection of entities that may be discussed or acted upon collectively but which are not expected to act collectively, and are not formally or legally recognized; i.e. a collection of entities that isn't an Organization.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Group",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Gruppo",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Groupe",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Grupo",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "群组",
                },
            ],
            "display": "Group",
        }
    )
    """
    Group

    Represents a defined collection of entities that may be discussed or acted upon collectively but which are not expected to act collectively, and are not formally or legally recognized; i.e. a collection of entities that isn't an Organization.
    """

    guidance_response = CodeSystemConcept(
        {
            "code": "GuidanceResponse",
            "definition": "A guidance response is the formal response to a guidance request, including any output parameters returned by the evaluation, as well as the description of any proposed actions to be taken.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "GuidanceResponse",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "RespuestaDeOrientacion",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "指导意见响应",
                },
            ],
            "display": "GuidanceResponse",
        }
    )
    """
    GuidanceResponse

    A guidance response is the formal response to a guidance request, including any output parameters returned by the evaluation, as well as the description of any proposed actions to be taken.
    """

    healthcare_service = CodeSystemConcept(
        {
            "code": "HealthcareService",
            "definition": "The details of a healthcare service available at a location.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "HealthcareService",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ServizioSanitario",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ServiceDeSanté",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ServicioDeCuidado",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "医疗保健服务项目",
                },
            ],
            "display": "HealthcareService",
        }
    )
    """
    HealthcareService

    The details of a healthcare service available at a location.
    """

    imaging_study = CodeSystemConcept(
        {
            "code": "ImagingStudy",
            "definition": "Representation of the content produced in a DICOM imaging study. A study comprises a set of series, each of which includes a set of Service-Object Pair Instances (SOP Instances - images or other data) acquired or produced in a common context.  A series is of only one modality (e.g. X-ray, CT, MR, ultrasound), but a study may have multiple series of different modalities.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ImagingStudy",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "EtudeImagerie",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "EstudioImagen  / EstudioImagen",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "成像检查",
                },
            ],
            "display": "ImagingStudy",
        }
    )
    """
    ImagingStudy

    Representation of the content produced in a DICOM imaging study. A study comprises a set of series, each of which includes a set of Service-Object Pair Instances (SOP Instances - images or other data) acquired or produced in a common context.  A series is of only one modality (e.g. X-ray, CT, MR, ultrasound), but a study may have multiple series of different modalities.
    """

    immunization = CodeSystemConcept(
        {
            "code": "Immunization",
            "definition": "Describes the event of a patient being administered a vaccine or a record of an immunization as reported by a patient, a clinician or another party.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Immunization",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Immunizzazione",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Immunisation",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "免疫接种",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Inmunización",
                },
            ],
            "display": "Immunization",
        }
    )
    """
    Immunization

    Describes the event of a patient being administered a vaccine or a record of an immunization as reported by a patient, a clinician or another party.
    """

    immunization_evaluation = CodeSystemConcept(
        {
            "code": "ImmunizationEvaluation",
            "definition": 'Describes a comparison of an immunization event against published recommendations to determine if the administration is "valid" in relation to those  recommendations.',
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ImmunizationEvaluation",
                }
            ],
            "display": "ImmunizationEvaluation",
        }
    )
    """
    ImmunizationEvaluation

    Describes a comparison of an immunization event against published recommendations to determine if the administration is "valid" in relation to those  recommendations.
    """

    immunization_recommendation = CodeSystemConcept(
        {
            "code": "ImmunizationRecommendation",
            "definition": "A patient's point-in-time set of recommendations (i.e. forecasting) according to a published schedule with optional supporting justification.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ImmunizationRecommendation",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "RecommendationImmunisation",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "免疫接种建议",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "RecomendaciónInmunización /",
                },
            ],
            "display": "ImmunizationRecommendation",
        }
    )
    """
    ImmunizationRecommendation

    A patient's point-in-time set of recommendations (i.e. forecasting) according to a published schedule with optional supporting justification.
    """

    implementation_guide = CodeSystemConcept(
        {
            "code": "ImplementationGuide",
            "definition": "A set of rules of how a particular interoperability or standards problem is solved - typically through the use of FHIR resources. This resource is used to gather all the parts of an implementation guide into a logical whole and to publish a computable definition of all the parts.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ImplementationGuide",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "GuiaDeImplementacion",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "实施指南",
                },
            ],
            "display": "ImplementationGuide",
        }
    )
    """
    ImplementationGuide

    A set of rules of how a particular interoperability or standards problem is solved - typically through the use of FHIR resources. This resource is used to gather all the parts of an implementation guide into a logical whole and to publish a computable definition of all the parts.
    """

    insurance_plan = CodeSystemConcept(
        {
            "code": "InsurancePlan",
            "definition": "Details of a Health Insurance product/plan provided by an organization.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "InsurancePlan",
                }
            ],
            "display": "InsurancePlan",
        }
    )
    """
    InsurancePlan

    Details of a Health Insurance product/plan provided by an organization.
    """

    invoice = CodeSystemConcept(
        {
            "code": "Invoice",
            "definition": "Invoice containing collected ChargeItems from an Account with calculated individual and total price for Billing purpose.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Invoice",
                }
            ],
            "display": "Invoice",
        }
    )
    """
    Invoice

    Invoice containing collected ChargeItems from an Account with calculated individual and total price for Billing purpose.
    """

    library = CodeSystemConcept(
        {
            "code": "Library",
            "definition": "The Library resource is a general-purpose container for knowledge asset definitions. It can be used to describe and expose existing knowledge assets such as logic libraries and information model descriptions, as well as to describe a collection of knowledge assets.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Library",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Librería",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "库",
                },
            ],
            "display": "Library",
        }
    )
    """
    Library

    The Library resource is a general-purpose container for knowledge asset definitions. It can be used to describe and expose existing knowledge assets such as logic libraries and information model descriptions, as well as to describe a collection of knowledge assets.
    """

    linkage = CodeSystemConcept(
        {
            "code": "Linkage",
            "definition": 'Identifies two or more records (resource instances) that refer to the same real-world "occurrence".',
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Linkage",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Enlace / Conexión / Vinculo / Acoplamiento ",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "链接关系",
                },
            ],
            "display": "Linkage",
        }
    )
    """
    Linkage

    Identifies two or more records (resource instances) that refer to the same real-world "occurrence".
    """

    list_ = CodeSystemConcept(
        {
            "code": "List",
            "definition": "A list is a curated collection of resources.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "List",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Lista",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Liste",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "列表",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Lista",
                },
            ],
            "display": "List",
        }
    )
    """
    List

    A list is a curated collection of resources.
    """

    location = CodeSystemConcept(
        {
            "code": "Location",
            "definition": "Details and position information for a physical place where services are provided and resources and participants may be stored, found, contained, or accommodated.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Location",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Localisation",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "位置",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Locacion",
                },
            ],
            "display": "Location",
        }
    )
    """
    Location

    Details and position information for a physical place where services are provided and resources and participants may be stored, found, contained, or accommodated.
    """

    measure = CodeSystemConcept(
        {
            "code": "Measure",
            "definition": "The Measure resource provides the definition of a quality measure.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Measure",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Misura",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Medida",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "指标",
                },
            ],
            "display": "Measure",
        }
    )
    """
    Measure

    The Measure resource provides the definition of a quality measure.
    """

    measure_report = CodeSystemConcept(
        {
            "code": "MeasureReport",
            "definition": "The MeasureReport resource contains the results of the calculation of a measure; and optionally a reference to the resources involved in that calculation.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "MeasureReport",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ReporteMedida",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "指标报告",
                },
            ],
            "display": "MeasureReport",
        }
    )
    """
    MeasureReport

    The MeasureReport resource contains the results of the calculation of a measure; and optionally a reference to the resources involved in that calculation.
    """

    media = CodeSystemConcept(
        {
            "code": "Media",
            "definition": "A photo, video, or audio recording acquired or used in healthcare. The actual content may be inline or provided by direct reference.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Media",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Media",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Média",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Medio",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "媒体",
                },
            ],
            "display": "Media",
        }
    )
    """
    Media

    A photo, video, or audio recording acquired or used in healthcare. The actual content may be inline or provided by direct reference.
    """

    medication = CodeSystemConcept(
        {
            "code": "Medication",
            "definition": "This resource is primarily used for the identification and definition of a medication for the purposes of prescribing, dispensing, and administering a medication as well as for making statements about medication use.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Medication",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Médication",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "药物",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Medicación /Medicamento",
                },
            ],
            "display": "Medication",
        }
    )
    """
    Medication

    This resource is primarily used for the identification and definition of a medication for the purposes of prescribing, dispensing, and administering a medication as well as for making statements about medication use.
    """

    medication_administration = CodeSystemConcept(
        {
            "code": "MedicationAdministration",
            "definition": "Describes the event of a patient consuming or otherwise being administered a medication.  This may be as simple as swallowing a tablet or it may be a long running infusion.  Related resources tie this event to the authorizing prescription, and the specific encounter between patient and health care practitioner.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "MedicationAdministration",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "AdministrationMédicaments",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "药物施用",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "AdministraciónMedicación / AdministracionMedicamento",
                },
            ],
            "display": "MedicationAdministration",
        }
    )
    """
    MedicationAdministration

    Describes the event of a patient consuming or otherwise being administered a medication.  This may be as simple as swallowing a tablet or it may be a long running infusion.  Related resources tie this event to the authorizing prescription, and the specific encounter between patient and health care practitioner.
    """

    medication_dispense = CodeSystemConcept(
        {
            "code": "MedicationDispense",
            "definition": "Indicates that a medication product is to be or has been dispensed for a named person/patient.  This includes a description of the medication product (supply) provided and the instructions for administering the medication.  The medication dispense is the result of a pharmacy system responding to a medication order.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "MedicationDispense",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "DispensationMédicaments",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "药物配发",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "DispensaciónMedicación /DispensacionMedicamento",
                },
            ],
            "display": "MedicationDispense",
        }
    )
    """
    MedicationDispense

    Indicates that a medication product is to be or has been dispensed for a named person/patient.  This includes a description of the medication product (supply) provided and the instructions for administering the medication.  The medication dispense is the result of a pharmacy system responding to a medication order.
    """

    medication_knowledge = CodeSystemConcept(
        {
            "code": "MedicationKnowledge",
            "definition": "Information about a medication that is used to support knowledge.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "MedicationKnowledge",
                }
            ],
            "display": "MedicationKnowledge",
        }
    )
    """
    MedicationKnowledge

    Information about a medication that is used to support knowledge.
    """

    medication_request = CodeSystemConcept(
        {
            "code": "MedicationRequest",
            "definition": 'An order or request for both supply of the medication and the instructions for administration of the medication to a patient. The resource is called "MedicationRequest" rather than "MedicationPrescription" or "MedicationOrder" to generalize the use across inpatient and outpatient settings, including care plans, etc., and to harmonize with workflow patterns.',
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "MedicationRequest",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "PrescriptionMédicamenteuseTODO",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "药物请求",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "PrescripciónMedicaciónTODO  /PrescripcionMedicamento",
                },
            ],
            "display": "MedicationRequest",
        }
    )
    """
    MedicationRequest

    An order or request for both supply of the medication and the instructions for administration of the medication to a patient. The resource is called "MedicationRequest" rather than "MedicationPrescription" or "MedicationOrder" to generalize the use across inpatient and outpatient settings, including care plans, etc., and to harmonize with workflow patterns.
    """

    medication_statement = CodeSystemConcept(
        {
            "code": "MedicationStatement",
            "definition": "A record of a medication that is being consumed by a patient.   A MedicationStatement may indicate that the patient may be taking the medication now or has taken the medication in the past or will be taking the medication in the future.  The source of this information can be the patient, significant other (such as a family member or spouse), or a clinician.  A common scenario where this information is captured is during the history taking process during a patient visit or stay.   The medication information may come from sources such as the patient's memory, from a prescription bottle,  or from a list of medications the patient, clinician or other party maintains. \n\nThe primary difference between a medication statement and a medication administration is that the medication administration has complete administration information and is based on actual administration information from the person who administered the medication.  A medication statement is often, if not always, less specific.  There is no required date/time when the medication was administered, in fact we only know that a source has reported the patient is taking this medication, where details such as time, quantity, or rate or even medication product may be incomplete or missing or less precise.  As stated earlier, the medication statement information may come from the patient's memory, from a prescription bottle or from a list of medications the patient, clinician or other party maintains.  Medication administration is more formal and is not missing detailed information.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "MedicationStatement",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ÉtatMédication",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "药物声明",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ResumenMedicación /ResumenMedicamento",
                },
            ],
            "display": "MedicationStatement",
        }
    )
    """
    MedicationStatement

    A record of a medication that is being consumed by a patient.   A MedicationStatement may indicate that the patient may be taking the medication now or has taken the medication in the past or will be taking the medication in the future.  The source of this information can be the patient, significant other (such as a family member or spouse), or a clinician.  A common scenario where this information is captured is during the history taking process during a patient visit or stay.   The medication information may come from sources such as the patient's memory, from a prescription bottle,  or from a list of medications the patient, clinician or other party maintains. 

The primary difference between a medication statement and a medication administration is that the medication administration has complete administration information and is based on actual administration information from the person who administered the medication.  A medication statement is often, if not always, less specific.  There is no required date/time when the medication was administered, in fact we only know that a source has reported the patient is taking this medication, where details such as time, quantity, or rate or even medication product may be incomplete or missing or less precise.  As stated earlier, the medication statement information may come from the patient's memory, from a prescription bottle or from a list of medications the patient, clinician or other party maintains.  Medication administration is more formal and is not missing detailed information.
    """

    medicinal_product = CodeSystemConcept(
        {
            "code": "MedicinalProduct",
            "definition": "Detailed definition of a medicinal product, typically for uses other than direct patient care (e.g. regulatory use).",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "MedicinalProduct",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ProdottoMedicinale",
                },
            ],
            "display": "MedicinalProduct",
        }
    )
    """
    MedicinalProduct

    Detailed definition of a medicinal product, typically for uses other than direct patient care (e.g. regulatory use).
    """

    medicinal_product_authorization = CodeSystemConcept(
        {
            "code": "MedicinalProductAuthorization",
            "definition": "The regulatory authorization of a medicinal product.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "MedicinalProductAuthorization",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "AutorizzazioneProdottoMedicinale",
                },
            ],
            "display": "MedicinalProductAuthorization",
        }
    )
    """
    MedicinalProductAuthorization

    The regulatory authorization of a medicinal product.
    """

    medicinal_product_contraindication = CodeSystemConcept(
        {
            "code": "MedicinalProductContraindication",
            "definition": "The clinical particulars - indications, contraindications etc. of a medicinal product, including for regulatory purposes.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "MedicinalProductContraindication",
                }
            ],
            "display": "MedicinalProductContraindication",
        }
    )
    """
    MedicinalProductContraindication

    The clinical particulars - indications, contraindications etc. of a medicinal product, including for regulatory purposes.
    """

    medicinal_product_indication = CodeSystemConcept(
        {
            "code": "MedicinalProductIndication",
            "definition": "Indication for the Medicinal Product.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "MedicinalProductInteraction",
                }
            ],
            "display": "MedicinalProductIndication",
        }
    )
    """
    MedicinalProductIndication

    Indication for the Medicinal Product.
    """

    medicinal_product_ingredient = CodeSystemConcept(
        {
            "code": "MedicinalProductIngredient",
            "definition": "An ingredient of a manufactured item or pharmaceutical product.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "MedicinalProductIngredient",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "IngredienteProdottoMedicinale",
                },
            ],
            "display": "MedicinalProductIngredient",
        }
    )
    """
    MedicinalProductIngredient

    An ingredient of a manufactured item or pharmaceutical product.
    """

    medicinal_product_interaction = CodeSystemConcept(
        {
            "code": "MedicinalProductInteraction",
            "definition": "The interactions of the medicinal product with other medicinal products, or other forms of interactions.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "MedicinalProductInteraction",
                }
            ],
            "display": "MedicinalProductInteraction",
        }
    )
    """
    MedicinalProductInteraction

    The interactions of the medicinal product with other medicinal products, or other forms of interactions.
    """

    medicinal_product_manufactured = CodeSystemConcept(
        {
            "code": "MedicinalProductManufactured",
            "definition": "The manufactured item as contained in the packaged medicinal product.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "MedicinalProductManufactured",
                }
            ],
            "display": "MedicinalProductManufactured",
        }
    )
    """
    MedicinalProductManufactured

    The manufactured item as contained in the packaged medicinal product.
    """

    medicinal_product_packaged = CodeSystemConcept(
        {
            "code": "MedicinalProductPackaged",
            "definition": "A medicinal product in a container or package.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "MedicinalProductPackaged",
                }
            ],
            "display": "MedicinalProductPackaged",
        }
    )
    """
    MedicinalProductPackaged

    A medicinal product in a container or package.
    """

    medicinal_product_pharmaceutical = CodeSystemConcept(
        {
            "code": "MedicinalProductPharmaceutical",
            "definition": "A pharmaceutical product described in terms of its composition and dose form.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "MedicinalProductPharmaceutical",
                }
            ],
            "display": "MedicinalProductPharmaceutical",
        }
    )
    """
    MedicinalProductPharmaceutical

    A pharmaceutical product described in terms of its composition and dose form.
    """

    medicinal_product_undesirable_effect = CodeSystemConcept(
        {
            "code": "MedicinalProductUndesirableEffect",
            "definition": "Describe the undesirable effects of the medicinal product.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "MedicinalProductUndesirableEffect",
                }
            ],
            "display": "MedicinalProductUndesirableEffect",
        }
    )
    """
    MedicinalProductUndesirableEffect

    Describe the undesirable effects of the medicinal product.
    """

    message_definition = CodeSystemConcept(
        {
            "code": "MessageDefinition",
            "definition": "Defines the characteristics of a message that can be shared between systems, including the type of event that initiates the message, the content to be transmitted and what response(s), if any, are permitted.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "MessageDefinition",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "DefinizioneMessaggio",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "DefinicionMensaje",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "消息定义",
                },
            ],
            "display": "MessageDefinition",
        }
    )
    """
    MessageDefinition

    Defines the characteristics of a message that can be shared between systems, including the type of event that initiates the message, the content to be transmitted and what response(s), if any, are permitted.
    """

    message_header = CodeSystemConcept(
        {
            "code": "MessageHeader",
            "definition": "The header for a message exchange that is either requesting or responding to an action.  The reference(s) that are the subject of the action as well as other information related to the action are typically transmitted in a bundle in which the MessageHeader resource instance is the first resource in the bundle.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "MessageHeader",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "EntêteMessage",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "消息标头",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "CabeceraMensaje",
                },
            ],
            "display": "MessageHeader",
        }
    )
    """
    MessageHeader

    The header for a message exchange that is either requesting or responding to an action.  The reference(s) that are the subject of the action as well as other information related to the action are typically transmitted in a bundle in which the MessageHeader resource instance is the first resource in the bundle.
    """

    molecular_sequence = CodeSystemConcept(
        {
            "code": "MolecularSequence",
            "definition": "Raw data describing a biological sequence.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "MolecularSequence",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "SecuenciaMolecular",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "分子序列",
                },
            ],
            "display": "MolecularSequence",
        }
    )
    """
    MolecularSequence

    Raw data describing a biological sequence.
    """

    naming_system = CodeSystemConcept(
        {
            "code": "NamingSystem",
            "definition": 'A curated namespace that issues unique symbols within that namespace for the identification of concepts, people, devices, etc.  Represents a "System" used within the Identifier and Coding data types.',
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "NamingSystem",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "SystèmeDeNommage",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "SistemaDeNombres",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "命名系统",
                },
            ],
            "display": "NamingSystem",
        }
    )
    """
    NamingSystem

    A curated namespace that issues unique symbols within that namespace for the identification of concepts, people, devices, etc.  Represents a "System" used within the Identifier and Coding data types.
    """

    nutrition_order = CodeSystemConcept(
        {
            "code": "NutritionOrder",
            "definition": "A request to supply a diet, formula feeding (enteral) or oral nutritional supplement to a patient/resident.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "NutritionOrder",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "OrdreNutrition",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "OrdenNutrición",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "营养医嘱",
                },
            ],
            "display": "NutritionOrder",
        }
    )
    """
    NutritionOrder

    A request to supply a diet, formula feeding (enteral) or oral nutritional supplement to a patient/resident.
    """

    observation = CodeSystemConcept(
        {
            "code": "Observation",
            "definition": "Measurements and simple assertions made about a patient, device or other subject.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Observation",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Osservazione",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Observation",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "观察",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Observación",
                },
            ],
            "display": "Observation",
        }
    )
    """
    Observation

    Measurements and simple assertions made about a patient, device or other subject.
    """

    observation_definition = CodeSystemConcept(
        {
            "code": "ObservationDefinition",
            "definition": "Set of definitional characteristics for a kind of observation or measurement produced or consumed by an orderable health care service.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ObservationDefinition",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "DefinizioneOsservazione",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "DefinicionDeEspecimen",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "观察定义",
                },
            ],
            "display": "ObservationDefinition",
        }
    )
    """
    ObservationDefinition

    Set of definitional characteristics for a kind of observation or measurement produced or consumed by an orderable health care service.
    """

    operation_definition = CodeSystemConcept(
        {
            "code": "OperationDefinition",
            "definition": "A formal computable definition of an operation (on the RESTful interface) or a named query (using the search interaction).",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "OperationDefinition",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "DefinizioneOperazione",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "DéfinitionOpération",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "DefinicionDeOperacion",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "操作定义",
                },
            ],
            "display": "OperationDefinition",
        }
    )
    """
    OperationDefinition

    A formal computable definition of an operation (on the RESTful interface) or a named query (using the search interaction).
    """

    operation_outcome = CodeSystemConcept(
        {
            "code": "OperationOutcome",
            "definition": "A collection of error, warning, or information messages that result from a system action.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "OperationOutcome",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "RisultatoOperazione",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "RésultatOpération",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "操作结局",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ResultadoOperación",
                },
            ],
            "display": "OperationOutcome",
        }
    )
    """
    OperationOutcome

    A collection of error, warning, or information messages that result from a system action.
    """

    organization = CodeSystemConcept(
        {
            "code": "Organization",
            "definition": "A formally or informally recognized grouping of people or organizations formed for the purpose of achieving some form of collective action.  Includes companies, institutions, corporations, departments, community groups, healthcare practice groups, payer/insurer, etc.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Organization",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Organizzazione",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Organisation",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "组织机构",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Organización",
                },
            ],
            "display": "Organization",
        }
    )
    """
    Organization

    A formally or informally recognized grouping of people or organizations formed for the purpose of achieving some form of collective action.  Includes companies, institutions, corporations, departments, community groups, healthcare practice groups, payer/insurer, etc.
    """

    organization_affiliation = CodeSystemConcept(
        {
            "code": "OrganizationAffiliation",
            "definition": "Defines an affiliation/assotiation/relationship between 2 distinct oganizations, that is not a part-of relationship/sub-division relationship.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "OrganizationAffiliation",
                }
            ],
            "display": "OrganizationAffiliation",
        }
    )
    """
    OrganizationAffiliation

    Defines an affiliation/assotiation/relationship between 2 distinct oganizations, that is not a part-of relationship/sub-division relationship.
    """

    parameters = CodeSystemConcept(
        {
            "code": "Parameters",
            "definition": "This resource is a non-persisted resource used to pass information into and back from an [operation](operations.html). It has no other use, and there is no RESTful endpoint associated with it.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Parameters",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Parametros",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "参数",
                },
            ],
            "display": "Parameters",
        }
    )
    """
    Parameters

    This resource is a non-persisted resource used to pass information into and back from an [operation](operations.html). It has no other use, and there is no RESTful endpoint associated with it.
    """

    patient = CodeSystemConcept(
        {
            "code": "Patient",
            "definition": "Demographics and other administrative information about an individual or animal receiving care or other health-related services.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Patient",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Paziente",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Patient",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "患者",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Paciente",
                },
            ],
            "display": "Patient",
        }
    )
    """
    Patient

    Demographics and other administrative information about an individual or animal receiving care or other health-related services.
    """

    payment_notice = CodeSystemConcept(
        {
            "code": "PaymentNotice",
            "definition": "This resource provides the status of the payment for goods and services rendered, and the request and response resource references.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "PaymentNotice",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "AvvisoDiPagamento",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "AvisPaiement",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "AvisoDePago",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "付款通知",
                },
            ],
            "display": "PaymentNotice",
        }
    )
    """
    PaymentNotice

    This resource provides the status of the payment for goods and services rendered, and the request and response resource references.
    """

    payment_reconciliation = CodeSystemConcept(
        {
            "code": "PaymentReconciliation",
            "definition": "This resource provides the details including amount of a payment and allocates the payment items being paid.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "PaymentReconciliation",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "RiconciliazionePagamento",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "RéconciliationPaiement",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ConciliacionDePago",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "付款对账",
                },
            ],
            "display": "PaymentReconciliation",
        }
    )
    """
    PaymentReconciliation

    This resource provides the details including amount of a payment and allocates the payment items being paid.
    """

    person = CodeSystemConcept(
        {
            "code": "Person",
            "definition": "Demographics and administrative information about a person independent of a specific health-related context.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Person",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Persona",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Personne",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Persona",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "人员",
                },
            ],
            "display": "Person",
        }
    )
    """
    Person

    Demographics and administrative information about a person independent of a specific health-related context.
    """

    plan_definition = CodeSystemConcept(
        {
            "code": "PlanDefinition",
            "definition": "This resource allows for the definition of various types of plans as a sharable, consumable, and executable artifact. The resource is general enough to support the description of a broad range of clinical artifacts such as clinical decision support rules, order sets and protocols.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "PlanDefinition",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "DefinicionDePlan",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "计划定义",
                },
            ],
            "display": "PlanDefinition",
        }
    )
    """
    PlanDefinition

    This resource allows for the definition of various types of plans as a sharable, consumable, and executable artifact. The resource is general enough to support the description of a broad range of clinical artifacts such as clinical decision support rules, order sets and protocols.
    """

    practitioner = CodeSystemConcept(
        {
            "code": "Practitioner",
            "definition": "A person who is directly or indirectly involved in the provisioning of healthcare.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Practitioner",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Praticien",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "执业人员",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Practicante / Profesional",
                },
            ],
            "display": "Practitioner",
        }
    )
    """
    Practitioner

    A person who is directly or indirectly involved in the provisioning of healthcare.
    """

    practitioner_role = CodeSystemConcept(
        {
            "code": "PractitionerRole",
            "definition": "A specific set of Roles/Locations/specialties/services that a practitioner may perform at an organization for a period of time.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "PractitionerRole",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "RolProfesional",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "执业人员角色",
                },
            ],
            "display": "PractitionerRole",
        }
    )
    """
    PractitionerRole

    A specific set of Roles/Locations/specialties/services that a practitioner may perform at an organization for a period of time.
    """

    procedure = CodeSystemConcept(
        {
            "code": "Procedure",
            "definition": "An action that is or was performed on or for a patient. This can be a physical intervention like an operation, or less invasive like long term services, counseling, or hypnotherapy.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Procedure",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Procedura",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Procédure",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "操作项目",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Procedimiento",
                },
            ],
            "display": "Procedure",
        }
    )
    """
    Procedure

    An action that is or was performed on or for a patient. This can be a physical intervention like an operation, or less invasive like long term services, counseling, or hypnotherapy.
    """

    provenance = CodeSystemConcept(
        {
            "code": "Provenance",
            "definition": "Provenance of a resource is a record that describes entities and processes involved in producing and delivering or otherwise influencing that resource. Provenance provides a critical foundation for assessing authenticity, enabling trust, and allowing reproducibility. Provenance assertions are a form of contextual metadata and can themselves become important records with their own provenance. Provenance statement indicates clinical significance in terms of confidence in authenticity, reliability, and trustworthiness, integrity, and stage in lifecycle (e.g. Document Completion - has the artifact been legally authenticated), all of which may impact security, privacy, and trust policies.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Provenance",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Provenienza",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Provenance",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "出处",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Procedencia",
                },
            ],
            "display": "Provenance",
        }
    )
    """
    Provenance

    Provenance of a resource is a record that describes entities and processes involved in producing and delivering or otherwise influencing that resource. Provenance provides a critical foundation for assessing authenticity, enabling trust, and allowing reproducibility. Provenance assertions are a form of contextual metadata and can themselves become important records with their own provenance. Provenance statement indicates clinical significance in terms of confidence in authenticity, reliability, and trustworthiness, integrity, and stage in lifecycle (e.g. Document Completion - has the artifact been legally authenticated), all of which may impact security, privacy, and trust policies.
    """

    questionnaire = CodeSystemConcept(
        {
            "code": "Questionnaire",
            "definition": "A structured set of questions intended to guide the collection of answers from end-users. Questionnaires provide detailed control over order, presentation, phraseology and grouping to allow coherent, consistent data collection.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Questionnaire",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Questionario",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Questionnaire",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "调查问卷",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Cuestionario",
                },
            ],
            "display": "Questionnaire",
        }
    )
    """
    Questionnaire

    A structured set of questions intended to guide the collection of answers from end-users. Questionnaires provide detailed control over order, presentation, phraseology and grouping to allow coherent, consistent data collection.
    """

    questionnaire_response = CodeSystemConcept(
        {
            "code": "QuestionnaireResponse",
            "definition": "A structured set of questions and their answers. The questions are ordered and grouped into coherent subsets, corresponding to the structure of the grouping of the questionnaire being responded to.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "QuestionnaireResponse",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "RispostaQuestionario",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "RéponseQuestionnaire",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "RespuestaAlCuestionario",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "调查问卷答复",
                },
            ],
            "display": "QuestionnaireResponse",
        }
    )
    """
    QuestionnaireResponse

    A structured set of questions and their answers. The questions are ordered and grouped into coherent subsets, corresponding to the structure of the grouping of the questionnaire being responded to.
    """

    related_person = CodeSystemConcept(
        {
            "code": "RelatedPerson",
            "definition": "Information about a person that is involved in the care for a patient, but who is not the target of healthcare, nor has a formal responsibility in the care process.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "RelatedPerson",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "PersonaCorrelata",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "PersonneEnRelation",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "PersonaRelacionada",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "相关人员",
                },
            ],
            "display": "RelatedPerson",
        }
    )
    """
    RelatedPerson

    Information about a person that is involved in the care for a patient, but who is not the target of healthcare, nor has a formal responsibility in the care process.
    """

    request_group = CodeSystemConcept(
        {
            "code": "RequestGroup",
            "definition": 'A group of related requests that can be used to capture intended activities that have inter-dependencies such as "give this medication after that one".',
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "RequestGroup",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "GruppoDiRichieste",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "GrupoDeSolicitudes",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "请求分组",
                },
            ],
            "display": "RequestGroup",
        }
    )
    """
    RequestGroup

    A group of related requests that can be used to capture intended activities that have inter-dependencies such as "give this medication after that one".
    """

    research_definition = CodeSystemConcept(
        {
            "code": "ResearchDefinition",
            "definition": "The ResearchDefinition resource describes the conditional state (population and any exposures being compared within the population) and outcome (if specified) that the knowledge (evidence, assertion, recommendation) is about.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ResearchDefinition",
                }
            ],
            "display": "ResearchDefinition",
        }
    )
    """
    ResearchDefinition

    The ResearchDefinition resource describes the conditional state (population and any exposures being compared within the population) and outcome (if specified) that the knowledge (evidence, assertion, recommendation) is about.
    """

    research_element_definition = CodeSystemConcept(
        {
            "code": "ResearchElementDefinition",
            "definition": 'The ResearchElementDefinition resource describes a "PICO" element that knowledge (evidence, assertion, recommendation) is about.',
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ResearchElementDefinition",
                }
            ],
            "display": "ResearchElementDefinition",
        }
    )
    """
    ResearchElementDefinition

    The ResearchElementDefinition resource describes a "PICO" element that knowledge (evidence, assertion, recommendation) is about.
    """

    research_study = CodeSystemConcept(
        {
            "code": "ResearchStudy",
            "definition": "A process where a researcher or organization plans and then executes a series of steps intended to increase the field of healthcare-related knowledge.  This includes studies of safety, efficacy, comparative effectiveness and other information about medications, devices, therapies and other interventional and investigative techniques.  A ResearchStudy involves the gathering of information about human or animal subjects.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ResearchStudy",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "EstudioDeInvestigacion",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "调查研究",
                },
            ],
            "display": "ResearchStudy",
        }
    )
    """
    ResearchStudy

    A process where a researcher or organization plans and then executes a series of steps intended to increase the field of healthcare-related knowledge.  This includes studies of safety, efficacy, comparative effectiveness and other information about medications, devices, therapies and other interventional and investigative techniques.  A ResearchStudy involves the gathering of information about human or animal subjects.
    """

    research_subject = CodeSystemConcept(
        {
            "code": "ResearchSubject",
            "definition": "A physical entity which is the primary unit of operational and/or administrative interest in a study.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ResearchSubject",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "SujetoDeInvestigacion",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "研究主题",
                },
            ],
            "display": "ResearchSubject",
        }
    )
    """
    ResearchSubject

    A physical entity which is the primary unit of operational and/or administrative interest in a study.
    """

    resource = CodeSystemConcept(
        {
            "code": "Resource",
            "definition": "This is the base resource type for everything.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Resource",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Recurso",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "资源",
                },
            ],
            "display": "Resource",
        }
    )
    """
    Resource

    This is the base resource type for everything.
    """

    risk_assessment = CodeSystemConcept(
        {
            "code": "RiskAssessment",
            "definition": "An assessment of the likely outcome(s) for a patient or other subject as well as the likelihood of each outcome.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "RiskAssessment",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ÉvaluationRisques",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "EvaluacionDeRiesgo",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "风险评估",
                },
            ],
            "display": "RiskAssessment",
        }
    )
    """
    RiskAssessment

    An assessment of the likely outcome(s) for a patient or other subject as well as the likelihood of each outcome.
    """

    risk_evidence_synthesis = CodeSystemConcept(
        {
            "code": "RiskEvidenceSynthesis",
            "definition": "The RiskEvidenceSynthesis resource describes the likelihood of an outcome in a population plus exposure state where the risk estimate is derived from a combination of research studies.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "RiskEvidenceSynthesis",
                }
            ],
            "display": "RiskEvidenceSynthesis",
        }
    )
    """
    RiskEvidenceSynthesis

    The RiskEvidenceSynthesis resource describes the likelihood of an outcome in a population plus exposure state where the risk estimate is derived from a combination of research studies.
    """

    schedule = CodeSystemConcept(
        {
            "code": "Schedule",
            "definition": "A container for slots of time that may be available for booking appointments.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Schedule",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Agenda",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "日程安排",
                },
            ],
            "display": "Schedule",
        }
    )
    """
    Schedule

    A container for slots of time that may be available for booking appointments.
    """

    search_parameter = CodeSystemConcept(
        {
            "code": "SearchParameter",
            "definition": "A search parameter that defines a named search item that can be used to search/filter on a resource.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "SearchParameter",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ParametroDiRicerca",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ParamètreRecherche",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ParametroDeBusqueda",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "搜索参数",
                },
            ],
            "display": "SearchParameter",
        }
    )
    """
    SearchParameter

    A search parameter that defines a named search item that can be used to search/filter on a resource.
    """

    service_request = CodeSystemConcept(
        {
            "code": "ServiceRequest",
            "definition": "A record of a request for service such as diagnostic investigations, treatments, or operations to be performed.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ServiceRequest",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "RichiestaDiServizio",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "DemandeService",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "PeticiónServicio",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "服务项目请求",
                },
            ],
            "display": "ServiceRequest",
        }
    )
    """
    ServiceRequest

    A record of a request for service such as diagnostic investigations, treatments, or operations to be performed.
    """

    slot = CodeSystemConcept(
        {
            "code": "Slot",
            "definition": "A slot of time on a schedule that may be available for booking appointments.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Slot",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Slot",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "槽位",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Hueco / Zocalo / Espacio",
                },
            ],
            "display": "Slot",
        }
    )
    """
    Slot

    A slot of time on a schedule that may be available for booking appointments.
    """

    specimen = CodeSystemConcept(
        {
            "code": "Specimen",
            "definition": "A sample to be used for analysis.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Specimen",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Campione",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Spécimen",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "标本",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Especimen",
                },
            ],
            "display": "Specimen",
        }
    )
    """
    Specimen

    A sample to be used for analysis.
    """

    specimen_definition = CodeSystemConcept(
        {
            "code": "SpecimenDefinition",
            "definition": "A kind of specimen with associated set of requirements.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "SpecimenDefinition",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "DefinizioneCampione",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "DefinicionDeEspecimen",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "标本定义",
                },
            ],
            "display": "SpecimenDefinition",
        }
    )
    """
    SpecimenDefinition

    A kind of specimen with associated set of requirements.
    """

    structure_definition = CodeSystemConcept(
        {
            "code": "StructureDefinition",
            "definition": "A definition of a FHIR structure. This resource is used to describe the underlying resources, data types defined in FHIR, and also for describing extensions and constraints on resources and data types.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "StructureDefinition",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "DefinizioneStruttura",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "DéfinitionStructure",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "DefinicionDeEstructura",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "结构定义",
                },
            ],
            "display": "StructureDefinition",
        }
    )
    """
    StructureDefinition

    A definition of a FHIR structure. This resource is used to describe the underlying resources, data types defined in FHIR, and also for describing extensions and constraints on resources and data types.
    """

    structure_map = CodeSystemConcept(
        {
            "code": "StructureMap",
            "definition": "A Map of relationships between 2 structures that can be used to transform data.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "StructureMap",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "MapaDeEstructura",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "结构映射",
                },
            ],
            "display": "StructureMap",
        }
    )
    """
    StructureMap

    A Map of relationships between 2 structures that can be used to transform data.
    """

    subscription = CodeSystemConcept(
        {
            "code": "Subscription",
            "definition": 'The subscription resource is used to define a push-based subscription from a server to another system. Once a subscription is registered with the server, the server checks every resource that is created or updated, and if the resource matches the given criteria, it sends a message on the defined "channel" so that another system can take an appropriate action.',
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Subscription",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Sottoscrizione",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Souscription",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "订阅",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Suscripción",
                },
            ],
            "display": "Subscription",
        }
    )
    """
    Subscription

    The subscription resource is used to define a push-based subscription from a server to another system. Once a subscription is registered with the server, the server checks every resource that is created or updated, and if the resource matches the given criteria, it sends a message on the defined "channel" so that another system can take an appropriate action.
    """

    substance = CodeSystemConcept(
        {
            "code": "Substance",
            "definition": "A homogeneous material with a definite composition.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Substance",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Sostanza",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Substance",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "物质",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Sustancia",
                },
            ],
            "display": "Substance",
        }
    )
    """
    Substance

    A homogeneous material with a definite composition.
    """

    substance_nucleic_acid = CodeSystemConcept(
        {
            "code": "SubstanceNucleicAcid",
            "definition": "Nucleic acids are defined by three distinct elements: the base, sugar and linkage. Individual substance/moiety IDs will be created for each of these elements. The nucleotide sequence will be always entered in the 5’-3’ direction.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "SubstanceNucleicAcid",
                }
            ],
            "display": "SubstanceNucleicAcid",
        }
    )
    """
    SubstanceNucleicAcid

    Nucleic acids are defined by three distinct elements: the base, sugar and linkage. Individual substance/moiety IDs will be created for each of these elements. The nucleotide sequence will be always entered in the 5’-3’ direction.
    """

    substance_polymer = CodeSystemConcept(
        {
            "code": "SubstancePolymer",
            "definition": "Todo.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "SubstancePolymer",
                }
            ],
            "display": "SubstancePolymer",
        }
    )
    """
    SubstancePolymer

    Todo.
    """

    substance_protein = CodeSystemConcept(
        {
            "code": "SubstanceProtein",
            "definition": "A SubstanceProtein is defined as a single unit of a linear amino acid sequence, or a combination of subunits that are either covalently linked or have a defined invariant stoichiometric relationship. This includes all synthetic, recombinant and purified SubstanceProteins of defined sequence, whether the use is therapeutic or prophylactic. This set of elements will be used to describe albumins, coagulation factors, cytokines, growth factors, peptide/SubstanceProtein hormones, enzymes, toxins, toxoids, recombinant vaccines, and immunomodulators.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "SubstanceProtein",
                }
            ],
            "display": "SubstanceProtein",
        }
    )
    """
    SubstanceProtein

    A SubstanceProtein is defined as a single unit of a linear amino acid sequence, or a combination of subunits that are either covalently linked or have a defined invariant stoichiometric relationship. This includes all synthetic, recombinant and purified SubstanceProteins of defined sequence, whether the use is therapeutic or prophylactic. This set of elements will be used to describe albumins, coagulation factors, cytokines, growth factors, peptide/SubstanceProtein hormones, enzymes, toxins, toxoids, recombinant vaccines, and immunomodulators.
    """

    substance_reference_information = CodeSystemConcept(
        {
            "code": "SubstanceReferenceInformation",
            "definition": "Todo.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "SubstanceReferenceInformation",
                }
            ],
            "display": "SubstanceReferenceInformation",
        }
    )
    """
    SubstanceReferenceInformation

    Todo.
    """

    substance_source_material = CodeSystemConcept(
        {
            "code": "SubstanceSourceMaterial",
            "definition": "Source material shall capture information on the taxonomic and anatomical origins as well as the fraction of a material that can result in or can be modified to form a substance. This set of data elements shall be used to define polymer substances isolated from biological matrices. Taxonomic and anatomical origins shall be described using a controlled vocabulary as required. This information is captured for naturally derived polymers ( . starch) and structurally diverse substances. For Organisms belonging to the Kingdom Plantae the Substance level defines the fresh material of a single species or infraspecies, the Herbal Drug and the Herbal preparation. For Herbal preparations, the fraction information will be captured at the Substance information level and additional information for herbal extracts will be captured at the Specified Substance Group 1 information level. See for further explanation the Substance Class: Structurally Diverse and the herbal annex.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "SubstanceSourceMaterial",
                }
            ],
            "display": "SubstanceSourceMaterial",
        }
    )
    """
    SubstanceSourceMaterial

    Source material shall capture information on the taxonomic and anatomical origins as well as the fraction of a material that can result in or can be modified to form a substance. This set of data elements shall be used to define polymer substances isolated from biological matrices. Taxonomic and anatomical origins shall be described using a controlled vocabulary as required. This information is captured for naturally derived polymers ( . starch) and structurally diverse substances. For Organisms belonging to the Kingdom Plantae the Substance level defines the fresh material of a single species or infraspecies, the Herbal Drug and the Herbal preparation. For Herbal preparations, the fraction information will be captured at the Substance information level and additional information for herbal extracts will be captured at the Specified Substance Group 1 information level. See for further explanation the Substance Class: Structurally Diverse and the herbal annex.
    """

    substance_specification = CodeSystemConcept(
        {
            "code": "SubstanceSpecification",
            "definition": "The detailed description of a substance, typically at a level beyond what is used for prescribing.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "SubstanceSpecification",
                }
            ],
            "display": "SubstanceSpecification",
        }
    )
    """
    SubstanceSpecification

    The detailed description of a substance, typically at a level beyond what is used for prescribing.
    """

    supply_delivery = CodeSystemConcept(
        {
            "code": "SupplyDelivery",
            "definition": "Record of delivery of what is supplied.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "SupplyDelivery",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Supply Livraison",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "供应交付",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Entrega de Suministro",
                },
            ],
            "display": "SupplyDelivery",
        }
    )
    """
    SupplyDelivery

    Record of delivery of what is supplied.
    """

    supply_request = CodeSystemConcept(
        {
            "code": "SupplyRequest",
            "definition": "A record of a request for a medication, substance or device used in the healthcare setting.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "SupplyRequest",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Demande d'approvisionnement",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "供应请求",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Solicitud de Suministro",
                },
            ],
            "display": "SupplyRequest",
        }
    )
    """
    SupplyRequest

    A record of a request for a medication, substance or device used in the healthcare setting.
    """

    task = CodeSystemConcept(
        {
            "code": "Task",
            "definition": "A task to be performed.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Task",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Tarea",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "任务",
                },
            ],
            "display": "Task",
        }
    )
    """
    Task

    A task to be performed.
    """

    terminology_capabilities = CodeSystemConcept(
        {
            "code": "TerminologyCapabilities",
            "definition": "A TerminologyCapabilities resource documents a set of capabilities (behaviors) of a FHIR Terminology Server that may be used as a statement of actual server functionality or a statement of required or desired server implementation.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "TerminologyCapabilities",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "CapacidadTerminologica",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "术语服务能力",
                },
            ],
            "display": "TerminologyCapabilities",
        }
    )
    """
    TerminologyCapabilities

    A TerminologyCapabilities resource documents a set of capabilities (behaviors) of a FHIR Terminology Server that may be used as a statement of actual server functionality or a statement of required or desired server implementation.
    """

    test_report = CodeSystemConcept(
        {
            "code": "TestReport",
            "definition": "A summary of information based on the results of executing a TestScript.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "TestReport",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "RapportTest",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ReporteDePrueba",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "测试报告",
                },
            ],
            "display": "TestReport",
        }
    )
    """
    TestReport

    A summary of information based on the results of executing a TestScript.
    """

    test_script = CodeSystemConcept(
        {
            "code": "TestScript",
            "definition": "A structured set of tests against a FHIR server or client implementation to determine compliance against the FHIR specification.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "TestScript",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ScriptTest",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ScriptDePrueba",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "测试脚本",
                },
            ],
            "display": "TestScript",
        }
    )
    """
    TestScript

    A structured set of tests against a FHIR server or client implementation to determine compliance against the FHIR specification.
    """

    value_set = CodeSystemConcept(
        {
            "code": "ValueSet",
            "definition": "A ValueSet resource instance specifies a set of codes drawn from one or more code systems, intended for use in a particular context. Value sets link between [[[CodeSystem]]] definitions and their use in [coded elements](terminologies.html).",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ValueSet",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "EnsembleValeurs",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "取值集合",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ConjuntoValores / ConjuntoDeValores",
                },
            ],
            "display": "ValueSet",
        }
    )
    """
    ValueSet

    A ValueSet resource instance specifies a set of codes drawn from one or more code systems, intended for use in a particular context. Value sets link between [[[CodeSystem]]] definitions and their use in [coded elements](terminologies.html).
    """

    verification_result = CodeSystemConcept(
        {
            "code": "VerificationResult",
            "definition": "Describes validation requirements, source(s), status and dates for one or more elements.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "VerificationResult",
                }
            ],
            "display": "VerificationResult",
        }
    )
    """
    VerificationResult

    Describes validation requirements, source(s), status and dates for one or more elements.
    """

    vision_prescription = CodeSystemConcept(
        {
            "code": "VisionPrescription",
            "definition": "An authorization for the provision of glasses and/or contact lenses to a patient.",
            "designation": [
                {
                    "language": "en",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "VisionPrescription",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "PrescriptionVision",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "PrescripcionDeVision",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "视力处方",
                },
            ],
            "display": "VisionPrescription",
        }
    )
    """
    VisionPrescription

    An authorization for the provision of glasses and/or contact lenses to a patient.
    """

    class Meta:
        resource = _resource
