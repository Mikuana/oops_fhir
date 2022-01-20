from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["DataType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class DataType:
    """
    DataType

    A version specific list of the data types defined by the FHIR
specification for use as an element  type (any of the FHIR defined data
types).

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/data-types
    """

    address = CodeSystemConcept(
        {
            "code": "Address",
            "definition": "An address expressed using postal conventions (as opposed to GPS or other location definition formats).  This data type may be used to convey addresses for use in delivering mail as well as for visiting locations which might not be valid for mail delivery.  There are a variety of postal address formats defined around the world.",
            "display": "Address",
        }
    )
    """
    Address

    An address expressed using postal conventions (as opposed to GPS or other location definition formats).  This data type may be used to convey addresses for use in delivering mail as well as for visiting locations which might not be valid for mail delivery.  There are a variety of postal address formats defined around the world.
    """

    age = CodeSystemConcept(
        {
            "code": "Age",
            "definition": "A duration of time during which an organism (or a process) has existed.",
            "display": "Age",
        }
    )
    """
    Age

    A duration of time during which an organism (or a process) has existed.
    """

    annotation = CodeSystemConcept(
        {
            "code": "Annotation",
            "definition": "A  text note which also  contains information about who made the statement and when.",
            "display": "Annotation",
        }
    )
    """
    Annotation

    A  text note which also  contains information about who made the statement and when.
    """

    attachment = CodeSystemConcept(
        {
            "code": "Attachment",
            "definition": "For referring to data content defined in other formats.",
            "display": "Attachment",
        }
    )
    """
    Attachment

    For referring to data content defined in other formats.
    """

    backbone_element = CodeSystemConcept(
        {
            "code": "BackboneElement",
            "definition": "Base definition for all elements that are defined inside a resource - but not those in a data type.",
            "display": "BackboneElement",
        }
    )
    """
    BackboneElement

    Base definition for all elements that are defined inside a resource - but not those in a data type.
    """

    codeable_concept = CodeSystemConcept(
        {
            "code": "CodeableConcept",
            "definition": "A concept that may be defined by a formal reference to a terminology or ontology or may be provided by text.",
            "display": "CodeableConcept",
        }
    )
    """
    CodeableConcept

    A concept that may be defined by a formal reference to a terminology or ontology or may be provided by text.
    """

    coding = CodeSystemConcept(
        {
            "code": "Coding",
            "definition": "A reference to a code defined by a terminology system.",
            "display": "Coding",
        }
    )
    """
    Coding

    A reference to a code defined by a terminology system.
    """

    contact_detail = CodeSystemConcept(
        {
            "code": "ContactDetail",
            "definition": "Specifies contact information for a person or organization.",
            "display": "ContactDetail",
        }
    )
    """
    ContactDetail

    Specifies contact information for a person or organization.
    """

    contact_point = CodeSystemConcept(
        {
            "code": "ContactPoint",
            "definition": "Details for all kinds of technology mediated contact points for a person or organization, including telephone, email, etc.",
            "display": "ContactPoint",
        }
    )
    """
    ContactPoint

    Details for all kinds of technology mediated contact points for a person or organization, including telephone, email, etc.
    """

    contributor = CodeSystemConcept(
        {
            "code": "Contributor",
            "definition": "A contributor to the content of a knowledge asset, including authors, editors, reviewers, and endorsers.",
            "display": "Contributor",
        }
    )
    """
    Contributor

    A contributor to the content of a knowledge asset, including authors, editors, reviewers, and endorsers.
    """

    count = CodeSystemConcept(
        {
            "code": "Count",
            "definition": "A measured amount (or an amount that can potentially be measured). Note that measured amounts include amounts that are not precisely quantified, including amounts involving arbitrary units and floating currencies.",
            "display": "Count",
        }
    )
    """
    Count

    A measured amount (or an amount that can potentially be measured). Note that measured amounts include amounts that are not precisely quantified, including amounts involving arbitrary units and floating currencies.
    """

    data_requirement = CodeSystemConcept(
        {
            "code": "DataRequirement",
            "definition": "Describes a required data item for evaluation in terms of the type of data, and optional code or date-based filters of the data.",
            "display": "DataRequirement",
        }
    )
    """
    DataRequirement

    Describes a required data item for evaluation in terms of the type of data, and optional code or date-based filters of the data.
    """

    distance = CodeSystemConcept(
        {
            "code": "Distance",
            "definition": "A length - a value with a unit that is a physical distance.",
            "display": "Distance",
        }
    )
    """
    Distance

    A length - a value with a unit that is a physical distance.
    """

    dosage = CodeSystemConcept(
        {
            "code": "Dosage",
            "definition": "Indicates how the medication is/was taken or should be taken by the patient.",
            "display": "Dosage",
        }
    )
    """
    Dosage

    Indicates how the medication is/was taken or should be taken by the patient.
    """

    duration = CodeSystemConcept(
        {"code": "Duration", "definition": "A length of time.", "display": "Duration"}
    )
    """
    Duration

    A length of time.
    """

    element = CodeSystemConcept(
        {
            "code": "Element",
            "definition": "Base definition for all elements in a resource.",
            "display": "Element",
        }
    )
    """
    Element

    Base definition for all elements in a resource.
    """

    element_definition = CodeSystemConcept(
        {
            "code": "ElementDefinition",
            "definition": "Captures constraints on each element within the resource, profile, or extension.",
            "display": "ElementDefinition",
        }
    )
    """
    ElementDefinition

    Captures constraints on each element within the resource, profile, or extension.
    """

    expression = CodeSystemConcept(
        {
            "code": "Expression",
            "definition": "A expression that is evaluated in a specified context and returns a value. The context of use of the expression must specify the context in which the expression is evaluated, and how the result of the expression is used.",
            "display": "Expression",
        }
    )
    """
    Expression

    A expression that is evaluated in a specified context and returns a value. The context of use of the expression must specify the context in which the expression is evaluated, and how the result of the expression is used.
    """

    extension = CodeSystemConcept(
        {
            "code": "Extension",
            "definition": "Optional Extension Element - found in all resources.",
            "display": "Extension",
        }
    )
    """
    Extension

    Optional Extension Element - found in all resources.
    """

    human_name = CodeSystemConcept(
        {
            "code": "HumanName",
            "definition": "A human's name with the ability to identify parts and usage.",
            "display": "HumanName",
        }
    )
    """
    HumanName

    A human's name with the ability to identify parts and usage.
    """

    identifier = CodeSystemConcept(
        {
            "code": "Identifier",
            "definition": "An identifier - identifies some entity uniquely and unambiguously. Typically this is used for business identifiers.",
            "display": "Identifier",
        }
    )
    """
    Identifier

    An identifier - identifies some entity uniquely and unambiguously. Typically this is used for business identifiers.
    """

    marketing_status = CodeSystemConcept(
        {
            "code": "MarketingStatus",
            "definition": "The marketing status describes the date when a medicinal product is actually put on the market or the date as of which it is no longer available.",
            "display": "MarketingStatus",
        }
    )
    """
    MarketingStatus

    The marketing status describes the date when a medicinal product is actually put on the market or the date as of which it is no longer available.
    """

    meta = CodeSystemConcept(
        {
            "code": "Meta",
            "definition": "The metadata about a resource. This is content in the resource that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource.",
            "display": "Meta",
        }
    )
    """
    Meta

    The metadata about a resource. This is content in the resource that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource.
    """

    money = CodeSystemConcept(
        {
            "code": "Money",
            "definition": "An amount of economic utility in some recognized currency.",
            "display": "Money",
        }
    )
    """
    Money

    An amount of economic utility in some recognized currency.
    """

    money_quantity = CodeSystemConcept(
        {"code": "MoneyQuantity", "display": "MoneyQuantity"}
    )
    """
    MoneyQuantity

    
    """

    narrative = CodeSystemConcept(
        {
            "code": "Narrative",
            "definition": "A human-readable summary of the resource conveying the essential clinical and business information for the resource.",
            "display": "Narrative",
        }
    )
    """
    Narrative

    A human-readable summary of the resource conveying the essential clinical and business information for the resource.
    """

    parameter_definition = CodeSystemConcept(
        {
            "code": "ParameterDefinition",
            "definition": "The parameters to the module. This collection specifies both the input and output parameters. Input parameters are provided by the caller as part of the $evaluate operation. Output parameters are included in the GuidanceResponse.",
            "display": "ParameterDefinition",
        }
    )
    """
    ParameterDefinition

    The parameters to the module. This collection specifies both the input and output parameters. Input parameters are provided by the caller as part of the $evaluate operation. Output parameters are included in the GuidanceResponse.
    """

    period = CodeSystemConcept(
        {
            "code": "Period",
            "definition": "A time period defined by a start and end date and optionally time.",
            "display": "Period",
        }
    )
    """
    Period

    A time period defined by a start and end date and optionally time.
    """

    population = CodeSystemConcept(
        {
            "code": "Population",
            "definition": "A populatioof people with some set of grouping criteria.",
            "display": "Population",
        }
    )
    """
    Population

    A populatioof people with some set of grouping criteria.
    """

    prod_characteristic = CodeSystemConcept(
        {
            "code": "ProdCharacteristic",
            "definition": "The marketing status describes the date when a medicinal product is actually put on the market or the date as of which it is no longer available.",
            "display": "ProdCharacteristic",
        }
    )
    """
    ProdCharacteristic

    The marketing status describes the date when a medicinal product is actually put on the market or the date as of which it is no longer available.
    """

    product_shelf_life = CodeSystemConcept(
        {
            "code": "ProductShelfLife",
            "definition": "The shelf-life and storage information for a medicinal product item or container can be described using this class.",
            "display": "ProductShelfLife",
        }
    )
    """
    ProductShelfLife

    The shelf-life and storage information for a medicinal product item or container can be described using this class.
    """

    quantity = CodeSystemConcept(
        {
            "code": "Quantity",
            "definition": "A measured amount (or an amount that can potentially be measured). Note that measured amounts include amounts that are not precisely quantified, including amounts involving arbitrary units and floating currencies.",
            "display": "Quantity",
        }
    )
    """
    Quantity

    A measured amount (or an amount that can potentially be measured). Note that measured amounts include amounts that are not precisely quantified, including amounts involving arbitrary units and floating currencies.
    """

    range_ = CodeSystemConcept(
        {
            "code": "Range",
            "definition": "A set of ordered Quantities defined by a low and high limit.",
            "display": "Range",
        }
    )
    """
    Range

    A set of ordered Quantities defined by a low and high limit.
    """

    ratio = CodeSystemConcept(
        {
            "code": "Ratio",
            "definition": "A relationship of two Quantity values - expressed as a numerator and a denominator.",
            "display": "Ratio",
        }
    )
    """
    Ratio

    A relationship of two Quantity values - expressed as a numerator and a denominator.
    """

    reference = CodeSystemConcept(
        {
            "code": "Reference",
            "definition": "A reference from one resource to another.",
            "display": "Reference",
        }
    )
    """
    Reference

    A reference from one resource to another.
    """

    related_artifact = CodeSystemConcept(
        {
            "code": "RelatedArtifact",
            "definition": "Related artifacts such as additional documentation, justification, or bibliographic references.",
            "display": "RelatedArtifact",
        }
    )
    """
    RelatedArtifact

    Related artifacts such as additional documentation, justification, or bibliographic references.
    """

    sampled_data = CodeSystemConcept(
        {
            "code": "SampledData",
            "definition": "A series of measurements taken by a device, with upper and lower limits. There may be more than one dimension in the data.",
            "display": "SampledData",
        }
    )
    """
    SampledData

    A series of measurements taken by a device, with upper and lower limits. There may be more than one dimension in the data.
    """

    signature = CodeSystemConcept(
        {
            "code": "Signature",
            "definition": "A signature along with supporting context. The signature may be a digital signature that is cryptographic in nature, or some other signature acceptable to the domain. This other signature may be as simple as a graphical image representing a hand-written signature, or a signature ceremony Different signature approaches have different utilities.",
            "display": "Signature",
        }
    )
    """
    Signature

    A signature along with supporting context. The signature may be a digital signature that is cryptographic in nature, or some other signature acceptable to the domain. This other signature may be as simple as a graphical image representing a hand-written signature, or a signature ceremony Different signature approaches have different utilities.
    """

    simple_quantity = CodeSystemConcept(
        {"code": "SimpleQuantity", "display": "SimpleQuantity"}
    )
    """
    SimpleQuantity

    
    """

    substance_amount = CodeSystemConcept(
        {
            "code": "SubstanceAmount",
            "definition": "Chemical substances are a single substance type whose primary defining element is the molecular structure. Chemical substances shall be defined on the basis of their complete covalent molecular structure; the presence of a salt (counter-ion) and/or solvates (water, alcohols) is also captured. Purity, grade, physical form or particle size are not taken into account in the definition of a chemical substance or in the assignment of a Substance ID.",
            "display": "SubstanceAmount",
        }
    )
    """
    SubstanceAmount

    Chemical substances are a single substance type whose primary defining element is the molecular structure. Chemical substances shall be defined on the basis of their complete covalent molecular structure; the presence of a salt (counter-ion) and/or solvates (water, alcohols) is also captured. Purity, grade, physical form or particle size are not taken into account in the definition of a chemical substance or in the assignment of a Substance ID.
    """

    timing = CodeSystemConcept(
        {
            "code": "Timing",
            "definition": "Specifies an event that may occur multiple times. Timing schedules are used to record when things are planned, expected or requested to occur. The most common usage is in dosage instructions for medications. They are also used when planning care of various kinds, and may be used for reporting the schedule to which past regular activities were carried out.",
            "display": "Timing",
        }
    )
    """
    Timing

    Specifies an event that may occur multiple times. Timing schedules are used to record when things are planned, expected or requested to occur. The most common usage is in dosage instructions for medications. They are also used when planning care of various kinds, and may be used for reporting the schedule to which past regular activities were carried out.
    """

    trigger_definition = CodeSystemConcept(
        {
            "code": "TriggerDefinition",
            "definition": "A description of a triggering event. Triggering events can be named events, data events, or periodic, as determined by the type element.",
            "display": "TriggerDefinition",
        }
    )
    """
    TriggerDefinition

    A description of a triggering event. Triggering events can be named events, data events, or periodic, as determined by the type element.
    """

    usage_context = CodeSystemConcept(
        {
            "code": "UsageContext",
            "definition": "Specifies clinical/business/etc. metadata that can be used to retrieve, index and/or categorize an artifact. This metadata can either be specific to the applicable population (e.g., age category, DRG) or the specific context of care (e.g., venue, care setting, provider of care).",
            "display": "UsageContext",
        }
    )
    """
    UsageContext

    Specifies clinical/business/etc. metadata that can be used to retrieve, index and/or categorize an artifact. This metadata can either be specific to the applicable population (e.g., age category, DRG) or the specific context of care (e.g., venue, care setting, provider of care).
    """

    base64_binary = CodeSystemConcept(
        {
            "code": "base64Binary",
            "definition": "A stream of bytes",
            "display": "base64Binary",
        }
    )
    """
    base64Binary

    A stream of bytes
    """

    boolean = CodeSystemConcept(
        {
            "code": "boolean",
            "definition": 'Value of "true" or "false"',
            "display": "boolean",
        }
    )
    """
    boolean

    Value of "true" or "false"
    """

    canonical = CodeSystemConcept(
        {
            "code": "canonical",
            "definition": "A URI that is a reference to a canonical URL on a FHIR resource",
            "display": "canonical",
        }
    )
    """
    canonical

    A URI that is a reference to a canonical URL on a FHIR resource
    """

    code = CodeSystemConcept(
        {
            "code": "code",
            "definition": "A string which has at least one character and no leading or trailing whitespace and where there is no whitespace other than single spaces in the contents",
            "display": "code",
        }
    )
    """
    code

    A string which has at least one character and no leading or trailing whitespace and where there is no whitespace other than single spaces in the contents
    """

    date = CodeSystemConcept(
        {
            "code": "date",
            "definition": "A date or partial date (e.g. just year or year + month). There is no time zone. The format is a union of the schema types gYear, gYearMonth and date.  Dates SHALL be valid dates.",
            "display": "date",
        }
    )
    """
    date

    A date or partial date (e.g. just year or year + month). There is no time zone. The format is a union of the schema types gYear, gYearMonth and date.  Dates SHALL be valid dates.
    """

    date_time = CodeSystemConcept(
        {
            "code": "dateTime",
            "definition": "A date, date-time or partial date (e.g. just year or year + month).  If hours and minutes are specified, a time zone SHALL be populated. The format is a union of the schema types gYear, gYearMonth, date and dateTime. Seconds must be provided due to schema type constraints but may be zero-filled and may be ignored.                 Dates SHALL be valid dates.",
            "display": "dateTime",
        }
    )
    """
    dateTime

    A date, date-time or partial date (e.g. just year or year + month).  If hours and minutes are specified, a time zone SHALL be populated. The format is a union of the schema types gYear, gYearMonth, date and dateTime. Seconds must be provided due to schema type constraints but may be zero-filled and may be ignored.                 Dates SHALL be valid dates.
    """

    decimal = CodeSystemConcept(
        {
            "code": "decimal",
            "definition": "A rational number with implicit precision",
            "display": "decimal",
        }
    )
    """
    decimal

    A rational number with implicit precision
    """

    id_ = CodeSystemConcept(
        {
            "code": "id",
            "definition": 'Any combination of letters, numerals, "-" and ".", with a length limit of 64 characters.  (This might be an integer, an unprefixed OID, UUID or any other identifier pattern that meets these constraints.)  Ids are case-insensitive.',
            "display": "id",
        }
    )
    """
    id

    Any combination of letters, numerals, "-" and ".", with a length limit of 64 characters.  (This might be an integer, an unprefixed OID, UUID or any other identifier pattern that meets these constraints.)  Ids are case-insensitive.
    """

    instant = CodeSystemConcept(
        {
            "code": "instant",
            "definition": "An instant in time - known at least to the second",
            "display": "instant",
        }
    )
    """
    instant

    An instant in time - known at least to the second
    """

    integer = CodeSystemConcept(
        {"code": "integer", "definition": "A whole number", "display": "integer"}
    )
    """
    integer

    A whole number
    """

    markdown = CodeSystemConcept(
        {
            "code": "markdown",
            "definition": "A string that may contain Github Flavored Markdown syntax for optional processing by a mark down presentation engine",
            "display": "markdown",
        }
    )
    """
    markdown

    A string that may contain Github Flavored Markdown syntax for optional processing by a mark down presentation engine
    """

    oid = CodeSystemConcept(
        {"code": "oid", "definition": "An OID represented as a URI", "display": "oid"}
    )
    """
    oid

    An OID represented as a URI
    """

    positive_int = CodeSystemConcept(
        {
            "code": "positiveInt",
            "definition": "An integer with a value that is positive (e.g. >0)",
            "display": "positiveInt",
        }
    )
    """
    positiveInt

    An integer with a value that is positive (e.g. >0)
    """

    string = CodeSystemConcept(
        {
            "code": "string",
            "definition": "A sequence of Unicode characters",
            "display": "string",
        }
    )
    """
    string

    A sequence of Unicode characters
    """

    time = CodeSystemConcept(
        {
            "code": "time",
            "definition": "A time during the day, with no date specified",
            "display": "time",
        }
    )
    """
    time

    A time during the day, with no date specified
    """

    unsigned_int = CodeSystemConcept(
        {
            "code": "unsignedInt",
            "definition": "An integer with a value that is not negative (e.g. >= 0)",
            "display": "unsignedInt",
        }
    )
    """
    unsignedInt

    An integer with a value that is not negative (e.g. >= 0)
    """

    uri = CodeSystemConcept(
        {
            "code": "uri",
            "definition": "String of characters used to identify a name or a resource",
            "display": "uri",
        }
    )
    """
    uri

    String of characters used to identify a name or a resource
    """

    url = CodeSystemConcept(
        {
            "code": "url",
            "definition": "A URI that is a literal reference",
            "display": "url",
        }
    )
    """
    url

    A URI that is a literal reference
    """

    uuid = CodeSystemConcept(
        {
            "code": "uuid",
            "definition": "A UUID, represented as a URI",
            "display": "uuid",
        }
    )
    """
    uuid

    A UUID, represented as a URI
    """

    xhtml = CodeSystemConcept(
        {
            "extension": [
                {
                    "url": "http://hl7.org/fhir/StructureDefinition/codesystem-concept-comments",
                    "valueString": "Special case: xhtml can only be used in the narrative Data Type",
                }
            ],
            "code": "xhtml",
            "definition": "XHTML format, as defined by W3C, but restricted usage (mainly, no active content)",
            "display": "XHTML",
        }
    )
    """
    XHTML

    XHTML format, as defined by W3C, but restricted usage (mainly, no active content)
    """

    class Meta:
        resource = _resource
