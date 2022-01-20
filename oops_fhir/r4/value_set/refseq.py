from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["REFSEQ"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class REFSEQ(ValueSet):
    """
    R e f s e q

    REFSEQ : National Center for Biotechnology Information (NCBI) Reference
Sequences

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/ref-sequences
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
