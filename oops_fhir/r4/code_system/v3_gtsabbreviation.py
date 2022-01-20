from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3GTSAbbreviation"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3GTSAbbreviation:
    """
    v3 Code System GTSAbbreviation

      Open Issue:  It appears that the printnames are suboptimal and should
be improved for many of the existing codes.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-GTSAbbreviation
    """

    am = CodeSystemConcept(
        {
            "code": "AM",
            "definition": "Every morning at institution specified times.",
            "display": "AM",
        }
    )
    """
    AM

    Every morning at institution specified times.
    """

    bed = CodeSystemConcept(
        {
            "code": "BED",
            "definition": "At bedtime (institution specified time).",
            "display": "at bedtime",
        }
    )
    """
    at bedtime

    At bedtime (institution specified time).
    """

    bid = CodeSystemConcept(
        {
            "code": "BID",
            "definition": "Two times a day at institution specified time",
            "display": "BID",
        }
    )
    """
    BID

    Two times a day at institution specified time
    """

    jb = CodeSystemConcept(
        {
            "code": "JB",
            "definition": "Regular business days (Monday to Friday excluding holidays)",
            "display": "JB",
        }
    )
    """
    JB

    Regular business days (Monday to Friday excluding holidays)
    """

    je = CodeSystemConcept(
        {
            "code": "JE",
            "definition": "Regular weekends (Saturday and Sunday excluding holidays)",
            "display": "JE",
        }
    )
    """
    JE

    Regular weekends (Saturday and Sunday excluding holidays)
    """

    jh = CodeSystemConcept(
        {
            "code": "JH",
            "concept": [
                {
                    "code": "_GTSAbbreviationHolidaysChristianRoman",
                    "concept": [
                        {
                            "code": "JHCHREAS",
                            "definition": "Easter Sunday.  The Easter date is a rather complex calculation based on Astronomical tables describing full moon dates.  Details can be found at [http://www.assa.org.au/edm.html, and http://aa.usno.navy.mil/AA/faq/docs/easter.html].  Note that the Christian Orthodox Holidays are based on the Julian calendar.",
                            "display": "JHCHREAS",
                        },
                        {
                            "code": "JHCHRGFR",
                            "definition": "Good Friday, is the Friday right before Easter Sunday.",
                            "display": "JHCHRGFR",
                        },
                        {
                            "code": "JHCHRNEW",
                            "definition": "New Year's Day (January 1)",
                            "display": "JHCHRNEW",
                        },
                        {
                            "code": "JHCHRPEN",
                            "definition": "Pentecost Sunday, is seven weeks after Easter (the 50th day of Easter).",
                            "display": "JHCHRPEN",
                        },
                        {
                            "code": "JHCHRXME",
                            "definition": "Christmas Eve (December 24)",
                            "display": "JHCHRXME",
                        },
                        {
                            "code": "JHCHRXMS",
                            "definition": "Christmas Day (December 25)",
                            "display": "JHCHRXMS",
                        },
                    ],
                    "definition": "Christian Holidays (Roman/Gregorian [Western] Tradition.)",
                    "display": "GTSAbbreviationHolidaysChristianRoman",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "JHNNL",
                    "concept": [
                        {
                            "code": "JHNNLLD",
                            "definition": "Description:Liberation day  (May 5 every five years)",
                            "display": "Liberation day (May 5 every five years)",
                        },
                        {
                            "code": "JHNNLQD",
                            "definition": "Description:Queen's day (April 30)",
                            "display": "Queen's day (April 30)",
                        },
                        {
                            "code": "JHNNLSK",
                            "definition": "Description:Sinterklaas (December 5)",
                            "display": "Sinterklaas (December 5)",
                        },
                    ],
                    "definition": "Description:The Netherlands National Holidays.",
                    "display": "The Netherlands National Holidays",
                },
                {
                    "code": "JHNUS",
                    "concept": [
                        {
                            "code": "JHNUSCLM",
                            "definition": "Columbus Day, the second Monday in October.",
                            "display": "JHNUSCLM",
                        },
                        {
                            "code": "JHNUSIND",
                            "definition": "Independence Day (4th of July)",
                            "display": "JHNUSIND",
                        },
                        {
                            "code": "JHNUSIND1",
                            "definition": "Alternative Monday after 4th of July Weekend [5 U.S.C. 6103(b)].",
                            "display": "JHNUSIND1",
                        },
                        {
                            "code": "JHNUSIND5",
                            "definition": "Alternative Friday before 4th of July Weekend [5 U.S.C. 6103(b)].",
                            "display": "JHNUSIND5",
                        },
                        {
                            "code": "JHNUSLBR",
                            "definition": "Labor Day, the first Monday in September.",
                            "display": "JHNUSLBR",
                        },
                        {
                            "code": "JHNUSMEM",
                            "definition": "Memorial Day, the last Monday in May.",
                            "display": "JHNUSMEM",
                        },
                        {
                            "code": "JHNUSMEM5",
                            "definition": "Friday before Memorial Day Weekend",
                            "display": "JHNUSMEM5",
                        },
                        {
                            "code": "JHNUSMEM6",
                            "definition": "Saturday of Memorial Day Weekend",
                            "display": "JHNUSMEM6",
                        },
                        {
                            "code": "JHNUSMLK",
                            "definition": "Dr. Martin Luther King, Jr. Day, the third Monday in January.",
                            "display": "JHNUSMLK",
                        },
                        {
                            "code": "JHNUSPRE",
                            "definition": "Washington's Birthday (Presidential Day) the third Monday in February.",
                            "display": "JHNUSPRE",
                        },
                        {
                            "code": "JHNUSTKS",
                            "definition": "Thanksgiving Day, the fourth Thursday in November.",
                            "display": "JHNUSTKS",
                        },
                        {
                            "code": "JHNUSTKS5",
                            "definition": "Friday after Thanksgiving.",
                            "display": "JHNUSTKS5",
                        },
                        {
                            "code": "JHNUSVET",
                            "definition": "Veteran's Day, November 11.",
                            "display": "JHNUSVET",
                        },
                    ],
                    "definition": "United States National Holidays (public holidays for federal employees established by U.S. Federal law 5 U.S.C. 6103).",
                    "display": "GTSAbbreviationHolidaysUSNational",
                },
            ],
            "definition": "Holidays",
            "display": "GTSAbbreviationHolidays",
        }
    )
    """
    GTSAbbreviationHolidays

    Holidays
    """

    mo = CodeSystemConcept(
        {
            "code": "MO",
            "definition": "Monthly at institution specified time.",
            "display": "monthly",
        }
    )
    """
    monthly

    Monthly at institution specified time.
    """

    pm = CodeSystemConcept(
        {
            "code": "PM",
            "definition": "Every afternoon at institution specified times.",
            "display": "PM",
        }
    )
    """
    PM

    Every afternoon at institution specified times.
    """

    q1_h = CodeSystemConcept(
        {
            "code": "Q1H",
            "definition": "Every hour at institution specified times.",
            "display": "every hour",
        }
    )
    """
    every hour

    Every hour at institution specified times.
    """

    q2_h = CodeSystemConcept(
        {
            "code": "Q2H",
            "definition": "Every 2 hours at institution specified times.",
            "display": "every 2 hours",
        }
    )
    """
    every 2 hours

    Every 2 hours at institution specified times.
    """

    q3_h = CodeSystemConcept(
        {
            "code": "Q3H",
            "definition": "Every 3 hours at institution specified times.",
            "display": "every 3 hours",
        }
    )
    """
    every 3 hours

    Every 3 hours at institution specified times.
    """

    q4_h = CodeSystemConcept(
        {
            "code": "Q4H",
            "definition": "Every 4 hours at institution specified time",
            "display": "Q4H",
        }
    )
    """
    Q4H

    Every 4 hours at institution specified time
    """

    q6_h = CodeSystemConcept(
        {
            "code": "Q6H",
            "definition": "Every 6 hours at institution specified time",
            "display": "Q6H",
        }
    )
    """
    Q6H

    Every 6 hours at institution specified time
    """

    q8_h = CodeSystemConcept(
        {
            "code": "Q8H",
            "definition": "Every 8 hours at institution specified times.",
            "display": "every 8 hours",
        }
    )
    """
    every 8 hours

    Every 8 hours at institution specified times.
    """

    qd = CodeSystemConcept(
        {
            "code": "QD",
            "definition": "Every day at institution specified times.",
            "display": "QD",
        }
    )
    """
    QD

    Every day at institution specified times.
    """

    qid = CodeSystemConcept(
        {
            "code": "QID",
            "definition": "Four times a day at institution specified time",
            "display": "QID",
        }
    )
    """
    QID

    Four times a day at institution specified time
    """

    qod = CodeSystemConcept(
        {
            "code": "QOD",
            "definition": "Every other day at institution specified times.",
            "display": "QOD",
        }
    )
    """
    QOD

    Every other day at institution specified times.
    """

    tid = CodeSystemConcept(
        {
            "code": "TID",
            "definition": "Three times a day at institution specified time",
            "display": "TID",
        }
    )
    """
    TID

    Three times a day at institution specified time
    """

    wk = CodeSystemConcept(
        {
            "code": "WK",
            "definition": "Weekly at institution specified time.",
            "display": "weekly",
        }
    )
    """
    weekly

    Weekly at institution specified time.
    """

    class Meta:
        resource = _resource
