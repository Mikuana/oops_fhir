from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["TemplateStatusCodeLifeCycle"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class TemplateStatusCodeLifeCycle:
    """
    TemplateStatusCode LifeCycle

    Life cycle of the Status Code of a Template Design (Version)

    Status: active - Version: None

    Copyright None

    urn:oid:2.16.840.1.113883.3.1937.98.5.8
    """

    draft = CodeSystemConcept(
        {
            "code": "draft",
            "definition": "Design is under development (nascent).",
            "display": "Draft",
        }
    )
    """
    Draft

    Design is under development (nascent).
    """

    pending = CodeSystemConcept(
        {
            "code": "pending",
            "definition": "Design is completed and is being reviewed.",
            "display": "Under pre-publication review",
        }
    )
    """
    Under pre-publication review

    Design is completed and is being reviewed.
    """

    active = CodeSystemConcept(
        {
            "code": "active",
            "definition": "Design has been deemed fit for the intended purpose and is published by the governance group.",
            "display": "active",
        }
    )
    """
    active

    Design has been deemed fit for the intended purpose and is published by the governance group.
    """

    review = CodeSystemConcept(
        {
            "code": "review",
            "definition": "Design is active, but is under review. The review may result in a change to the design. The change may necessitate a new version to be created. This in turn may result in the prior version of the template to be retired. Alternatively, the review may result in a change to the design that does not require a new version to be created, or it may result in no change to the design at all.",
            "display": "In Review",
        }
    )
    """
    In Review

    Design is active, but is under review. The review may result in a change to the design. The change may necessitate a new version to be created. This in turn may result in the prior version of the template to be retired. Alternatively, the review may result in a change to the design that does not require a new version to be created, or it may result in no change to the design at all.
    """

    cancelled = CodeSystemConcept(
        {
            "code": "cancelled",
            "definition": "A drafted design is determined to be erroneous or not fit for intended purpose and is discontinued before ever being published in an active state.",
            "display": "Cancelled",
        }
    )
    """
    Cancelled

    A drafted design is determined to be erroneous or not fit for intended purpose and is discontinued before ever being published in an active state.
    """

    rejected = CodeSystemConcept(
        {
            "code": "rejected",
            "definition": "A previously drafted design is determined to be erroneous or not fit for intended purpose and is discontinued before ever being published for consideration in a pending state.",
            "display": "Rejected",
        }
    )
    """
    Rejected

    A previously drafted design is determined to be erroneous or not fit for intended purpose and is discontinued before ever being published for consideration in a pending state.
    """

    retired = CodeSystemConcept(
        {
            "code": "retired",
            "definition": "A previously active design is discontinued from use. It should no longer be used for future designs, but for historical purposes may be used to process data previously recorded using this design. A newer design may or may not exist. The design is published in the retired state.",
            "display": "retired",
        }
    )
    """
    retired

    A previously active design is discontinued from use. It should no longer be used for future designs, but for historical purposes may be used to process data previously recorded using this design. A newer design may or may not exist. The design is published in the retired state.
    """

    terminated = CodeSystemConcept(
        {
            "code": "terminated",
            "definition": "A design is determined to be erroneous or not fit for the intended purpose and should no longer be used, even for historical purposes. No new designs can be developed for this template. The associated template no longer needs to be published, but if published, is shown in the terminated state.",
            "display": "Terminated",
        }
    )
    """
    Terminated

    A design is determined to be erroneous or not fit for the intended purpose and should no longer be used, even for historical purposes. No new designs can be developed for this template. The associated template no longer needs to be published, but if published, is shown in the terminated state.
    """

    class Meta:
        resource = _resource
