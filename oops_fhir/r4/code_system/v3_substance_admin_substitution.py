from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3substanceAdminSubstitution"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3substanceAdminSubstitution:
    """
    v3 Code System substanceAdminSubstitution

     Identifies what sort of change is permitted or has occurred between the
therapy that was ordered and the therapy that was/will be provided.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-substanceAdminSubstitution
    """

    underscore_act_substance_admin_substitution_code = CodeSystemConcept(
        {
            "code": "_ActSubstanceAdminSubstitutionCode",
            "concept": [
                {
                    "code": "E",
                    "concept": [
                        {
                            "code": "EC",
                            "concept": [
                                {
                                    "code": "BC",
                                    "definition": "Description: \n                        \r\n\n                        Substitution occurred or is permitted between equivalent Brands but not Generics\r\n\n                        \n                           Examples: \n                        \r\n\n                        \n                           Zestril  for Prinivil\n                           Coumadin for Jantoven",
                                    "display": "brand composition",
                                },
                                {
                                    "code": "G",
                                    "definition": "Description: Substitution occurred or is permitted between equivalent Generics but not Brands\r\n\n                        \n                           Examples: \n                        \r\n\n                        \n                           Lisnopril (Lupin Corp) for Lisnopril (Wockhardt Corp)",
                                    "display": "generic composition",
                                },
                            ],
                            "definition": "Description: \n                        \r\n\n                        Substitution occurred or is permitted with another product that is a:\r\n\n                        \n                           pharmaceutical alternative containing the same active ingredient but is formulated with different salt, ester\n                           pharmaceutical equivalent that has the same active ingredient, strength, dosage form and route of administration\n                        \n                        \n                           Examples: \n                        \r\n\n                        \n                           \n                              Pharmaceutical alternative: Erythromycin Ethylsuccinate for Erythromycin Stearate\n                           \n                              Pharmaceutical equivalent: Lisonpril for Zestril",
                            "display": "equivalent composition",
                        },
                        {
                            "code": "TE",
                            "concept": [
                                {
                                    "code": "TB",
                                    "definition": "Description: Substitution occurred or is permitted between therapeutically equivalent Brands but not Generics\r\n>\n                           Examples: \n                        \r\n\n                        \n                           Zantac for Tagamet",
                                    "display": "therapeutic brand",
                                },
                                {
                                    "code": "TG",
                                    "definition": "Description: Substitution occurred or is permitted between therapeutically equivalent Generics but not Brands\r\n>\n                           Examples: \n                        \r\n\n                        \n                           Ranitidine  for cimetidine",
                                    "display": "therapeutic generic",
                                },
                            ],
                            "definition": "Description: Substitution occurred or is permitted with another product having the same therapeutic objective and safety profile.\r\n\n                        \n                           Examples: \n                        \r\n\n                        \n                           ranitidine for Tagamet",
                            "display": "therapeutic alternative",
                        },
                    ],
                    "definition": "Description: Substitution occurred or is permitted with another bioequivalent and therapeutically equivalent product.",
                    "display": "equivalent",
                },
                {
                    "code": "F",
                    "definition": "Description: This substitution was performed or is permitted based on formulary guidelines.",
                    "display": "formulary",
                },
                {
                    "code": "N",
                    "definition": "No substitution occurred or is permitted.",
                    "display": "none",
                },
            ],
            "definition": "Description: Substitution occurred or is permitted with another product that may potentially have different ingredients, but having the same biological and therapeutic effects.",
            "display": "ActSubstanceAdminSubstitutionCode",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ActSubstanceAdminSubstitutionCode

    Description: Substitution occurred or is permitted with another product that may potentially have different ingredients, but having the same biological and therapeutic effects.
    """

    class Meta:
        resource = _resource
