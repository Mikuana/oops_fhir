from typing import Optional, List, Union

from oops_fhir.r4.data_type import primitive as p
from oops_fhir.r4.value_set.address_type import AddressType
from oops_fhir.r4.value_set.address_use import AddressUse
from oops_fhir.r4.value_set.common_languages import CommonLanguages
from oops_fhir.r4.value_set.contact_point_system import ContactPointSystem
from oops_fhir.r4.value_set.contact_point_use import ContactPointUse
from oops_fhir.r4.value_set.days_of_week import DaysOfWeek
from oops_fhir.r4.value_set.event_timing import EventTiming
from oops_fhir.r4.value_set.identifier_type_codes import IdentifierTypeCodes
from oops_fhir.r4.value_set.identifier_use import IdentifierUse
from oops_fhir.r4.value_set.mime_types import MimeTypes
from oops_fhir.r4.value_set.name_use import NameUse
from oops_fhir.r4.value_set.quantity_comparator import QuantityComparator

__all__ = [
    'Attachment',
    'Coding',
    'CodeableConcept',
    'Quantity',
    'SimpleQuantity',
    'Range',
    'Ratio',
    'Period',
    'SampledData',
    'Identifier',
    'HumanName',
    'Address',
    'ContactPoint',
    'Timing',
    'Signature',
    'Annotation',
    'OpenTypeElement',
]

from oops_fhir.r4.value_set.signature_type_codes import SignatureTypeCodes

from oops_fhir.r4.value_set.timing_abbreviation import TimingAbbreviation

from oops_fhir.r4.value_set.units_of_time import UnitsOfTime


class Attachment:
    """
    This type is for containing or referencing attachments - additional data
    content defined in other formats. The most common use of this type is to
    include images or reports in some reports format such as PDF. However, it can
    be used for any data that has a MIME type.

    The actual content of an Attachment can be conveyed directly using the data
    element or a URL reference can be provided. If both are provided, the
    reference SHALL point to the same content as found in the data. The
    reference can never be reused to point to some different data (i.e. the
    reference is version specific). The URL reference SHALL point to a location
    that resolves to actual data; some URIs such as cid: meet this requirement.
    If the URL is a relative reference, it is interpreted in the same way as a
    resource reference.

    The contentType element SHALL always be populated when an Attachment
    contains data, and MAY be populated when there is an url. It can include
    charset information and other mime type extensions as appropriate. If there
    is no character set in the contentType then the correct course of action is
    undefined, though some media types may define a default character set and/or
    the correct character set may be able to be determined by inspection of the
    content.

    The hash is included so that applications can verify that the content
    returned by the URL has not changed. The hash and size relate to the data
    before it is represented in base64 form.

    In many cases where Attachment is used, the cardinality is >1. A valid use
    of repeats is to convey the same content in different mime types and
    languages. Guidance on the meaning of repeating elements SHALL be provided
    in the definition of the repeating resource element or extension that
    references this type. The language element describes the language of the
    attachment using the codes defined in BCP 47.
    """
    content_type: Optional[MimeTypes] = MimeTypes
    """ Mime type of the content, with charset etc. """
    language: Optional[CommonLanguages] = CommonLanguages
    """ Human language of the content (BCP-47) """
    data: Optional[p.base_64_binary] = None
    """ Data inline, base64ed """
    url: Optional[p.url] = None
    """ Uri where the data can be found """
    size: Optional[p.unsigned_int] = None
    """ Number of bytes of content (if url provided) """
    hash: Optional[p.base_64_binary] = None
    """ Hash of the data (sha-1, base64ed) """
    title: Optional[p.string] = None
    """ Label to display in place of the data """
    creation: Optional[p.datetime] = None
    """ date attachment was first created """


