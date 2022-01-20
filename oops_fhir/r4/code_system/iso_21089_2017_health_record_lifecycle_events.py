from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ISO210892017HealthRecordLifecycleEvents"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ISO210892017HealthRecordLifecycleEvents:
    """
    None

    Attached is vocabulary for the 27 record lifecycle events, as per ISO TS
21089-2017, Health Informatics - Trusted End-to-End Information Flows,
Section 3, Terms and Definitions (2017, at ISO Central Secretariat,
passed ballot and ready for publication).  This will also be included in
the FHIR EHR Record Lifecycle Event Implementation Guide, balloted and
(to be) published with FHIR STU-3.

    Status: active - Version: None

    Copyright These codes are excerpted from ISO Standard, TS 21089-2017 - Health Informatics - Trusted End-to-End Information Flows, Copyright by ISO International. Copies of this standard are available through the ISO Web Site at www.iso.org.

    http://terminology.hl7.org/CodeSystem/iso-21089-lifecycle
    """

    access = CodeSystemConcept(
        {
            "code": "access",
            "definition": "Occurs when an agent causes the system to obtain and open a record entry for inspection or review.",
            "display": "Access/View Record Lifecycle Event",
        }
    )
    """
    Access/View Record Lifecycle Event

    Occurs when an agent causes the system to obtain and open a record entry for inspection or review.
    """

    hold = CodeSystemConcept(
        {
            "code": "hold",
            "definition": "Occurs when an agent causes the system to tag or otherwise indicate special access management and suspension of record entry deletion/destruction, if deemed relevant to a lawsuit or which are reasonably anticipated to be relevant or to fulfill organizational policy under the legal doctrine of “duty to preserve”.",
            "display": "Add Legal Hold Record Lifecycle Event",
        }
    )
    """
    Add Legal Hold Record Lifecycle Event

    Occurs when an agent causes the system to tag or otherwise indicate special access management and suspension of record entry deletion/destruction, if deemed relevant to a lawsuit or which are reasonably anticipated to be relevant or to fulfill organizational policy under the legal doctrine of “duty to preserve”.
    """

    amend = CodeSystemConcept(
        {
            "code": "amend",
            "definition": "Occurs when an agent makes any change to record entry content currently residing in storage considered permanent (persistent).",
            "display": "Amend (Update) Record Lifecycle Event",
        }
    )
    """
    Amend (Update) Record Lifecycle Event

    Occurs when an agent makes any change to record entry content currently residing in storage considered permanent (persistent).
    """

    archive = CodeSystemConcept(
        {
            "code": "archive",
            "definition": "Occurs when an agent causes the system to create and move archive artifacts containing record entry content, typically to long-term offline storage.",
            "display": "Archive Record Lifecycle Event",
        }
    )
    """
    Archive Record Lifecycle Event

    Occurs when an agent causes the system to create and move archive artifacts containing record entry content, typically to long-term offline storage.
    """

    attest = CodeSystemConcept(
        {
            "code": "attest",
            "definition": "Occurs when an agent causes the system to capture the agent’s digital signature (or equivalent indication) during formal validation of record entry content.",
            "display": "Attest Record Lifecycle Event",
        }
    )
    """
    Attest Record Lifecycle Event

    Occurs when an agent causes the system to capture the agent’s digital signature (or equivalent indication) during formal validation of record entry content.
    """

    decrypt = CodeSystemConcept(
        {
            "code": "decrypt",
            "definition": "Occurs when an agent causes the system to decode record entry content from a cipher.",
            "display": "Decrypt Record Lifecycle Event",
        }
    )
    """
    Decrypt Record Lifecycle Event

    Occurs when an agent causes the system to decode record entry content from a cipher.
    """

    deidentify = CodeSystemConcept(
        {
            "code": "deidentify",
            "definition": "Occurs when an agent causes the system to scrub record entry content to reduce the association between a set of identifying data and the data subject in a way that might or might not be reversible.",
            "display": "De-Identify (Anononymize) Record Lifecycle Event",
        }
    )
    """
    De-Identify (Anononymize) Record Lifecycle Event

    Occurs when an agent causes the system to scrub record entry content to reduce the association between a set of identifying data and the data subject in a way that might or might not be reversible.
    """

    deprecate = CodeSystemConcept(
        {
            "code": "deprecate",
            "definition": "Occurs when an agent causes the system to tag record entry(ies) as obsolete, erroneous or untrustworthy, to warn against its future use.",
            "display": "Deprecate Record Lifecycle Event",
        }
    )
    """
    Deprecate Record Lifecycle Event

    Occurs when an agent causes the system to tag record entry(ies) as obsolete, erroneous or untrustworthy, to warn against its future use.
    """

    destroy = CodeSystemConcept(
        {
            "code": "destroy",
            "definition": "Occurs when an agent causes the system to permanently erase record entry content from the system.",
            "display": "Destroy/Delete Record Lifecycle Event",
        }
    )
    """
    Destroy/Delete Record Lifecycle Event

    Occurs when an agent causes the system to permanently erase record entry content from the system.
    """

    disclose = CodeSystemConcept(
        {
            "code": "disclose",
            "definition": "Occurs when an agent causes the system to release, transfer, provision access to, or otherwise divulge record entry content.",
            "display": "Disclose Record Lifecycle Event",
        }
    )
    """
    Disclose Record Lifecycle Event

    Occurs when an agent causes the system to release, transfer, provision access to, or otherwise divulge record entry content.
    """

    encrypt = CodeSystemConcept(
        {
            "code": "encrypt",
            "definition": "Occurs when an agent causes the system to encode record entry content in a cipher.",
            "display": "Encrypt Record Lifecycle Event",
        }
    )
    """
    Encrypt Record Lifecycle Event

    Occurs when an agent causes the system to encode record entry content in a cipher.
    """

    extract = CodeSystemConcept(
        {
            "code": "extract",
            "definition": "Occurs when an agent causes the system to selectively pull out a subset of record entry content, based on explicit criteria.",
            "display": "Extract Record Lifecycle Event",
        }
    )
    """
    Extract Record Lifecycle Event

    Occurs when an agent causes the system to selectively pull out a subset of record entry content, based on explicit criteria.
    """

    link = CodeSystemConcept(
        {
            "code": "link",
            "definition": "Occurs when an agent causes the system to connect related record entries.",
            "display": "Link Record Lifecycle Event",
        }
    )
    """
    Link Record Lifecycle Event

    Occurs when an agent causes the system to connect related record entries.
    """

    merge = CodeSystemConcept(
        {
            "code": "merge",
            "definition": "Occurs when an agent causes the system to combine or join content from two or more record entries, resulting in a single logical record entry.",
            "display": "Merge Record Lifecycle Event",
        }
    )
    """
    Merge Record Lifecycle Event

    Occurs when an agent causes the system to combine or join content from two or more record entries, resulting in a single logical record entry.
    """

    originate = CodeSystemConcept(
        {
            "code": "originate",
            "definition": "Occurs when an agent causes the system to: a) initiate capture of potential record content, and b) incorporate that content into the storage considered a permanent part of the health record.",
            "display": "Originate/Retain Record Lifecycle Event",
        }
    )
    """
    Originate/Retain Record Lifecycle Event

    Occurs when an agent causes the system to: a) initiate capture of potential record content, and b) incorporate that content into the storage considered a permanent part of the health record.
    """

    pseudonymize = CodeSystemConcept(
        {
            "code": "pseudonymize",
            "definition": "Occurs when an agent causes the system to remove record entry content to reduce the association between a set of identifying data and the data subject in a way that may be reversible.",
            "display": "Pseudonymize Record Lifecycle Event",
        }
    )
    """
    Pseudonymize Record Lifecycle Event

    Occurs when an agent causes the system to remove record entry content to reduce the association between a set of identifying data and the data subject in a way that may be reversible.
    """

    reactivate = CodeSystemConcept(
        {
            "code": "reactivate",
            "definition": "Occurs when an agent causes the system to recreate or restore full status to record entries previously deleted or deprecated.",
            "display": "Re-activate Record Lifecycle Event",
        }
    )
    """
    Re-activate Record Lifecycle Event

    Occurs when an agent causes the system to recreate or restore full status to record entries previously deleted or deprecated.
    """

    receive = CodeSystemConcept(
        {
            "code": "receive",
            "definition": "Occurs when an agent causes the system to a) initiate capture of data content from elsewhere, and b) incorporate that content into the storage considered a permanent part of the health record.",
            "display": "Receive/Retain Record Lifecycle Event",
        }
    )
    """
    Receive/Retain Record Lifecycle Event

    Occurs when an agent causes the system to a) initiate capture of data content from elsewhere, and b) incorporate that content into the storage considered a permanent part of the health record.
    """

    reidentify = CodeSystemConcept(
        {
            "code": "reidentify",
            "definition": "Occurs when an agent causes the system to restore information to data that allows identification of information source and/or information subject.",
            "display": "Re-identify Record Lifecycle Event",
        }
    )
    """
    Re-identify Record Lifecycle Event

    Occurs when an agent causes the system to restore information to data that allows identification of information source and/or information subject.
    """

    unhold = CodeSystemConcept(
        {
            "code": "unhold",
            "definition": "Occurs when an agent causes the system to remove a tag or other cues for special access management had required to fulfill organizational policy under the legal doctrine of “duty to preserve”.",
            "display": "Remove Legal Hold Record Lifecycle Event",
        }
    )
    """
    Remove Legal Hold Record Lifecycle Event

    Occurs when an agent causes the system to remove a tag or other cues for special access management had required to fulfill organizational policy under the legal doctrine of “duty to preserve”.
    """

    report = CodeSystemConcept(
        {
            "code": "report",
            "definition": "Occurs when an agent causes the system to produce and deliver record entry content in a particular form and manner.",
            "display": "Report (Output) Record Lifecycle Event",
        }
    )
    """
    Report (Output) Record Lifecycle Event

    Occurs when an agent causes the system to produce and deliver record entry content in a particular form and manner.
    """

    restore = CodeSystemConcept(
        {
            "code": "restore",
            "definition": "Occurs when an agent causes the system to recreate record entries and their content from a previous created archive artefact.",
            "display": "Restore Record Lifecycle Event",
        }
    )
    """
    Restore Record Lifecycle Event

    Occurs when an agent causes the system to recreate record entries and their content from a previous created archive artefact.
    """

    transform = CodeSystemConcept(
        {
            "code": "transform",
            "definition": "Occurs when an agent causes the system to change the form, language or code system used to represent record entry content.",
            "display": "Transform/Translate Record Lifecycle Event",
        }
    )
    """
    Transform/Translate Record Lifecycle Event

    Occurs when an agent causes the system to change the form, language or code system used to represent record entry content.
    """

    transmit = CodeSystemConcept(
        {
            "code": "transmit",
            "definition": "Occurs when an agent causes the system to send record entry content from one (EHR/PHR/other) system to another.",
            "display": "Transmit Record Lifecycle Event",
        }
    )
    """
    Transmit Record Lifecycle Event

    Occurs when an agent causes the system to send record entry content from one (EHR/PHR/other) system to another.
    """

    unlink = CodeSystemConcept(
        {
            "code": "unlink",
            "definition": "Occurs when an agent causes the system to disconnect two or more record entries previously connected, rendering them separate (disconnected) again.",
            "display": "Unlink Record Lifecycle Event",
        }
    )
    """
    Unlink Record Lifecycle Event

    Occurs when an agent causes the system to disconnect two or more record entries previously connected, rendering them separate (disconnected) again.
    """

    unmerge = CodeSystemConcept(
        {
            "code": "unmerge",
            "definition": "Occurs when an agent causes the system to reverse a previous record entry merge operation, rendering them separate again.",
            "display": "Unmerge Record Lifecycle Event",
        }
    )
    """
    Unmerge Record Lifecycle Event

    Occurs when an agent causes the system to reverse a previous record entry merge operation, rendering them separate again.
    """

    verify = CodeSystemConcept(
        {
            "code": "verify",
            "definition": "Occurs when an agent causes the system to confirm compliance of data or data objects with regulations, requirements, specifications, or other imposed conditions based on organizational policy.",
            "display": "Verify Record Lifecycle Event",
        }
    )
    """
    Verify Record Lifecycle Event

    Occurs when an agent causes the system to confirm compliance of data or data objects with regulations, requirements, specifications, or other imposed conditions based on organizational policy.
    """

    class Meta:
        resource = _resource
