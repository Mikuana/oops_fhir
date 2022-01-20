from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3CompressionAlgorithm"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3CompressionAlgorithm:
    """
    v3 Code System CompressionAlgorithm

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-CompressionAlgorithm
    """

    bz = CodeSystemConcept(
        {
            "code": "BZ",
            "definition": "bzip-2 compression format. See [http://www.bzip.org/] for more information.",
            "display": "bzip",
        }
    )
    """
    bzip

    bzip-2 compression format. See [http://www.bzip.org/] for more information.
    """

    df = CodeSystemConcept(
        {
            "code": "DF",
            "definition": "The deflate compressed data format as specified in RFC 1951 [http://www.ietf.org/rfc/rfc1951.txt].",
            "display": "deflate",
        }
    )
    """
    deflate

    The deflate compressed data format as specified in RFC 1951 [http://www.ietf.org/rfc/rfc1951.txt].
    """

    gz = CodeSystemConcept(
        {
            "code": "GZ",
            "definition": "A compressed data format that is compatible with the widely used GZIP utility as specified in RFC 1952 [http://www.ietf.org/rfc/rfc1952.txt] (uses the deflate algorithm).",
            "display": "gzip",
        }
    )
    """
    gzip

    A compressed data format that is compatible with the widely used GZIP utility as specified in RFC 1952 [http://www.ietf.org/rfc/rfc1952.txt] (uses the deflate algorithm).
    """

    z = CodeSystemConcept(
        {
            "code": "Z",
            "definition": "Original UNIX compress algorithm and file format using the LZC algorithm (a variant of LZW).  Patent encumbered and less efficient than deflate.",
            "display": "compress",
        }
    )
    """
    compress

    Original UNIX compress algorithm and file format using the LZC algorithm (a variant of LZW).  Patent encumbered and less efficient than deflate.
    """

    z7 = CodeSystemConcept(
        {
            "code": "Z7",
            "definition": "7z compression file format. See [http://www.7-zip.org/7z.html] for more information.",
            "display": "Z7",
        }
    )
    """
    Z7

    7z compression file format. See [http://www.7-zip.org/7z.html] for more information.
    """

    zl = CodeSystemConcept(
        {
            "code": "ZL",
            "definition": "A compressed data format that also uses the deflate algorithm.  Specified as RFC 1950 [http://www.ietf.org/rfc/rfc1952.txt]",
            "display": "zlib",
        }
    )
    """
    zlib

    A compressed data format that also uses the deflate algorithm.  Specified as RFC 1950 [http://www.ietf.org/rfc/rfc1952.txt]
    """

    class Meta:
        resource = _resource
