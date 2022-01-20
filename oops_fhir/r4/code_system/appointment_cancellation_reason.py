from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AppointmentCancellationReason"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AppointmentCancellationReason:
    """
    Appointment cancellation reason

    This example value set defines a set of reasons for the cancellation of
an appointment.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/appointment-cancellation-reason
    """

    pat = CodeSystemConcept(
        {
            "code": "pat",
            "concept": [
                {
                    "code": "pat-crs",
                    "display": "Patient: Canceled via automated reminder system",
                },
                {"code": "pat-cpp", "display": "Patient: Canceled via Patient Portal"},
                {"code": "pat-dec", "display": "Patient: Deceased"},
                {"code": "pat-fb", "display": "Patient: Feeling Better"},
                {"code": "pat-lt", "display": "Patient: Lack of Transportation"},
                {"code": "pat-mt", "display": "Patient: Member Terminated"},
                {"code": "pat-mv", "display": "Patient: Moved"},
                {"code": "pat-preg", "display": "Patient: Pregnant"},
                {"code": "pat-swl", "display": "Patient: Scheduled from Wait List"},
                {"code": "pat-ucp", "display": "Patient: Unhappy/Changed Provider"},
            ],
            "display": "Patient",
        }
    )
    """
    Patient

    
    """

    prov = CodeSystemConcept(
        {
            "code": "prov",
            "concept": [
                {"code": "prov-pers", "display": "Provider: Personal"},
                {"code": "prov-dch", "display": "Provider: Discharged"},
                {"code": "prov-edu", "display": "Provider: Edu/Meeting"},
                {"code": "prov-hosp", "display": "Provider: Hospitalized"},
                {
                    "code": "prov-labs",
                    "display": "Provider: Labs Out of Acceptable Range",
                },
                {
                    "code": "prov-mri",
                    "display": "Provider: MRI Screening Form Marked Do Not Proceed",
                },
                {
                    "code": "prov-onc",
                    "display": "Provider: Oncology Treatment Plan Changes",
                },
            ],
            "display": "Provider",
        }
    )
    """
    Provider

    
    """

    maint = CodeSystemConcept(
        {"code": "maint", "display": "Equipment Maintenance/Repair"}
    )
    """
    Equipment Maintenance/Repair

    
    """

    meds_inc = CodeSystemConcept({"code": "meds-inc", "display": "Prep/Med Incomplete"})
    """
    Prep/Med Incomplete

    
    """

    other = CodeSystemConcept(
        {
            "code": "other",
            "concept": [
                {
                    "code": "oth-cms",
                    "display": "Other: CMS Therapy Cap Service Not Authorized",
                },
                {"code": "oth-err", "display": "Other: Error"},
                {"code": "oth-fin", "display": "Other: Financial"},
                {
                    "code": "oth-iv",
                    "display": "Other: Improper IV Access/Infiltrate IV",
                },
                {"code": "oth-int", "display": "Other: No Interpreter Available"},
                {"code": "oth-mu", "display": "Other: Prep/Med/Results Unavailable"},
                {"code": "oth-room", "display": "Other: Room/Resource Maintenance"},
                {"code": "oth-oerr", "display": "Other: Schedule Order Error"},
                {"code": "oth-swie", "display": "Other: Silent Walk In Error"},
                {"code": "oth-weath", "display": "Other: Weather"},
            ],
            "display": "Other",
        }
    )
    """
    Other

    
    """

    class Meta:
        resource = _resource
