from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["MeasurePopulationType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class MeasurePopulationType:
    """
    MeasurePopulationType

    The type of population.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/measure-population
    """

    initial_population = CodeSystemConcept(
        {
            "code": "initial-population",
            "definition": "The initial population refers to all patients or events to be evaluated by a quality measure involving patients who share a common set of specified characterstics. All patients or events counted (for example, as numerator, as denominator) are drawn from the initial population.",
            "display": "Initial Population",
        }
    )
    """
    Initial Population

    The initial population refers to all patients or events to be evaluated by a quality measure involving patients who share a common set of specified characterstics. All patients or events counted (for example, as numerator, as denominator) are drawn from the initial population.
    """

    numerator = CodeSystemConcept(
        {
            "code": "numerator",
            "definition": "The upper portion of a fraction used to calculate a rate, proportion, or ratio. Also called the measure focus, it is the target process, condition, event, or outcome. Numerator criteria are the processes or outcomes expected for each patient, or event defined in the denominator. A numerator statement describes the clinical action that satisfies the conditions of the measure.",
            "display": "Numerator",
        }
    )
    """
    Numerator

    The upper portion of a fraction used to calculate a rate, proportion, or ratio. Also called the measure focus, it is the target process, condition, event, or outcome. Numerator criteria are the processes or outcomes expected for each patient, or event defined in the denominator. A numerator statement describes the clinical action that satisfies the conditions of the measure.
    """

    numerator_exclusion = CodeSystemConcept(
        {
            "code": "numerator-exclusion",
            "definition": "Numerator exclusion criteria define patients or events to be removed from the numerator. Numerator exclusions are used in proportion and ratio measures to help narrow the numerator (for inverted measures).",
            "display": "Numerator Exclusion",
        }
    )
    """
    Numerator Exclusion

    Numerator exclusion criteria define patients or events to be removed from the numerator. Numerator exclusions are used in proportion and ratio measures to help narrow the numerator (for inverted measures).
    """

    denominator = CodeSystemConcept(
        {
            "code": "denominator",
            "definition": "The lower portion of a fraction used to calculate a rate, proportion, or ratio. The denominator can be the same as the initial population, or a subset of the initial population to further constrain the population for the purpose of the measure.",
            "display": "Denominator",
        }
    )
    """
    Denominator

    The lower portion of a fraction used to calculate a rate, proportion, or ratio. The denominator can be the same as the initial population, or a subset of the initial population to further constrain the population for the purpose of the measure.
    """

    denominator_exclusion = CodeSystemConcept(
        {
            "code": "denominator-exclusion",
            "definition": "Denominator exclusion criteria define patients or events that should be removed from the denominator before determining if numerator criteria are met. Denominator exclusions are used in proportion and ratio measures to help narrow the denominator. For example, patients with bilateral lower extremity amputations would be listed as a denominator exclusion for a measure requiring foot exams.",
            "display": "Denominator Exclusion",
        }
    )
    """
    Denominator Exclusion

    Denominator exclusion criteria define patients or events that should be removed from the denominator before determining if numerator criteria are met. Denominator exclusions are used in proportion and ratio measures to help narrow the denominator. For example, patients with bilateral lower extremity amputations would be listed as a denominator exclusion for a measure requiring foot exams.
    """

    denominator_exception = CodeSystemConcept(
        {
            "code": "denominator-exception",
            "definition": "Denominator exceptions are conditions that should remove a patient or event from the denominator of a measure only if the numerator criteria are not met. Denominator exception allows for adjustment of the calculated score for those providers with higher risk populations. Denominator exception criteria are only used in proportion measures.",
            "display": "Denominator Exception",
        }
    )
    """
    Denominator Exception

    Denominator exceptions are conditions that should remove a patient or event from the denominator of a measure only if the numerator criteria are not met. Denominator exception allows for adjustment of the calculated score for those providers with higher risk populations. Denominator exception criteria are only used in proportion measures.
    """

    measure_population = CodeSystemConcept(
        {
            "code": "measure-population",
            "definition": "Measure population criteria define the patients or events for which the individual observation for the measure should be taken. Measure populations are used for continuous variable measures rather than numerator and denominator criteria.",
            "display": "Measure Population",
        }
    )
    """
    Measure Population

    Measure population criteria define the patients or events for which the individual observation for the measure should be taken. Measure populations are used for continuous variable measures rather than numerator and denominator criteria.
    """

    measure_population_exclusion = CodeSystemConcept(
        {
            "code": "measure-population-exclusion",
            "definition": "Measure population criteria define the patients or events that should be removed from the measure population before determining the outcome of one or more continuous variables defined for the measure observation. Measure population exclusion criteria are used within continuous variable measures to help narrow the measure population.",
            "display": "Measure Population Exclusion",
        }
    )
    """
    Measure Population Exclusion

    Measure population criteria define the patients or events that should be removed from the measure population before determining the outcome of one or more continuous variables defined for the measure observation. Measure population exclusion criteria are used within continuous variable measures to help narrow the measure population.
    """

    measure_observation = CodeSystemConcept(
        {
            "code": "measure-observation",
            "definition": "Defines the individual observation to be performed for each patient or event in the measure population. Measure observations for each case in the population are aggregated to determine the overall measure score for the population.",
            "display": "Measure Observation",
        }
    )
    """
    Measure Observation

    Defines the individual observation to be performed for each patient or event in the measure population. Measure observations for each case in the population are aggregated to determine the overall measure score for the population.
    """

    class Meta:
        resource = _resource