class Coding:
    """
    A Coding is a representation of a defined concept using a symbol from a
    defined "code system" - see Using Codes in resources for more details.

    The meaning of the Coding is defined by the code. The system provides the
    source of the definition of the code, along with an optional version
    reference. The display is a human display for the text defined by the
    system - it is not intended for computation.

    The system is a URI that references the code system that defines the code.
    Choosing the correct system is important; for more information about the
    code system URI, read Managing Terminology System URIs. The system URI SHALL
    NOT contain a reference to a value set (e.g. ValueSet.url). If the code is
    taken from a CodeSystem resource, CodeSystem.url is the correct value for
    the system uri. Resolvable URLs are generally preferred by implementers over
    non-resolvable URNs, particularly opaque URNs such as OIDs (urn:oid:) or
    UUIDs (urn:uuid:).

    A code system version may also be supplied. If the meaning of codes within
    the code system is consistent across releases, this is not required. The
    version SHOULD be exchanged when the system does not maintain consistent
    definitions across versions. Note that the following systems SHOULD always
    have a version specified:

    National releases of SNOMED CT (consistency of definitions varies amongst
    jurisdictions, and some jurisdictions may make their own rules on this)
    Various versions of ICD (note: the major releases are labeled as different
    code systems altogether, but there is variation within versions)
    More generally, any classification (e.g. a code system that includes
    concepts with relative definitions such as "not otherwise coded" will
    require a version. See the discussion of code system versions in the Code
    System resource for further discussion on versioning.

    If present, the code SHALL be a syntactically correct symbol as defined by
    the system. In some code systems such as SNOMED CT, the symbol may be an
    expression composed of other predefined symbol (e.g. post-coordination).
    Note that codes are case-sensitive unless specified otherwise by the code
    system. The display is a text representation of the code defined by the
    system and is used to display the meaning of the code by an application
    that is not aware of the system.

    Where the code system defines multiple possible display strings, one of
    these SHALL be used in display. If one is labeled as preferred, it SHOULD be
    used. If the code system does not define a text representation (e.g. SNOMED
    CT Expressions) then display cannot be populated, and the meaning of the
    code won't be accessible to systems that don't understand the code expression.

    In some cases, the system may not be known - only the code is known. In
    this case, no useful processing of the code may be performed unless the
    system can be safely inferred by the context. This practice should be
    avoided where possible, as information sharing in a wider context is very
    likely to arise eventually, and codes cannot be used in the absence of a
    known system.

    If the system is present, and there is no code, then this is understood to
    mean that there is no suitable code in the system in which to represent the
    code.

    If two codings have the same system, version and code then they have the
    same meaning. If the version information is missing, or the system, version
    or the code elements differ, then how the codes are related can only be
    determined by consulting the definitions of the system(s) and any mappings
    available.

    A coding may be marked as a "userSelected" if a user selected the particular
    coded value in a user interface (e.g. the user selects an item in a
    pick-list). If a user selected coding exists, it is the preferred choice for
    performing translations etc.
    """
    system: Optional[p.uri] = None
    """ Identity of the terminology system """
    version: Optional[p.string] = None
    """ Version of the system - if relevant """
    code: Optional[p.code] = None
    """ Symbol in syntax defined by the system """
    display: Optional[p.string] = None
    """ Representation defined by the system """
    user_selected: Optional[p.boolean] = None
    """ If this coding was chosen directly by the user """


class CodeableConcept:
    """
    A CodeableConcept represents a value that is usually supplied by providing
    a reference to one or more terminologies or ontologies, but may also be
    defined by the provision of text. This is a common pattern in healthcare data.

    Each coding is a representation of the concept as described above. The
    concept may be coded multiple times in different code systems (or even
    multiple times in the same code systems, where multiple forms are possible,
    such as with SNOMED CT). The different codings may have slightly different
    granularity due to the differences in the definitions of the underlying
    codes. There is no meaning associated with the ordering of coding within a
    CodeableConcept. A typical use of CodeableConcept is to send the local code
    that the concept was coded with, and also one or more translations to
    publicly defined code systems such as LOINC or SNOMED CT. Sending local
    codes is useful and important for the purposes of debugging and integrity
    auditing.

    Whether coding elements are present, the text is the representation
    of the concept as entered or chosen by the user, and which most closely
    represents the intended meaning of the user or concept. Very often the text
    is the same as a display of one of the codings. One of the codings may be
    flagged as the userSelected - the code or concept that the user actually
    selected directly. When none of the coding elements is marked as
    userSelected, the text (if present) is the preferred source of meaning.
    """

    coding: Union[Coding, List[Coding], None] = None
    """ Code defined by a terminology system """
    text: Optional[p.string] = None
    """ Plain text representation of the concept """


