from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.statistics_code import StatisticsCode as StatisticsCode_


__all__ = ["StatisticsCode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class StatisticsCode(StatisticsCode_):
    """
    StatisticsCode

    The statistical operation parameter -"statistic" codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/observation-statistics
    """

    class Meta:
        resource = _resource
