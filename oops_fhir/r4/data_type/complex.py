from typing import Optional, List, Union

from oops_fhir.r4.data_type import primitive as p
from oops_fhir.r4.value_set.common_languages import CommonLanguages
from oops_fhir.r4.value_set.mime_types import MimeTypes
from oops_fhir.r4.value_set.quantity_comparator import QuantityComparator


class Attachment:
    """
    This type is for containing or referencing attachments - additional data
    content defined in other formats. The most common use of this type is to
    include images or reports in some report format such as PDF. However it can
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
    contains data, and MAY be populated when there is a url. It can include
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
    content_type: Optional[MimeTypes] = None
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
    Note that codes are case sensitive unless specified otherwise by the code
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

    Whether or not coding elements are present, the text is the representation
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
    comparator: Optional[QuantityComparator] = None
    """ "< | <= | >= | > - how to understand the value """
    unit: Optional[p.string] = None
    """ Unit representation """
    system: Optional[p.uri] = None
    """ System that defines coded unit form """
    code: Optional[p.code] = None
    """ Coded form of the unit """

