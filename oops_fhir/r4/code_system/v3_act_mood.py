from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3ActMood"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3ActMood:
    """
    v3 Code System ActMood

     OpenIssue:  In Ballot 2009May, a strong Negative vote was lodged
against several of the concept definitions in the vocabulary used for
Act.moodCode. The vote was found "Persuasive With Mod", with the
understanding that M and M would undertake a detailed review of these
concept definitions for a future release of the RIM.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-ActMood
    """

    underscore_act_mood_completion_track = CodeSystemConcept(
        {
            "code": "_ActMoodCompletionTrack",
            "concept": [
                {
                    "code": "_ActMoodPotential",
                    "concept": [
                        {
                            "code": "DEF",
                            "definition": 'Definition: A definition of a kind of act that can occur .\r\n\n                        \n                           OpenIssue: The semantic constructs embodied in DEF and CRT moods seem indistinguishable, and their uses can readily be determined by the context in which these are used. Therefore, this OpenIssue has been created to declare that it is likely that ActMood.DEF will be "retired" in the future in favor of the more general ActMood.CRT.',
                            "display": "definition",
                        },
                        {
                            "code": "PERM",
                            "definition": "Definition: A kind of act that defines a permission that has been granted.",
                            "display": "permission",
                        },
                        {
                            "code": "SLOT",
                            "definition": "Definition: A kind of act that may occur during the specified time period.",
                            "display": "resource slot",
                        },
                    ],
                    "definition": "Definition: A possible act.",
                    "display": "potential",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "EVN",
                    "definition": "Definition: An act that actually happens (may be an ongoing act or a documentation of a past act).",
                    "display": "event (occurrence)",
                },
                {
                    "code": "INT",
                    "concept": [
                        {
                            "code": "_ActMoodDesire",
                            "concept": [
                                {
                                    "code": "_ActMoodActRequest",
                                    "concept": [
                                        {
                                            "code": "ARQ",
                                            "definition": "Definition: A request act that is specialized for the appointment scheduling request/fulfillment cycle. An appointment request is fulfilled only and completely by an appointment (APT), i.e., all that the appointment request intends is to create an appointment (the actual act may well not happen if that is the professional decision during the appointment).",
                                            "display": "appointment request",
                                        },
                                        {
                                            "code": "PERMRQ",
                                            "definition": "Definition: A request for a permission to perform the act. Typically a payer (or possibly a supervisor) is being requested to give permission to perform the act. As opposed to the RQO, the requestee is not asked to perform or cause to perform the act but only to give the permission.",
                                            "display": "permission request",
                                        },
                                        {
                                            "code": "RQO",
                                            "definition": 'Definition: A request act that is specialized for an event request/fulfillment cycle. \r\n\n                        \n                           UsageNotes: The fulfillment cycle may involve intermediary fulfilling acts in moods such as PRMS, APT, or even another RQO before being fulfilled by the final event. \r\n\n                        \n                           UsageNotes: The concepts of a "request" and an "order" are viewed as different, because there is an implication of a mandate associated with order.  In practice, however, this distinction has no general functional value in the inter-operation of health care computing.  "Orders" are commonly refused for a variety of clinical and business reasons, and the notion of a "request" obligates the recipient (the fulfiller) to respond to the sender (the author).  Indeed, in many regions, including Australia and Europe, the common term used is "request."\r\n\n                        Thus, the concept embodies both notions, as there is no useful distinction to be made.  If a mandate is to be associated with a request, this will be embodied in the "local" business rules applied to the transactions.  Should HL7 desire to provide a distinction between these in the future, the individual concepts could be added as specializations of this concept.\r\n\n                        The critical distinction here, is the difference between this concept and an "intent", of which it is a specialization.  An intent involves decisions by a single party, the author.  A request, however, involves decisions by two parties, the author and the fulfiller, with an obligation on the part of the fulfiller to respond to the request indicating that the fulfiller will indeed fulfill the request.',
                                            "display": "request",
                                        },
                                    ],
                                    "definition": "Definition: A request (or order) for an act that is part of a defined request/fulfillment cycle.\r\n\n                        \n                           UsageNotes: Use of an HL7 defined request/fulfillment framework is not required to use this mood code.",
                                    "display": "act request",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                                {
                                    "code": "PRP",
                                    "concept": [
                                        {
                                            "code": "RMD",
                                            "definition": 'Definition: A suggestion that an act should be performed with an acceptance of some degree of professional responsibility for the resulting act. Not an explicit request. .\r\n\n                        \n                           UsageNotes: Where there is no clear definition or applicable concept of "professional responsibilityâ€?, RMD becomes indistinguishable from PRP. .',
                                            "display": "recommendation",
                                        }
                                    ],
                                    "definition": "Definition: A suggestion that an act might be performed. Not an explicit request, and professional responsibility may or may not be present.",
                                    "display": "proposal",
                                },
                            ],
                            "definition": "Definition:  A desire to have an act occur.",
                            "display": "desire",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "PRMS",
                            "concept": [
                                {
                                    "code": "APT",
                                    "definition": "Definition: An act that has been scheduled to be performed at a specific place and time.",
                                    "display": "appointment",
                                }
                            ],
                            "definition": "Definition: A commitment to perform an act (may be either solicited or unsolicited). The committer becomes responsible to the other party for executing the act, and, as a consequence, the other party may rely on the first party to perform or cause to perform the act.\r\n\n                        \n                           UsageNotes: Commitments may be retracted or cancelled.",
                            "display": "promise",
                        },
                    ],
                    "definition": "Definition: An intention or plan for an act. \r\n\n                        \n                           >UsageNotes: The final outcome of the intent, the act that is intended to occur, is always an event. However the final outcome may be reached indirectly via steps through other intents, such as promise, permission request, or an appointment that may lead to an actual event to occur. Alternatively, the intended act may never occur.",
                    "display": "intent",
                },
            ],
            "definition": "These are moods describing activities as they progress in the business cycle, from defined, through planned and ordered to completed.",
            "display": "ActMoodCompletionTrack",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActMoodCompletionTrack

    These are moods describing activities as they progress in the business cycle, from defined, through planned and ordered to completed.
    """

    underscore_act_mood_predicate = CodeSystemConcept(
        {
            "code": "_ActMoodPredicate",
            "concept": [
                {
                    "code": "CRT",
                    "concept": [
                        {
                            "code": "EVN.CRT",
                            "definition": 'Deprecation Comment: \n                           This concept This codes should no longer be used.  Instead, set attribute Act.isCriterionInd to "true" and use the desired mood for your criterion.\r\n\n                        \n                           Definition: A criterion (CRT) that has_match = an event (EVN).',
                            "display": "event criterion",
                            "property": [
                                {"code": "status", "valueCode": "deprecated"},
                                {
                                    "code": "deprecationDate",
                                    "valueDateTime": "2010-07-12",
                                },
                            ],
                        },
                        {
                            "code": "GOL.CRT",
                            "definition": "A criterion expressed over goals (ActMood.GOL).",
                            "display": "goal criterion",
                            "property": [{"code": "status", "valueCode": "retired"}],
                        },
                        {
                            "code": "INT.CRT",
                            "concept": [
                                {
                                    "code": "PRMS.CRT",
                                    "definition": "A criterion expressed over promises (ActMood.PRMS).",
                                    "display": "promise criterion",
                                    "property": [
                                        {"code": "status", "valueCode": "retired"}
                                    ],
                                },
                                {
                                    "code": "RQO.CRT",
                                    "definition": "A criterion expressed over requests or orders (ActMood.RQO).",
                                    "display": "request criterion",
                                    "property": [
                                        {"code": "status", "valueCode": "retired"}
                                    ],
                                },
                            ],
                            "definition": "A criterion expressed over intents (ActMood.INT).",
                            "display": "intent criterion",
                            "property": [{"code": "status", "valueCode": "retired"}],
                        },
                        {
                            "code": "RSK.CRT",
                            "definition": "A criterion expressed over risks (ActMood.RSK).",
                            "display": "risk criterion",
                            "property": [{"code": "status", "valueCode": "retired"}],
                        },
                    ],
                    "definition": 'Deprecation Comment: \n                           This concept This codes should no longer be used.  Instead, set attribute Act.isCriterionInd to "true" and use the desired mood for your criterion.\r\n\n                        \n                           Definition: A condition that must be true for the source act to be considered.',
                    "display": "criterion",
                    "property": [
                        {"code": "status", "valueCode": "deprecated"},
                        {"code": "deprecationDate", "valueDateTime": "2010-07-12"},
                    ],
                },
                {
                    "code": "EXPEC",
                    "concept": [
                        {
                            "code": "GOL",
                            "definition": 'Definition: An expectation that is considered to be desirable to occur in the future \r\n\n                        \n                           Examples:Target weight below 80Kg, Stop smoking, Regain ability to walk, goal is to administer thrombolytics to candidate patients presenting with acute myocardial infarction.\r\n\n                        \n                           UsageNotes: INT (intent) reflects a plan for the future, which is a declaration to do something.  This contrasts with goal which doesn\'t represent an intention to act, merely a hope for an eventual result.  A goal is distinct from the intended actions to reach that goal.  "I will reduce the dose of drug x to 20mg" is an intent.  "I hope to be able to get the patient to the point where I can reduce the dose of drug x to 20mg" is a goal. EXPEC (expectation) reflects a prediction rather than a hope. RSK (risk) reflects a potential negative event rather than a hope.',
                            "display": "Goal",
                        },
                        {
                            "code": "RSK",
                            "definition": "Definition:An act that may occur in the future and which is regarded as undesirable \r\n\n                        \n                           Examples:Increased risk of DVT, at risk for sub-acute bacterial endocarditis.\r\n\n                        \n                           UsageNotes:Note: An observation in RSK mood expresses the undesirable act, and not the underlying risk factor. A risk factor that is present (e.g. obesity, smoking, etc) should be expressed in event mood. INT (intent) reflects a plan for the future, which is a declaration to do something. This contrasts with RSK (risk), which is the potential that something negative will occur that may or may not ever happen. GOL (goal) reflects a hope to achieve something. EXPEC (expectation) is the prediction of a positive or negative event. This contrasts with RSK (risk), which is the potential that something negative will occur that may or may not ever happen, and may not be expected to happen.",
                            "display": "risk",
                        },
                    ],
                    "definition": "Definition: An act that is considered to have some noteworthy likelihood of occurring in the future (has_match = event).\r\n\n                        \n                           Examples:Prognosis of a condition, Expected date of discharge from hospital, patient will likely need an emergency decompression of the intracranial pressure by morning.\r\n\n                        \n                           UsageNotes:INT (intent) reflects a plan for the future, which is a declaration to do something. This contrasts with expectation, which is a prediction that something will happen in the future. GOL (goal) reflects a hope rather than a prediction. RSK (risk) reflects a potential negative event that may or may not be expected to happen.",
                    "display": "expectation",
                },
                {
                    "code": "OPT",
                    "definition": "Definition: One of a set of acts that specify an option for the property values that the parent act may have. Typically used in definitions or orders to describe alternatives. An option can only be used as a group, that is, all assigned values must be used together. The actual mood of the act is the same as the parent act, and they must be linked by an actrelationship with type = OPTN.",
                    "display": "option",
                },
            ],
            "definition": "Definition: An act that expresses condition statements for other acts.",
            "display": "ActMoodPredicate",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActMoodPredicate

    Definition: An act that expresses condition statements for other acts.
    """

    class Meta:
        resource = _resource
