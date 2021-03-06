from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3ProbabilityDistributionType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3ProbabilityDistributionType:
    """
    v3 Code System ProbabilityDistributionType

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-ProbabilityDistributionType
    """

    b = CodeSystemConcept(
        {
            "code": "B",
            "definition": "The beta-distribution is used for data that is bounded on both sides and may or may not be skewed (e.g., occurs when probabilities are estimated.)  Two parameters a and b  are available to adjust the curve.  The mean m and variance s2 relate as follows: m = a/ (a + b) and s2 = ab/((a + b)2 (a + b + 1)).",
            "display": "beta",
        }
    )
    """
    beta

    The beta-distribution is used for data that is bounded on both sides and may or may not be skewed (e.g., occurs when probabilities are estimated.)  Two parameters a and b  are available to adjust the curve.  The mean m and variance s2 relate as follows: m = a/ (a + b) and s2 = ab/((a + b)2 (a + b + 1)).
    """

    e = CodeSystemConcept(
        {
            "code": "E",
            "definition": "Used for data that describes extinction.  The exponential distribution is a special form of g-distribution where a = 1, hence, the relationship to mean m and variance s2 are m = b and s2 = b2.",
            "display": "exponential",
        }
    )
    """
    exponential

    Used for data that describes extinction.  The exponential distribution is a special form of g-distribution where a = 1, hence, the relationship to mean m and variance s2 are m = b and s2 = b2.
    """

    f = CodeSystemConcept(
        {
            "code": "F",
            "definition": "Used to describe the quotient of two c2 random variables.  The F-distribution has two parameters n1 and n2, which are the numbers of degrees of freedom of the numerator and denominator variable respectively. The relationship to mean m  and variance s2 are: m = n2 / (n2 - 2) and s2 = (2 n2 (n2 + n1 - 2)) / (n1 (n2 - 2)2 (n2 - 4)).",
            "display": "F",
        }
    )
    """
    F

    Used to describe the quotient of two c2 random variables.  The F-distribution has two parameters n1 and n2, which are the numbers of degrees of freedom of the numerator and denominator variable respectively. The relationship to mean m  and variance s2 are: m = n2 / (n2 - 2) and s2 = (2 n2 (n2 + n1 - 2)) / (n1 (n2 - 2)2 (n2 - 4)).
    """

    g = CodeSystemConcept(
        {
            "code": "G",
            "definition": "The gamma-distribution used for data that is skewed and bounded to the right, i.e. where the maximum of the distribution curve is located near the origin.  The g-distribution has a two parameters a and b.  The relationship to mean m and variance s2 is m = a b and s2 = a b2.",
            "display": "(gamma)",
        }
    )
    """
    (gamma)

    The gamma-distribution used for data that is skewed and bounded to the right, i.e. where the maximum of the distribution curve is located near the origin.  The g-distribution has a two parameters a and b.  The relationship to mean m and variance s2 is m = a b and s2 = a b2.
    """

    ln = CodeSystemConcept(
        {
            "code": "LN",
            "definition": "The logarithmic normal distribution is used to transform skewed random variable X into a normally distributed random variable U = log X. The log-normal distribution can be specified with the properties mean m and standard deviation s.  Note however that mean m and standard deviation s are the parameters of the raw value distribution, not the transformed parameters of the lognormal distribution that are conventionally referred to by the same letters.  Those log-normal parameters mlog and slog relate to the mean m and standard deviation s of the data value through slog2 = log (s2/m2 + 1) and mlog = log m - slog2/2.",
            "display": "log-normal",
        }
    )
    """
    log-normal

    The logarithmic normal distribution is used to transform skewed random variable X into a normally distributed random variable U = log X. The log-normal distribution can be specified with the properties mean m and standard deviation s.  Note however that mean m and standard deviation s are the parameters of the raw value distribution, not the transformed parameters of the lognormal distribution that are conventionally referred to by the same letters.  Those log-normal parameters mlog and slog relate to the mean m and standard deviation s of the data value through slog2 = log (s2/m2 + 1) and mlog = log m - slog2/2.
    """

    n = CodeSystemConcept(
        {
            "code": "N",
            "definition": 'This is the well-known bell-shaped normal distribution.  Because of the central limit theorem, the normal distribution is the distribution of choice for an unbounded random variable that is an outcome of a combination of many stochastic processes.  Even for values bounded on a single side (i.e. greater than 0) the normal distribution may be accurate enough if the mean is "far away" from the bound of the scale measured in terms of standard deviations.',
            "display": "normal (Gaussian)",
        }
    )
    """
    normal (Gaussian)

    This is the well-known bell-shaped normal distribution.  Because of the central limit theorem, the normal distribution is the distribution of choice for an unbounded random variable that is an outcome of a combination of many stochastic processes.  Even for values bounded on a single side (i.e. greater than 0) the normal distribution may be accurate enough if the mean is "far away" from the bound of the scale measured in terms of standard deviations.
    """

    t = CodeSystemConcept(
        {
            "code": "T",
            "definition": "Used to describe the quotient of a normal random variable and the square root of a c2 random variable.  The t-distribution has one parameter n, the number of degrees of freedom. The relationship to mean m  and variance s2 are: m = 0 and s2 = n / (n - 2)",
            "display": "T",
        }
    )
    """
    T

    Used to describe the quotient of a normal random variable and the square root of a c2 random variable.  The t-distribution has one parameter n, the number of degrees of freedom. The relationship to mean m  and variance s2 are: m = 0 and s2 = n / (n - 2)
    """

    u = CodeSystemConcept(
        {
            "code": "U",
            "definition": "The uniform distribution assigns a constant probability over the entire interval of possible outcomes, while all outcomes outside this interval are assumed to have zero probability.  The width of this interval is 2s sqrt(3).  Thus, the uniform distribution assigns the probability densities f(x) = sqrt(2 s sqrt(3))  to values m - s sqrt(3) >= x <= m + s sqrt(3) and f(x) = 0 otherwise.",
            "display": "uniform",
        }
    )
    """
    uniform

    The uniform distribution assigns a constant probability over the entire interval of possible outcomes, while all outcomes outside this interval are assumed to have zero probability.  The width of this interval is 2s sqrt(3).  Thus, the uniform distribution assigns the probability densities f(x) = sqrt(2 s sqrt(3))  to values m - s sqrt(3) >= x <= m + s sqrt(3) and f(x) = 0 otherwise.
    """

    x2 = CodeSystemConcept(
        {
            "code": "X2",
            "definition": "Used to describe the sum of squares of random variables which occurs when a variance is estimated (rather than presumed) from the sample.  The only parameter of the c2-distribution is n, so called the number of degrees of freedom (which is the number of independent parts in the sum).  The c2-distribution is a special type of g-distribution with parameter a = n /2 and b  = 2.  Hence, m = n and s2 = 2 n.",
            "display": "chi square",
        }
    )
    """
    chi square

    Used to describe the sum of squares of random variables which occurs when a variance is estimated (rather than presumed) from the sample.  The only parameter of the c2-distribution is n, so called the number of degrees of freedom (which is the number of independent parts in the sum).  The c2-distribution is a special type of g-distribution with parameter a = n /2 and b  = 2.  Hence, m = n and s2 = 2 n.
    """

    class Meta:
        resource = _resource
