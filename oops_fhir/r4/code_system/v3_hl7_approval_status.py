from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3hl7ApprovalStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3hl7ApprovalStatus:
    """
    v3 Code System hl7ApprovalStatus

      Description:  Codes for concepts describing the approval level of HL7
artifacts.  This code system reflects the concepts expressed in HL7's
Governance & Operations Manual (GOM) past and present.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-hl7ApprovalStatus
    """

    affd = CodeSystemConcept(
        {
            "code": "affd",
            "definition": "Description: Content that is being presented to an international affiliate for consideration as a realm-specific draft standard for trial use.",
            "display": "affiliate ballot - DSTU",
        }
    )
    """
    affiliate ballot - DSTU

    Description: Content that is being presented to an international affiliate for consideration as a realm-specific draft standard for trial use.
    """

    affi = CodeSystemConcept(
        {
            "code": "affi",
            "definition": "Description: Content that is being presented to an international affiliate for consideration as a realm-specific informative standard.",
            "display": "affiliate ballot - informative",
        }
    )
    """
    affiliate ballot - informative

    Description: Content that is being presented to an international affiliate for consideration as a realm-specific informative standard.
    """

    affn = CodeSystemConcept(
        {
            "code": "affn",
            "definition": "Description: Content that is being presented to an international affiliate for consideration as a realm-specific normative standard.",
            "display": "affiliate ballot - normative",
        }
    )
    """
    affiliate ballot - normative

    Description: Content that is being presented to an international affiliate for consideration as a realm-specific normative standard.
    """

    appad = CodeSystemConcept(
        {
            "code": "appad",
            "definition": "Description: Content that has passed ballot as a realm-specific draft standard for trial use.",
            "display": "approved affiliate DSTU",
        }
    )
    """
    approved affiliate DSTU

    Description: Content that has passed ballot as a realm-specific draft standard for trial use.
    """

    appai = CodeSystemConcept(
        {
            "code": "appai",
            "definition": "Description: Content that has passed ballot as a realm-specific informative standard.",
            "display": "approved affiliate informative",
        }
    )
    """
    approved affiliate informative

    Description: Content that has passed ballot as a realm-specific informative standard.
    """

    appan = CodeSystemConcept(
        {
            "code": "appan",
            "definition": "Description: Content that has passed ballot as a realm-specific normative standard",
            "display": "approved affiliate normative",
        }
    )
    """
    approved affiliate normative

    Description: Content that has passed ballot as a realm-specific normative standard
    """

    appd = CodeSystemConcept(
        {
            "code": "appd",
            "definition": "Description: Content that has passed ballot as a draft standard for trial use.",
            "display": "approved DSTU",
        }
    )
    """
    approved DSTU

    Description: Content that has passed ballot as a draft standard for trial use.
    """

    appi = CodeSystemConcept(
        {
            "code": "appi",
            "definition": "Description: Content that has passed ballot as a normative standard.",
            "display": "approved informative",
        }
    )
    """
    approved informative

    Description: Content that has passed ballot as a normative standard.
    """

    appn = CodeSystemConcept(
        {
            "code": "appn",
            "definition": "Description: Content that has passed ballot as a normative standard.",
            "display": "approved normative",
        }
    )
    """
    approved normative

    Description: Content that has passed ballot as a normative standard.
    """

    comi = CodeSystemConcept(
        {
            "code": "comi",
            "definition": "Description: Content prepared by a committee and submitted for internal consideration as an informative standard.\r\n\n                        \n                           \n                              Deprecation Comment\n                            No longer supported as ballot statuses within the HL7 Governance and Operations Manual.  Use normative or informative variants instead.",
            "display": "committee ballot - informative",
            "property": [
                {"code": "status", "valueCode": "deprecated"},
                {"code": "deprecationDate", "valueDateTime": "2010-11-23"},
            ],
        }
    )
    """
    committee ballot - informative

    Description: Content prepared by a committee and submitted for internal consideration as an informative standard.

                        
                           
                              Deprecation Comment
                            No longer supported as ballot statuses within the HL7 Governance and Operations Manual.  Use normative or informative variants instead.
    """

    comn = CodeSystemConcept(
        {
            "code": "comn",
            "definition": "Description: Content prepared by a committee and submitted for internal consideration as an informative standard.\r\n\n                        \n                           \n                              Deprecation Comment\n                            No longer supported as ballot statuses within the HL7 Governance and Operations Manual.  Use normative or informative variants instead.",
            "display": "committee ballot - normative",
            "property": [
                {"code": "status", "valueCode": "deprecated"},
                {"code": "deprecationDate", "valueDateTime": "2010-11-23"},
            ],
        }
    )
    """
    committee ballot - normative

    Description: Content prepared by a committee and submitted for internal consideration as an informative standard.

                        
                           
                              Deprecation Comment
                            No longer supported as ballot statuses within the HL7 Governance and Operations Manual.  Use normative or informative variants instead.
    """

    draft = CodeSystemConcept(
        {
            "code": "draft",
            "definition": "Description: Content that is under development and is not intended to be used.",
            "display": "draft",
        }
    )
    """
    draft

    Description: Content that is under development and is not intended to be used.
    """

    loc = CodeSystemConcept(
        {
            "code": "loc",
            "definition": "Description: Content that represents an adaption of a implementable balloted material to represent the needs or capabilities of a particular installation.",
            "display": "localized adaptation",
        }
    )
    """
    localized adaptation

    Description: Content that represents an adaption of a implementable balloted material to represent the needs or capabilities of a particular installation.
    """

    memd = CodeSystemConcept(
        {
            "code": "memd",
            "definition": "Description: Content prepared by a committee and submitted for membership consideration as a draft standard for trial use.",
            "display": "membership ballot - DSTU",
        }
    )
    """
    membership ballot - DSTU

    Description: Content prepared by a committee and submitted for membership consideration as a draft standard for trial use.
    """

    memi = CodeSystemConcept(
        {
            "code": "memi",
            "definition": "Description: Content prepared by a committee and submitted for membership consideration as an informative standard.",
            "display": "membership ballot - informative",
        }
    )
    """
    membership ballot - informative

    Description: Content prepared by a committee and submitted for membership consideration as an informative standard.
    """

    memn = CodeSystemConcept(
        {
            "code": "memn",
            "definition": "Description: Content prepared by a committee and submitted for membership consideration as a normative standard.",
            "display": "membership ballot - normative",
        }
    )
    """
    membership ballot - normative

    Description: Content prepared by a committee and submitted for membership consideration as a normative standard.
    """

    ns = CodeSystemConcept(
        {
            "code": "ns",
            "definition": "Description: Content developed independently by an organization or individual that is declared to be 'usable' but for which there is no present intention to submit through the standards submission and review process.",
            "display": "non-standard - available for use",
        }
    )
    """
    non-standard - available for use

    Description: Content developed independently by an organization or individual that is declared to be 'usable' but for which there is no present intention to submit through the standards submission and review process.
    """

    prop = CodeSystemConcept(
        {
            "code": "prop",
            "definition": "Description: Content submitted to a committee for consideration for future inclusion in the standard.",
            "display": "proposal",
        }
    )
    """
    proposal

    Description: Content submitted to a committee for consideration for future inclusion in the standard.
    """

    ref = CodeSystemConcept(
        {
            "code": "ref",
            "definition": "Description: Content intended to support other content that is subject to approval, but which is not itself subject to formal approval.",
            "display": "reference",
        }
    )
    """
    reference

    Description: Content intended to support other content that is subject to approval, but which is not itself subject to formal approval.
    """

    wd = CodeSystemConcept(
        {
            "code": "wd",
            "definition": "Description: Content that represents an item that was at one point a normative or informative standard, but was subsequently withdrawn.",
            "display": "withdrawn",
        }
    )
    """
    withdrawn

    Description: Content that represents an item that was at one point a normative or informative standard, but was subsequently withdrawn.
    """

    class Meta:
        resource = _resource
