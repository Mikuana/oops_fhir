from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_work_classification_odh import (
    v3WorkClassificationODH as v3WorkClassificationODH_,
)


__all__ = ["v3WorkClassificationODH"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3WorkClassificationODH(v3WorkClassificationODH_):
    """
    v3 Code System WorkClassificationODH

     Code system of concepts representing a person's job type as defined by
compensation and sector (e.g. paid vs. unpaid, self-employed vs. not
self-employed, government vs. private, etc.).

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-WorkClassificationODH
    """

    class Meta:
        resource = _resource