class Quantity:
    """
    A measured amount (or an amount that can potentially be measured).

    The value contains the numerical value of the quantity, including an
    implicit precision. If no comparator is specified, the value is a point
    value (i.e. '='). The comparator element can never be ignored.

    The unit element contains a displayable unit that defines what is measured.
    The unit may additionally be coded in some formal way using the code and the
    system (see Coding for further information about how to use the system
    element).

    If the unit can be coded in UCUM and a code is provided, it SHOULD be a UCUM
    code. If a UCUM unit is provided in the code, then a canonical value can be
    generated for purposes of comparison between quantities. Note that the unit
    element will often contain text that is a valid UCUM unit, but it cannot be
    assumed that the unit actually contains a valid UCUM unit.
    """
    value: Optional[p.decimal] = None
    """ Numerical value (with implicit precision) """
    comparator: Optional[QuantityComparator] = QuantityComparator
    """ "< | <= | >= | > - how to understand the value """
    unit: Optional[p.string] = None
    """ Unit representation """
    system: Optional[p.uri] = None
    """ System that defines coded unit form """
    code: Optional[p.code] = None
    """ Coded form of the unit """


class SimpleQuantity(Quantity):
    comparator = None
    """ The comparator is not used on a SimpleQuantity """


class Range:
    """
    A set of ordered Quantity values defined by a low and high limit.

    A Range specifies a set of possible values; usually, one value from the
    range applies (e.g. "give the patient between 2 and 4 tablets"). Ranges
    are typically used in instructions.

    The unit and code/system elements of the low or high elements SHALL match.
    If the low or high elements are missing, the meaning is that the low or high
    boundaries are not known and therefore neither is the complete range.

    The comparator flag on the low or high elements cannot be present. Note that
    the Range type should not be used to represent out of range measurements: A
    quantity type with the comparator element should be used instead.

    The low and the high values are inclusive, and are assumed to have
    arbitrarily high precision; e.g. the range 1.5 to 2.5 includes 1.50, and
    2.50 but not 1.49 or 2.51.
    """
    low: Optional[SimpleQuantity] = SimpleQuantity
    """ Low limit """
    high: Optional[SimpleQuantity] = SimpleQuantity
    """ High limit """


class Ratio:
    """
    A relationship between two Quantity values expressed as a numerator and a
    denominator.

    Common factors in the numerator and denominator are not automatically
    cancelled out. The Ratio data type is used for titers (e.g. "1:128") and
    other quantities produced by laboratories that truly represent ratios.
    Ratios are not simply "structured numbers" - for example blood pressure
    measurements (e.g. "120/60") are not ratios. In addition, ratios are used
    where common factors in the numerator and denominator do not cancel out. The
    most common example of this is where the ratio represents a unit cost, and
    the numerator is a currency (e.g. 50/$10).

    A proper ratio has both a numerator and a denominator; however these are not
    mandatory in order to allow an invalid ratio with an extension with further
    information.
    """
    numerator: Optional[Quantity] = Quantity
    """ Numerator value """
    denominator: Optional[Quantity] = Quantity
    """ Denominator value """


class Period:
    """
    A time period defined by a start and end date/time.

    A period specifies a range of times. The context of use will specify whether
    the entire range applies (e.g. "the patient was an inpatient of the hospital
    for this time range") or one value from the period applies (e.g. "give to
    the patient between 2 and 4 pm on 24-Jun 2013").

    If the start element is missing, the start of the period is not known. If
    the end element is missing, it means that the period is ongoing, or the
    start may be in the past, and the end date in the future, which means that
    period is expected/planned to end at the specified time

    The end value includes any matching date/time. For example, the period
    2011-05-23 to 2011-05-27 includes all the times from the start of the
    23rd May through to the end of the 27th of May.
    """
    start: Optional[p.datetime] = None
    """ Starting time with inclusive boundary """
    end: Optional[p.datetime] = None
    """ End time with inclusive boundary, if not ongoing """


