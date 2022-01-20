from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.snomed_ct import SNOMEDCT


__all__ = ["ObservationMethods"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ObservationMethods(ValueSet):
    """
    Observation Methods

    Observation Method codes from [SNOMED CT](http://snomed.info/sct) where
concept is-a 272394005 (Technique (qualifier value)) or is-a 129264002
(Action (qualifier value)) or is-a 386053000 (Evaluation
procedure(procedure))

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/observation-methods
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
