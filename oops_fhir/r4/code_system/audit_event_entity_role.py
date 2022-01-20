from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AuditEventEntityRole"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AuditEventEntityRole:
    """
    AuditEventEntityRole

    Code representing the role the entity played in the audit event.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/object-role
    """

    one = CodeSystemConcept(
        {
            "code": "1",
            "definition": "This object is the patient that is the subject of care related to this event.  It is identifiable by patient ID or equivalent.  The patient may be either human or animal.",
            "display": "Patient",
        }
    )
    """
    Patient

    This object is the patient that is the subject of care related to this event.  It is identifiable by patient ID or equivalent.  The patient may be either human or animal.
    """

    two = CodeSystemConcept(
        {
            "code": "2",
            "definition": "This is a location identified as related to the event.  This is usually the location where the event took place.  Note that for shipping, the usual events are arrival at a location or departure from a location.",
            "display": "Location",
        }
    )
    """
    Location

    This is a location identified as related to the event.  This is usually the location where the event took place.  Note that for shipping, the usual events are arrival at a location or departure from a location.
    """

    three = CodeSystemConcept(
        {
            "code": "3",
            "definition": "This object is any kind of persistent document created as a result of the event.  This could be a paper report, film, electronic report, DICOM Study, etc.  Issues related to medical records life cycle management are conveyed elsewhere.",
            "display": "Report",
        }
    )
    """
    Report

    This object is any kind of persistent document created as a result of the event.  This could be a paper report, film, electronic report, DICOM Study, etc.  Issues related to medical records life cycle management are conveyed elsewhere.
    """

    four = CodeSystemConcept(
        {
            "code": "4",
            "definition": "A logical object related to a health record event.  This is any healthcare  specific resource (object) not restricted to FHIR defined Resources.",
            "display": "Domain Resource",
        }
    )
    """
    Domain Resource

    A logical object related to a health record event.  This is any healthcare  specific resource (object) not restricted to FHIR defined Resources.
    """

    five = CodeSystemConcept(
        {
            "code": "5",
            "definition": "This is any configurable file used to control creation of documents.  Examples include the objects maintained by the HL7 Master File transactions, Value Sets, etc.",
            "display": "Master file",
        }
    )
    """
    Master file

    This is any configurable file used to control creation of documents.  Examples include the objects maintained by the HL7 Master File transactions, Value Sets, etc.
    """

    six = CodeSystemConcept(
        {
            "code": "6",
            "definition": "A human participant not otherwise identified by some other category.",
            "display": "User",
        }
    )
    """
    User

    A human participant not otherwise identified by some other category.
    """

    seven = CodeSystemConcept(
        {"code": "7", "definition": "(deprecated).", "display": "List"}
    )
    """
    List

    (deprecated).
    """

    eight = CodeSystemConcept(
        {
            "code": "8",
            "definition": "Typically, a licensed person who is providing or performing care related to the event, generally a physician.   The key distinction between doctor and practitioner is with regards to their role, not the licensing.  The doctor is the human who actually performed the work.  The practitioner is the human or organization that is responsible for the work.",
            "display": "Doctor",
        }
    )
    """
    Doctor

    Typically, a licensed person who is providing or performing care related to the event, generally a physician.   The key distinction between doctor and practitioner is with regards to their role, not the licensing.  The doctor is the human who actually performed the work.  The practitioner is the human or organization that is responsible for the work.
    """

    nine = CodeSystemConcept(
        {
            "code": "9",
            "definition": "A person or system that is being notified as part of the event.  This is relevant in situations where automated systems provide notifications to other parties when an event took place.",
            "display": "Subscriber",
        }
    )
    """
    Subscriber

    A person or system that is being notified as part of the event.  This is relevant in situations where automated systems provide notifications to other parties when an event took place.
    """

    one0 = CodeSystemConcept(
        {
            "code": "10",
            "definition": "Insurance company, or any other organization who accepts responsibility for paying for the healthcare event.",
            "display": "Guarantor",
        }
    )
    """
    Guarantor

    Insurance company, or any other organization who accepts responsibility for paying for the healthcare event.
    """

    one1 = CodeSystemConcept(
        {
            "code": "11",
            "definition": "A person or active system object involved in the event with a security role.",
            "display": "Security User Entity",
        }
    )
    """
    Security User Entity

    A person or active system object involved in the event with a security role.
    """

    one2 = CodeSystemConcept(
        {
            "code": "12",
            "definition": "A person or system object involved in the event with the authority to modify security roles of other objects.",
            "display": "Security User Group",
        }
    )
    """
    Security User Group

    A person or system object involved in the event with the authority to modify security roles of other objects.
    """

    one3 = CodeSystemConcept(
        {
            "code": "13",
            "definition": "A passive object, such as a role table, that is relevant to the event.",
            "display": "Security Resource",
        }
    )
    """
    Security Resource

    A passive object, such as a role table, that is relevant to the event.
    """

    one4 = CodeSystemConcept(
        {
            "code": "14",
            "definition": "(deprecated)  Relevant to certain RBAC security methodologies.",
            "display": "Security Granularity Definition",
        }
    )
    """
    Security Granularity Definition

    (deprecated)  Relevant to certain RBAC security methodologies.
    """

    one5 = CodeSystemConcept(
        {
            "code": "15",
            "definition": "Any person or organization responsible for providing care.  This encompasses all forms of care, licensed or otherwise, and all sorts of teams and care groups. Note the distinction between practitioner and the doctor that actually provided the care to the patient.",
            "display": "Practitioner",
        }
    )
    """
    Practitioner

    Any person or organization responsible for providing care.  This encompasses all forms of care, licensed or otherwise, and all sorts of teams and care groups. Note the distinction between practitioner and the doctor that actually provided the care to the patient.
    """

    one6 = CodeSystemConcept(
        {
            "code": "16",
            "definition": "The source or destination for data transfer, when it does not match some other role.",
            "display": "Data Destination",
        }
    )
    """
    Data Destination

    The source or destination for data transfer, when it does not match some other role.
    """

    one7 = CodeSystemConcept(
        {
            "code": "17",
            "definition": "A source or destination for data transfer that acts as an archive, database, or similar role.",
            "display": "Data Repository",
        }
    )
    """
    Data Repository

    A source or destination for data transfer that acts as an archive, database, or similar role.
    """

    one8 = CodeSystemConcept(
        {
            "code": "18",
            "definition": "An object that holds schedule information.  This could be an appointment book, availability information, etc.",
            "display": "Schedule",
        }
    )
    """
    Schedule

    An object that holds schedule information.  This could be an appointment book, availability information, etc.
    """

    one9 = CodeSystemConcept(
        {
            "code": "19",
            "definition": "An organization or person that is the recipient of services.  This could be an organization that is buying services for a patient, or a person that is buying services for an animal.",
            "display": "Customer",
        }
    )
    """
    Customer

    An organization or person that is the recipient of services.  This could be an organization that is buying services for a patient, or a person that is buying services for an animal.
    """

    two0 = CodeSystemConcept(
        {
            "code": "20",
            "definition": "An order, task, work item, procedure step, or other description of work to be performed; e.g. a particular instance of an MPPS.",
            "display": "Job",
        }
    )
    """
    Job

    An order, task, work item, procedure step, or other description of work to be performed; e.g. a particular instance of an MPPS.
    """

    two1 = CodeSystemConcept(
        {
            "code": "21",
            "definition": "A list of jobs or a system that provides lists of jobs; e.g. an MWL SCP.",
            "display": "Job Stream",
        }
    )
    """
    Job Stream

    A list of jobs or a system that provides lists of jobs; e.g. an MWL SCP.
    """

    two2 = CodeSystemConcept(
        {"code": "22", "definition": "(Deprecated).", "display": "Table"}
    )
    """
    Table

    (Deprecated).
    """

    two3 = CodeSystemConcept(
        {
            "code": "23",
            "definition": "An object that specifies or controls the routing or delivery of items.  For example, a distribution list is the routing criteria for mail.  The items delivered may be documents, jobs, or other objects.",
            "display": "Routing Criteria",
        }
    )
    """
    Routing Criteria

    An object that specifies or controls the routing or delivery of items.  For example, a distribution list is the routing criteria for mail.  The items delivered may be documents, jobs, or other objects.
    """

    two4 = CodeSystemConcept(
        {
            "code": "24",
            "definition": "The contents of a query.  This is used to capture the contents of any kind of query.  For security surveillance purposes knowing the queries being made is very important.",
            "display": "Query",
        }
    )
    """
    Query

    The contents of a query.  This is used to capture the contents of any kind of query.  For security surveillance purposes knowing the queries being made is very important.
    """

    class Meta:
        resource = _resource
