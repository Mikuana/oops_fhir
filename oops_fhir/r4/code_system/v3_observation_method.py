from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3ObservationMethod"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3ObservationMethod:
    """
    v3 Code System ObservationMethod

     A code that provides additional detail about the means or technique
used to ascertain the observation.  Examples:  Blood pressure
measurement method: arterial puncture vs. sphygmomanometer (Riva-Rocci),
sitting vs. supine position, etc.  OpenIssue:  Description copied from
Concept Domain of same name.  Must be verified.  Note that the Domain
has a full discussion about use of the attribute and constraining that
is not appropriate for the code system description.  Needs to be
improved.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-ObservationMethod
    """

    underscore_decision_observation_method = CodeSystemConcept(
        {
            "code": "_DecisionObservationMethod",
            "concept": [
                {
                    "code": "ALGM",
                    "concept": [
                        {
                            "code": "BYCL",
                            "definition": "Reaching a decision through the use of Bayesian statistical analysis.",
                            "display": "bayesian calculation",
                        }
                    ],
                    "definition": "Reaching a decision through the application of an algorithm designed to weigh the different factors involved.",
                    "display": "algorithm",
                },
                {
                    "code": "GINT",
                    "definition": "Reaching a decision by consideration of the totality of factors involved in order to reach a judgement.",
                    "display": "global introspection",
                },
            ],
            "definition": "Provides codes for decision methods, initially for assessing the causality of events.",
            "display": "DecisionObservationMethod",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    DecisionObservationMethod

    Provides codes for decision methods, initially for assessing the causality of events.
    """

    underscore_genetic_observation_method = CodeSystemConcept(
        {
            "code": "_GeneticObservationMethod",
            "concept": [
                {
                    "code": "PCR",
                    "definition": "Description: Polymerase Chain Reaction",
                    "display": "PCR",
                }
            ],
            "definition": "A code that provides additional detail about the means or technique used to ascertain the genetic analysis. Example, PCR, Micro Array",
            "display": "GeneticObservationMethod",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    GeneticObservationMethod

    A code that provides additional detail about the means or technique used to ascertain the genetic analysis. Example, PCR, Micro Array
    """

    underscore_observation_method_aggregate = CodeSystemConcept(
        {
            "code": "_ObservationMethodAggregate",
            "concept": [
                {
                    "code": "AVERAGE",
                    "definition": "Average of non-null values in the referenced set of values",
                    "display": "average",
                },
                {
                    "code": "COUNT",
                    "definition": "Count of non-null values in the referenced set of values",
                    "display": "count",
                },
                {
                    "code": "MAX",
                    "definition": "Largest of all non-null values in the referenced set of values.",
                    "display": "maxima",
                },
                {
                    "code": "MEDIAN",
                    "definition": "The median of all non-null values in the referenced set of values.",
                    "display": "median",
                },
                {
                    "code": "MIN",
                    "definition": "Smallest of all non-null values in the referenced set of values.",
                    "display": "minima",
                },
                {
                    "code": "MODE",
                    "definition": "The most common value of all non-null values in the referenced set of values.",
                    "display": "mode",
                },
                {
                    "code": "STDEV.P",
                    "definition": "Standard Deviation of the values in the referenced set of values, computed over the population.",
                    "display": "population standard deviation",
                },
                {
                    "code": "STDEV.S",
                    "definition": "Standard Deviation of the values in the referenced set of values, computed over a sample of the population.",
                    "display": "sample standard deviation",
                },
                {
                    "code": "SUM",
                    "definition": "Sum of non-null values in the referenced set of values",
                    "display": "sum",
                },
                {
                    "code": "VARIANCE.P",
                    "definition": "Variance of the values in the referenced set of values, computed over the population.",
                    "display": "population variance",
                },
                {
                    "code": "VARIANCE.S",
                    "definition": "Variance of the values in the referenced set of values, computed over a sample of the population.",
                    "display": "sample variance",
                },
            ],
            "definition": "Provides additional detail about the aggregation methods used to compute the aggregated values for an observation. This is an abstract code.",
            "display": "observation method aggregate",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    observation method aggregate

    Provides additional detail about the aggregation methods used to compute the aggregated values for an observation. This is an abstract code.
    """

    underscore_verification_method = CodeSystemConcept(
        {
            "code": "_VerificationMethod",
            "concept": [
                {
                    "code": "VDOC",
                    "definition": "Verification by means of document.\r\n\n                        \n                           Example: Fax, letter, attachment to e-mail.",
                    "display": "document verification",
                },
                {
                    "code": "VREG",
                    "definition": "verification by means of  a response to an electronic query\r\n\n                        \n                           Example: query message to a Covered Party registry application or Coverage Administrator.",
                    "display": "registry verification",
                },
                {
                    "code": "VTOKEN",
                    "definition": "Verification by means of electronic token.\r\n\n                        \n                           Example: smartcard, magnetic swipe card, RFID device.",
                    "display": "electronic token verification",
                },
                {
                    "code": "VVOICE",
                    "definition": "Verification by means of voice.\r\n\n                        \n                           Example: By speaking with or calling the Coverage Administrator or Covered Party",
                    "display": "voice-based verification",
                },
            ],
            "definition": "VerificationMethod",
            "display": "VerificationMethod",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    VerificationMethod

    VerificationMethod
    """

    zero001 = CodeSystemConcept(
        {
            "code": "0001",
            "definition": "Complement fixation",
            "display": "Complement fixation",
        }
    )
    """
    Complement fixation

    Complement fixation
    """

    zero002 = CodeSystemConcept(
        {
            "code": "0002",
            "definition": "Computed axial tomography",
            "display": "Computed axial tomography",
        }
    )
    """
    Computed axial tomography

    Computed axial tomography
    """

    zero003 = CodeSystemConcept(
        {
            "code": "0003",
            "definition": "Susceptibility, High Level Aminoglycoside Resistance agar test",
            "display": "HLAR agar test",
        }
    )
    """
    HLAR agar test

    Susceptibility, High Level Aminoglycoside Resistance agar test
    """

    zero004 = CodeSystemConcept(
        {
            "code": "0004",
            "definition": "Visual, Macroscopic observation",
            "display": "Macroscopic observation",
        }
    )
    """
    Macroscopic observation

    Visual, Macroscopic observation
    """

    zero005 = CodeSystemConcept(
        {
            "code": "0005",
            "definition": "Computed, Magnetic resonance",
            "display": "Magnetic resonance",
        }
    )
    """
    Magnetic resonance

    Computed, Magnetic resonance
    """

    zero006 = CodeSystemConcept(
        {
            "code": "0006",
            "definition": "Computed, Morphometry",
            "display": "Morphometry",
        }
    )
    """
    Morphometry

    Computed, Morphometry
    """

    zero007 = CodeSystemConcept(
        {
            "code": "0007",
            "definition": "Computed, Positron emission tomography",
            "display": "Positron emission tomography",
        }
    )
    """
    Positron emission tomography

    Computed, Positron emission tomography
    """

    zero008 = CodeSystemConcept(
        {
            "code": "0008",
            "definition": "SAMHSA drug assay confirmation",
            "display": "SAMHSA confirmation",
        }
    )
    """
    SAMHSA confirmation

    SAMHSA drug assay confirmation
    """

    zero009 = CodeSystemConcept(
        {
            "code": "0009",
            "definition": "SAMHSA drug assay screening",
            "display": "SAMHSA screening",
        }
    )
    """
    SAMHSA screening

    SAMHSA drug assay screening
    """

    zero010 = CodeSystemConcept(
        {
            "code": "0010",
            "definition": "Serum Neutralization",
            "display": "Serum Neutralization",
        }
    )
    """
    Serum Neutralization

    Serum Neutralization
    """

    zero011 = CodeSystemConcept(
        {"code": "0011", "definition": "Titration", "display": "Titration"}
    )
    """
    Titration

    Titration
    """

    zero012 = CodeSystemConcept(
        {"code": "0012", "definition": "Ultrasound", "display": "Ultrasound"}
    )
    """
    Ultrasound

    Ultrasound
    """

    zero013 = CodeSystemConcept(
        {
            "code": "0013",
            "definition": "X-ray crystallography",
            "display": "X-ray crystallography",
        }
    )
    """
    X-ray crystallography

    X-ray crystallography
    """

    zero014 = CodeSystemConcept(
        {"code": "0014", "definition": "Agglutination", "display": "Agglutination"}
    )
    """
    Agglutination

    Agglutination
    """

    zero015 = CodeSystemConcept(
        {
            "code": "0015",
            "definition": "Agglutination, Buffered acidified plate",
            "display": "Buffered acidified plate agglutination",
        }
    )
    """
    Buffered acidified plate agglutination

    Agglutination, Buffered acidified plate
    """

    zero016 = CodeSystemConcept(
        {
            "code": "0016",
            "definition": "Agglutination, Card",
            "display": "Card agglutination",
        }
    )
    """
    Card agglutination

    Agglutination, Card
    """

    zero017 = CodeSystemConcept(
        {
            "code": "0017",
            "definition": "Agglutination, Hemagglutination",
            "display": "Hemagglutination",
        }
    )
    """
    Hemagglutination

    Agglutination, Hemagglutination
    """

    zero018 = CodeSystemConcept(
        {
            "code": "0018",
            "definition": "Agglutination, Hemagglutination inhibition",
            "display": "Hemagglutination inhibition",
        }
    )
    """
    Hemagglutination inhibition

    Agglutination, Hemagglutination inhibition
    """

    zero019 = CodeSystemConcept(
        {
            "code": "0019",
            "definition": "Agglutination, Latex",
            "display": "Latex agglutination",
        }
    )
    """
    Latex agglutination

    Agglutination, Latex
    """

    zero020 = CodeSystemConcept(
        {
            "code": "0020",
            "definition": "Agglutination, Plate",
            "display": "Plate agglutination",
        }
    )
    """
    Plate agglutination

    Agglutination, Plate
    """

    zero021 = CodeSystemConcept(
        {
            "code": "0021",
            "definition": "Agglutination, Rapid Plate",
            "display": "Rapid agglutination",
        }
    )
    """
    Rapid agglutination

    Agglutination, Rapid Plate
    """

    zero022 = CodeSystemConcept(
        {
            "code": "0022",
            "definition": "Agglutination, RBC",
            "display": "RBC agglutination",
        }
    )
    """
    RBC agglutination

    Agglutination, RBC
    """

    zero023 = CodeSystemConcept(
        {
            "code": "0023",
            "definition": "Agglutination, Rivanol",
            "display": "Rivanol agglutination",
        }
    )
    """
    Rivanol agglutination

    Agglutination, Rivanol
    """

    zero024 = CodeSystemConcept(
        {
            "code": "0024",
            "definition": "Agglutination, Tube",
            "display": "Tube agglutination",
        }
    )
    """
    Tube agglutination

    Agglutination, Tube
    """

    zero025 = CodeSystemConcept(
        {"code": "0025", "definition": "Bioassay", "display": "Bioassay"}
    )
    """
    Bioassay

    Bioassay
    """

    zero026 = CodeSystemConcept(
        {
            "code": "0026",
            "definition": "Bioassay, Animal Inoculation",
            "display": "Animal Inoculation",
        }
    )
    """
    Animal Inoculation

    Bioassay, Animal Inoculation
    """

    zero027 = CodeSystemConcept(
        {
            "code": "0027",
            "definition": "Bioassay, Cytotoxicity",
            "display": "Cytotoxicity",
        }
    )
    """
    Cytotoxicity

    Bioassay, Cytotoxicity
    """

    zero028 = CodeSystemConcept(
        {
            "code": "0028",
            "definition": "Bioassay, Embryo Infective Dose 50",
            "display": "Embryo infective dose 50",
        }
    )
    """
    Embryo infective dose 50

    Bioassay, Embryo Infective Dose 50
    """

    zero029 = CodeSystemConcept(
        {
            "code": "0029",
            "definition": "Bioassay, Embryo Lethal Dose 50",
            "display": "Embryo lethal dose 50",
        }
    )
    """
    Embryo lethal dose 50

    Bioassay, Embryo Lethal Dose 50
    """

    zero030 = CodeSystemConcept(
        {
            "code": "0030",
            "definition": "Bioassay, Mouse intercerebral inoculation",
            "display": "Mouse intercerebral inoculation",
        }
    )
    """
    Mouse intercerebral inoculation

    Bioassay, Mouse intercerebral inoculation
    """

    zero031 = CodeSystemConcept(
        {
            "code": "0031",
            "definition": "Bioassay, qualitative",
            "display": "Bioassay, qualitative",
        }
    )
    """
    Bioassay, qualitative

    Bioassay, qualitative
    """

    zero032 = CodeSystemConcept(
        {
            "code": "0032",
            "definition": "Bioassay, quantitative",
            "display": "Bioassay, quantitative",
        }
    )
    """
    Bioassay, quantitative

    Bioassay, quantitative
    """

    zero033 = CodeSystemConcept(
        {"code": "0033", "definition": "Chemical", "display": "Chemical method"}
    )
    """
    Chemical method

    Chemical
    """

    zero034 = CodeSystemConcept(
        {
            "code": "0034",
            "definition": "Chemical, Differential light absorption",
            "display": "Differential light absorption chemical test",
        }
    )
    """
    Differential light absorption chemical test

    Chemical, Differential light absorption
    """

    zero035 = CodeSystemConcept(
        {"code": "0035", "definition": "Chemical, Dipstick", "display": "Dipstick"}
    )
    """
    Dipstick

    Chemical, Dipstick
    """

    zero036 = CodeSystemConcept(
        {
            "code": "0036",
            "definition": "Chemical, Dipstick colorimetric laboratory test",
            "display": "Dipstick colorimetric laboratory test",
        }
    )
    """
    Dipstick colorimetric laboratory test

    Chemical, Dipstick colorimetric laboratory test
    """

    zero037 = CodeSystemConcept(
        {"code": "0037", "definition": "Chemical, Test strip", "display": "Test strip"}
    )
    """
    Test strip

    Chemical, Test strip
    """

    zero038 = CodeSystemConcept(
        {"code": "0038", "definition": "Chromatography", "display": "Chromatography"}
    )
    """
    Chromatography

    Chromatography
    """

    zero039 = CodeSystemConcept(
        {
            "code": "0039",
            "definition": "Chromatography, Affinity",
            "display": "Affinity chromatography",
        }
    )
    """
    Affinity chromatography

    Chromatography, Affinity
    """

    zero040 = CodeSystemConcept(
        {
            "code": "0040",
            "definition": "Chromatography, Gas liquid",
            "display": "Gas liquid chromatography",
        }
    )
    """
    Gas liquid chromatography

    Chromatography, Gas liquid
    """

    zero041 = CodeSystemConcept(
        {
            "code": "0041",
            "definition": "Chromatography, High performance liquid",
            "display": "High performance liquid chromatography",
        }
    )
    """
    High performance liquid chromatography

    Chromatography, High performance liquid
    """

    zero042 = CodeSystemConcept(
        {
            "code": "0042",
            "definition": "Chromatography, Liquid",
            "display": "Liquid Chromatography",
        }
    )
    """
    Liquid Chromatography

    Chromatography, Liquid
    """

    zero043 = CodeSystemConcept(
        {
            "code": "0043",
            "definition": "Chromatography, Protein A affinity",
            "display": "Protein A affinity chromatography",
        }
    )
    """
    Protein A affinity chromatography

    Chromatography, Protein A affinity
    """

    zero044 = CodeSystemConcept(
        {"code": "0044", "definition": "Coagulation", "display": "Coagulation"}
    )
    """
    Coagulation

    Coagulation
    """

    zero045 = CodeSystemConcept(
        {
            "code": "0045",
            "definition": "Coagulation, Tilt tube",
            "display": "Tilt tube coagulation time",
        }
    )
    """
    Tilt tube coagulation time

    Coagulation, Tilt tube
    """

    zero046 = CodeSystemConcept(
        {
            "code": "0046",
            "definition": "Coagulation, Tilt tube reptilase induced",
            "display": "Tilt tube reptilase induced coagulation",
        }
    )
    """
    Tilt tube reptilase induced coagulation

    Coagulation, Tilt tube reptilase induced
    """

    zero047 = CodeSystemConcept(
        {"code": "0047", "definition": "Count, Automated", "display": "Automated count"}
    )
    """
    Automated count

    Count, Automated
    """

    zero048 = CodeSystemConcept(
        {"code": "0048", "definition": "Count, Manual", "display": "Manual cell count"}
    )
    """
    Manual cell count

    Count, Manual
    """

    zero049 = CodeSystemConcept(
        {
            "code": "0049",
            "definition": "Count, Platelet, Rees-Ecker",
            "display": "Platelet count, Rees-Ecker",
        }
    )
    """
    Platelet count, Rees-Ecker

    Count, Platelet, Rees-Ecker
    """

    zero050 = CodeSystemConcept(
        {"code": "0050", "definition": "Culture, Aerobic", "display": "Aerobic Culture"}
    )
    """
    Aerobic Culture

    Culture, Aerobic
    """

    zero051 = CodeSystemConcept(
        {
            "code": "0051",
            "definition": "Culture, Anaerobic",
            "display": "Anaerobic Culture",
        }
    )
    """
    Anaerobic Culture

    Culture, Anaerobic
    """

    zero052 = CodeSystemConcept(
        {
            "code": "0052",
            "definition": "Culture, Chicken Embryo",
            "display": "Chicken embryo culture",
        }
    )
    """
    Chicken embryo culture

    Culture, Chicken Embryo
    """

    zero053 = CodeSystemConcept(
        {
            "code": "0053",
            "definition": "Culture, Delayed secondary enrichment",
            "display": "Delayed secondary enrichment",
        }
    )
    """
    Delayed secondary enrichment

    Culture, Delayed secondary enrichment
    """

    zero054 = CodeSystemConcept(
        {
            "code": "0054",
            "definition": "Culture, Microaerophilic",
            "display": "Microaerophilic Culture",
        }
    )
    """
    Microaerophilic Culture

    Culture, Microaerophilic
    """

    zero055 = CodeSystemConcept(
        {
            "code": "0055",
            "definition": "Culture, Quantitative microbial, cup",
            "display": "Quantitative microbial culture, cup",
        }
    )
    """
    Quantitative microbial culture, cup

    Culture, Quantitative microbial, cup
    """

    zero056 = CodeSystemConcept(
        {
            "code": "0056",
            "definition": "Culture, Quantitative microbial, droplet",
            "display": "Quantitative microbial culture, droplet",
        }
    )
    """
    Quantitative microbial culture, droplet

    Culture, Quantitative microbial, droplet
    """

    zero057 = CodeSystemConcept(
        {
            "code": "0057",
            "definition": "Culture, Quantitative microbial, filter paper",
            "display": "Quantitative microbial culture, filter paper",
        }
    )
    """
    Quantitative microbial culture, filter paper

    Culture, Quantitative microbial, filter paper
    """

    zero058 = CodeSystemConcept(
        {
            "code": "0058",
            "definition": "Culture, Quantitative microbial, pad",
            "display": "Quantitative microbial culture, pad culture",
        }
    )
    """
    Quantitative microbial culture, pad culture

    Culture, Quantitative microbial, pad
    """

    zero059 = CodeSystemConcept(
        {
            "code": "0059",
            "definition": "Culture, Quantitative microbial, pour plate",
            "display": "Quantitative microbial culture, pour plate",
        }
    )
    """
    Quantitative microbial culture, pour plate

    Culture, Quantitative microbial, pour plate
    """

    zero060 = CodeSystemConcept(
        {
            "code": "0060",
            "definition": "Culture, Quantitative microbial, surface streak",
            "display": "Quantitative microbial culture, surface streak",
        }
    )
    """
    Quantitative microbial culture, surface streak

    Culture, Quantitative microbial, surface streak
    """

    zero061 = CodeSystemConcept(
        {
            "code": "0061",
            "definition": "Culture, Somatic Cell",
            "display": "Somatic Cell culture",
        }
    )
    """
    Somatic Cell culture

    Culture, Somatic Cell
    """

    zero062 = CodeSystemConcept(
        {"code": "0062", "definition": "Diffusion, Agar", "display": "Agar diffusion"}
    )
    """
    Agar diffusion

    Diffusion, Agar
    """

    zero063 = CodeSystemConcept(
        {
            "code": "0063",
            "definition": "Diffusion, Agar Gel Immunodiffusion",
            "display": "Agar Gel Immunodiffusion",
        }
    )
    """
    Agar Gel Immunodiffusion

    Diffusion, Agar Gel Immunodiffusion
    """

    zero064 = CodeSystemConcept(
        {"code": "0064", "definition": "Electrophoresis", "display": "Electrophoresis"}
    )
    """
    Electrophoresis

    Electrophoresis
    """

    zero065 = CodeSystemConcept(
        {
            "code": "0065",
            "definition": "Electrophoresis, Agaorse gel",
            "display": "Agaorse gel electrophoresis",
        }
    )
    """
    Agaorse gel electrophoresis

    Electrophoresis, Agaorse gel
    """

    zero066 = CodeSystemConcept(
        {
            "code": "0066",
            "definition": "Electrophoresis, citrate agar",
            "display": "Electrophoresis, citrate agar",
        }
    )
    """
    Electrophoresis, citrate agar

    Electrophoresis, citrate agar
    """

    zero067 = CodeSystemConcept(
        {
            "code": "0067",
            "definition": "Electrophoresis, Immuno",
            "display": "Immunoelectrophoresis",
        }
    )
    """
    Immunoelectrophoresis

    Electrophoresis, Immuno
    """

    zero068 = CodeSystemConcept(
        {
            "code": "0068",
            "definition": "Electrophoresis, Polyacrylamide gel",
            "display": "Polyacrylamide gel electrophoresis",
        }
    )
    """
    Polyacrylamide gel electrophoresis

    Electrophoresis, Polyacrylamide gel
    """

    zero069 = CodeSystemConcept(
        {
            "code": "0069",
            "definition": "Electrophoresis, Starch gel",
            "display": "Starch gel electrophoresis",
        }
    )
    """
    Starch gel electrophoresis

    Electrophoresis, Starch gel
    """

    zero070 = CodeSystemConcept(
        {"code": "0070", "definition": "ELISA", "display": "ELISA"}
    )
    """
    ELISA

    ELISA
    """

    zero071 = CodeSystemConcept(
        {
            "code": "0071",
            "definition": "ELISA, antigen capture",
            "display": "ELISA, antigen capture",
        }
    )
    """
    ELISA, antigen capture

    ELISA, antigen capture
    """

    zero072 = CodeSystemConcept(
        {
            "code": "0072",
            "definition": "ELISA, avidin biotin peroxidase complex",
            "display": "ELISA, avidin biotin peroxidase complex",
        }
    )
    """
    ELISA, avidin biotin peroxidase complex

    ELISA, avidin biotin peroxidase complex
    """

    zero073 = CodeSystemConcept(
        {"code": "0073", "definition": "ELISA, Kinetic", "display": "Kinetic ELISA"}
    )
    """
    Kinetic ELISA

    ELISA, Kinetic
    """

    zero074 = CodeSystemConcept(
        {
            "code": "0074",
            "definition": "ELISA, peroxidase-antiperoxidase",
            "display": "ELISA, peroxidase-antiperoxidase",
        }
    )
    """
    ELISA, peroxidase-antiperoxidase

    ELISA, peroxidase-antiperoxidase
    """

    zero075 = CodeSystemConcept(
        {
            "code": "0075",
            "definition": "Identification, API 20 Strep",
            "display": "API 20 Strep",
        }
    )
    """
    API 20 Strep

    Identification, API 20 Strep
    """

    zero076 = CodeSystemConcept(
        {"code": "0076", "definition": "Identification, API 20A", "display": "API 20A"}
    )
    """
    API 20A

    Identification, API 20A
    """

    zero077 = CodeSystemConcept(
        {
            "code": "0077",
            "definition": "Identification, API 20C AUX",
            "display": "API 20C AUX",
        }
    )
    """
    API 20C AUX

    Identification, API 20C AUX
    """

    zero078 = CodeSystemConcept(
        {"code": "0078", "definition": "Identification, API 20E", "display": "API 20E"}
    )
    """
    API 20E

    Identification, API 20E
    """

    zero079 = CodeSystemConcept(
        {
            "code": "0079",
            "definition": "Identification, API 20NE",
            "display": "API 20NE",
        }
    )
    """
    API 20NE

    Identification, API 20NE
    """

    zero080 = CodeSystemConcept(
        {
            "code": "0080",
            "definition": "Identification, API 50 CH",
            "display": "API 50 CH",
        }
    )
    """
    API 50 CH

    Identification, API 50 CH
    """

    zero081 = CodeSystemConcept(
        {
            "code": "0081",
            "definition": "Identification, API An-IDENT",
            "display": "API An-IDENT",
        }
    )
    """
    API An-IDENT

    Identification, API An-IDENT
    """

    zero082 = CodeSystemConcept(
        {
            "code": "0082",
            "definition": "Identification, API Coryne",
            "display": "API Coryne",
        }
    )
    """
    API Coryne

    Identification, API Coryne
    """

    zero083 = CodeSystemConcept(
        {
            "code": "0083",
            "definition": "Identification, API Rapid 20E",
            "display": "API Rapid 20E",
        }
    )
    """
    API Rapid 20E

    Identification, API Rapid 20E
    """

    zero084 = CodeSystemConcept(
        {
            "code": "0084",
            "definition": "Identification, API Staph",
            "display": "API Staph",
        }
    )
    """
    API Staph

    Identification, API Staph
    """

    zero085 = CodeSystemConcept(
        {"code": "0085", "definition": "Identification, API ZYM", "display": "API ZYM"}
    )
    """
    API ZYM

    Identification, API ZYM
    """

    zero086 = CodeSystemConcept(
        {
            "code": "0086",
            "definition": "Identification, Bacterial",
            "display": "Bacterial identification",
        }
    )
    """
    Bacterial identification

    Identification, Bacterial
    """

    zero087 = CodeSystemConcept(
        {
            "code": "0087",
            "definition": "Identification, mini VIDAS",
            "display": "mini VIDAS",
        }
    )
    """
    mini VIDAS

    Identification, mini VIDAS
    """

    zero088 = CodeSystemConcept(
        {
            "code": "0088",
            "definition": "Identification, Phage susceptibility typing",
            "display": "Phage susceptibility typing",
        }
    )
    """
    Phage susceptibility typing

    Identification, Phage susceptibility typing
    """

    zero089 = CodeSystemConcept(
        {
            "code": "0089",
            "definition": "Identification, Quad-FERM+",
            "display": "Quad-FERM+",
        }
    )
    """
    Quad-FERM+

    Identification, Quad-FERM+
    """

    zero090 = CodeSystemConcept(
        {
            "code": "0090",
            "definition": "Identification, RAPIDEC Staph",
            "display": "RAPIDEC Staph",
        }
    )
    """
    RAPIDEC Staph

    Identification, RAPIDEC Staph
    """

    zero091 = CodeSystemConcept(
        {
            "code": "0091",
            "definition": "Identification, Staphaurex",
            "display": "Staphaurex",
        }
    )
    """
    Staphaurex

    Identification, Staphaurex
    """

    zero092 = CodeSystemConcept(
        {"code": "0092", "definition": "Identification, VIDAS", "display": "VIDAS"}
    )
    """
    VIDAS

    Identification, VIDAS
    """

    zero093 = CodeSystemConcept(
        {"code": "0093", "definition": "Identification, Vitek", "display": "Vitek"}
    )
    """
    Vitek

    Identification, Vitek
    """

    zero094 = CodeSystemConcept(
        {"code": "0094", "definition": "Identification, VITEK 2", "display": "VITEK 2"}
    )
    """
    VITEK 2

    Identification, VITEK 2
    """

    zero095 = CodeSystemConcept(
        {"code": "0095", "definition": "Immune stain", "display": "Immune stain"}
    )
    """
    Immune stain

    Immune stain
    """

    zero096 = CodeSystemConcept(
        {
            "code": "0096",
            "definition": "Immune stain, Immunofluorescent antibody, direct",
            "display": "Immunofluorescent antibody, direct",
        }
    )
    """
    Immunofluorescent antibody, direct

    Immune stain, Immunofluorescent antibody, direct
    """

    zero097 = CodeSystemConcept(
        {
            "code": "0097",
            "definition": "Immune stain, Immunofluorescent antibody, indirect",
            "display": "Immunofluorescent antibody, indirect",
        }
    )
    """
    Immunofluorescent antibody, indirect

    Immune stain, Immunofluorescent antibody, indirect
    """

    zero098 = CodeSystemConcept(
        {
            "code": "0098",
            "definition": "Immune stain, Immunoperoxidase, Avidin-Biotin Complex",
            "display": "Immunoperoxidase, Avidin-Biotin Complex",
        }
    )
    """
    Immunoperoxidase, Avidin-Biotin Complex

    Immune stain, Immunoperoxidase, Avidin-Biotin Complex
    """

    zero099 = CodeSystemConcept(
        {
            "code": "0099",
            "definition": "Immune stain, Immunoperoxidase, Peroxidase anti-peroxidase complex",
            "display": "Immunoperoxidase, Peroxidase anti-peroxidase complex",
        }
    )
    """
    Immunoperoxidase, Peroxidase anti-peroxidase complex

    Immune stain, Immunoperoxidase, Peroxidase anti-peroxidase complex
    """

    zero100 = CodeSystemConcept(
        {
            "code": "0100",
            "definition": "Immune stain, Immunoperoxidase, Protein A-peroxidase complex",
            "display": "Immunoperoxidase, Protein A-peroxidase complex",
        }
    )
    """
    Immunoperoxidase, Protein A-peroxidase complex

    Immune stain, Immunoperoxidase, Protein A-peroxidase complex
    """

    zero101 = CodeSystemConcept(
        {"code": "0101", "definition": "Immunoassay", "display": "Immunoassay"}
    )
    """
    Immunoassay

    Immunoassay
    """

    zero102 = CodeSystemConcept(
        {
            "code": "0102",
            "definition": "Immunoassay, qualitative, multiple step",
            "display": "Immunoassay, qualitative, multiple step",
        }
    )
    """
    Immunoassay, qualitative, multiple step

    Immunoassay, qualitative, multiple step
    """

    zero103 = CodeSystemConcept(
        {
            "code": "0103",
            "definition": "Immunoassay, qualitative, single step",
            "display": "Immunoassay, qualitative, single step",
        }
    )
    """
    Immunoassay, qualitative, single step

    Immunoassay, qualitative, single step
    """

    zero104 = CodeSystemConcept(
        {
            "code": "0104",
            "definition": "Immunoassay, Radioimmunoassay",
            "display": "Radioimmunoassay",
        }
    )
    """
    Radioimmunoassay

    Immunoassay, Radioimmunoassay
    """

    zero105 = CodeSystemConcept(
        {
            "code": "0105",
            "definition": "Immunoassay, semi-quantitative, multiple step",
            "display": "Immunoassay, semi-quantitative, multiple step",
        }
    )
    """
    Immunoassay, semi-quantitative, multiple step

    Immunoassay, semi-quantitative, multiple step
    """

    zero106 = CodeSystemConcept(
        {
            "code": "0106",
            "definition": "Immunoassay, semi-quantitative, single step",
            "display": "Immunoassay, semi-quantitative, single step",
        }
    )
    """
    Immunoassay, semi-quantitative, single step

    Immunoassay, semi-quantitative, single step
    """

    zero107 = CodeSystemConcept(
        {"code": "0107", "definition": "Microscopy", "display": "Microscopy"}
    )
    """
    Microscopy

    Microscopy
    """

    zero108 = CodeSystemConcept(
        {
            "code": "0108",
            "definition": "Microscopy, Darkfield",
            "display": "Darkfield microscopy",
        }
    )
    """
    Darkfield microscopy

    Microscopy, Darkfield
    """

    zero109 = CodeSystemConcept(
        {
            "code": "0109",
            "definition": "Microscopy, Electron",
            "display": "Electron microscopy",
        }
    )
    """
    Electron microscopy

    Microscopy, Electron
    """

    zero110 = CodeSystemConcept(
        {
            "code": "0110",
            "definition": "Microscopy, Electron microscopy tomography",
            "display": "Electron microscopy tomography",
        }
    )
    """
    Electron microscopy tomography

    Microscopy, Electron microscopy tomography
    """

    zero111 = CodeSystemConcept(
        {
            "code": "0111",
            "definition": "Microscopy, Electron, negative stain",
            "display": "Electron microscopy, negative stain",
        }
    )
    """
    Electron microscopy, negative stain

    Microscopy, Electron, negative stain
    """

    zero112 = CodeSystemConcept(
        {
            "code": "0112",
            "definition": "Microscopy, Electron, thick section transmission",
            "display": "Electron microscopy, thick section",
        }
    )
    """
    Electron microscopy, thick section

    Microscopy, Electron, thick section transmission
    """

    zero113 = CodeSystemConcept(
        {
            "code": "0113",
            "definition": "Microscopy, Electron, thin section transmission",
            "display": "Electron microscopy, thin section",
        }
    )
    """
    Electron microscopy, thin section

    Microscopy, Electron, thin section transmission
    """

    zero114 = CodeSystemConcept(
        {
            "code": "0114",
            "definition": "Microscopy, Light",
            "display": "Microscopy, Light",
        }
    )
    """
    Microscopy, Light

    Microscopy, Light
    """

    zero115 = CodeSystemConcept(
        {
            "code": "0115",
            "definition": "Microscopy, Polarized light",
            "display": "Polarizing light microscopy",
        }
    )
    """
    Polarizing light microscopy

    Microscopy, Polarized light
    """

    zero116 = CodeSystemConcept(
        {
            "code": "0116",
            "definition": "Microscopy, Scanning electron",
            "display": "Scanning electron microscopy",
        }
    )
    """
    Scanning electron microscopy

    Microscopy, Scanning electron
    """

    zero117 = CodeSystemConcept(
        {
            "code": "0117",
            "definition": "Microscopy, Transmission electron",
            "display": "Transmission electron microscopy",
        }
    )
    """
    Transmission electron microscopy

    Microscopy, Transmission electron
    """

    zero118 = CodeSystemConcept(
        {
            "code": "0118",
            "definition": "Microscopy, Transparent tape direct examination",
            "display": "Transparent tape direct examination",
        }
    )
    """
    Transparent tape direct examination

    Microscopy, Transparent tape direct examination
    """

    zero119 = CodeSystemConcept(
        {
            "code": "0119",
            "definition": "Molecular, 3 Self-Sustaining Sequence Replication",
            "display": "3 Self-Sustaining Sequence Replication",
        }
    )
    """
    3 Self-Sustaining Sequence Replication

    Molecular, 3 Self-Sustaining Sequence Replication
    """

    zero120 = CodeSystemConcept(
        {
            "code": "0120",
            "definition": "Molecular, Branched Chain DNA",
            "display": "Branched Chain DNA",
        }
    )
    """
    Branched Chain DNA

    Molecular, Branched Chain DNA
    """

    zero121 = CodeSystemConcept(
        {
            "code": "0121",
            "definition": "Molecular, Hybridization Protection Assay",
            "display": "Hybridization Protection Assay",
        }
    )
    """
    Hybridization Protection Assay

    Molecular, Hybridization Protection Assay
    """

    zero122 = CodeSystemConcept(
        {
            "code": "0122",
            "definition": "Molecular, Immune blot",
            "display": "Immune blot",
        }
    )
    """
    Immune blot

    Molecular, Immune blot
    """

    zero123 = CodeSystemConcept(
        {
            "code": "0123",
            "definition": "Molecular, In-situ hybridization",
            "display": "In-situ hybridization",
        }
    )
    """
    In-situ hybridization

    Molecular, In-situ hybridization
    """

    zero124 = CodeSystemConcept(
        {
            "code": "0124",
            "definition": "Molecular, Ligase Chain Reaction",
            "display": "Ligase Chain Reaction",
        }
    )
    """
    Ligase Chain Reaction

    Molecular, Ligase Chain Reaction
    """

    zero125 = CodeSystemConcept(
        {
            "code": "0125",
            "definition": "Molecular, Ligation Activated Transcription",
            "display": "Ligation Activated Transcription",
        }
    )
    """
    Ligation Activated Transcription

    Molecular, Ligation Activated Transcription
    """

    zero126 = CodeSystemConcept(
        {
            "code": "0126",
            "definition": "Molecular, Nucleic Acid Probe",
            "display": "Nucleic Acid Probe",
        }
    )
    """
    Nucleic Acid Probe

    Molecular, Nucleic Acid Probe
    """

    zero128 = CodeSystemConcept(
        {
            "code": "0128",
            "definition": "Molecular, Nucleic acid probe with amplification\r\n\n                        \r\n\n                        Rationale: Duplicate of code 0126. Use code 0126 instead.",
            "display": "Nucleic acid probe with amplification",
        }
    )
    """
    Nucleic acid probe with amplification

    Molecular, Nucleic acid probe with amplification

                        

                        Rationale: Duplicate of code 0126. Use code 0126 instead.
    """

    zero129 = CodeSystemConcept(
        {
            "code": "0129",
            "definition": "Molecular, Nucleic acid probe with target amplification",
            "display": "Nucleic acid probe with target amplification",
        }
    )
    """
    Nucleic acid probe with target amplification

    Molecular, Nucleic acid probe with target amplification
    """

    zero130 = CodeSystemConcept(
        {
            "code": "0130",
            "definition": "Molecular, Nucleic acid reverse transcription",
            "display": "Nucleic acid reverse transcription",
        }
    )
    """
    Nucleic acid reverse transcription

    Molecular, Nucleic acid reverse transcription
    """

    zero131 = CodeSystemConcept(
        {
            "code": "0131",
            "definition": "Molecular, Nucleic Acid Sequence Based Analysis",
            "display": "Nucleic Acid Sequence Based Analysis",
        }
    )
    """
    Nucleic Acid Sequence Based Analysis

    Molecular, Nucleic Acid Sequence Based Analysis
    """

    zero132 = CodeSystemConcept(
        {
            "code": "0132",
            "definition": "Molecular, Polymerase chain reaction",
            "display": "Polymerase chain reaction",
        }
    )
    """
    Polymerase chain reaction

    Molecular, Polymerase chain reaction
    """

    zero133 = CodeSystemConcept(
        {
            "code": "0133",
            "definition": "Molecular, Q-Beta Replicase or probe amplification category method",
            "display": "Q-Beta Replicase or probe amplification category method",
        }
    )
    """
    Q-Beta Replicase or probe amplification category method

    Molecular, Q-Beta Replicase or probe amplification category method
    """

    zero134 = CodeSystemConcept(
        {
            "code": "0134",
            "definition": "Molecular, Restriction Fragment Length Polymorphism",
            "display": "Restriction Fragment Length Polymorphism",
        }
    )
    """
    Restriction Fragment Length Polymorphism

    Molecular, Restriction Fragment Length Polymorphism
    """

    zero135 = CodeSystemConcept(
        {
            "code": "0135",
            "definition": "Molecular, Southern Blot",
            "display": "Southern Blot",
        }
    )
    """
    Southern Blot

    Molecular, Southern Blot
    """

    zero136 = CodeSystemConcept(
        {
            "code": "0136",
            "definition": "Molecular, Strand Displacement Amplification",
            "display": "Strand Displacement Amplification",
        }
    )
    """
    Strand Displacement Amplification

    Molecular, Strand Displacement Amplification
    """

    zero137 = CodeSystemConcept(
        {
            "code": "0137",
            "definition": "Molecular, Transcription Mediated Amplification",
            "display": "Transcription Mediated Amplification",
        }
    )
    """
    Transcription Mediated Amplification

    Molecular, Transcription Mediated Amplification
    """

    zero138 = CodeSystemConcept(
        {
            "code": "0138",
            "definition": "Molecular, Western Blot",
            "display": "Western Blot",
        }
    )
    """
    Western Blot

    Molecular, Western Blot
    """

    zero139 = CodeSystemConcept(
        {
            "code": "0139",
            "definition": "Precipitation, Flocculation",
            "display": "Flocculation",
        }
    )
    """
    Flocculation

    Precipitation, Flocculation
    """

    zero140 = CodeSystemConcept(
        {
            "code": "0140",
            "definition": "Precipitation, Immune precipitation",
            "display": "Immune precipitation",
        }
    )
    """
    Immune precipitation

    Precipitation, Immune precipitation
    """

    zero141 = CodeSystemConcept(
        {
            "code": "0141",
            "definition": "Precipitation, Milk ring test",
            "display": "Milk ring test",
        }
    )
    """
    Milk ring test

    Precipitation, Milk ring test
    """

    zero142 = CodeSystemConcept(
        {
            "code": "0142",
            "definition": "Precipitation, Precipitin",
            "display": "Precipitin",
        }
    )
    """
    Precipitin

    Precipitation, Precipitin
    """

    zero143 = CodeSystemConcept(
        {"code": "0143", "definition": "Stain, Acid fast", "display": "Acid fast stain"}
    )
    """
    Acid fast stain

    Stain, Acid fast
    """

    zero144 = CodeSystemConcept(
        {
            "code": "0144",
            "definition": "Stain, Acid fast, fluorochrome",
            "display": "Acid fast stain, fluorochrome",
        }
    )
    """
    Acid fast stain, fluorochrome

    Stain, Acid fast, fluorochrome
    """

    zero145 = CodeSystemConcept(
        {
            "code": "0145",
            "definition": "Stain, Acid fast, Kinyoun's cold carbolfuchsin",
            "display": "Acid fast stain, Kinyoun's cold carbolfuchsin",
        }
    )
    """
    Acid fast stain, Kinyoun's cold carbolfuchsin

    Stain, Acid fast, Kinyoun's cold carbolfuchsin
    """

    zero146 = CodeSystemConcept(
        {
            "code": "0146",
            "definition": "Stain, Acid fast, Ziehl-Neelsen",
            "display": "Acid fast stain, Ziehl-Neelsen",
        }
    )
    """
    Acid fast stain, Ziehl-Neelsen

    Stain, Acid fast, Ziehl-Neelsen
    """

    zero147 = CodeSystemConcept(
        {
            "code": "0147",
            "definition": "Stain, Acid phosphatase",
            "display": "Acid phosphatase stain",
        }
    )
    """
    Acid phosphatase stain

    Stain, Acid phosphatase
    """

    zero148 = CodeSystemConcept(
        {
            "code": "0148",
            "definition": "Stain, Acridine orange",
            "display": "Acridine orange stain",
        }
    )
    """
    Acridine orange stain

    Stain, Acridine orange
    """

    zero149 = CodeSystemConcept(
        {
            "code": "0149",
            "definition": "Stain, Active brilliant orange KH",
            "display": "Active brilliant orange KH stain",
        }
    )
    """
    Active brilliant orange KH stain

    Stain, Active brilliant orange KH
    """

    zero150 = CodeSystemConcept(
        {
            "code": "0150",
            "definition": "Stain, Alazarin red S",
            "display": "Alazarin red S stain",
        }
    )
    """
    Alazarin red S stain

    Stain, Alazarin red S
    """

    zero151 = CodeSystemConcept(
        {
            "code": "0151",
            "definition": "Stain, Alcian blue",
            "display": "Alcian blue stain",
        }
    )
    """
    Alcian blue stain

    Stain, Alcian blue
    """

    zero152 = CodeSystemConcept(
        {
            "code": "0152",
            "definition": "Stain, Alcian blue with Periodic acid Schiff",
            "display": "Alcian blue with Periodic acid Schiff stain",
        }
    )
    """
    Alcian blue with Periodic acid Schiff stain

    Stain, Alcian blue with Periodic acid Schiff
    """

    zero153 = CodeSystemConcept(
        {
            "code": "0153",
            "definition": "Stain, Argentaffin",
            "display": "Argentaffin stain",
        }
    )
    """
    Argentaffin stain

    Stain, Argentaffin
    """

    zero154 = CodeSystemConcept(
        {
            "code": "0154",
            "definition": "Stain, Argentaffin silver",
            "display": "Argentaffin silver stain",
        }
    )
    """
    Argentaffin silver stain

    Stain, Argentaffin silver
    """

    zero155 = CodeSystemConcept(
        {
            "code": "0155",
            "definition": "Stain, Azure-eosin",
            "display": "Azure-eosin stain",
        }
    )
    """
    Azure-eosin stain

    Stain, Azure-eosin
    """

    zero156 = CodeSystemConcept(
        {
            "code": "0156",
            "definition": "Stain, Basic Fuschin",
            "display": "Basic Fuschin stain",
        }
    )
    """
    Basic Fuschin stain

    Stain, Basic Fuschin
    """

    zero157 = CodeSystemConcept(
        {"code": "0157", "definition": "Stain, Bennhold", "display": "Bennhold stain"}
    )
    """
    Bennhold stain

    Stain, Bennhold
    """

    zero158 = CodeSystemConcept(
        {
            "code": "0158",
            "definition": "Stain, Bennhold's Congo red",
            "display": "Bennhold's Congo red stain",
        }
    )
    """
    Bennhold's Congo red stain

    Stain, Bennhold's Congo red
    """

    zero159 = CodeSystemConcept(
        {
            "code": "0159",
            "definition": "Stain, Bielschowsky",
            "display": "Bielschowsky stain",
        }
    )
    """
    Bielschowsky stain

    Stain, Bielschowsky
    """

    zero160 = CodeSystemConcept(
        {
            "code": "0160",
            "definition": "Stain, Bielschowsky's silver",
            "display": "Bielschowsky's silver stain",
        }
    )
    """
    Bielschowsky's silver stain

    Stain, Bielschowsky's silver
    """

    zero161 = CodeSystemConcept(
        {"code": "0161", "definition": "Stain, Bleach", "display": "Bleach stain"}
    )
    """
    Bleach stain

    Stain, Bleach
    """

    zero162 = CodeSystemConcept(
        {"code": "0162", "definition": "Stain, Bodian", "display": "Bodian stain"}
    )
    """
    Bodian stain

    Stain, Bodian
    """

    zero163 = CodeSystemConcept(
        {
            "code": "0163",
            "definition": "Stain, Brown-Brenn",
            "display": "Brown-Brenn stain",
        }
    )
    """
    Brown-Brenn stain

    Stain, Brown-Brenn
    """

    zero164 = CodeSystemConcept(
        {
            "code": "0164",
            "definition": "Stain, Butyrate-esterase",
            "display": "Butyrate-esterase stain",
        }
    )
    """
    Butyrate-esterase stain

    Stain, Butyrate-esterase
    """

    zero165 = CodeSystemConcept(
        {
            "code": "0165",
            "definition": "Stain, Calcofluor white fluorescent",
            "display": "Calcofluor white fluorescent stain",
        }
    )
    """
    Calcofluor white fluorescent stain

    Stain, Calcofluor white fluorescent
    """

    zero166 = CodeSystemConcept(
        {
            "code": "0166",
            "definition": "Stain, Carbol-fuchsin",
            "display": "Carbol-fuchsin stain",
        }
    )
    """
    Carbol-fuchsin stain

    Stain, Carbol-fuchsin
    """

    zero167 = CodeSystemConcept(
        {"code": "0167", "definition": "Stain, Carmine", "display": "Carmine stain"}
    )
    """
    Carmine stain

    Stain, Carmine
    """

    zero168 = CodeSystemConcept(
        {
            "code": "0168",
            "definition": "Stain, Churukian-Schenk",
            "display": "Churukian-Schenk stain",
        }
    )
    """
    Churukian-Schenk stain

    Stain, Churukian-Schenk
    """

    zero169 = CodeSystemConcept(
        {"code": "0169", "definition": "Stain, Congo red", "display": "Congo red stain"}
    )
    """
    Congo red stain

    Stain, Congo red
    """

    zero170 = CodeSystemConcept(
        {
            "code": "0170",
            "definition": "Stain, Cresyl echt violet",
            "display": "Cresyl echt violet stain",
        }
    )
    """
    Cresyl echt violet stain

    Stain, Cresyl echt violet
    """

    zero171 = CodeSystemConcept(
        {
            "code": "0171",
            "definition": "Stain, Crystal violet",
            "display": "Crystal violet stain",
        }
    )
    """
    Crystal violet stain

    Stain, Crystal violet
    """

    zero172 = CodeSystemConcept(
        {
            "code": "0172",
            "definition": "Stain, De Galantha",
            "display": "De Galantha stain",
        }
    )
    """
    De Galantha stain

    Stain, De Galantha
    """

    zero173 = CodeSystemConcept(
        {
            "code": "0173",
            "definition": "Stain, Dieterle silver impregnation",
            "display": "Dieterle silver impregnation stain",
        }
    )
    """
    Dieterle silver impregnation stain

    Stain, Dieterle silver impregnation
    """

    zero174 = CodeSystemConcept(
        {
            "code": "0174",
            "definition": "Stain, Fite-Farco",
            "display": "Fite-Farco stain",
        }
    )
    """
    Fite-Farco stain

    Stain, Fite-Farco
    """

    zero175 = CodeSystemConcept(
        {
            "code": "0175",
            "definition": "Stain, Fontana-Masson silver",
            "display": "Fontana-Masson silver stain",
        }
    )
    """
    Fontana-Masson silver stain

    Stain, Fontana-Masson silver
    """

    zero176 = CodeSystemConcept(
        {"code": "0176", "definition": "Stain, Fouchet", "display": "Fouchet stain"}
    )
    """
    Fouchet stain

    Stain, Fouchet
    """

    zero177 = CodeSystemConcept(
        {"code": "0177", "definition": "Stain, Gomori", "display": "Gomori stain"}
    )
    """
    Gomori stain

    Stain, Gomori
    """

    zero178 = CodeSystemConcept(
        {
            "code": "0178",
            "definition": "Stain, Gomori methenamine silver",
            "display": "Gomori methenamine silver stain",
        }
    )
    """
    Gomori methenamine silver stain

    Stain, Gomori methenamine silver
    """

    zero179 = CodeSystemConcept(
        {
            "code": "0179",
            "definition": "Stain, Gomori-Wheatly trichrome",
            "display": "Gomori-Wheatly trichrome stain",
        }
    )
    """
    Gomori-Wheatly trichrome stain

    Stain, Gomori-Wheatly trichrome
    """

    zero180 = CodeSystemConcept(
        {"code": "0180", "definition": "Stain, Gridley", "display": "Gridley stain"}
    )
    """
    Gridley stain

    Stain, Gridley
    """

    zero181 = CodeSystemConcept(
        {
            "code": "0181",
            "definition": "Stain, Grimelius silver",
            "display": "Grimelius silver stain",
        }
    )
    """
    Grimelius silver stain

    Stain, Grimelius silver
    """

    zero182 = CodeSystemConcept(
        {"code": "0182", "definition": "Stain, Grocott", "display": "Grocott stain"}
    )
    """
    Grocott stain

    Stain, Grocott
    """

    zero183 = CodeSystemConcept(
        {
            "code": "0183",
            "definition": "Stain, Grocott methenamine silver",
            "display": "Grocott methenamine silver stain",
        }
    )
    """
    Grocott methenamine silver stain

    Stain, Grocott methenamine silver
    """

    zero184 = CodeSystemConcept(
        {
            "code": "0184",
            "definition": "Stain, Hale's colloidal ferric oxide",
            "display": "Hale's colloidal ferric oxide stain",
        }
    )
    """
    Hale's colloidal ferric oxide stain

    Stain, Hale's colloidal ferric oxide
    """

    zero185 = CodeSystemConcept(
        {
            "code": "0185",
            "definition": "Stain, Hale's colloidal iron",
            "display": "Hale's colloidal iron stain",
        }
    )
    """
    Hale's colloidal iron stain

    Stain, Hale's colloidal iron
    """

    zero186 = CodeSystemConcept(
        {"code": "0186", "definition": "Stain, Hansel", "display": "Hansel stain"}
    )
    """
    Hansel stain

    Stain, Hansel
    """

    zero187 = CodeSystemConcept(
        {
            "code": "0187",
            "definition": "Stain, Harris regressive hematoxylin and eosin",
            "display": "Harris regressive hematoxylin and eosin stain",
        }
    )
    """
    Harris regressive hematoxylin and eosin stain

    Stain, Harris regressive hematoxylin and eosin
    """

    zero188 = CodeSystemConcept(
        {
            "code": "0188",
            "definition": "Stain, Hematoxylin and eosin",
            "display": "Hematoxylin and eosin stain",
        }
    )
    """
    Hematoxylin and eosin stain

    Stain, Hematoxylin and eosin
    """

    zero189 = CodeSystemConcept(
        {"code": "0189", "definition": "Stain, Highman", "display": "Highman stain"}
    )
    """
    Highman stain

    Stain, Highman
    """

    zero190 = CodeSystemConcept(
        {"code": "0190", "definition": "Stain, Holzer", "display": "Holzer stain"}
    )
    """
    Holzer stain

    Stain, Holzer
    """

    zero191 = CodeSystemConcept(
        {
            "code": "0191",
            "definition": "Stain, Iron hematoxylin",
            "display": "Iron hematoxylin stain",
        }
    )
    """
    Iron hematoxylin stain

    Stain, Iron hematoxylin
    """

    zero192 = CodeSystemConcept(
        {"code": "0192", "definition": "Stain, Jones", "display": "Jones stain"}
    )
    """
    Jones stain

    Stain, Jones
    """

    zero193 = CodeSystemConcept(
        {
            "code": "0193",
            "definition": "Stain, Jones methenamine silver",
            "display": "Jones methenamine silver stain",
        }
    )
    """
    Jones methenamine silver stain

    Stain, Jones methenamine silver
    """

    zero194 = CodeSystemConcept(
        {"code": "0194", "definition": "Stain, Kossa", "display": "Kossa stain"}
    )
    """
    Kossa stain

    Stain, Kossa
    """

    zero195 = CodeSystemConcept(
        {
            "code": "0195",
            "definition": "Stain, Lawson-Van Gieson",
            "display": "Lawson-Van Gieson stain",
        }
    )
    """
    Lawson-Van Gieson stain

    Stain, Lawson-Van Gieson
    """

    zero196 = CodeSystemConcept(
        {
            "code": "0196",
            "definition": "Stain, Loeffler methylene blue",
            "display": "Loeffler methylene blue stain",
        }
    )
    """
    Loeffler methylene blue stain

    Stain, Loeffler methylene blue
    """

    zero197 = CodeSystemConcept(
        {
            "code": "0197",
            "definition": "Stain, Luxol fast blue with cresyl violet",
            "display": "Luxol fast blue with cresyl violet stain",
        }
    )
    """
    Luxol fast blue with cresyl violet stain

    Stain, Luxol fast blue with cresyl violet
    """

    zero198 = CodeSystemConcept(
        {
            "code": "0198",
            "definition": "Stain, Luxol fast blue with Periodic acid-Schiff",
            "display": "Luxol fast blue with Periodic acid-Schiff stain",
        }
    )
    """
    Luxol fast blue with Periodic acid-Schiff stain

    Stain, Luxol fast blue with Periodic acid-Schiff
    """

    zero199 = CodeSystemConcept(
        {
            "code": "0199",
            "definition": "Stain, MacNeal's tetrachrome blood",
            "display": "MacNeal's tetrachrome blood stain",
        }
    )
    """
    MacNeal's tetrachrome blood stain

    Stain, MacNeal's tetrachrome blood
    """

    zero200 = CodeSystemConcept(
        {
            "code": "0200",
            "definition": "Stain, Mallory-Heidenhain",
            "display": "Mallory-Heidenhain stain",
        }
    )
    """
    Mallory-Heidenhain stain

    Stain, Mallory-Heidenhain
    """

    zero201 = CodeSystemConcept(
        {
            "code": "0201",
            "definition": "Stain, Masson trichrome",
            "display": "Masson trichrome stain",
        }
    )
    """
    Masson trichrome stain

    Stain, Masson trichrome
    """

    zero202 = CodeSystemConcept(
        {
            "code": "0202",
            "definition": "Stain, Mayer mucicarmine",
            "display": "Mayer mucicarmine stain",
        }
    )
    """
    Mayer mucicarmine stain

    Stain, Mayer mucicarmine
    """

    zero203 = CodeSystemConcept(
        {
            "code": "0203",
            "definition": "Stain, Mayers progressive hematoxylin and eosin",
            "display": "Mayers progressive hematoxylin and eosin stain",
        }
    )
    """
    Mayers progressive hematoxylin and eosin stain

    Stain, Mayers progressive hematoxylin and eosin
    """

    zero204 = CodeSystemConcept(
        {
            "code": "0204",
            "definition": "Stain, May-Grunwald Giemsa",
            "display": "May-Grunwald Giemsa stain",
        }
    )
    """
    May-Grunwald Giemsa stain

    Stain, May-Grunwald Giemsa
    """

    zero205 = CodeSystemConcept(
        {
            "code": "0205",
            "definition": "Stain, Methyl green",
            "display": "Methyl green stain",
        }
    )
    """
    Methyl green stain

    Stain, Methyl green
    """

    zero206 = CodeSystemConcept(
        {
            "code": "0206",
            "definition": "Stain, Methyl green pyronin",
            "display": "Methyl green pyronin stain",
        }
    )
    """
    Methyl green pyronin stain

    Stain, Methyl green pyronin
    """

    zero207 = CodeSystemConcept(
        {
            "code": "0207",
            "definition": "Stain, Modified Gomori-Wheatly trichrome",
            "display": "Modified Gomori-Wheatly trichrome stain",
        }
    )
    """
    Modified Gomori-Wheatly trichrome stain

    Stain, Modified Gomori-Wheatly trichrome
    """

    zero208 = CodeSystemConcept(
        {
            "code": "0208",
            "definition": "Stain, Modified Masson trichrome",
            "display": "Modified Masson trichrome stain",
        }
    )
    """
    Modified Masson trichrome stain

    Stain, Modified Masson trichrome
    """

    zero209 = CodeSystemConcept(
        {
            "code": "0209",
            "definition": "Stain, Modified trichrome",
            "display": "Modified trichrome stain",
        }
    )
    """
    Modified trichrome stain

    Stain, Modified trichrome
    """

    zero210 = CodeSystemConcept(
        {
            "code": "0210",
            "definition": "Stain, Movat pentachrome",
            "display": "Movat pentachrome stain",
        }
    )
    """
    Movat pentachrome stain

    Stain, Movat pentachrome
    """

    zero211 = CodeSystemConcept(
        {
            "code": "0211",
            "definition": "Stain, Mucicarmine",
            "display": "Mucicarmine stain",
        }
    )
    """
    Mucicarmine stain

    Stain, Mucicarmine
    """

    zero212 = CodeSystemConcept(
        {
            "code": "0212",
            "definition": "Stain, Neutral red",
            "display": "Neutral red stain",
        }
    )
    """
    Neutral red stain

    Stain, Neutral red
    """

    zero213 = CodeSystemConcept(
        {
            "code": "0213",
            "definition": "Stain, Night blue",
            "display": "Night blue stain",
        }
    )
    """
    Night blue stain

    Stain, Night blue
    """

    zero214 = CodeSystemConcept(
        {
            "code": "0214",
            "definition": "Stain, Non-specific esterase",
            "display": "Non-specific esterase stain",
        }
    )
    """
    Non-specific esterase stain

    Stain, Non-specific esterase
    """

    zero215 = CodeSystemConcept(
        {"code": "0215", "definition": "Stain, Oil red-O", "display": "Oil red-O stain"}
    )
    """
    Oil red-O stain

    Stain, Oil red-O
    """

    zero216 = CodeSystemConcept(
        {"code": "0216", "definition": "Stain, Orcein", "display": "Orcein stain"}
    )
    """
    Orcein stain

    Stain, Orcein
    """

    zero217 = CodeSystemConcept(
        {"code": "0217", "definition": "Stain, Perls'", "display": "Perls' stain"}
    )
    """
    Perls' stain

    Stain, Perls'
    """

    zero218 = CodeSystemConcept(
        {
            "code": "0218",
            "definition": "Stain, Phosphotungstic acid-hematoxylin",
            "display": "Phosphotungstic acid-hematoxylin stain",
        }
    )
    """
    Phosphotungstic acid-hematoxylin stain

    Stain, Phosphotungstic acid-hematoxylin
    """

    zero219 = CodeSystemConcept(
        {
            "code": "0219",
            "definition": "Stain, Potassium ferrocyanide",
            "display": "Potassium ferrocyanide stain",
        }
    )
    """
    Potassium ferrocyanide stain

    Stain, Potassium ferrocyanide
    """

    zero220 = CodeSystemConcept(
        {
            "code": "0220",
            "definition": "Stain, Prussian blue",
            "display": "Prussian blue stain",
        }
    )
    """
    Prussian blue stain

    Stain, Prussian blue
    """

    zero221 = CodeSystemConcept(
        {
            "code": "0221",
            "definition": "Stain, Putchler modified Bennhold",
            "display": "Putchler modified Bennhold stain",
        }
    )
    """
    Putchler modified Bennhold stain

    Stain, Putchler modified Bennhold
    """

    zero222 = CodeSystemConcept(
        {
            "code": "0222",
            "definition": "Stain, Quinacrine fluorescent",
            "display": "Quinacrine fluorescent stain",
        }
    )
    """
    Quinacrine fluorescent stain

    Stain, Quinacrine fluorescent
    """

    zero223 = CodeSystemConcept(
        {"code": "0223", "definition": "Stain, Reticulin", "display": "Reticulin stain"}
    )
    """
    Reticulin stain

    Stain, Reticulin
    """

    zero224 = CodeSystemConcept(
        {"code": "0224", "definition": "Stain, Rhodamine", "display": "Rhodamine stain"}
    )
    """
    Rhodamine stain

    Stain, Rhodamine
    """

    zero225 = CodeSystemConcept(
        {"code": "0225", "definition": "Stain, Safranin", "display": "Safranin stain"}
    )
    """
    Safranin stain

    Stain, Safranin
    """

    zero226 = CodeSystemConcept(
        {"code": "0226", "definition": "Stain, Schmorl", "display": "Schmorl stain"}
    )
    """
    Schmorl stain

    Stain, Schmorl
    """

    zero227 = CodeSystemConcept(
        {
            "code": "0227",
            "definition": "Stain, Seiver-Munger",
            "display": "Seiver-Munger stain",
        }
    )
    """
    Seiver-Munger stain

    Stain, Seiver-Munger
    """

    zero228 = CodeSystemConcept(
        {"code": "0228", "definition": "Stain, Silver", "display": "Silver stain"}
    )
    """
    Silver stain

    Stain, Silver
    """

    zero229 = CodeSystemConcept(
        {
            "code": "0229",
            "definition": "Stain, Specific esterase",
            "display": "Specific esterase stain",
        }
    )
    """
    Specific esterase stain

    Stain, Specific esterase
    """

    zero230 = CodeSystemConcept(
        {
            "code": "0230",
            "definition": "Stain, Steiner silver",
            "display": "Steiner silver stain",
        }
    )
    """
    Steiner silver stain

    Stain, Steiner silver
    """

    zero231 = CodeSystemConcept(
        {"code": "0231", "definition": "Stain, Sudan III", "display": "Sudan III stain"}
    )
    """
    Sudan III stain

    Stain, Sudan III
    """

    zero232 = CodeSystemConcept(
        {"code": "0232", "definition": "Stain, Sudan IVI", "display": "Sudan IVI stain"}
    )
    """
    Sudan IVI stain

    Stain, Sudan IVI
    """

    zero233 = CodeSystemConcept(
        {
            "code": "0233",
            "definition": "Stain, Sulfated alcian blue",
            "display": "Sulfated alcian blue stain",
        }
    )
    """
    Sulfated alcian blue stain

    Stain, Sulfated alcian blue
    """

    zero234 = CodeSystemConcept(
        {
            "code": "0234",
            "definition": "Stain, Supravital",
            "display": "Supravital stain",
        }
    )
    """
    Supravital stain

    Stain, Supravital
    """

    zero235 = CodeSystemConcept(
        {
            "code": "0235",
            "definition": "Stain, Thioflavine-S",
            "display": "Thioflavine-S stain",
        }
    )
    """
    Thioflavine-S stain

    Stain, Thioflavine-S
    """

    zero236 = CodeSystemConcept(
        {
            "code": "0236",
            "definition": "Stain, Three micron Giemsa",
            "display": "Three micron Giemsa stain",
        }
    )
    """
    Three micron Giemsa stain

    Stain, Three micron Giemsa
    """

    zero237 = CodeSystemConcept(
        {
            "code": "0237",
            "definition": "Stain, Vassar-Culling",
            "display": "Vassar-Culling stain",
        }
    )
    """
    Vassar-Culling stain

    Stain, Vassar-Culling
    """

    zero238 = CodeSystemConcept(
        {"code": "0238", "definition": "Stain, Vital", "display": "Vital Stain"}
    )
    """
    Vital Stain

    Stain, Vital
    """

    zero239 = CodeSystemConcept(
        {"code": "0239", "definition": "Stain, von Kossa", "display": "von Kossa stain"}
    )
    """
    von Kossa stain

    Stain, von Kossa
    """

    zero243 = CodeSystemConcept(
        {
            "code": "0243",
            "definition": "Susceptibility, Minimum bactericidal concentration, macrodilution",
            "display": "Minimum bactericidal concentration test, macrodilution",
        }
    )
    """
    Minimum bactericidal concentration test, macrodilution

    Susceptibility, Minimum bactericidal concentration, macrodilution
    """

    zero244 = CodeSystemConcept(
        {
            "code": "0244",
            "definition": "Susceptibility, Minimum bactericidal concentration, microdilution",
            "display": "Minimum bactericidal concentration test, microdilution",
        }
    )
    """
    Minimum bactericidal concentration test, microdilution

    Susceptibility, Minimum bactericidal concentration, microdilution
    """

    zero247 = CodeSystemConcept(
        {"code": "0247", "definition": "Turbidometric", "display": "Turbidometric"}
    )
    """
    Turbidometric

    Turbidometric
    """

    zero248 = CodeSystemConcept(
        {
            "code": "0248",
            "definition": "Turbidometric, Refractometric",
            "display": "Refractometric",
        }
    )
    """
    Refractometric

    Turbidometric, Refractometric
    """

    zero249 = CodeSystemConcept(
        {
            "code": "0249",
            "definition": "Chromatography, Thin Layer",
            "display": "Thin layer chromatography (TLC)",
        }
    )
    """
    Thin layer chromatography (TLC)

    Chromatography, Thin Layer
    """

    zero250 = CodeSystemConcept(
        {
            "code": "0250",
            "definition": "Immunoassay, enzyme-multiplied technique (EMIT)",
            "display": "EMIT",
        }
    )
    """
    EMIT

    Immunoassay, enzyme-multiplied technique (EMIT)
    """

    zero251 = CodeSystemConcept(
        {
            "code": "0251",
            "definition": "Flow Cytometry",
            "display": "Flow cytometry (FC)",
        }
    )
    """
    Flow cytometry (FC)

    Flow Cytometry
    """

    zero252 = CodeSystemConcept(
        {
            "code": "0252",
            "definition": "Radial Immunodiffusion",
            "display": "Radial immunodiffusion (RID)",
        }
    )
    """
    Radial immunodiffusion (RID)

    Radial Immunodiffusion
    """

    zero253 = CodeSystemConcept(
        {
            "code": "0253",
            "definition": "Immunoassay, Fluorescence Polarization",
            "display": "Fluorescence polarization immunoassay (FPIA)",
        }
    )
    """
    Fluorescence polarization immunoassay (FPIA)

    Immunoassay, Fluorescence Polarization
    """

    zero254 = CodeSystemConcept(
        {
            "code": "0254",
            "definition": "Electrophoresis, Immunofixation",
            "display": "Immunofixation electrophoresis (IFE)",
        }
    )
    """
    Immunofixation electrophoresis (IFE)

    Electrophoresis, Immunofixation
    """

    zero255 = CodeSystemConcept(
        {
            "code": "0255",
            "definition": "Dialysis, Direct Equilibrium",
            "display": "Equilibrium dialysis",
        }
    )
    """
    Equilibrium dialysis

    Dialysis, Direct Equilibrium
    """

    zero256 = CodeSystemConcept(
        {
            "code": "0256",
            "definition": "Acid Elution, Kleihauer-Betke Method",
            "display": "Kleihauer-Betke acid elution",
        }
    )
    """
    Kleihauer-Betke acid elution

    Acid Elution, Kleihauer-Betke Method
    """

    zero257 = CodeSystemConcept(
        {
            "code": "0257",
            "definition": "Immunofluorescence, Anti-Complement",
            "display": "Anti-complement immunofluorescence (ACIF)",
        }
    )
    """
    Anti-complement immunofluorescence (ACIF)

    Immunofluorescence, Anti-Complement
    """

    zero258 = CodeSystemConcept(
        {
            "code": "0258",
            "definition": "Gas Chromatography/Mass Spectroscopy",
            "display": "GC/MS",
        }
    )
    """
    GC/MS

    Gas Chromatography/Mass Spectroscopy
    """

    zero259 = CodeSystemConcept(
        {
            "code": "0259",
            "definition": "Light Scatter, Nephelometry",
            "display": "Nephelometry",
        }
    )
    """
    Nephelometry

    Light Scatter, Nephelometry
    """

    zero260 = CodeSystemConcept(
        {
            "code": "0260",
            "definition": "Immunoassay, IgE Antibody Test",
            "display": "IgE immunoassay antibody",
        }
    )
    """
    IgE immunoassay antibody

    Immunoassay, IgE Antibody Test
    """

    zero261 = CodeSystemConcept(
        {
            "code": "0261",
            "definition": "Lymphocyte Microcytotoxicity Assay",
            "display": "Lymphocyte Microcytotoxicity Assay",
        }
    )
    """
    Lymphocyte Microcytotoxicity Assay

    Lymphocyte Microcytotoxicity Assay
    """

    zero262 = CodeSystemConcept(
        {
            "code": "0262",
            "definition": "Spectrophotometry",
            "display": "Spectrophotometry",
        }
    )
    """
    Spectrophotometry

    Spectrophotometry
    """

    zero263 = CodeSystemConcept(
        {
            "code": "0263",
            "definition": "Spectrophotometry, Atomic Absorption",
            "display": "Atomic absorption spectrophotometry (AAS)",
        }
    )
    """
    Atomic absorption spectrophotometry (AAS)

    Spectrophotometry, Atomic Absorption
    """

    zero264 = CodeSystemConcept(
        {
            "code": "0264",
            "definition": "Electrochemical, Ion Selective Electrode",
            "display": "Ion selective electrode (ISE)",
        }
    )
    """
    Ion selective electrode (ISE)

    Electrochemical, Ion Selective Electrode
    """

    zero265 = CodeSystemConcept(
        {
            "code": "0265",
            "definition": "Chromatography, Gas",
            "display": "Gas chromatography (GC)",
        }
    )
    """
    Gas chromatography (GC)

    Chromatography, Gas
    """

    zero266 = CodeSystemConcept(
        {
            "code": "0266",
            "definition": "Isoelectric Focusing",
            "display": "Isoelectric focusing (IEF)",
        }
    )
    """
    Isoelectric focusing (IEF)

    Isoelectric Focusing
    """

    zero267 = CodeSystemConcept(
        {
            "code": "0267",
            "definition": "Immunoassay, Chemiluminescent",
            "display": "Immunochemiluminescence",
        }
    )
    """
    Immunochemiluminescence

    Immunoassay, Chemiluminescent
    """

    zero268 = CodeSystemConcept(
        {
            "code": "0268",
            "definition": "Immunoassay, Microparticle Enzyme",
            "display": "Microparticle enzyme immunoassay (MEIA)",
        }
    )
    """
    Microparticle enzyme immunoassay (MEIA)

    Immunoassay, Microparticle Enzyme
    """

    zero269 = CodeSystemConcept(
        {
            "code": "0269",
            "definition": "Inductively-Coupled Plasma/Mass Spectrometry",
            "display": "ICP/MS",
        }
    )
    """
    ICP/MS

    Inductively-Coupled Plasma/Mass Spectrometry
    """

    zero270 = CodeSystemConcept(
        {
            "code": "0270",
            "definition": "Immunoassay, Immunoradiometric Assay",
            "display": "Immunoradiometric assay (IRMA)",
        }
    )
    """
    Immunoradiometric assay (IRMA)

    Immunoassay, Immunoradiometric Assay
    """

    zero271 = CodeSystemConcept(
        {
            "code": "0271",
            "definition": "Coagulation, Photo Optical Clot Detection",
            "display": "Photo optical clot detection",
        }
    )
    """
    Photo optical clot detection

    Coagulation, Photo Optical Clot Detection
    """

    zero280 = CodeSystemConcept(
        {
            "code": "0280",
            "concept": [
                {
                    "code": "0240",
                    "definition": "Susceptibility, Antibiotic sensitivity, disk",
                    "display": "Antibiotic sensitivity, disk",
                },
                {
                    "code": "0241",
                    "definition": "Susceptibility, BACTEC susceptibility test",
                    "display": "BACTEC susceptibility test",
                },
                {
                    "code": "0242",
                    "definition": "Susceptibility, Disk dilution",
                    "display": "Disk dilution",
                },
                {
                    "code": "0272",
                    "concept": [
                        {
                            "code": "0245",
                            "definition": "Susceptibility, Minimum Inhibitory concentration, macrodilution",
                            "display": "Minimum Inhibitory Concentration, macrodilution",
                        },
                        {
                            "code": "0246",
                            "definition": "Susceptibility, Minimum Inhibitory concentration, microdilution",
                            "display": "Minimum Inhibitory Concentration, microdilution",
                        },
                    ],
                    "definition": "Testing to measure the minimum concentration of the antibacterial agent in a given culture medium below which bacterial growth is not inhibited.",
                    "display": "Minimum Inhibitory Concentration",
                },
                {
                    "code": "0273",
                    "definition": "Viral Genotype Susceptibility",
                    "display": "Viral Genotype Susceptibility",
                },
                {
                    "code": "0274",
                    "definition": "Viral Phenotype Susceptibility",
                    "display": "Viral Phenotype Susceptibility",
                },
                {
                    "code": "0275",
                    "definition": "Gradient Strip",
                    "display": "Gradient Strip",
                },
                {
                    "code": "0275a",
                    "definition": "Minimum Lethal Concentration (MLC)",
                    "display": "Minimum Lethal Concentration (MLC)",
                },
                {
                    "code": "0276",
                    "definition": "Testing to measure the minimum concentration of the antibacterial agent in a given culture medium below which bacterial growth is not inhibited.",
                    "display": "Slow Mycobacteria Susceptibility",
                },
                {
                    "code": "0277",
                    "definition": "Serum bactericidal titer",
                    "display": "Serum bactericidal titer",
                },
                {"code": "0278", "definition": "Agar screen", "display": "Agar screen"},
                {
                    "code": "0279",
                    "definition": "Disk induction",
                    "display": "Disk induction",
                },
            ],
            "definition": "Test methods designed to determine a microorganismaTMs susceptibility to being killed by an antibiotic.",
            "display": "Susceptibility Testing",
        }
    )
    """
    Susceptibility Testing

    Test methods designed to determine a microorganismaTMs susceptibility to being killed by an antibiotic.
    """

    zero127 = CodeSystemConcept(
        {
            "code": "0127",
            "definition": "Molecular, Nucleic acid probe",
            "display": "Nucleic acid probe",
            "property": [{"code": "status", "valueCode": "retired"}],
        }
    )
    """
    Nucleic acid probe

    Molecular, Nucleic acid probe
    """

    class Meta:
        resource = _resource
