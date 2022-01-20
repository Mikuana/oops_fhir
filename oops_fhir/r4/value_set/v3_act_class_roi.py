from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_class import v3ActClass


__all__ = ["v3ActClassROI"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ActClassROI(v3ActClass):
    """
    V3 Value SetActClassROI

     Regions of Interest (ROI) within a subject Act. Primarily used for
making secondary observations on a subset of a subject observation. The
relationship between a ROI and its referenced Act is specified through
an ActRelationship of type "subject" (SUBJ), which must always be
present.

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-ActClassROI
    """

    class Meta:
        resource = _resource