class SampledData:
    """
    Data that comes from a series of measurements taken by a device,
    which may have upper and lower limits. The data type also supports more than
    one dimension in the data.

    A SampledData provides a concise way to handle the data produced by devices
    that sample a particular physical state at a high frequency. A typical use
    for this is for the output of an ECG or EKG device. The data type includes a
    series of raw decimal values (which are mostly simple integers), along with
    adjustments for scale and factor. These are interpreted such that:

    original measured value[i] = SampledData.data[i] * SampledData.scaleFactor + SampledData.origin.value

    The digits are a set of decimal values separated by a single space (Unicode
    character u20). In addition to decimal values, the special values "E"
    (error), "L" (below detection limit) and "U" (above detection limit) can
    also be used. If there is more than one dimension, the different dimensions
    are interlaced - all the data points for a particular time are represented
    together. The default value for factor is 1.
    """
    origin: [SimpleQuantity] = SimpleQuantity
    """ Zero value and units """
    period: p.decimal = None
    """ Number of milliseconds between samples """
    factor: Optional[p.decimal] = None
    """ Multiply data by this before adding to origin """
    lowerLimit: Optional[p.decimal] = None
    """ Lower limit of detection """
    upperLimit: Optional[p.decimal] = None
    """ Upper limit of detection """
    dimensions: p.positive_int = None
    """ Number of sample points at each time point """
    data: p.string = None
    """ Decimal values with spaces, or "E" | "U" | "L" """


class Identifier:
    """
    A numeric or alphanumeric string that is associated with a single object or
    entity within a given system. Typically, identifiers are used to connect
    content in resources to external content available in other frameworks or
    protocols. Identifiers are associated with objects, and may be changed or
    retired due to human or system process and errors.

    The value SHALL be unique within the defined system and have a consistent
    meaning wherever it appears. Both system and value are always case-sensitive.

    The system is a URI that defines a set of identifiers (i.e. how the value is
    made unique). It might be a specific application or a recognized
    standard/specification for a set or identifiers or a way of making
    identifiers unique. FHIR defines some useful or important system URIs
    directly. Here are some example identifier namespaces:

    http://hl7.org/fhir/sid/us-ssn for United States Social Security Number (SSN)
    values
    http://ns.electronichealth.net.au/id/hi/ihi/1.0 for Australian Individual
    Healthcare Identifier (IHI) numbers
    urn:ietf:rfc:3986 for when the value of the identifier is itself a globally
    unique URI
    If the system is a URL, it SHOULD resolve. Resolution might be to a web page
    that describes the identifier system and/or supports look-up of identifiers.
    Alternatively, it could be to a NamingSystem resource instance. Resolvable
    URLs are generally preferred by implementers over non-resolvable URNs,
    particularly opaque URNs such as OIDs (urn:oid:) or UUIDs (urn:uuid:). If
    used, OIDs and UUIDs may be registered in the HL7 OID registry  and SHOULD
    be registered if the content is shared or exchanged across institutional
    boundaries.

    It is up to the implementer organization to determine an appropriate URL or
    URN structure that will avoid collisions and to manage that space (and the
    resolvability of URLs) over time.

    Note that the scope of a given identifier system may extend beyond
    identifiers that might be captured by a single resource. For example, some
    systems might draw all "order" identifiers from a single namespace, though
    some might be used on MedicationRequest while others would appear on
    ProcedureRequest.

    If the identifier value itself is naturally a globally unique URI (e.g. an
    OID, a UUID, or a URI with no trailing local part), then the system SHALL be
    "urn:ietf:rfc:3986", and the URI is in the value (OIDs and UUIDs using
    urn:oid: and urn:uuid: - see examples).

    In some cases, the system may not be known - only the value is known (e.g.
    a simple device that scans a barcode), or the system is known implicitly
    (simple exchange in a limited context, often driven by barcode readers). In
    this case, no useful matching may be performed using the value unless the
    system can be safely inferred by the context. Applications should provide a
    system wherever possible, as information sharing in a wider context is very
    likely to arise eventually, and values without a system are inherently
    limited in use.

    In addition to the system (which provides a uniqueness scope) and the value,
    identifiers may also have a type, which may be useful when a system
    encounters identifiers with unknown system values. Note, however, that the
    type of identifier is not a well-controlled vocabulary with wide
    variations in practice. The type deals only with general categories of
    identifiers and SHOULD not be used for codes that correspond 1..1 with the
    Identifier.system. Some identifiers may fall into multiple categories due to
    variations in common usage.

    The assigner is used to indicate what registry/state/facility/etc. assigned
    the identifier. As a Reference, the assigner can include just a text
    description in the display.
    """
    use: Optional[IdentifierUse] = IdentifierUse
    """ usual | official | temp | secondary (If known) """
    type: Optional[IdentifierTypeCodes] = IdentifierTypeCodes
    """ Description of identifier """
    system: Optional[p.uri] = None
    """ The namespace for the identifier value """
    value: Optional[p.string] = None
    """ The value that is unique """
    period: Optional[Period] = Period
    """ Time period when id is/was valid for use """
    assigner = None  # TODO: reference type needs to be implemented
    """ Organization that issued id (may be just text) """


