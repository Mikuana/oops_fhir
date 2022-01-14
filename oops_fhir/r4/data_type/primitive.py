from datetime import date as dt, datetime as dtm, time as tm

base_64_binary = str
"""
A stream of bytes, base64 encoded (RFC 4648)

There is no specified upper limit to the size of a binary, but systems will have
to impose some implementation based limit to the size they support. This should
be clearly documented, though there is no computable for this at this time
"""

boolean = bool
""" true | false """

date = dt
"""
A date, or partial date (e.g. just year or year + month) as used in human
communication. The format is YYYY, YYYY-MM, or YYYY-MM-DD, e.g. 2018, 1973-06,
or 1905-08-23. There SHALL be no time zone.
"""

datetime = dtm
"""
A date, date-time or partial date (e.g. just year or year + month) as used in
human communication. The format is YYYY, YYYY-MM, YYYY-MM-DD or
YYYY-MM-DDThh:mm:ss+zz:zz, e.g. 2018, 1973-06, 1905-08-23,
2015-02-07T13:28:17-05:00 or 2017-01-01T00:00:00.000Z. If hours and minutes are
specified, a time zone SHALL be populated. Seconds must be provided due to
schema type constraints but may be zero-filled and may be ignored at receiver
discretion. Dates SHALL be valid dates. The time "24:00" is not allowed. Leap
Seconds are allowed.
"""

decimal = float
"""
Rational numbers that have a decimal representation.
"""

instant = dtm
"""
An instant in time in the format YYYY-MM-DDThh:mm:ss.sss+zz:zz
(e.g. 2015-02-07T13:28:17.239+02:00 or 2017-01-01T00:00:00Z). The time SHALL
specified at least to the second and SHALL include a time zone. Note: This is
intended for when precisely observed times are required (typically system logs
etc.), and not human-reported times - for those, use date or dateTime (which can
be as precise as instant, but is not required to be). instant is a more
constrained dateTime	xs:dateTime	A JSON string - an xs:dateTime

Note: This type is for system times, not human times (see date and dateTime).
"""

string = str
"""
A sequence of Unicode characters

Note that strings SHALL NOT exceed 1MB (1024*1024 characters) in size. Strings
SHOULD not contain Unicode character points below 32, except for u0009
(horizontal tab), u0010 (carriage return) and u0013 (line feed). Leading and
Trailing whitespace is allowed, but SHOULD be removed when using the XML format.
Note: This means that a string that consists only of whitespace could be trimmed
to nothing, which would be treated as an invalid element value. Therefore
strings SHOULD always contain non-whitespace content

This data type can be bound to a ValueSet.
"""

id_ = string
"""
Any combination of upper- or lower-case ASCII letters ('A'..'Z', and 'a'..'z',
numerals ('0'..'9'), '-' and '.', with a length limit of 64 characters. (This
might be an integer, an un-prefixed OID, UUID or any other identifier pattern
that meets these constraints.)
"""

markdown = string
"""
A FHIR string (see above) that may contain markdown syntax for optional
processing by a markdown presentation engine, in the GFM extension of CommonMark
formt.
"""

code = string
"""
A coded value

Indicates that the value is taken from a set of controlled strings defined
elsewhere (see Using codes for further discussion). Technically, a code is
restricted to a string which has at least one character and no leading or
trailing whitespace, and where there is no whitespace other than single spaces
in the contents
"""

integer = int
"""
A signed integer in the range −2,147,483,648..2,147,483,647 (32-bit; for larger
values, use decimal)
"""

positive_int = integer
""" Any positive integer in the range 1..2,147,483,647 """

unsigned_int = int
""" Any non-negative integer in the range 0..2,147,483,647 """

time = tm
"""
A time during the day, in the format hh:mm:ss. There is no date specified.
Seconds must be provided due to schema type constraints but may be zero-filled
and may be ignored at receiver discretion. The time "24:00" SHALL NOT be used.
A time zone SHALL NOT be present. Times can be converted to a Duration since
midnight.
"""

uri = str
"""
A Uniform Resource Identifier Reference (RFC 3986 ). Note: URIs are case
sensitive. For UUID (urn:uuid:53fefa32-fcbb-4ff8-8a92-55ee120877b7) use all
lowercase

URIs can be absolute or relative, and may have an optional fragment identifier

This data type can be bound to a ValueSet
"""

url = uri
"""
A Uniform Resource Locator (RFC 1738 ). Note URLs are accessed directly using
the specified protocol. Common URL protocols are http{s}:, ftp:, mailto: and
mllp:, though many others are defined
"""

canonical = uri
"""
A URI that refers to a resource by its canonical URL (resources with a url
property). The canonical type differs from a uri in that it has special meaning
in this specification, and in that it may have a version appended, separated by
a vertical bar (|). Note that the type canonical is not used for the actual
canonical URLs that are the target of these references, but for the URIs that
refer to them, and may have the version suffix in them. Like other URIs,
elements of type canonical may also have #fragment references.
"""

uuid = uri
"""
A UUID (aka GUID) represented as a URI (RFC 4122 )

e.g. urn:uuid:c757873d-ec9a-4326-a141-556f43239520
"""

oid = uri
""" An OID represented as a URI (RFC 3001 ); e.g. urn:oid:1.2.3.4.5 """
