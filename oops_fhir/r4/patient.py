from typing import List, Union, Optional

from oops_fhir.r4.data_type import primitive as p
from oops_fhir.r4.data_type.complex import Identifier, HumanName, ContactPoint, Address, Attachment, Period
from oops_fhir.r4.value_set.administrative_gender import AdministrativeGender
from oops_fhir.r4.value_set.common_languages import CommonLanguages
from oops_fhir.r4.value_set.marital_status_codes import MaritalStatusCodes
from oops_fhir.r4.value_set.patient_contact_relationship import PatientContactRelationship


class _Deceased:
    """
    Indicates if the individual is deceased or not.

    If there's no value in the instance, it means there is no statement on
    whether the individual is deceased. Most systems will interpret the
    absence of a value as a sign of the person being alive.
    """
    deceased_boolean: Optional[p.boolean] = None
    deceased_datetime: Optional[p.datetime] = None


class _MultipleBirth:
    """
    Indicates whether the patient is part of a multiple (boolean) or indicates
    the actual birth order (integer).

    Where the valueInteger is provided, the number is the birth number in the
    sequence. E.g. The middle birth in triplets would be valueInteger=2 and the
    third born would have valueInteger=3 If a boolean value was provided for
    this triplets example, then all 3 patient records would have
    valueBoolean=true (the ordering is not indicated).
    """
    multiple_birth_boolean: Optional[p.boolean] = None
    multiple_birth_integer: Optional[p.integer] = None


class _Contact:
    """
    A contact party (e.g. guardian, partner, friend) for the patient

    Contact covers all kinds of contact parties: family members, business
    contacts, guardians, caregivers. Not applicable to register pedigree and
    family ties beyond use of having contact.

    + Rule: SHALL at least contain a contact's details or a reference to an
    organization
    """
    relationship: Union[
        PatientContactRelationship, List[PatientContactRelationship], None
    ] = PatientContactRelationship
    """ The kind of relationship """
    name: Optional[HumanName] = HumanName
    """ A name associated with the contact person """
    telecom: Union[ContactPoint, List[ContactPoint], None] = ContactPoint
    """ A contact detail for the person """
    address: Optional[Address] = Address
    """ Address for the contact person """
    gender: Optional[AdministrativeGender] = AdministrativeGender
    """ male | female | other | unknown """
    organization = None
    """ Organization that is associated with the contact """
    period: Optional[Period] = Period
    """
    The period during which this contact person or organization is valid to
    be contacted relating to this patient
    """


class _Communication:
    """
    A language which may be used to communicate with the patient about his or
    her health
    """
    language: CommonLanguages = CommonLanguages
    """
    The language which can be used to communicate with the patient about his or
    her health
    """
    preferred: Optional[p.boolean] = None
    """ Language preference indicator """


class Patient:
    """
    This Resource covers data about patients and animals involved in a wide
    range of health-related activities, including:

    - Curative activities
    - Psychiatric care
    - Social services
    - Pregnancy care
    - Nursing and assisted living
    - Dietary services
    - Tracking of personal health and exercise data

    The data in the Resource covers the "who" information about the patient:
    its attributes are focused on the demographic information necessary to
    support the administrative, financial and logistic procedures. A Patient
    record is generally created and maintained by each organization
    providing care for a patient. A patient or animal receiving care at
    multiple organizations may therefore have its information present in
    multiple Patient Resources.

    Not all concepts are included within the base resource (such as race,
    ethnicity, organ donor status, nationality, etc.), but may be found in
    profiles defined for specific jurisdictions (e.g., US Meaningful Use
    Program) or standard extensions. Such fields vary widely between
    jurisdictions and often have different names and valuesets for the similar
    concepts, but they are not similar enough to be able to map and exchange.
    """
    identifier: Union[Identifier, List[Identifier], None] = Identifier
    """An identifier for this patient"""
    active: Optional[p.boolean] = None
    """Whether this patient's record is in active use"""
    name: Union[HumanName, List[HumanName], None] = HumanName
    """A name associated with the patient"""
    telecom: Union[ContactPoint, List[ContactPoint], None] = ContactPoint
    """A contact detail for the individual"""
    gender: Optional[AdministrativeGender] = AdministrativeGender
    """male | female | other | unknown"""
    birthDate: Optional[p.date] = None
    """The date of birth for the individual"""
    deceased: Optional[_Deceased] = _Deceased
    """ Indicates if the individual is deceased or not """
    address: Union[Address, List[Address], None] = Address
    """An address for the individual"""
    marital_status: Optional[MaritalStatusCodes] = MaritalStatusCodes
    """Marital (civil) status of a patient"""
    multiple_birth: Optional[_MultipleBirth] = _MultipleBirth
    """ Whether patient is part of a multiple birth """
    photo: Union[Attachment, List[Attachment], None] = None
    """Image of the patient"""
    contact: Union[_Contact, List[_Contact], None] = None
    """
    A contact party (e.g. guardian, partner, friend) for the patient

    + Rule: SHALL at least contain a contact's details or a reference to an organization
    """
    communication: Union[_Communication, List[_Communication], None] = _Communication
    """A language which may be used to communicate with the patient about his or her health"""
    generalPractitioner = None
    """ Patient's nominated primary care provider """
    managingOrganization = None
    """ Organization that is the custodian of the patient record """
    link = None
    """ Link to another patient resource that concerns the same actual person """
