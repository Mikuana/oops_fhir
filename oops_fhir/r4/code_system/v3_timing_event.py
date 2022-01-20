from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3TimingEvent"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3TimingEvent:
    """
    v3 Code System TimingEvent

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-TimingEvent
    """

    ac = CodeSystemConcept(
        {
            "code": "AC",
            "definition": "before meal (from lat. ante cibus)",
            "display": "AC",
        }
    )
    """
    AC

    before meal (from lat. ante cibus)
    """

    acd = CodeSystemConcept(
        {
            "code": "ACD",
            "definition": "before lunch (from lat. ante cibus diurnus)",
            "display": "ACD",
        }
    )
    """
    ACD

    before lunch (from lat. ante cibus diurnus)
    """

    acm = CodeSystemConcept(
        {
            "code": "ACM",
            "definition": "before breakfast (from lat. ante cibus matutinus)",
            "display": "ACM",
        }
    )
    """
    ACM

    before breakfast (from lat. ante cibus matutinus)
    """

    acv = CodeSystemConcept(
        {
            "code": "ACV",
            "definition": "before dinner (from lat. ante cibus vespertinus)",
            "display": "ACV",
        }
    )
    """
    ACV

    before dinner (from lat. ante cibus vespertinus)
    """

    c = CodeSystemConcept(
        {
            "code": "C",
            "concept": [
                {
                    "code": "CD",
                    "definition": "Description: lunch (from lat. cibus diurnus)",
                    "display": "CD",
                },
                {
                    "code": "CM",
                    "definition": "Description: breakfast (from lat. cibus matutinus)",
                    "display": "CM",
                },
                {
                    "code": "CV",
                    "definition": "Description: dinner (from lat. cibus vespertinus)",
                    "display": "CV",
                },
            ],
            "definition": "Description: meal (from lat. ante cibus)",
            "display": "C",
        }
    )
    """
    C

    Description: meal (from lat. ante cibus)
    """

    hs = CodeSystemConcept(
        {
            "code": "HS",
            "definition": "Description: Prior to beginning a regular period of extended sleep (this would exclude naps).  Note that this might occur at different times of day depending on a person's regular sleep schedule.",
            "display": "HS",
        }
    )
    """
    HS

    Description: Prior to beginning a regular period of extended sleep (this would exclude naps).  Note that this might occur at different times of day depending on a person's regular sleep schedule.
    """

    ic = CodeSystemConcept(
        {
            "code": "IC",
            "definition": "between meals (from lat. inter cibus)",
            "display": "IC",
        }
    )
    """
    IC

    between meals (from lat. inter cibus)
    """

    icd = CodeSystemConcept(
        {"code": "ICD", "definition": "between lunch and dinner", "display": "ICD"}
    )
    """
    ICD

    between lunch and dinner
    """

    icm = CodeSystemConcept(
        {"code": "ICM", "definition": "between breakfast and lunch", "display": "ICM"}
    )
    """
    ICM

    between breakfast and lunch
    """

    icv = CodeSystemConcept(
        {
            "code": "ICV",
            "definition": "between dinner and the hour of sleep",
            "display": "ICV",
        }
    )
    """
    ICV

    between dinner and the hour of sleep
    """

    pc = CodeSystemConcept(
        {
            "code": "PC",
            "definition": "after meal (from lat. post cibus)",
            "display": "PC",
        }
    )
    """
    PC

    after meal (from lat. post cibus)
    """

    pcd = CodeSystemConcept(
        {
            "code": "PCD",
            "definition": "after lunch (from lat. post cibus diurnus)",
            "display": "PCD",
        }
    )
    """
    PCD

    after lunch (from lat. post cibus diurnus)
    """

    pcm = CodeSystemConcept(
        {
            "code": "PCM",
            "definition": "after breakfast (from lat. post cibus matutinus)",
            "display": "PCM",
        }
    )
    """
    PCM

    after breakfast (from lat. post cibus matutinus)
    """

    pcv = CodeSystemConcept(
        {
            "code": "PCV",
            "definition": "after dinner (from lat. post cibus vespertinus)",
            "display": "PCV",
        }
    )
    """
    PCV

    after dinner (from lat. post cibus vespertinus)
    """

    wake = CodeSystemConcept(
        {
            "code": "WAKE",
            "definition": "Description: Upon waking up from a regular period of sleep, in order to start regular activities (this would exclude waking up from a nap or temporarily waking up during a period of sleep)\r\n\n                        \n                           Usage Notes: e.g.\r\n\n                        Take pulse rate on waking in management of thyrotoxicosis.\r\n\n                        Take BP on waking in management of hypertension\r\n\n                        Take basal body temperature on waking in establishing date of ovulation",
            "display": "WAKE",
        }
    )
    """
    WAKE

    Description: Upon waking up from a regular period of sleep, in order to start regular activities (this would exclude waking up from a nap or temporarily waking up during a period of sleep)

                        
                           Usage Notes: e.g.

                        Take pulse rate on waking in management of thyrotoxicosis.

                        Take BP on waking in management of hypertension

                        Take basal body temperature on waking in establishing date of ovulation
    """

    class Meta:
        resource = _resource
