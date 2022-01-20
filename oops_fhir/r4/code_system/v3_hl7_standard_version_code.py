from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3HL7StandardVersionCode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3HL7StandardVersionCode:
    """
    v3 Code System HL7StandardVersionCode

     This code system holds version codes for the Version 3 standards.
Values are to be determined by HL7 and added with each new version of
the HL7 Standard.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-HL7StandardVersionCode
    """

    ballot2008_jan = CodeSystemConcept(
        {
            "code": "Ballot2008Jan",
            "definition": "The complete set of normative, DSTU, proposed (under ballot) and draft artifacts as published in the ballot whose ballot cycle ended in January 2008.",
            "display": "Ballot 2008 January",
        }
    )
    """
    Ballot 2008 January

    The complete set of normative, DSTU, proposed (under ballot) and draft artifacts as published in the ballot whose ballot cycle ended in January 2008.
    """

    ballot2008_may = CodeSystemConcept(
        {
            "code": "Ballot2008May",
            "definition": "The complete set of normative, DSTU, proposed (under ballot) and draft artifacts as published in the ballot whose ballot cycle ended in May 2008.",
            "display": "Ballot 2008 May",
        }
    )
    """
    Ballot 2008 May

    The complete set of normative, DSTU, proposed (under ballot) and draft artifacts as published in the ballot whose ballot cycle ended in May 2008.
    """

    ballot2008_sep = CodeSystemConcept(
        {
            "code": "Ballot2008Sep",
            "definition": "The complete set of normative, DSTU, proposed (under ballot) and draft artifacts as published in the ballot whose ballot cycle ended in September 2008.",
            "display": "Ballot 2008 September",
        }
    )
    """
    Ballot 2008 September

    The complete set of normative, DSTU, proposed (under ballot) and draft artifacts as published in the ballot whose ballot cycle ended in September 2008.
    """

    ballot2009_jan = CodeSystemConcept(
        {
            "code": "Ballot2009Jan",
            "definition": "The complete set of normative, DSTU, proposed (under ballot) and draft artifacts as published in the ballot whose ballot cycle ended in January 2009.",
            "display": "Ballot 2009 January",
        }
    )
    """
    Ballot 2009 January

    The complete set of normative, DSTU, proposed (under ballot) and draft artifacts as published in the ballot whose ballot cycle ended in January 2009.
    """

    ballot2009_may = CodeSystemConcept(
        {
            "code": "Ballot2009May",
            "definition": "The complete set of normative, DSTU, proposed (under ballot) and draft artifacts as published in the ballot whose ballot cycle ended in May 2009.",
            "display": "Ballot 2009 May",
        }
    )
    """
    Ballot 2009 May

    The complete set of normative, DSTU, proposed (under ballot) and draft artifacts as published in the ballot whose ballot cycle ended in May 2009.
    """

    ballot2009_sep = CodeSystemConcept(
        {
            "code": "Ballot2009Sep",
            "definition": "The complete set of normative, DSTU, proposed (under ballot) and draft artifacts as published in the ballot whose ballot cycle ended in September 2009.",
            "display": "Ballot 2009 September",
        }
    )
    """
    Ballot 2009 September

    The complete set of normative, DSTU, proposed (under ballot) and draft artifacts as published in the ballot whose ballot cycle ended in September 2009.
    """

    ballot2010_jan = CodeSystemConcept(
        {
            "code": "Ballot2010Jan",
            "definition": "Definition: The complete set of normative, DSTU, proposed (under ballot) and draft artifacts as published in the ballot whose ballot cycle ended in January 2010.",
            "display": "Ballot 2010 Jan",
        }
    )
    """
    Ballot 2010 Jan

    Definition: The complete set of normative, DSTU, proposed (under ballot) and draft artifacts as published in the ballot whose ballot cycle ended in January 2010.
    """

    ballot2010_may = CodeSystemConcept(
        {
            "code": "Ballot2010May",
            "definition": "Definition: The complete set of normative, DSTU, proposed (under ballot) and draft artifacts as published in the ballot whose ballot cycle ended in May 2010.",
            "display": "Ballot 2010 May",
        }
    )
    """
    Ballot 2010 May

    Definition: The complete set of normative, DSTU, proposed (under ballot) and draft artifacts as published in the ballot whose ballot cycle ended in May 2010.
    """

    ballot2010_sep = CodeSystemConcept(
        {
            "code": "Ballot2010Sep",
            "definition": "Definition: The complete set of normative, DSTU, proposed (under ballot) and draft artifacts as published in the ballot whose ballot cycle ended in September 2010.",
            "display": "Ballot 2010 Sep",
        }
    )
    """
    Ballot 2010 Sep

    Definition: The complete set of normative, DSTU, proposed (under ballot) and draft artifacts as published in the ballot whose ballot cycle ended in September 2010.
    """

    ballot2011_jan = CodeSystemConcept(
        {
            "code": "Ballot2011Jan",
            "definition": "Definition: The complete set of normative, DSTU, proposed (under ballot) and draft artifacts as published in the ballot whose ballot cycle ended in January 2011.",
            "display": "Ballot 2011 Jan",
        }
    )
    """
    Ballot 2011 Jan

    Definition: The complete set of normative, DSTU, proposed (under ballot) and draft artifacts as published in the ballot whose ballot cycle ended in January 2011.
    """

    ballot2011_may = CodeSystemConcept(
        {
            "code": "Ballot2011May",
            "definition": "Definition: The complete set of normative, DSTU, proposed (under ballot) and draft artifacts as published in the ballot whose ballot cycle ended in May 2011.",
            "display": "Ballot 2011 May",
        }
    )
    """
    Ballot 2011 May

    Definition: The complete set of normative, DSTU, proposed (under ballot) and draft artifacts as published in the ballot whose ballot cycle ended in May 2011.
    """

    ballot2011_sep = CodeSystemConcept(
        {
            "code": "Ballot2011Sep",
            "definition": "Definition: The complete set of normative, DSTU, proposed (under ballot) and draft artifacts as published in the ballot whose ballot cycle ended in September 2011.",
            "display": "Ballot 2011 Sep",
        }
    )
    """
    Ballot 2011 Sep

    Definition: The complete set of normative, DSTU, proposed (under ballot) and draft artifacts as published in the ballot whose ballot cycle ended in September 2011.
    """

    ballot2012_jan = CodeSystemConcept(
        {
            "code": "Ballot2012Jan",
            "definition": "Definition: The complete set of normative, DSTU, proposed (under ballot) and draft artifacts as published in the ballot whose ballot cycle ended in January 2012.",
            "display": "Ballot 2012 Jan",
        }
    )
    """
    Ballot 2012 Jan

    Definition: The complete set of normative, DSTU, proposed (under ballot) and draft artifacts as published in the ballot whose ballot cycle ended in January 2012.
    """

    ballot2012_may = CodeSystemConcept(
        {
            "code": "Ballot2012May",
            "definition": "Definition: The complete set of normative, DSTU, proposed (under ballot) and draft artifacts as published in the ballot whose ballot cycle ended in May 2012.",
            "display": "Ballot 2012 May",
        }
    )
    """
    Ballot 2012 May

    Definition: The complete set of normative, DSTU, proposed (under ballot) and draft artifacts as published in the ballot whose ballot cycle ended in May 2012.
    """

    ballot2012_sep = CodeSystemConcept(
        {
            "code": "Ballot2012Sep",
            "definition": "Definition: The complete set of normative, DSTU, proposed (under ballot) and draft artifacts as published in the ballot whose ballot cycle ended in September 2012.",
            "display": "Ballot 2012 Sep",
        }
    )
    """
    Ballot 2012 Sep

    Definition: The complete set of normative, DSTU, proposed (under ballot) and draft artifacts as published in the ballot whose ballot cycle ended in September 2012.
    """

    v3_2003_12 = CodeSystemConcept(
        {
            "code": "V3-2003-12",
            "definition": "The consistent set of messaging artefacts as published or contained in repositories in December of 2003, based on the latest version of any V3 models or artefacts (RIM, Datatypes, CMETS, Common Messages, Vocabularies) as available in December of 2003. Note: This versioncode does not cover the version of the XML ITS.",
            "display": "HL7 Version V3-2003-12",
        }
    )
    """
    HL7 Version V3-2003-12

    The consistent set of messaging artefacts as published or contained in repositories in December of 2003, based on the latest version of any V3 models or artefacts (RIM, Datatypes, CMETS, Common Messages, Vocabularies) as available in December of 2003. Note: This versioncode does not cover the version of the XML ITS.
    """

    v3_2005_n = CodeSystemConcept(
        {
            "code": "V3-2005N",
            "definition": "Description:The consistent set of normative and DSTU messaging artifacts as published or contained in repositories in December of 2004, based on the latest version of any V3 models or artifacts (RIM, Datatypes, CMETS, Common Messages, Vocabularies) as published under the title of Normative Edition 2005. Note: This versioncode does not cover the version of the XML ITS.",
            "display": "2005 Normative Edition",
        }
    )
    """
    2005 Normative Edition

    Description:The consistent set of normative and DSTU messaging artifacts as published or contained in repositories in December of 2004, based on the latest version of any V3 models or artifacts (RIM, Datatypes, CMETS, Common Messages, Vocabularies) as published under the title of Normative Edition 2005. Note: This versioncode does not cover the version of the XML ITS.
    """

    v3_2006_n = CodeSystemConcept(
        {
            "code": "V3-2006N",
            "definition": "Description:The consistent set of normative and DSTU messaging artifacts as published or contained in repositories in December of 2005, based on the latest version of any V3 models or artifacts (RIM, Datatypes, CMETS, Common Messages, Vocabularies) as published under the title of Normative Edition 2006. Note: This versioncode does not cover the version of the XML ITS.",
            "display": "2006 Normative Edition",
        }
    )
    """
    2006 Normative Edition

    Description:The consistent set of normative and DSTU messaging artifacts as published or contained in repositories in December of 2005, based on the latest version of any V3 models or artifacts (RIM, Datatypes, CMETS, Common Messages, Vocabularies) as published under the title of Normative Edition 2006. Note: This versioncode does not cover the version of the XML ITS.
    """

    v3_2008_n = CodeSystemConcept(
        {
            "code": "V3-2008N",
            "definition": "Definition: The consistent set of normative and DSTU messaging artifacts as published or contained in repositories in December of 2007, based on the latest version of any V3 models or artifacts (RIM, Data Types, CMETS, Common Messages, Vocabularies) published under the title of Normative Edition 2008. Note: This version code does not cover the version of the XML ITS.",
            "display": "2008 Normative Edition",
        }
    )
    """
    2008 Normative Edition

    Definition: The consistent set of normative and DSTU messaging artifacts as published or contained in repositories in December of 2007, based on the latest version of any V3 models or artifacts (RIM, Data Types, CMETS, Common Messages, Vocabularies) published under the title of Normative Edition 2008. Note: This version code does not cover the version of the XML ITS.
    """

    v3_2009_n = CodeSystemConcept(
        {
            "code": "V3-2009N",
            "definition": "Description: The consistent set of normative and DSTU messaging artifacts as published or contained in repositories in December of 2008, based on the latest version of any V3 models or artifacts (RIM, Data Types, CMETS, Common Messages, Vocabularies) published under the title of Normative Edition 2009. Note: This version code does not cover the version of the XML ITS.",
            "display": "2009 Normative Edition",
        }
    )
    """
    2009 Normative Edition

    Description: The consistent set of normative and DSTU messaging artifacts as published or contained in repositories in December of 2008, based on the latest version of any V3 models or artifacts (RIM, Data Types, CMETS, Common Messages, Vocabularies) published under the title of Normative Edition 2009. Note: This version code does not cover the version of the XML ITS.
    """

    v3_2010_n = CodeSystemConcept(
        {
            "code": "V3-2010N",
            "definition": "Definition: The consistent set of normative and DSTU messaging artifacts as published or contained in repositories in December of 2009, based on the latest version of any V3 models or artifacts (RIM, Data Types, CMETS, Common Messages, Vocabularies) published under the title of Normative Edition 2010. Note: This version code does not cover the version of the XML ITS.",
            "display": "2010 Normative Edition",
        }
    )
    """
    2010 Normative Edition

    Definition: The consistent set of normative and DSTU messaging artifacts as published or contained in repositories in December of 2009, based on the latest version of any V3 models or artifacts (RIM, Data Types, CMETS, Common Messages, Vocabularies) published under the title of Normative Edition 2010. Note: This version code does not cover the version of the XML ITS.
    """

    v3_2011_n = CodeSystemConcept(
        {
            "code": "V3-2011N",
            "definition": "Definition: The consistent set of normative and DSTU messaging artifacts as published or contained in repositories in December of 2010, based on the latest version of any V3 models or artifacts (RIM, Data Types, CMETS, Common Messages, Vocabularies) published under the title of Normative Edition 2011. Note: This version code does not cover the version of the XML ITS.",
            "display": "2011 Normative Edition",
        }
    )
    """
    2011 Normative Edition

    Definition: The consistent set of normative and DSTU messaging artifacts as published or contained in repositories in December of 2010, based on the latest version of any V3 models or artifacts (RIM, Data Types, CMETS, Common Messages, Vocabularies) published under the title of Normative Edition 2011. Note: This version code does not cover the version of the XML ITS.
    """

    v3_2012_n = CodeSystemConcept(
        {
            "code": "V3-2012N",
            "definition": "Definition: The consistent set of normative and DSTU messaging artifacts as published or contained in repositories in December of 2011, based on the latest version of any V3 models or artifacts (RIM, Data Types, CMETS, Common Messages, Vocabularies) published under the title of Normative Edition 2012. Note: This version code does not cover the version of the XML ITS.",
            "display": "2012 Normative Edition",
        }
    )
    """
    2012 Normative Edition

    Definition: The consistent set of normative and DSTU messaging artifacts as published or contained in repositories in December of 2011, based on the latest version of any V3 models or artifacts (RIM, Data Types, CMETS, Common Messages, Vocabularies) published under the title of Normative Edition 2012. Note: This version code does not cover the version of the XML ITS.
    """

    v3_pr1 = CodeSystemConcept(
        {
            "code": "V3PR1",
            "definition": "Includes all material published as part of the ballot package released for vote in July-August 2003.",
            "display": "Version3 Pre-release #1",
        }
    )
    """
    Version3 Pre-release #1

    Includes all material published as part of the ballot package released for vote in July-August 2003.
    """

    v3_2007_n = CodeSystemConcept(
        {
            "code": "V3-2007N",
            "definition": "Description:The consistent set of normative and DSTU messaging artifacts as published or contained in repositories in December of 2006, based on the latest version of any V3 models or artifacts (RIM, Datatypes, CMETS, Common Messages, Vocabularies) published under the title of Normative Edition 2007. Note: This versioncode does not cover the version of the XML ITS.",
            "display": "2007 Normative Edition",
            "property": [{"code": "status", "valueCode": "retired"}],
        }
    )
    """
    2007 Normative Edition

    Description:The consistent set of normative and DSTU messaging artifacts as published or contained in repositories in December of 2006, based on the latest version of any V3 models or artifacts (RIM, Datatypes, CMETS, Common Messages, Vocabularies) published under the title of Normative Edition 2007. Note: This versioncode does not cover the version of the XML ITS.
    """

    class Meta:
        resource = _resource
