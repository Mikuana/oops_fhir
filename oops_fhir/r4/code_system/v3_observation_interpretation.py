from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3ObservationInterpretation"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3ObservationInterpretation:
    """
    v3 Code System ObservationInterpretation

    One or more codes providing a rough qualitative interpretation of the
observation, such as "normal" / "abnormal", "low" / "high", "better" /
"worse", "resistant" /  "susceptible", "expected" / "not expected". The
value set is intended to be for ANY use where coded representation of an
interpretation is needed.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation
    """

    underscore_genetic_observation_interpretation = CodeSystemConcept(
        {
            "code": "_GeneticObservationInterpretation",
            "concept": [
                {
                    "code": "CAR",
                    "definition": "The patient is considered as carrier based on the testing results. A carrier is an individual who carries an altered form of a gene which can lead to having a child or offspring in future generations with a genetic disorder.",
                    "display": "Carrier",
                },
                {
                    "code": "Carrier",
                    "definition": 'The patient is considered as carrier based on the testing results. A carrier is an individual who carries an altered form of a gene which can lead to having a child or offspring in future generations with a genetic disorder.\r\n\n                        \n                           \n                              Deprecation Comment: \n                           This code is currently the same string as the print name for this concept and is inconsistent with the conventions being used for the other codes in the coding system, as it is a full word with initial capitalization, rather than an all upper case mnemonic.  The recommendation from OO is to deprecate the code "Carrier" and to add "CAR" as the new active code representation for this concept.',
                    "display": "Carrier",
                    "property": [
                        {"code": "status", "valueCode": "deprecated"},
                        {"code": "deprecationDate", "valueDateTime": "2013-07-28"},
                    ],
                },
            ],
            "definition": 'Codes that specify interpretation of genetic analysis, such as "positive", "negative", "carrier", "responsive", etc.',
            "display": "GeneticObservationInterpretation",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    GeneticObservationInterpretation

    Codes that specify interpretation of genetic analysis, such as "positive", "negative", "carrier", "responsive", etc.
    """

    underscore_observation_interpretation_change = CodeSystemConcept(
        {
            "code": "_ObservationInterpretationChange",
            "concept": [
                {
                    "code": "B",
                    "definition": "The current result or observation value has improved compared to the previous result or observation value (the change is significant as defined in the respective test procedure).\r\n\n                        [Note: This can be applied to quantitative or qualitative observations.]",
                    "display": "Better",
                },
                {
                    "code": "D",
                    "definition": "The current result has decreased from the previous result for a quantitative observation (the change is significant as defined in the respective test procedure).",
                    "display": "Significant change down",
                },
                {
                    "code": "U",
                    "definition": "The current result has increased from the previous result for a quantitative observation (the change is significant as defined in the respective test procedure).",
                    "display": "Significant change up",
                },
                {
                    "code": "W",
                    "definition": "The current result or observation value has degraded compared to the previous result or observation value (the change is significant as defined in the respective test procedure).\r\n\n                        [Note: This can be applied to quantitative or qualitative observations.]",
                    "display": "Worse",
                },
            ],
            "definition": "Interpretations of change of quantity and/or severity. At most one of B or W and one of U or D allowed.",
            "display": "ObservationInterpretationChange",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ObservationInterpretationChange

    Interpretations of change of quantity and/or severity. At most one of B or W and one of U or D allowed.
    """

    underscore_observation_interpretation_exceptions = CodeSystemConcept(
        {
            "code": "_ObservationInterpretationExceptions",
            "concept": [
                {
                    "code": "<",
                    "definition": "The result is below the minimum detection limit (the test procedure or equipment is the limiting factor).\r\n\n                        Synonyms: Below analytical limit, low off scale.",
                    "display": "Off scale low",
                },
                {
                    "code": ">",
                    "definition": "The result is above the maximum quantifiable limit (the test procedure or equipment is the limiting factor).\r\n\n                        Synonyms: Above analytical limit, high off scale.",
                    "display": "Off scale high",
                },
                {
                    "code": "AC",
                    "definition": 'A valid result cannot be obtained for the specified component / analyte due to the presence of anti-complementary substances in the sample.\r\n\n                        \n                           \n                              Deprecation Comment: \n                           This code is being deprecated to match the status in V2 Table 0078 "Interpretation Codes.',
                    "display": "Anti-complementary substances present",
                    "property": [
                        {"code": "status", "valueCode": "deprecated"},
                        {"code": "deprecationDate", "valueDateTime": "2016-11-10"},
                    ],
                },
                {
                    "code": "IE",
                    "definition": 'There is insufficient evidence that the species in question is a good target for therapy with the drug.  A categorical interpretation is not possible.\r\n\n                        [Note: A MIC with "IE" and/or a comment may be reported (without an accompanying S, I or R-categorization).]',
                    "display": "Insufficient evidence",
                },
                {
                    "code": "QCF",
                    "definition": 'A result cannot be considered valid for the specified component / analyte or organism due to failure in the quality control testing component.\r\n\n                        \n                           \n                              Deprecation Comment: \n                           This code is being deprecated to match the status in V2 Table 0078 "Interpretation Codes.',
                    "display": "Quality control failure",
                    "property": [
                        {"code": "status", "valueCode": "deprecated"},
                        {"code": "deprecationDate", "valueDateTime": "2016-11-10"},
                    ],
                },
                {
                    "code": "TOX",
                    "definition": 'A valid result cannot be obtained for the specified organism or cell line due to the presence of cytotoxic substances in the sample or culture.\r\n\n                        \n                           \n                              Deprecation Comment: \n                           This code is being deprecated to match the status in V2 Table 0078 "Interpretation Codes.',
                    "display": "Cytotoxic substance present",
                    "property": [
                        {"code": "status", "valueCode": "deprecated"},
                        {"code": "deprecationDate", "valueDateTime": "2016-11-10"},
                    ],
                },
            ],
            "definition": "Technical exceptions resulting in the inability to provide an interpretation. At most one allowed. Does not imply normality or severity.",
            "display": "ObservationInterpretationExceptions",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ObservationInterpretationExceptions

    Technical exceptions resulting in the inability to provide an interpretation. At most one allowed. Does not imply normality or severity.
    """

    underscore_observation_interpretation_normality = CodeSystemConcept(
        {
            "code": "_ObservationInterpretationNormality",
            "concept": [
                {
                    "code": "A",
                    "concept": [
                        {
                            "code": "AA",
                            "concept": [
                                {
                                    "code": "HH",
                                    "definition": "The result for a quantitative observation is above a reference level at which immediate action should be considered for patient safety (as defined for the respective test procedure).\r\n\n                        Synonym: Above upper panic limits.",
                                    "display": "Critical high",
                                },
                                {
                                    "code": "LL",
                                    "definition": "The result for a quantitative observation is below a reference level at which immediate action should be considered for patient safety (as defined for the respective test procedure).\r\n\n                        Synonym: Below lower panic limits.",
                                    "display": "Critical low",
                                },
                            ],
                            "definition": "The result or observation value is outside a reference range or expected norm at a level at which immediate action should be considered for patient safety (as defined for the respective test procedure).\r\n\n                        [Note: Typically applies to non-numeric results.  Analogous to critical/panic limits for numeric results.]",
                            "display": "Critical abnormal",
                        },
                        {
                            "code": "H",
                            "concept": [
                                {
                                    "code": "H>",
                                    "definition": "A test result that is significantly higher than the reference (normal) or therapeutic interval, but has not reached the critically high value and might need special attention, as defined by the laboratory or the clinician.[Note: This level is situated between 'H' and 'HH'.]\r\n\n                        \n                           Deprecation Comment: The code 'H>' is being deprecated in order to align with the use of the code 'HU' for \"Very high\" in V2 Table 0078 \"Interpretation Codes\".\r\n\n                        [Note: The use of code 'H>' is non-preferred, as this code is deprecated and on track to be retired; use code 'HU' instead.",
                                    "display": "Significantly high",
                                    "property": [
                                        {"code": "status", "valueCode": "deprecated"},
                                        {
                                            "code": "deprecationDate",
                                            "valueDateTime": "2015-03-23",
                                        },
                                        {"code": "child", "valueCode": "HH"},
                                    ],
                                },
                                {
                                    "code": "HU",
                                    "definition": "A test result that is significantly higher than the reference (normal) or therapeutic interval, but has not reached the critically high value and might need special attention, as defined by the laboratory or the clinician.",
                                    "display": "Significantly high",
                                    "property": [{"code": "child", "valueCode": "HH"}],
                                },
                            ],
                            "definition": "The result for a quantitative observation is above the upper limit of the reference range (as defined for the respective test procedure).\r\n\n                        Synonym: Above high normal",
                            "display": "High",
                        },
                        {
                            "code": "L",
                            "concept": [
                                {
                                    "code": "L<",
                                    "definition": "A test result that is significantly lower than the reference (normal) or therapeutic interval, but has not reached the critically low value and might need special attention, as defined by the laboratory or the clinician.[Note: This level is situated between 'L' and 'LL'.]\r\n\n                        \n                           Deprecation Comment: The code 'L<' is being deprecated in order to align with the use of the code 'LU' for \"Very low\" in V2 Table 0078 \"Interpretation Codes\".\r\n\n                        [Note: The use of code 'L<' is non-preferred, as this code is deprecated and on track to be retired; use code 'LU' instead.",
                                    "display": "Significantly low",
                                    "property": [
                                        {"code": "status", "valueCode": "deprecated"},
                                        {
                                            "code": "deprecationDate",
                                            "valueDateTime": "2015-03-23",
                                        },
                                        {"code": "child", "valueCode": "LL"},
                                    ],
                                },
                                {
                                    "code": "LU",
                                    "definition": "A test result that is significantly lower than the reference (normal) or therapeutic interval, but has not reached the critically low value and might need special attention, as defined by the laboratory or the clinician.",
                                    "display": "Significantly low",
                                    "property": [{"code": "child", "valueCode": "LL"}],
                                },
                            ],
                            "definition": "The result for a quantitative observation is below the lower limit of the reference range (as defined for the respective test procedure).\r\n\n                        Synonym: Below low normal",
                            "display": "Low",
                        },
                    ],
                    "definition": "The result or observation value is outside the reference range or expected norm (as defined for the respective test procedure).\r\n\n                        [Note: Typically applies to non-numeric results.]",
                    "display": "Abnormal",
                },
                {
                    "code": "N",
                    "definition": "The result or observation value is within the reference range or expected norm (as defined for the respective test procedure).\r\n\n                        [Note: Applies to numeric or non-numeric results.]",
                    "display": "Normal",
                },
            ],
            "definition": 'Interpretation of normality or degree of abnormality (including critical or "alert" level). Concepts in this category are mutually exclusive, i.e., at most one is allowed.',
            "display": "ObservationInterpretationNormality",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ObservationInterpretationNormality

    Interpretation of normality or degree of abnormality (including critical or "alert" level). Concepts in this category are mutually exclusive, i.e., at most one is allowed.
    """

    underscore_observation_interpretation_susceptibility = CodeSystemConcept(
        {
            "code": "_ObservationInterpretationSusceptibility",
            "concept": [
                {
                    "code": "I",
                    "definition": 'Bacterial strain inhibited in vitro by a concentration of an antimicrobial agent that is associated with uncertain therapeutic effect. Reference: CLSI (http://www.clsi.org/Content/NavigationMenu/Resources/HarmonizedTerminologyDatabase/Harmonized_Terminolo.htm)\nProjects: ISO 20776-1, ISO 20776-2\r\n\n                        [Note 1: Bacterial strains are categorized as intermediate by applying the appropriate breakpoints in a defined phenotypic test system.]\r\n\n                        [Note 2: This class of susceptibility implies that an infection due to the isolate can be appropriately treated in body sites where the drugs are physiologically concentrated or when a high dosage of drug can be used.]\r\n\n                        [Note 3: This class also indicates a "buffer zone," to prevent small, uncontrolled, technical factors from causing major discrepancies in interpretations.]\r\n\n                        [Note 4: These breakpoints can be altered due to changes in circumstances (e.g., changes in commonly used drug dosages, emergence of new resistance mechanisms).]',
                    "display": "Intermediate",
                },
                {
                    "code": "MS",
                    "definition": "The patient is considered as carrier based on the testing results. A carrier is an individual who carries an altered form of a gene which can lead to having a child or offspring in future generations with a genetic disorder.\r\n\n                        \n                           \n                              Deprecation Comment: \n                           This antimicrobial susceptibility test interpretation concept is recommended by OO to be deprecated as it is no longer recommended for use in susceptibility testing by CLSI (reference CLSI document M100-S22; Vol. 32 No.3; CLSI Performance Standards for Antimicrobial Susceptibility Testing; Twenty-Second Informational Supplement. Jan 2012).",
                    "display": "moderately susceptible",
                    "property": [
                        {"code": "status", "valueCode": "deprecated"},
                        {"code": "deprecationDate", "valueDateTime": "2013-07-28"},
                    ],
                },
                {
                    "code": "NCL",
                    "definition": "Use when not enough clinical trial data published by the Clinical and Laboratory Standards Institutes (CLSI) is available to establish the breakpoints for susceptible / intermediate and resistant.",
                    "display": "No CLSI defined breakpoint",
                },
                {
                    "code": "NS",
                    "definition": 'A category used for isolates for which only a susceptible interpretive criterion has been designated because of the absence or rare occurrence of resistant strains. Isolates that have MICs above or zone diameters below the value indicated for the susceptible breakpoint should be reported as non-susceptible.\r\n\n                        NOTE 1: An isolate that is interpreted as non-susceptible does not necessarily mean that the isolate has a resistance mechanism. It is possible that isolates with MICs above the susceptible breakpoint that lack resistance mechanisms may be encountered within the wild-type distribution subsequent to the time the susceptible-only breakpoint is set. \r\n\n                        NOTE 2: For strains yielding results in the "nonsusceptible" category, organism identification and antimicrobial susceptibility test results should be confirmed.\r\n\n                        Synonym: decreased susceptibility.',
                    "display": "Non-susceptible",
                },
                {
                    "code": "R",
                    "concept": [
                        {
                            "code": "SYN-R",
                            "definition": "A category for isolates where the bacteria (e.g. enterococci) are not susceptible in vitro to a combination therapy (e.g., high-level aminoglycoside and cell wall active agent).  This is predictive that this combination therapy will not be effective. \r\n\n                        \n                           Usage Note: Since the use of penicillin or ampicillin alone often results in treatment failure of serious enterococcal or other bacterial infections, combination therapy is usually indicated to enhance bactericidal activity. The synergy between a cell wall active agent (such as penicillin, ampicillin, or vancomycin) and an aminoglycoside (such as gentamicin, kanamycin or streptomycin) is best predicted by screening for high-level bacterial resistance to the aminoglycoside.\r\n\n                        \n                           Open Issue: The print name of the code is very general and the description is very specific to a pair of classes of agents, which may lead to confusion of these concepts in the future should other synergies be found.",
                            "display": "Synergy - resistant",
                        }
                    ],
                    "definition": "Bacterial strain inhibited in vitro by a concentration of an antimicrobial agent that is associated with a high likelihood of therapeutic failure.\nReference: CLSI (http://www.clsi.org/Content/NavigationMenu/Resources/HarmonizedTerminologyDatabase/Harmonized_Terminolo.htm)  \nProjects: ISO 20776-1, ISO 20776-2\r\n\n                        [Note 1: Bacterial strains are categorized as resistant by applying the appropriate breakpoints in a defined phenotypic test system.]\r\n\n                        [Note 2: This breakpoint can be altered due to changes in circumstances (e.g., changes in commonly used drug dosages, emergence of new resistance mechanisms).]",
                    "display": "Resistant",
                },
                {
                    "code": "S",
                    "concept": [
                        {
                            "code": "SDD",
                            "definition": 'A category that includes isolates with antimicrobial agent minimum inhibitory concentrations (MICs) that approach usually attainable blood and tissue levels and for which response rates may be lower than for susceptible isolates.\r\n\n                        Reference: CLSI document M44-A2 2009 "Method for antifungal disk diffusion susceptibility testing of yeasts; approved guideline - second edition" - page 2.',
                            "display": "Susceptible-dose dependent",
                        },
                        {
                            "code": "SYN-S",
                            "definition": "A category for isolates where the bacteria (e.g. enterococci) are susceptible in vitro to a combination therapy (e.g., high-level aminoglycoside and cell wall active agent).  This is predictive that this combination therapy will be effective. \r\n\n                        \n                           Usage Note: Since the use of penicillin or ampicillin alone often results in treatment failure of serious enterococcal or other bacterial infections, combination therapy is usually indicated to enhance bactericidal activity. The synergy between a cell wall active agent (such as penicillin, ampicillin, or vancomycin) and an aminoglycoside (such as gentamicin, kanamycin or streptomycin) is best predicted by screening for high-level bacterial resistance to the aminoglycoside.\r\n\n                        \n                           Open Issue: The print name of the code is very general and the description is very specific to a pair of classes of agents, which may lead to confusion of these concepts in the future should other synergies be found.",
                            "display": "Synergy - susceptible",
                        },
                    ],
                    "definition": "Bacterial strain inhibited by in vitro concentration of an antimicrobial agent that is associated with a high likelihood of therapeutic success.\nReference: CLSI (http://www.clsi.org/Content/NavigationMenu/Resources/HarmonizedTerminologyDatabase/Harmonized_Terminolo.htm)\nSynonym (earlier term): Sensitive Projects: ISO 20776-1, ISO 20776-2\r\n\n                        [Note 1: Bacterial strains are categorized as susceptible by applying the appropriate breakpoints in a defined phenotypic system.]\r\n\n                        [Note 2: This breakpoint can be altered due to changes in circumstances (e.g., changes in commonly used drug dosages, emergence of new resistance mechanisms).]",
                    "display": "Susceptible",
                },
                {
                    "code": "VS",
                    "definition": "The patient is considered as carrier based on the testing results. A carrier is an individual who carries an altered form of a gene which can lead to having a child or offspring in future generations with a genetic disorder.\r\n\n                        \n                           \n                              Deprecation Comment: \n                           This antimicrobial susceptibility test interpretation concept is recommended by OO to be deprecated as it is no longer recommended for use in susceptibility testing by CLSI (reference CLSI document M100-S22; Vol. 32 No.3; CLSI Performance Standards for Antimicrobial Susceptibility Testing; Twenty-Second Informational Supplement. Jan 2012).",
                    "display": "very susceptible",
                    "property": [
                        {"code": "status", "valueCode": "deprecated"},
                        {"code": "deprecationDate", "valueDateTime": "2013-07-28"},
                    ],
                },
            ],
            "definition": "Interpretations of anti-microbial susceptibility testing results (microbiology). At most one allowed.",
            "display": "ObservationInterpretationSusceptibility",
            "property": [
                {"code": "notSelectable", "valueBoolean": True},
                {"code": "child", "valueCode": "IE"},
            ],
        }
    )
    """
    ObservationInterpretationSusceptibility

    Interpretations of anti-microbial susceptibility testing results (microbiology). At most one allowed.
    """

    ex = CodeSystemConcept(
        {
            "code": "EX",
            "concept": [
                {
                    "code": "HX",
                    "definition": 'The observation/test result is interpreted as being outside the inclusion range for a particular protocol within which the result is being reported.\n\r\n\n                        Example: A positive result on a Hepatitis screening test.\n                           Open Issue: EX, HX, LX: These three concepts do not seem to meet a clear need in the vocabulary, and their use in observation interpretation appears likely to be covered by other existing concepts (e.g., A, H, L).  The only apparent significant difference is their reference to use in protocols for exclusion of study subjects.  These concepts/codes were proposed by RCRIM for use in the CTLaboratory message.  They were submitted and approved in the November 2005 Harmonization cycle in proposal "030103C_VOCAB_RCRIM_l_quade_RCRIM Obs Interp_20051028154455". However, this proposal was not fully implemented in the vocabulary.  The proposal recommended creation of the x_ClinicalResearchExclusion domain in ObservationInterpretation with a value set including those three concepts/codes, but there is no subdomain of that name or equivalent with a binding to either of the value sets that contain these concepts/codes.  Members of the OO WG have recently attempted to contact members of RCRIM regarding these concepts, both by email and at the recent WGM in Atlanta, without response.  It is felt by OO that the best course of action to take at this time is to add this comprehensive Open Issue rather than deprecate these three concepts at this time, until further discussion is held.',
                    "display": "above high threshold",
                },
                {
                    "code": "LX",
                    "definition": 'The numeric observation/test result is interpreted as being below the low threshold value for a particular protocol within which the result is being reported.\r\n\n                        Example: A Total White Blood Cell Count falling below a protocol-defined threshold value of 3000/mm^3\n                           Open Issue: EX, HX, LX: These three concepts do not seem to meet a clear need in the vocabulary, and their use in observation interpretation appears likely to be covered by other existing concepts (e.g., A, H, L).  The only apparent significant difference is their reference to use in protocols for exclusion of study subjects.  These concepts/codes were proposed by RCRIM for use in the CTLaboratory message.  They were submitted and approved in the November 2005 Harmonization cycle in proposal "030103C_VOCAB_RCRIM_l_quade_RCRIM Obs Interp_20051028154455".  However, this proposal was not fully implemented in the vocabulary.  The proposal recommended creation of the x_ClinicalResearchExclusion domain in ObservationInterpretation with a value set including those three concepts/codes, but there is no subdomain of that name or equivalent with a binding to either of the value sets that contain these concepts/codes.  Members of the OO WG have recently attempted to contact members of RCRIM regarding these concepts, both by email and at the recent WGM in Atlanta, without response.  It is felt by OO that the best course of action to take at this time is to add this comprehensive Open Issue rather than deprecate these three concepts at this time, until further discussion is held.',
                    "display": "below low threshold",
                },
            ],
            "definition": 'The observation/test result is interpreted as being outside the inclusion range for a particular protocol within which the result is being reported.\n\r\n\n                        Example: A positive result on a Hepatitis screening test.\n                           Open Issue: EX, HX, LX: These three concepts do not seem to meet a clear need in the vocabulary, and their use in observation interpretation appears likely to be covered by other existing concepts (e.g., A, H, L).  The only apparent significant difference is their reference to use in protocols for exclusion of study subjects.\nThese concepts/codes were proposed by RCRIM for use in the CTLaboratory message.  They were submitted and approved in the November 2005 Harmonization cycle in proposal "030103C_VOCAB_RCRIM_l_quade_RCRIM Obs Interp_20051028154455".  However, this proposal was not fully implemented in the vocabulary.  The proposal recommended creation of the x_ClinicalResearchExclusion domain in ObservationInterpretation with a value set including those three concepts/codes, but there is no subdomain of that name or equivalent with a binding to either of the value sets that contain these concepts/codes.\nMembers of the OO WG have recently attempted to contact members of RCRIM regarding these concepts, both by email and at the recent WGM in Atlanta, without response.  It is felt by OO that the best course of action to take at this time is to add this comprehensive Open Issue rather than deprecate these three concepts at this time, until further discussion is held.',
            "display": "outside threshold",
        }
    )
    """
    outside threshold

    The observation/test result is interpreted as being outside the inclusion range for a particular protocol within which the result is being reported.


                        Example: A positive result on a Hepatitis screening test.
                           Open Issue: EX, HX, LX: These three concepts do not seem to meet a clear need in the vocabulary, and their use in observation interpretation appears likely to be covered by other existing concepts (e.g., A, H, L).  The only apparent significant difference is their reference to use in protocols for exclusion of study subjects.
These concepts/codes were proposed by RCRIM for use in the CTLaboratory message.  They were submitted and approved in the November 2005 Harmonization cycle in proposal "030103C_VOCAB_RCRIM_l_quade_RCRIM Obs Interp_20051028154455".  However, this proposal was not fully implemented in the vocabulary.  The proposal recommended creation of the x_ClinicalResearchExclusion domain in ObservationInterpretation with a value set including those three concepts/codes, but there is no subdomain of that name or equivalent with a binding to either of the value sets that contain these concepts/codes.
Members of the OO WG have recently attempted to contact members of RCRIM regarding these concepts, both by email and at the recent WGM in Atlanta, without response.  It is felt by OO that the best course of action to take at this time is to add this comprehensive Open Issue rather than deprecate these three concepts at this time, until further discussion is held.
    """

    hm = CodeSystemConcept(
        {
            "code": "HM",
            "definition": 'Hold for Medical Review\r\n\n                        \n                           Usage Note: This code is not intended for use in V3 artifacts.  It is included in the code system to maintain alignment with the V2 Table 0078 "Interpretation Codes."',
            "display": "Hold for Medical Review",
            "property": [
                {"code": "status", "valueCode": "deprecated"},
                {"code": "deprecationDate", "valueDateTime": "2016-11-10"},
            ],
        }
    )
    """
    Hold for Medical Review

    Hold for Medical Review

                        
                           Usage Note: This code is not intended for use in V3 artifacts.  It is included in the code system to maintain alignment with the V2 Table 0078 "Interpretation Codes."
    """

    observation_interpretation_detection = CodeSystemConcept(
        {
            "code": "ObservationInterpretationDetection",
            "concept": [
                {
                    "code": "IND",
                    "concept": [
                        {
                            "code": "E",
                            "definition": "The test or procedure was successfully performed, but the results are borderline and can neither be declared positive / negative nor detected / not detected according to the current established criteria.",
                            "display": "Equivocal",
                        }
                    ],
                    "definition": 'The specified component / analyte, organism or clinical sign could neither be declared positive / negative nor detected / not detected by the performed test or procedure.\r\n\n                        \n                           Usage Note: For example, if the specimen was degraded, poorly processed, or was missing the required anatomic structures, then "indeterminate" (i.e. "cannot be determined") is the appropriate response, not "equivocal".',
                    "display": "Indeterminate",
                },
                {
                    "code": "NEG",
                    "concept": [
                        {
                            "code": "ND",
                            "definition": "The presence of the specified component / analyte, organism or clinical sign could not be determined within the limit of detection of the performed test or procedure.",
                            "display": "Not detected",
                        }
                    ],
                    "definition": "An absence finding of the specified component / analyte, organism or clinical sign based on the established threshold of the performed test or procedure.\r\n\n                        [Note: Negative does not necessarily imply the complete absence of the specified item.]",
                    "display": "Negative",
                },
                {
                    "code": "POS",
                    "concept": [
                        {
                            "code": "DET",
                            "definition": "The measurement of the specified component / analyte, organism or clinical sign above the limit of detection of the performed test or procedure.",
                            "display": "Detected",
                        }
                    ],
                    "definition": "A presence finding of the specified component / analyte, organism or clinical sign based on the established threshold of the performed test or procedure.",
                    "display": "Positive",
                },
            ],
            "definition": 'Interpretations of the presence or absence of a component / analyte or organism in a test or of a sign in a clinical observation. In keeping with laboratory data processing practice, these concepts provide a categorical interpretation of the "meaning" of the quantitative value for the same observation.',
            "display": "ObservationInterpretationDetection",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ObservationInterpretationDetection

    Interpretations of the presence or absence of a component / analyte or organism in a test or of a sign in a clinical observation. In keeping with laboratory data processing practice, these concepts provide a categorical interpretation of the "meaning" of the quantitative value for the same observation.
    """

    observation_interpretation_expectation = CodeSystemConcept(
        {
            "code": "ObservationInterpretationExpectation",
            "concept": [
                {
                    "code": "EXP",
                    "definition": 'This result has been evaluated in light of known contraindicators.  Once those contraindicators have been taken into account the result is determined to be "Expected"  (e.g., presence of drugs in a patient that is taking prescription medication for pain management).',
                    "display": "Expected",
                },
                {
                    "code": "UNE",
                    "definition": 'This result has been evaluated in light of known contraindicators.  Once those contraindicators have been taken into account the result is determined to be "Unexpected" (e.g., presence of non-prescribed drugs in a patient that is taking prescription medication for pain management).',
                    "display": "Unexpected",
                },
            ],
            "definition": "Interpretation of the observed result taking into account additional information (contraindicators) about the patient's situation. Concepts in this category are mutually exclusive, i.e., at most one is allowed.",
            "display": "ObservationInterpretationExpectation",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ObservationInterpretationExpectation

    Interpretation of the observed result taking into account additional information (contraindicators) about the patient's situation. Concepts in this category are mutually exclusive, i.e., at most one is allowed.
    """

    obx = CodeSystemConcept(
        {
            "code": "OBX",
            "definition": 'Interpretation qualifiers in separate OBX segments\r\n\n                        \n                           Usage Note: This code is not intended for use in V3 artifacts.  It is included in the code system to maintain alignment with the V2 Table 0078 "Interpretation Codes."',
            "display": "Interpretation qualifiers in separate OBX segments",
            "property": [
                {"code": "status", "valueCode": "deprecated"},
                {"code": "deprecationDate", "valueDateTime": "2016-11-10"},
            ],
        }
    )
    """
    Interpretation qualifiers in separate OBX segments

    Interpretation qualifiers in separate OBX segments

                        
                           Usage Note: This code is not intended for use in V3 artifacts.  It is included in the code system to maintain alignment with the V2 Table 0078 "Interpretation Codes."
    """

    reactivity_observation_interpretation = CodeSystemConcept(
        {
            "code": "ReactivityObservationInterpretation",
            "concept": [
                {
                    "code": "NR",
                    "definition": "An absence finding used to indicate that the specified component / analyte did not react measurably with the reagent.",
                    "display": "Non-reactive",
                },
                {
                    "code": "RR",
                    "concept": [
                        {
                            "code": "WR",
                            "definition": "A weighted presence finding used to indicate that the specified component / analyte reacted with the reagent, but below the reliably measurable limit of the performed test.",
                            "display": "Weakly reactive",
                        }
                    ],
                    "definition": "A presence finding used to indicate that the specified component / analyte reacted with the reagent above the reliably measurable limit of the performed test.",
                    "display": "Reactive",
                },
            ],
            "definition": "Interpretations of the presence and level of reactivity of the specified component / analyte with the reagent in the performed laboratory test.",
            "display": "ReactivityObservationInterpretation",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ReactivityObservationInterpretation

    Interpretations of the presence and level of reactivity of the specified component / analyte with the reagent in the performed laboratory test.
    """

    class Meta:
        resource = _resource