class HumanName:
    """
    A name of a human with text, parts and usage information.

    Names may be changed or repudiated. People may have different names in
    different contexts. Names may be divided into parts of different type that
    have variable significance depending on context, though the division into
    parts is not always significant. With personal names, the different parts
    may or may not be imbued with some implicit meaning; various cultures
    associate different importance with the name parts and the degree to which
    systems SHALL care about name parts around the world varies widely.

    This table summarizes where common parts of a person's name are found.

    **Name**	**Example**	 **Destination / Comments**
    Surname	Smith	Family Name
    First name	John	Given Name
    Title	Mr	Prefix
    Middle Name	Samuel	Subsequent Given Names
    Patronymic	bin Osman	Family Name
    Multiple family names	Carreño Quiñones	Family Name. See note below about decomposition of family name
    Initials	Q.	Given Name as initial ("." recommended)
    Nick Name	Jock	Given name, with Use = common
    Qualifications	PhD	Suffix
    Honorifics	Senior	Suffix
    Voorvoegsel / Nobility	van Beethoven	Family Name. See note below about decomposition of family name

    For further information, including all W3C International Examples , consult
    the examples. Note: Implementers should read the name examples for a full
    understanding of how name works.

    The multiple given parts and family name combine to form a single name.
    Where a person has alternate names that may be used in place of each other
    (e.g. Nicknames, Aliases), these are different instances of HumanName.

    The text element specifies the entire name as it should be represented. This
    may be provided instead of or as well as specific parts, and can be built
    from the parts, though the correct order of assembly of the parts is culture
    dependent: the order of the parts within a given part type has significance
    and SHALL be observed. The appropriate order between family name and given
    names depends on culture and context of use. Note that there is an extension
    for the few times name assembly order is not fixed by the culture.

    The given name parts may contain whitespace, though generally they don't.
    Initials may be used in place of the full name if that is all that is
    recorded. Systems that operate across cultures should generally rely on the
    text form for presentation, and use the parts for index/search functionality.
    For these reasons, applications SHOULD populate the text element for future
    robustness.

    In some cultures (e.g. German, Dutch, Spanish, Portuguese), family names are
    complex and composed of various parts that may need to be managed separately,
    e.g. they have differing significance for searching. In these cases, the full
    family name is populated in family, and a decomposition of the name can be
    provided using the family extensions own-name, own-prefix, partner-name,
    partner-prefix, fathers-family and mothers-family.

    For robust search, servers should search the parts of a family name
    independently. E.g. Searching either Carreno or Quinones should match a
    family name of "Carreno Quinones". HL7 affiliates may make more specific
    recommendations about how search should work in their specific culture.
    """
    use: Optional[NameUse] = NameUse
    """ usual | official | temp | nickname | anonymous | old | maiden """
    text: Optional[p.string] = None
    """ Text representation of the full name """
    family: Optional[p.string] = None
    """ Family name (often called 'Surname') """
    given: Union[p.string, List[p.string], None] = None
    """ Given names (not always 'first'). Includes middle names """
    prefix: Union[p.string, List[p.string], None] = None
    """ Parts that come before the name """
    suffix: Union[p.string, List[p.string], None] = None
    """ Parts that come after the name """
    period: Optional[Period] = Period
    """ Time period when name was/is in use """


class Address:
    """
    An address expressed using postal conventions (as opposed to GPS or other
    location definition formats). This data type may be used to convey addresses
    for use in delivering mail as well as for visiting locations which might not
    be valid for mail delivery. There are a variety of postal address formats
    defined around the world.

    The text element specifies the entire address as it should be represented.
    This may be provided instead of or as well as the specific parts.
    Applications updating an address SHALL ensure either that the text and the
    parts are in agreement, or that only one of the two is present.
    """
    use: Optional[AddressUse] = AddressUse
    """ home | work | temp | old - purpose of this address """
    type: Optional[AddressType] = AddressType
    """ postal | physical | both """
    text: Optional[p.string] = None
    """ Text representation of the address """
    line: Union[p.string, List[p.string], None] = None
    """ Street name, number, direction & P.O. Box etc ."""
    city: Optional[p.string] = None
    """ Name of city, town etc ."""
    district: Optional[p.string] = None
    """ District name (aka county )"""
    state: Optional[p.string] = None
    """ Sub-unit of country (abbreviations ok )"""
    postalCode: Optional[p.string] = None
    """ Postal code for area """
    country: Optional[p.string] = None
    """ Country (e.g. can be ISO 3166 2 or 3 letter code )"""
    period: Optional[Period] = Period
    """ Time period when address was/is in use """


