from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["v3SecurityControlObservationValue"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3SecurityControlObservationValue(ValueSet):
    """
    V3 Value SetSecurityControlObservationValue

     Security observation values used to indicate security control metadata.
V:SecurityControl is the union of V:SecurityPolicy,V:ObligationPolicy,
V:RefrainPolicy, V:PurposeOfUse, and V:GeneralPurpose of Use used to
populate the SecurityControlObservationValue attribute in order to
convey one or more nonhierarchical security control metadata dictating
handling caveats, purpose of use, dissemination controls and other
refrain policies, and obligations to which a custodian or receiver is
required to comply.

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-SecurityControlObservationValue
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
