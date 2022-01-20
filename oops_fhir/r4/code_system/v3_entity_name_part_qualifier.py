from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3EntityNamePartQualifier"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3EntityNamePartQualifier:
    """
    v3 Code System EntityNamePartQualifier

      OpenIssue:  Needs description

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-EntityNamePartQualifier
    """

    underscore_organization_name_part_qualifier = CodeSystemConcept(
        {
            "code": "_OrganizationNamePartQualifier",
            "concept": [
                {
                    "code": "AC",
                    "definition": 'Indicates that a prefix like "Dr." or a suffix like "M.D." or "Ph.D." is an academic title.',
                    "display": "academic",
                },
                {
                    "code": "AD",
                    "definition": "The name the person was given at the time of adoption.",
                    "display": "adopted",
                },
                {
                    "code": "BR",
                    "definition": "A name that a person had shortly after being born. Usually for family names but may be used to mark given names at birth that may have changed later.",
                    "display": "birth",
                },
                {
                    "code": "CL",
                    "definition": "A callme name is (usually a given name) that is preferred when a person is directly addressed.",
                    "display": "callme",
                },
                {
                    "code": "IN",
                    "definition": 'Indicates that a name part is just an initial. Initials do not imply a trailing period since this would not work with non-Latin scripts.  Initials may consist of more than one letter, e.g., "Ph." could stand for "Philippe" or "Th." for "Thomas".',
                    "display": "initial",
                },
                {
                    "code": "LS",
                    "definition": 'For organizations a suffix indicating the legal status, e.g., "Inc.", "Co.", "AG", "GmbH", "B.V." "S.A.",  "Ltd." etc.',
                    "display": "Legal status",
                },
                {
                    "code": "NB",
                    "definition": 'In Europe and Asia, there are still people with nobility titles (aristocrats).  German "von" is generally a nobility title, not a mere voorvoegsel.  Others are "Earl of" or "His Majesty King of..." etc.  Rarely used nowadays, but some systems do keep track of this.',
                    "display": "nobility",
                },
                {
                    "code": "PR",
                    "definition": "Primarily in the British Imperial culture people tend to have an abbreviation of their professional organization as part of their credential suffices.",
                    "display": "professional",
                },
                {
                    "code": "SP",
                    "definition": 'The name assumed from the partner in a marital relationship (hence the "SP"). Usually the spouse\'s family name. Note that no inference about gender can be made from the existence of spouse names.',
                    "display": "spouse",
                },
                {
                    "code": "TITLE",
                    "definition": "Indicates that a prefix or a suffix is a title that applies to the whole name, not just the adjacent name part.",
                    "display": "title",
                },
                {
                    "code": "VV",
                    "definition": 'A Dutch "voorvoegsel" is something like "van" or "de" that might have indicated nobility in the past but no longer so. Similar prefixes exist in other languages such as Spanish, French or Portugese.',
                    "display": "voorvoegsel",
                },
            ],
            "definition": "OrganizationNamePartQualifier",
            "display": "OrganizationNamePartQualifier",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    OrganizationNamePartQualifier

    OrganizationNamePartQualifier
    """

    pharmaceutical_entity_name_part_qualifiers = CodeSystemConcept(
        {
            "code": "PharmaceuticalEntityNamePartQualifiers",
            "concept": [
                {
                    "code": "CON",
                    "definition": "Description: This refers to the container if present in the medicinal product name.\r\n\n                        EXAMPLES: \r\n\n                        \n                           \n                              For Optaflu suspension for injection in pre-filled syringe Influenza vaccine (surface antigen, inactivated, prepared in cell culture) (2007/2008 season): pre-filled syringe",
                    "display": "container name",
                },
                {
                    "code": "DEV",
                    "definition": "Description: This refers to the qualifiers in the name for devices and is at the moment mainly applicable to insulins and inhalation products.\r\n\n                        EXAMPLES: \r\n\n                        \n                           \n                              For the medicinal product Actrapid FlexPen 100 IU/ml Solution for injection Subcutaneous use: FlexPen.",
                    "display": "device name",
                },
                {
                    "code": "FLAV",
                    "definition": "Description: This refers to a flavor of the medicinal product if present in the medicinal product name.\r\n\n                        \n                           Examples:\n                        \r\n\n                        \n                           For 'CoughCure Linctus Orange Flavor', the flavor part is \"Orange\"\n                           For 'Wonderdrug Syrup Cherry Flavor', the flavor part is \"Cherry\"",
                    "display": "FlavorName",
                },
                {
                    "code": "FORMUL",
                    "definition": "Description: This refers to the formulation of the medicinal product if present in the medicinal product name.\r\n\n                        \n                           Examples:\n                        \r\n\n                        \n                           For 'SpecialMed Sugar Free Cough Syrup', the formulation name part is \"Sugar Free\"\n                           For 'QuickCure Gluten-free Bulk Fibre', the formulation name part is \"gluten-free\"",
                    "display": "FormulationPartName",
                },
                {
                    "code": "FRM",
                    "definition": "Description: This refers to the pharmaceutical form/ if present in the medicinal product name.\r\n\n                        EXAMPLES: \r\n\n                        \n                           \n                              For Agenerase 50 mg soft capsules: Soft Capsules\r\n\n                           \n                           \n                              For Ludiomil 25mg-Filmtabletten: Filmtabletten\r\n\n                           \n                           \n                              For Optaflu suspension for injection in pre-filled syringe Influenza vaccine (surface antigen, inactivated, prepared in cell culture) (2007/2008 season): suspension for injection",
                    "display": "form name",
                },
                {
                    "code": "INV",
                    "definition": "Description: This refers to the product name without the trademark or the name of the marketing authorization holder or any other descriptor reflected in the product name and, if appropriate, whether it is intended e.g. for babies, children or adults. \r\n\n                        EXAMPLES: \r\n\n                        \n                           \n                              Agenerase\r\n\n                           \n                           \n                              Optaflu\r\n\n                           \n                           \n                              Ludiomil",
                    "display": "invented name",
                },
                {
                    "code": "POPUL",
                    "definition": "Description: This refers to the target population for the medicinal product if present in the medicinal product name\r\n\n                        \n                           Examples:\n                        \r\n\n                        \n                           For 'Broncho-Drug 3.5 mg-capsules for children', the target population part is \"children\"\n                           For 'Adult Chesty Cough Syrup', the target population part is \"adult\"",
                    "display": "TargetPopulationName",
                },
                {
                    "code": "SCI",
                    "definition": "Description: This refers to the product common or scientific name without the trademark or the name of the marketing authorization holder or any other descriptor reflected in the product name.\r\n\n                        EXAMPLES: \r\n\n                        \n                           \n                              For Agenerase: N/A\r\n\n                           \n                           \n                              For Optaflu: Influenza vaccine (surface antigen, inactivated, prepared in cell culture) (2007/2008 season)\r\n\n                           \n                           \n                              For Ludiomil: N/A",
                    "display": "scientific name",
                },
                {
                    "code": "STR",
                    "definition": "Description: This refers to the strength if present in the medicinal product name. The use of decimal points should be accommodated if required.\r\n\n                        EXAMPLES:\r\n\n                        \n                           \n                              For Agenerase 50 mg soft capsules: 50mg\r\n\n                           \n                           \n                              For Ludiomil 25mg-Filmtabletten: 25 mg\r\n\n                           \n                           \n                              For Optaflu suspension for injection in pre-filled syringe Influenza vaccine (surface antigen, inactivated, prepared in cell culture) (2007/2008 season): N/A",
                    "display": "strength name",
                },
                {
                    "code": "TIME",
                    "definition": "Description: This refers to a time or time period that may be specified in the text of the medicinal product name\r\n\n                        \n                           Example:\n                        \r\n\n                        \n                           For an influenza vaccine 'Drug-FLU season 2008/2009', the time/period part is \"2008/2009 season\"",
                    "display": "TimeOrPeriodName",
                },
                {
                    "code": "TMK",
                    "definition": "Description: This refers to trademark/company element if present in the medicinal product name.\r\n\n                        EXAMPLES: \r\n\n                        \n                           \n                              for Insulin Human Winthrop Comb 15: Winthrop",
                    "display": "trademark name",
                },
                {
                    "code": "USE",
                    "definition": "Description: This refers to the intended use if present in the medicinal product name without the trademark or the name of the marketing authorization holder or any other descriptor reflected in the product name.\n\r\n\n                        \n                           Examples:\n                        \r\n\n                        \n                           For 'Drug-BI Caplets - Heartburn Relief', the intended use part is: \"Heartburn Relief\"\n                           For 'Medicine Honey Syrup for Soothing Coughs' the intended use part is \"Soothing Coughs\"",
                    "display": "intended use name",
                },
            ],
            "definition": 'Description: Medication Name Parts are a means of specifying a range of acceptable "official" forms of the name of a product.  They are used as patterns against which input name strings may be matched for automatic identification of products from input text reports.   While they cover the concepts held under "doseForm" or "route" or "strength" the name parts are not the same and do not fit into a controlled vocabulary in the same way. By specifying up to 8 name parts a much larger range of possible names can be generated.',
            "display": "PharmaceuticalEntityNamePartQualifiers",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    PharmaceuticalEntityNamePartQualifiers

    Description: Medication Name Parts are a means of specifying a range of acceptable "official" forms of the name of a product.  They are used as patterns against which input name strings may be matched for automatic identification of products from input text reports.   While they cover the concepts held under "doseForm" or "route" or "strength" the name parts are not the same and do not fit into a controlled vocabulary in the same way. By specifying up to 8 name parts a much larger range of possible names can be generated.
    """

    underscore_person_name_part_qualifier = CodeSystemConcept(
        {
            "code": "_PersonNamePartQualifier",
            "concept": [
                {
                    "code": "_PersonNamePartAffixTypes",
                    "definition": "PersonNamePartAffixTypes",
                    "display": "PersonNamePartAffixTypes",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "status", "valueCode": "retired"},
                        {"code": "child", "valueCode": "AC"},
                        {"code": "child", "valueCode": "NB"},
                        {"code": "child", "valueCode": "PR"},
                        {"code": "child", "valueCode": "VV"},
                    ],
                },
                {
                    "code": "_PersonNamePartChangeQualifier",
                    "definition": "PersonNamePartChangeQualifier",
                    "display": "PersonNamePartChangeQualifier",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "status", "valueCode": "retired"},
                        {"code": "child", "valueCode": "AD"},
                        {"code": "child", "valueCode": "BR"},
                        {"code": "child", "valueCode": "SP"},
                    ],
                },
                {
                    "code": "_PersonNamePartMiscQualifier",
                    "definition": "PersonNamePartMiscQualifier",
                    "display": "PersonNamePartMiscQualifier",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "status", "valueCode": "retired"},
                        {"code": "child", "valueCode": "CL"},
                    ],
                },
            ],
            "definition": "PersonNamePartQualifier",
            "display": "PersonNamePartQualifier",
            "property": [
                {"code": "notSelectable", "valueBoolean": True},
                {"code": "status", "valueCode": "retired"},
                {"code": "child", "valueCode": "IN"},
                {"code": "child", "valueCode": "TITLE"},
            ],
        }
    )
    """
    PersonNamePartQualifier

    PersonNamePartQualifier
    """

    class Meta:
        resource = _resource