class ContactPoint:
    """
    Details for all kinds of technology-mediated contact points for a person or
    organization, including telephone, email, etc.

    If capturing a phone, fax or similar contact point, the value should be a
    properly formatted telephone number according to ITU-T E.123 . However, this
    is frequently not possible due to legacy data and/or clerical practices when
    recording contact details. For this reason, phone, fax, pager, and email
    addresses are not handled as formal URLs. For other kinds of contact points,
    the system is "other" and the value SHOULD be a URL so that its use can be
    determined automatically. Typical URL schemes used in the value are http(s):
    for web addresses, and URL schemes for various kinds of messaging systems.
    If the value is not a URL, then human interpretation will be required.

    The rank element can be used to specify a preference for the order in which
    a set of contacts is used. Contacts are ranked with lower values coming
    before higher values. Note that rank does not necessarily follow the order
    in which the contacts are represented in the instance.
    """
    system: Optional[ContactPointSystem] = ContactPointSystem
    """ phone | fax | email | pager | url | sms | other """
    value: Optional[p.string] = None
    """ The actual contact point details """
    use: Optional[ContactPointUse] = ContactPointUse
    """ home | work | temp | old | mobile - purpose of this contact point """
    rank: Optional[p.positive_int] = None
    """ Specify preferred order of use (1 = highest )"""
    period: Optional[Period] = Period
    """ Time period when the contact point was/is in use """


class _Bounds:
    bounds_duration = None  # TODO: this
    bounds_range: Range = Range
    bounds_period: Period = Period


class _Repeat:
    """
    Specifies repetition of an event
    """
    bounds: Optional[_Bounds] = _Bounds
    count: Optional[p.integer] = None
    """ Number of times to repeat """
    count_max: Optional[p.integer] = None
    """ Maximum number of times to repeat """
    duration: Optional[p.decimal] = None
    """ How long when it happens """
    duration_max: Optional[p.decimal] = None
    """ How long when it happens (Max )"""
    duration_unit: Optional[UnitsOfTime] = UnitsOfTime
    """ s | min | h | d | wk | mo | a - unit of time (UCUM )"""
    frequency: Optional[p.integer] = None
    """ Event occurs frequency times per period """
    frequency_max: Optional[p.integer] = None
    """ Event occurs up to frequencyMax times per period """
    period: Optional[p.decimal] = None
    """ Event occurs frequency times per period """
    period_max: Optional[p.decimal] = None
    """ Upper limit of period (3-4 hours )"""
    period_unit: Optional[UnitsOfTime] = UnitsOfTime
    """ s | min | h | d | wk | mo | a - unit of time (UCUM )"""
    day_of_week: Union[DaysOfWeek, List[DaysOfWeek], None] = DaysOfWeek
    """ mon | tue | wed | thu | fri | sat | sun """
    time_of_day: Union[p.time, List[p.time], None] = None
    """ Time of day for action """
    when: Union[EventTiming, List[EventTiming], None] = EventTiming
    """ Regular life events the event is tied to """
    offset: Optional[p.unsigned_int] = None
    """ Minutes from event (before or after )"""


