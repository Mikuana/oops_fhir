from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3IntegrityCheckAlgorithm"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3IntegrityCheckAlgorithm:
    """
    v3 Code System IntegrityCheckAlgorithm

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-IntegrityCheckAlgorithm
    """

    sha_1 = CodeSystemConcept(
        {
            "code": "SHA-1",
            "definition": "This algorithm is defined in FIPS PUB 180-1: Secure Hash Standard.  As of April 17, 1995.",
            "display": "secure hash algorithm - 1",
        }
    )
    """
    secure hash algorithm - 1

    This algorithm is defined in FIPS PUB 180-1: Secure Hash Standard.  As of April 17, 1995.
    """

    sha_256 = CodeSystemConcept(
        {
            "code": "SHA-256",
            "definition": "This algorithm is defined in FIPS PUB 180-2: Secure Hash Standard.",
            "display": "secure hash algorithm - 256",
        }
    )
    """
    secure hash algorithm - 256

    This algorithm is defined in FIPS PUB 180-2: Secure Hash Standard.
    """

    class Meta:
        resource = _resource
