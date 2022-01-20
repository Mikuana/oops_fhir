from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.snomed_ct import SNOMEDCT


__all__ = ["ProcedureNotPerformedReasonSNOMEDCT"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ProcedureNotPerformedReasonSNOMEDCT(ValueSet):
    """
    Procedure Not Performed Reason (SNOMED-CT)

    Situation codes describing the reason that a procedure, which might
otherwise be expected, was not performed, or a procedure that was
started and was not completed. Consists of SNOMED CT codes, children of
procedure contraindicated (183932001), procedure discontinued
(416406003), procedure not done (416237000), procedure not indicated
(428119001), procedure not offered (416064006), procedure not wanted
(416432009), procedure refused (183944003), and procedure stopped
(394908001).

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/procedure-not-performed-reason
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
