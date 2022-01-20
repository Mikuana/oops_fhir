from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.snomed_ct import SNOMEDCT


__all__ = ["DataElementSDCObjectClass"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class DataElementSDCObjectClass(SNOMEDCT):
    """
    DataElement SDC Object Class

    The allowed codes for identifying the ISO 11179 ObjectClass Property for
a particular data element if intended for registration/use within the
U.S. Structured Data Capture (SDC) project.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/dataelement-sdcobjectclassproperty
    """

    class Meta:
        resource = _resource
