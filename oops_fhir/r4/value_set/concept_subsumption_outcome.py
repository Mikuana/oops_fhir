from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.concept_subsumption_outcome import (
    ConceptSubsumptionOutcome as ConceptSubsumptionOutcome_,
)


__all__ = ["ConceptSubsumptionOutcome"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ConceptSubsumptionOutcome(ConceptSubsumptionOutcome_):
    """
    ConceptSubsumptionOutcome

    The subsumption relationship between code/Coding "A" and code/Coding
"B". There are 4 possible codes to be returned: equivalent, subsumes,
subsumed-by, and not-subsumed. If the server is unable to determine the
relationship between the codes/Codings, then it returns an error (i.e.
an OperationOutcome).

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/concept-subsumption-outcome
    """

    class Meta:
        resource = _resource
