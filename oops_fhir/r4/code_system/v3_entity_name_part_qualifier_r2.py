from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3EntityNamePartQualifierR2"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3EntityNamePartQualifierR2:
    """
    v3 Code System EntityNamePartQualifierR2

      Description:  The qualifier is a set of codes each of which specifies
a certain subcategory of the name part in addition to the main name part
type. For example, a given name may be flagged as a nickname, a family
name may be a pseudonym or a name of public records.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-EntityNamePartQualifierR2
    """

    ad = CodeSystemConcept(
        {
            "code": "AD",
            "concept": [
                {
                    "code": "SP",
                    "definition": "Description:The name assumed from the partner in a marital relationship.  Usually the spouse's family name.  Note that no inference about gender can be made from the existence of spouse names.",
                    "display": "spouse",
                }
            ],
            "definition": "Description:A name part a person acquired.  The name part may be acquired by adoption, or the person may have chosen to use the name part for some other reason.\r\n\n                        \n                           Note: this differs from an Other/Psuedonym/Alias in that an acquired name part is acquired on a formal basis rather than an informal one (e.g. registered as part of the official name).",
            "display": "acquired",
        }
    )
    """
    acquired

    Description:A name part a person acquired.  The name part may be acquired by adoption, or the person may have chosen to use the name part for some other reason.

                        
                           Note: this differs from an Other/Psuedonym/Alias in that an acquired name part is acquired on a formal basis rather than an informal one (e.g. registered as part of the official name).
    """

    br = CodeSystemConcept(
        {
            "code": "BR",
            "definition": 'Description:A name that a person was given at birth or established as a consequence of adoption. \r\n\n                        \n                           Note: This is not used for temporary names assigned at birth such as "Baby of Smith" a" which is just a name with a use code of "TEMP".',
            "display": "birth",
        }
    )
    """
    birth

    Description:A name that a person was given at birth or established as a consequence of adoption. 

                        
                           Note: This is not used for temporary names assigned at birth such as "Baby of Smith" a" which is just a name with a use code of "TEMP".
    """

    cl = CodeSystemConcept(
        {
            "code": "CL",
            "definition": "Description:Used to indicate which of the various name parts is used when interacting with the person.",
            "display": "callme",
        }
    )
    """
    callme

    Description:Used to indicate which of the various name parts is used when interacting with the person.
    """

    in_ = CodeSystemConcept(
        {
            "code": "IN",
            "definition": 'Description:Indicates that a name part is just an initial.  Initials do not imply a trailing period since this would not work with non-Latin scripts.  In some languages, initials may consist of more than one letter, e.g., "Ph" could stand for "Philippe" or "Th" For "Thomas".',
            "display": "initial",
        }
    )
    """
    initial

    Description:Indicates that a name part is just an initial.  Initials do not imply a trailing period since this would not work with non-Latin scripts.  In some languages, initials may consist of more than one letter, e.g., "Ph" could stand for "Philippe" or "Th" For "Thomas".
    """

    ls = CodeSystemConcept(
        {
            "code": "LS",
            "definition": 'Description:For organizations a suffix indicating the legal status, e.g., "Inc.", "Co.", "AG", "GmbH", "B.V." "S.A.", "Ltd." etc.',
            "display": "legal status",
        }
    )
    """
    legal status

    Description:For organizations a suffix indicating the legal status, e.g., "Inc.", "Co.", "AG", "GmbH", "B.V." "S.A.", "Ltd." etc.
    """

    mid = CodeSystemConcept(
        {
            "code": "MID",
            "definition": 'Description:Indicates that the name part is a middle name.\r\n\n                        \n                           Usage Notes: In general, the english "middle name" concept is all of the given names after the first. This qualifier may be used to explicitly indicate which given names are considered to be middle names. The middle name qualifier may also be used with family names. This is a Scandinavian use case, matching the concept of "mellomnavn","mellannamn". Note that there are specific rules that indicate what names may be taken as a mellannamn in different Scandinavian countries.',
            "display": "middle name",
        }
    )
    """
    middle name

    Description:Indicates that the name part is a middle name.

                        
                           Usage Notes: In general, the english "middle name" concept is all of the given names after the first. This qualifier may be used to explicitly indicate which given names are considered to be middle names. The middle name qualifier may also be used with family names. This is a Scandinavian use case, matching the concept of "mellomnavn","mellannamn". Note that there are specific rules that indicate what names may be taken as a mellannamn in different Scandinavian countries.
    """

    pfx = CodeSystemConcept(
        {
            "code": "PFX",
            "definition": "Description:A prefix has a strong association to the immediately following name part. A prefix has no implicit trailing white space (it has implicit leading white space though).",
            "display": "prefix",
        }
    )
    """
    prefix

    Description:A prefix has a strong association to the immediately following name part. A prefix has no implicit trailing white space (it has implicit leading white space though).
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

    sfx = CodeSystemConcept(
        {
            "code": "SFX",
            "definition": "Description:A suffix has a strong association to the immediately preceding name part. A suffix has no implicit leading white space (it has implicit trailing white space though).",
            "display": "suffix",
        }
    )
    """
    suffix

    Description:A suffix has a strong association to the immediately preceding name part. A suffix has no implicit leading white space (it has implicit trailing white space though).
    """

    title_styles = CodeSystemConcept(
        {
            "code": "TitleStyles",
            "concept": [
                {
                    "code": "AC",
                    "definition": 'Description:Indicates that a title like "Dr.", "M.D." or "Ph.D." is an academic title.',
                    "display": "academic",
                },
                {
                    "code": "HON",
                    "definition": 'Description:A honorific such as "The Right Honourable" or "Weledelgeleerde Heer".',
                    "display": "honorific",
                },
                {
                    "code": "NB",
                    "definition": "Description:A nobility title such as Sir, Count, Grafin.",
                    "display": "nobility",
                },
                {
                    "code": "PR",
                    "definition": "Description:Primarily in the British Imperial culture people tend to have an abbreviation of their professional organization as part of their credential titles.",
                    "display": "professional",
                },
            ],
            "definition": "Description:Extra information about the style of a title",
            "display": "TitleStyles",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    TitleStyles

    Description:Extra information about the style of a title
    """

    class Meta:
        resource = _resource
