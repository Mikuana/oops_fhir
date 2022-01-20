from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3hl7VoteResolution"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3hl7VoteResolution:
    """
    v3 Code System hl7VoteResolution

      Description:  Based on concepts for resolutions from HL7 ballot
spreadsheet according to HL7's Governance & Operations Manual (GOM).

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-hl7VoteResolution
    """

    affirmative_resolution = CodeSystemConcept(
        {
            "code": "affirmativeResolution",
            "concept": [
                {
                    "code": "affdef",
                    "definition": "Description: The recommended change has been deferred to consideration for a future release.",
                    "display": "affirmative-deferred",
                },
                {
                    "code": "affi",
                    "definition": "Description: The recommended change has been incorporated or identified issue has been answered.",
                    "display": "affirmative-incorporated",
                },
                {
                    "code": "affr",
                    "definition": "Description: The recommended change has been refused and is not expected to be incorporated.",
                    "display": "affirmative-rejected",
                },
            ],
            "definition": "Description: An abstract concept grouping resolutions that can be applied to affirmative ballot comments.",
            "display": "affirmative resolution",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    affirmative resolution

    Description: An abstract concept grouping resolutions that can be applied to affirmative ballot comments.
    """

    negative_resolution = CodeSystemConcept(
        {
            "code": "negativeResolution",
            "concept": [
                {
                    "code": "nonsubp",
                    "definition": "Description: Responsible group has recommended that the negative vote be considered non-substantive.  (Issue raised does not provide sufficiently convincing reason to make changes to the item under ballot, or otherwise impede its adoption.)",
                    "display": "non-substantive proposed",
                },
                {
                    "code": "nonsubv",
                    "definition": "Description: Ballot group has voted and declared the negative vote non-substantive.",
                    "display": "non-substantive voted",
                },
                {
                    "code": "notrelp",
                    "definition": "Description: Responsible group has recommended that the negative vote be considered not-related.  (Issue raised is not related to the current scope of the item under ballot, or does not prevent the item under ballot for being used for its defined intent.  Recommended changes may be considered as part of future versions.)  (Perhaps after further reading or explanation).",
                    "display": "not related proposed",
                },
                {
                    "code": "notrelv",
                    "definition": "Description: Ballot group has voted and declared the negative vote non-related.",
                    "display": "not related voted",
                },
                {
                    "code": "prevcons",
                    "definition": "Description: Committee identifies that the same issue has been raised as part of a previous ballot on the same element version and was found by the ballot group to be non-substantive or not related.)",
                    "display": "previously considered",
                },
                {
                    "code": "retract",
                    "definition": "Description: Voter has formally withdrawn their vote or comment as having been in error.  (Perhaps after further reading or explanation).",
                    "display": "retracted",
                },
                {
                    "code": "unresolved",
                    "definition": "Description: Vote has not yet gone through resolution.",
                    "display": "unresolved",
                },
                {
                    "code": "withdraw",
                    "definition": "Description: Voter has formally withdrawn their vote or comment on the basis of agreed changes or proposed future changes.",
                    "display": "withdrawn",
                },
            ],
            "definition": "Description: An abstract concept grouping resolutions that can be applied to negative ballot comments.",
            "display": "negative resolution",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    negative resolution

    Description: An abstract concept grouping resolutions that can be applied to negative ballot comments.
    """

    class Meta:
        resource = _resource
