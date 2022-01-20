from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["StatisticsCode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class StatisticsCode:
    """
    StatisticsCode

    The statistical operation parameter -"statistic" codes.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/observation-statistics
    """

    average = CodeSystemConcept(
        {
            "code": "average",
            "definition": "The [mean](https://en.wikipedia.org/wiki/Arithmetic_mean) of N measurements over the stated period.",
            "display": "Average",
        }
    )
    """
    Average

    The [mean](https://en.wikipedia.org/wiki/Arithmetic_mean) of N measurements over the stated period.
    """

    maximum = CodeSystemConcept(
        {
            "code": "maximum",
            "definition": "The [maximum](https://en.wikipedia.org/wiki/Maximal_element) value of N measurements over the stated period.",
            "display": "Maximum",
        }
    )
    """
    Maximum

    The [maximum](https://en.wikipedia.org/wiki/Maximal_element) value of N measurements over the stated period.
    """

    minimum = CodeSystemConcept(
        {
            "code": "minimum",
            "definition": "The [minimum](https://en.wikipedia.org/wiki/Minimal_element) value of N measurements over the stated period.",
            "display": "Minimum",
        }
    )
    """
    Minimum

    The [minimum](https://en.wikipedia.org/wiki/Minimal_element) value of N measurements over the stated period.
    """

    count = CodeSystemConcept(
        {
            "code": "count",
            "definition": "The [number] of valid measurements over the stated period that contributed to the other statistical outputs.",
            "display": "Count",
        }
    )
    """
    Count

    The [number] of valid measurements over the stated period that contributed to the other statistical outputs.
    """

    total_count = CodeSystemConcept(
        {
            "code": "total-count",
            "definition": "The total [number] of valid measurements over the stated period, including observations that were ignored because they did not contain valid result values.",
            "display": "Total Count",
        }
    )
    """
    Total Count

    The total [number] of valid measurements over the stated period, including observations that were ignored because they did not contain valid result values.
    """

    median = CodeSystemConcept(
        {
            "code": "median",
            "definition": "The [median](https://en.wikipedia.org/wiki/Median) of N measurements over the stated period.",
            "display": "Median",
        }
    )
    """
    Median

    The [median](https://en.wikipedia.org/wiki/Median) of N measurements over the stated period.
    """

    std_dev = CodeSystemConcept(
        {
            "code": "std-dev",
            "definition": "The [standard deviation](https://en.wikipedia.org/wiki/Standard_deviation) of N measurements over the stated period.",
            "display": "Standard Deviation",
        }
    )
    """
    Standard Deviation

    The [standard deviation](https://en.wikipedia.org/wiki/Standard_deviation) of N measurements over the stated period.
    """

    sum_ = CodeSystemConcept(
        {
            "code": "sum",
            "definition": "The [sum](https://en.wikipedia.org/wiki/Summation) of N measurements over the stated period.",
            "display": "Sum",
        }
    )
    """
    Sum

    The [sum](https://en.wikipedia.org/wiki/Summation) of N measurements over the stated period.
    """

    variance = CodeSystemConcept(
        {
            "code": "variance",
            "definition": "The [variance](https://en.wikipedia.org/wiki/Variance) of N measurements over the stated period.",
            "display": "Variance",
        }
    )
    """
    Variance

    The [variance](https://en.wikipedia.org/wiki/Variance) of N measurements over the stated period.
    """

    two0_percent = CodeSystemConcept(
        {
            "code": "20-percent",
            "definition": "The 20th [Percentile](https://en.wikipedia.org/wiki/Percentile) of N measurements over the stated period.",
            "display": "20th Percentile",
        }
    )
    """
    20th Percentile

    The 20th [Percentile](https://en.wikipedia.org/wiki/Percentile) of N measurements over the stated period.
    """

    eight0_percent = CodeSystemConcept(
        {
            "code": "80-percent",
            "definition": "The 80th [Percentile](https://en.wikipedia.org/wiki/Percentile) of N measurements over the stated period.",
            "display": "80th Percentile",
        }
    )
    """
    80th Percentile

    The 80th [Percentile](https://en.wikipedia.org/wiki/Percentile) of N measurements over the stated period.
    """

    four_lower = CodeSystemConcept(
        {
            "code": "4-lower",
            "definition": "The lower [Quartile](https://en.wikipedia.org/wiki/Quartile) Boundary of N measurements over the stated period.",
            "display": "Lower Quartile",
        }
    )
    """
    Lower Quartile

    The lower [Quartile](https://en.wikipedia.org/wiki/Quartile) Boundary of N measurements over the stated period.
    """

    four_upper = CodeSystemConcept(
        {
            "code": "4-upper",
            "definition": "The upper [Quartile](https://en.wikipedia.org/wiki/Quartile) Boundary of N measurements over the stated period.",
            "display": "Upper Quartile",
        }
    )
    """
    Upper Quartile

    The upper [Quartile](https://en.wikipedia.org/wiki/Quartile) Boundary of N measurements over the stated period.
    """

    four_dev = CodeSystemConcept(
        {
            "code": "4-dev",
            "definition": "The difference between the upper and lower [Quartiles](https://en.wikipedia.org/wiki/Quartile) is called the Interquartile range. (IQR = Q3-Q1) Quartile deviation or Semi-interquartile range is one-half the difference between the first and the third quartiles.",
            "display": "Quartile Deviation",
        }
    )
    """
    Quartile Deviation

    The difference between the upper and lower [Quartiles](https://en.wikipedia.org/wiki/Quartile) is called the Interquartile range. (IQR = Q3-Q1) Quartile deviation or Semi-interquartile range is one-half the difference between the first and the third quartiles.
    """

    five_1 = CodeSystemConcept(
        {
            "code": "5-1",
            "definition": "The lowest of four values that divide the N measurements into a frequency distribution of five classes with each containing one fifth of the total population.",
            "display": "1st Quintile",
        }
    )
    """
    1st Quintile

    The lowest of four values that divide the N measurements into a frequency distribution of five classes with each containing one fifth of the total population.
    """

    five_2 = CodeSystemConcept(
        {
            "code": "5-2",
            "definition": "The second of four values that divide the N measurements into a frequency distribution of five classes with each containing one fifth of the total population.",
            "display": "2nd Quintile",
        }
    )
    """
    2nd Quintile

    The second of four values that divide the N measurements into a frequency distribution of five classes with each containing one fifth of the total population.
    """

    five_3 = CodeSystemConcept(
        {
            "code": "5-3",
            "definition": "The third of four values that divide the N measurements into a frequency distribution of five classes with each containing one fifth of the total population.",
            "display": "3rd Quintile",
        }
    )
    """
    3rd Quintile

    The third of four values that divide the N measurements into a frequency distribution of five classes with each containing one fifth of the total population.
    """

    five_4 = CodeSystemConcept(
        {
            "code": "5-4",
            "definition": "The fourth of four values that divide the N measurements into a frequency distribution of five classes with each containing one fifth of the total population.",
            "display": "4th Quintile",
        }
    )
    """
    4th Quintile

    The fourth of four values that divide the N measurements into a frequency distribution of five classes with each containing one fifth of the total population.
    """

    skew = CodeSystemConcept(
        {
            "code": "skew",
            "definition": "Skewness is a measure of the asymmetry of the probability distribution of a real-valued random variable about its mean. The skewness value can be positive or negative, or even undefined.  Source: [Wikipedia](https://en.wikipedia.org/wiki/Skewness).",
            "display": "Skew",
        }
    )
    """
    Skew

    Skewness is a measure of the asymmetry of the probability distribution of a real-valued random variable about its mean. The skewness value can be positive or negative, or even undefined.  Source: [Wikipedia](https://en.wikipedia.org/wiki/Skewness).
    """

    kurtosis = CodeSystemConcept(
        {
            "code": "kurtosis",
            "definition": 'Kurtosis  is a measure of the "tailedness" of the probability distribution of a real-valued random variable.   Source: [Wikipedia](https://en.wikipedia.org/wiki/Kurtosis).',
            "display": "Kurtosis",
        }
    )
    """
    Kurtosis

    Kurtosis  is a measure of the "tailedness" of the probability distribution of a real-valued random variable.   Source: [Wikipedia](https://en.wikipedia.org/wiki/Kurtosis).
    """

    regression = CodeSystemConcept(
        {
            "code": "regression",
            "definition": "Linear regression is an approach for modeling two-dimensional sample points with one independent variable and one dependent variable (conventionally, the x and y coordinates in a Cartesian coordinate system) and finds a linear function (a non-vertical straight line) that, as accurately as possible, predicts the dependent variable values as a function of the independent variables. Source: [Wikipedia](https://en.wikipedia.org/wiki/Simple_linear_regression)  This Statistic code will return both a gradient and an intercept value.",
            "display": "Regression",
        }
    )
    """
    Regression

    Linear regression is an approach for modeling two-dimensional sample points with one independent variable and one dependent variable (conventionally, the x and y coordinates in a Cartesian coordinate system) and finds a linear function (a non-vertical straight line) that, as accurately as possible, predicts the dependent variable values as a function of the independent variables. Source: [Wikipedia](https://en.wikipedia.org/wiki/Simple_linear_regression)  This Statistic code will return both a gradient and an intercept value.
    """

    class Meta:
        resource = _resource