class Timing:
    """
    Specifies an event that may occur multiple times. Timing schedules are used
    for specifying when events are expected or requested to occur, and may also
    be used to represent a schedule that was followed for past events. A Timing
    schedule can be a list of events and/or criteria for when the event happens,
    which can be expressed in a structured form and/or as a code. When both
    event and a repeating specification are provided, the list of events should
    be understood as an interpretation of the information in the repeat
    structure.

    If the timing schedule has repeating criteria, the repeat can occur a given
    number of times per the specified duration or in relation to some repeating
    real world event. If no end condition is specified, the schedule will
    terminate on some criteria that are expressed elsewhere.

    Many systems avoid the complexity of the Timing structure by using a text
    field for these things (e.g. "Dosage Text"). Those systems do not use the
    Timing data type. Other systems use a set of 'common' codes - including,
    but usually not limited to, widely understood acronyms such as "BID". If a
    code is provided, the code is understood to be a complete statement of
    whatever is specified in the structured timing data (except for
    Timing.repeat.bounds, which applies to the code), and either the code or the
    data may be used to interpret the Timing. A structured timing specification
    SHOULD be provided whenever possible, unless the code is BID, TID, QID, AM
    or PM, which have a ubiquitous meaning.

    These codes SHALL be understood as having the formal meanings documented in
    this table. Note that BID, etc. are defined as 'at institutionally specified
    times'. For example, an institution may choose that BID is "always at 7am
    and 6pm". If it is inappropriate for this choice to be made, the code BID
    should not be used. Instead, a distinct organization-specific code should be
    used in place of the HL7-defined BID code and/or a structured representation
    should be used (in this case, timeOfDay).
    """
    event: Union[p.datetime, List[p.datetime], None]
    """ When the event occurs """
    repeat: Optional[_Repeat] = _Repeat
    """
    When the event is to occur

    + If there's an offset, there must be a when (and not C, CM, CD, CV)
    + period SHALL be a non-negative value
    + If there's a periodMax, there must be a period
    + If there's a durationMax, there must be a duration
    + If there's a countMax, there must be a count
    + if there's a duration, there needs to be duration units
    + If there's a timeOfDay, there cannot be be a when, or vice versa
    + if there's a period, there needs to be period units
    + duration SHALL be a non-negative value
    """
    code: Optional[TimingAbbreviation] = TimingAbbreviation
    """ BID | TID | QID | AM | PM | QD | QOD | Q4H | Q6H + """


class _Who:
    who_uri: p.uri = None
    who_reference = None  # TODO: this


class _OnBehalfOf:
    on_behalf_of_uri: p.uri = None
    on_behalf_of_reference = None  # TODO: this


class Signature:
    """
    A Signature holds an electronic representation of a signature and its
    supporting context in a FHIR accessible form. The signature may either be
    a cryptographic type (XML DigSig or a JWT), which is able to provide
    non-repudiation proof, or it may be a graphical image that represents a
    signature or a signature process.

    Note: One consequence of signing the document is that URLs, identifiers and
    internal references are frozen and cannot be changed. This might be a
    desired feature, but it may also cripple interoperability between closed
    ecosystems where re-identification frequently occurs. For this reason, it is
    recommended that systems consider carefully the impact of any signature
    processes. The impact of signatures on Document bundles and their related
    processes is the most well understood use of digital signatures.
    """
    type: SignatureTypeCodes = SignatureTypeCodes
    """ Indication of the reason the entity signed the object(s )"""
    when: p.instant = None
    """ When the signature was created """
    who: _Who = _Who
    """ Who signed """
    on_behalf_of: Optional[_OnBehalfOf] = _OnBehalfOf
    """ The part represented """
    content_type: Optional[MimeTypes] = MimeTypes
    """ The technical format of the signature """
    blob: Optional[p.base_64_binary] = None
    """ The actual signature content (XML DigSig. JWT, picture, etc .)"""


class _Author:
    author_reference = None  # TODO: this
    author_string: p.string = None


class Annotation:
    """
    A text note which also contains information about who made the statement and
    when.

    Systems that do not have structured annotations simply communicate a single
    annotation with no author or time.

    This element may need to be included in narrative because of the potential
    for modifying information.

    Annotations SHOULD NOT be used to communicate "modifying" information that
    could be computable (this is a SHOULD because enforcing user behavior is
    nearly impossible).
    """
    author: Optional[_Author] = _Author
    """ Individual responsible for the annotation """
    time: Optional[p.datetime] = None
    """ When the annotation was made """
    text: p.string = None
    """ The annotation - text content """


OpenTypeElement = Union[
    p.boolean, p.integer, p.decimal, p.base_64_binary, p.instant, p.string, p.uri,
    p.date, p.datetime, p.time, p.code, p.oid, p.id_, p.unsigned_int, p.positive_int,
    p.markdown, Annotation, Attachment, Identifier, CodeableConcept, Coding, Quantity,
    Range, Period, Ratio, SampledData, Signature, HumanName, Address, ContactPoint,
    Timing,
    # Reference,  # TODO: add this
    # Meta  # TODO: add this
]
