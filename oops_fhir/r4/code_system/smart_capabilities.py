from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["SmartCapabilities"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class SmartCapabilities:
    """
    SmartCapabilities

    Codes that define what the server is capable of.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/smart-capabilities
    """

    launch_ehr = CodeSystemConcept(
        {
            "code": "launch-ehr",
            "definition": "support for SMART’s EHR Launch mode.",
            "display": "EHR Launch Mode",
        }
    )
    """
    EHR Launch Mode

    support for SMART’s EHR Launch mode.
    """

    launch_standalone = CodeSystemConcept(
        {
            "code": "launch-standalone",
            "definition": "support for SMART’s Standalone Launch mode.",
            "display": "Standalone Launch Mode",
        }
    )
    """
    Standalone Launch Mode

    support for SMART’s Standalone Launch mode.
    """

    client_public = CodeSystemConcept(
        {
            "code": "client-public",
            "definition": "support for SMART’s public client profile (no client authentication).",
            "display": "Public Client Profile",
        }
    )
    """
    Public Client Profile

    support for SMART’s public client profile (no client authentication).
    """

    client_confidential_symmetric = CodeSystemConcept(
        {
            "code": "client-confidential-symmetric",
            "definition": "support for SMART’s confidential client profile (symmetric client secret authentication).",
            "display": "Confidential Client Profile",
        }
    )
    """
    Confidential Client Profile

    support for SMART’s confidential client profile (symmetric client secret authentication).
    """

    sso_openid_connect = CodeSystemConcept(
        {
            "code": "sso-openid-connect",
            "definition": "support for SMART’s OpenID Connect profile.",
            "display": "Supports OpenID Connect",
        }
    )
    """
    Supports OpenID Connect

    support for SMART’s OpenID Connect profile.
    """

    context_passthrough_banner = CodeSystemConcept(
        {
            "code": "context-passthrough-banner",
            "definition": "support for “need patient banner” launch context (conveyed via need_patient_banner token parameter).",
            "display": 'Allows "Need Patient Banner"',
        }
    )
    """
    Allows "Need Patient Banner"

    support for “need patient banner” launch context (conveyed via need_patient_banner token parameter).
    """

    context_passthrough_style = CodeSystemConcept(
        {
            "code": "context-passthrough-style",
            "definition": "support for “SMART style URL” launch context (conveyed via smart_style_url token parameter).",
            "display": 'Allows "Smart Style Style"',
        }
    )
    """
    Allows "Smart Style Style"

    support for “SMART style URL” launch context (conveyed via smart_style_url token parameter).
    """

    context_ehr_patient = CodeSystemConcept(
        {
            "code": "context-ehr-patient",
            "definition": "support for patient-level launch context (requested by launch/patient scope, conveyed via patient token parameter).",
            "display": 'Allows "Patient Level Launch Context (EHR)"',
        }
    )
    """
    Allows "Patient Level Launch Context (EHR)"

    support for patient-level launch context (requested by launch/patient scope, conveyed via patient token parameter).
    """

    context_ehr_encounter = CodeSystemConcept(
        {
            "code": "context-ehr-encounter",
            "definition": "support for encounter-level launch context (requested by launch/encounter scope, conveyed via encounter token parameter).",
            "display": 'Allows "Encounter Level Launch Context (EHR)"',
        }
    )
    """
    Allows "Encounter Level Launch Context (EHR)"

    support for encounter-level launch context (requested by launch/encounter scope, conveyed via encounter token parameter).
    """

    context_standalone_patient = CodeSystemConcept(
        {
            "code": "context-standalone-patient",
            "definition": "support for patient-level launch context (requested by launch/patient scope, conveyed via patient token parameter).",
            "display": 'Allows "Patient Level Launch Context (STANDALONE)"',
        }
    )
    """
    Allows "Patient Level Launch Context (STANDALONE)"

    support for patient-level launch context (requested by launch/patient scope, conveyed via patient token parameter).
    """

    context_standalone_encounter = CodeSystemConcept(
        {
            "code": "context-standalone-encounter",
            "definition": "support for encounter-level launch context (requested by launch/encounter scope, conveyed via encounter token parameter).",
            "display": 'Allows "Encounter Level Launch Context (STANDALONE)"',
        }
    )
    """
    Allows "Encounter Level Launch Context (STANDALONE)"

    support for encounter-level launch context (requested by launch/encounter scope, conveyed via encounter token parameter).
    """

    permission_offline = CodeSystemConcept(
        {
            "code": "permission-offline",
            "definition": "support for refresh tokens (requested by offline_access scope).",
            "display": "Supports Refresh Token",
        }
    )
    """
    Supports Refresh Token

    support for refresh tokens (requested by offline_access scope).
    """

    permission_patient = CodeSystemConcept(
        {
            "code": "permission-patient",
            "definition": "support for patient-level scopes (e.g. patient/Observation.read).",
            "display": "Supports Patient Level Scopes",
        }
    )
    """
    Supports Patient Level Scopes

    support for patient-level scopes (e.g. patient/Observation.read).
    """

    permission_user = CodeSystemConcept(
        {
            "code": "permission-user",
            "definition": "support for user-level scopes (e.g. user/Appointment.read).",
            "display": "Supports User Level Scopes",
        }
    )
    """
    Supports User Level Scopes

    support for user-level scopes (e.g. user/Appointment.read).
    """

    class Meta:
        resource = _resource
