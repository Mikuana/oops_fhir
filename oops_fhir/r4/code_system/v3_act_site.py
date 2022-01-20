from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3ActSite"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3ActSite:
    """
    v3 Code System ActSite

     An anatomical location on an organism which can be the focus of an act.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-ActSite
    """

    underscore_human_act_site = CodeSystemConcept(
        {
            "code": "_HumanActSite",
            "concept": [
                {
                    "code": "_HumanSubstanceAdministrationSite",
                    "concept": [
                        {
                            "code": "BE",
                            "definition": "bilateral ears",
                            "display": "bilateral ears",
                        },
                        {
                            "code": "BN",
                            "definition": "bilateral nares",
                            "display": "bilateral nares",
                        },
                        {"code": "BU", "definition": "buttock", "display": "buttock"},
                        {"code": "LA", "definition": "left arm", "display": "left arm"},
                        {
                            "code": "LAC",
                            "definition": "left anterior chest",
                            "display": "left anterior chest",
                        },
                        {
                            "code": "LACF",
                            "definition": "left antecubital fossa",
                            "display": "left antecubital fossa",
                        },
                        {
                            "code": "LD",
                            "definition": "left deltoid",
                            "display": "left deltoid",
                        },
                        {"code": "LE", "definition": "left ear", "display": "left ear"},
                        {
                            "code": "LEJ",
                            "definition": "left external jugular",
                            "display": "left external jugular",
                        },
                        {
                            "code": "LF",
                            "definition": "left foot",
                            "display": "left foot",
                        },
                        {
                            "code": "LG",
                            "definition": "left gluteus medius",
                            "display": "left gluteus medius",
                        },
                        {
                            "code": "LH",
                            "definition": "left hand",
                            "display": "left hand",
                        },
                        {
                            "code": "LIJ",
                            "definition": "left internal jugular",
                            "display": "left internal jugular",
                        },
                        {
                            "code": "LLAQ",
                            "definition": "left lower abd quadrant",
                            "display": "left lower abd quadrant",
                        },
                        {
                            "code": "LLFA",
                            "definition": "left lower forearm",
                            "display": "left lower forearm",
                        },
                        {
                            "code": "LMFA",
                            "definition": "left mid forearm",
                            "display": "left mid forearm",
                        },
                        {
                            "code": "LN",
                            "definition": "left naris",
                            "display": "left naris",
                        },
                        {
                            "code": "LPC",
                            "definition": "left posterior chest",
                            "display": "left posterior chest",
                        },
                        {
                            "code": "LSC",
                            "definition": "left subclavian",
                            "display": "left subclavian",
                        },
                        {
                            "code": "LT",
                            "definition": "left thigh",
                            "display": "left thigh",
                        },
                        {
                            "code": "LUA",
                            "definition": "left upper arm",
                            "display": "left upper arm",
                        },
                        {
                            "code": "LUAQ",
                            "definition": "left upper abd quadrant",
                            "display": "left upper abd quadrant",
                        },
                        {
                            "code": "LUFA",
                            "definition": "left upper forearm",
                            "display": "left upper forearm",
                        },
                        {
                            "code": "LVG",
                            "definition": "left ventragluteal",
                            "display": "left ventragluteal",
                        },
                        {
                            "code": "LVL",
                            "definition": "left vastus lateralis",
                            "display": "left vastus lateralis",
                        },
                        {
                            "code": "OD",
                            "definition": "right eye",
                            "display": "right eye",
                        },
                        {"code": "OS", "definition": "left eye", "display": "left eye"},
                        {
                            "code": "OU",
                            "definition": "bilateral eyes",
                            "display": "bilateral eyes",
                        },
                        {"code": "PA", "definition": "perianal", "display": "perianal"},
                        {
                            "code": "PERIN",
                            "definition": "perineal",
                            "display": "perineal",
                        },
                        {
                            "code": "RA",
                            "definition": "right arm",
                            "display": "right arm",
                        },
                        {
                            "code": "RAC",
                            "definition": "right anterior chest",
                            "display": "right anterior chest",
                        },
                        {
                            "code": "RACF",
                            "definition": "right antecubital fossa",
                            "display": "right antecubital fossa",
                        },
                        {
                            "code": "RD",
                            "definition": "right deltoid",
                            "display": "right deltoid",
                        },
                        {
                            "code": "RE",
                            "definition": "right ear",
                            "display": "right ear",
                        },
                        {
                            "code": "REJ",
                            "definition": "right external jugular",
                            "display": "right external jugular",
                        },
                        {
                            "code": "RF",
                            "definition": "right foot",
                            "display": "right foot",
                        },
                        {
                            "code": "RG",
                            "definition": "right gluteus medius",
                            "display": "right gluteus medius",
                        },
                        {
                            "code": "RH",
                            "definition": "right hand",
                            "display": "right hand",
                        },
                        {
                            "code": "RIJ",
                            "definition": "right internal jugular",
                            "display": "right internal jugular",
                        },
                        {
                            "code": "RLAQ",
                            "definition": "right lower abd quadrant",
                            "display": "right lower abd quadrant",
                        },
                        {
                            "code": "RLFA",
                            "definition": "right lower forearm",
                            "display": "right lower forearm",
                        },
                        {
                            "code": "RMFA",
                            "definition": "right mid forearm",
                            "display": "right mid forearm",
                        },
                        {
                            "code": "RN",
                            "definition": "right naris",
                            "display": "right naris",
                        },
                        {
                            "code": "RPC",
                            "definition": "right posterior chest",
                            "display": "right posterior chest",
                        },
                        {
                            "code": "RSC",
                            "definition": "right subclavian",
                            "display": "right subclavian",
                        },
                        {
                            "code": "RT",
                            "definition": "right thigh",
                            "display": "right thigh",
                        },
                        {
                            "code": "RUA",
                            "definition": "right upper arm",
                            "display": "right upper arm",
                        },
                        {
                            "code": "RUAQ",
                            "definition": "right upper abd quadrant",
                            "display": "right upper abd quadrant",
                        },
                        {
                            "code": "RUFA",
                            "definition": "right upper forearm",
                            "display": "right upper forearm",
                        },
                        {
                            "code": "RVG",
                            "definition": "right ventragluteal",
                            "display": "right ventragluteal",
                        },
                        {
                            "code": "RVL",
                            "definition": "right vastus lateralis",
                            "display": "right vastus lateralis",
                        },
                    ],
                    "definition": "The set of body locations to or through which a drug product may be administered.",
                    "display": "HumanSubstanceAdministrationSite",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                }
            ],
            "definition": "An anatomical location on a human which can be the focus of an act.",
            "display": "HumanActSite",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    HumanActSite

    An anatomical location on a human which can be the focus of an act.
    """

    class Meta:
        resource = _resource
