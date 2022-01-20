from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["PatientMedicineChangeTypes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class PatientMedicineChangeTypes:
    """
    Patient Medicine Change Types

    Example Item Flags for the List Resource. In this case, these are the
kind of flags that would be used on a medication list at the end of a
consultation.

    Status: draft - Version: 4.0.1

    Copyright  Copyright © 2012-2013 National E-Health Transition Authority Ltd : This document contains information which is protected by copyright. All Rights Reserved. No part of this work may be reproduced or used in any form or by any means--graphic, electronic, or mechanical, including photocopying,  recording, taping, or information storage and retrieval systems--without the permission of NEHTA. All copies of this  document must include the copyright and other information contained on this page.  Revision 1  Telephone: 1300 901 001 or email: servicedesk@nehta.gov.au  Disclaimer: The National E-Health Transition Authority Ltd (NEHTA) makes the information and other material ('Information') in  this document available in good faith but without any representation or warranty as to its accuracy or completeness.  NEHTA cannot accept any responsibility for the consequences of any use of the Information. As the Information is of a  general nature only, it is up to any person using or relying on the Information to ensure that it is accurate, complete  and suitable for the circumstances of its use.

    urn:oid:1.2.36.1.2001.1001.101.104.16592
    """

    zero1 = CodeSystemConcept(
        {
            "code": "01",
            "definition": "No change has been made to the status of this medicine item.",
            "display": "Unchanged",
        }
    )
    """
    Unchanged

    No change has been made to the status of this medicine item.
    """

    zero2 = CodeSystemConcept(
        {
            "code": "02",
            "definition": "The medicine item has changed. The change may be described in an extension (not defined yet)",
            "display": "Changed",
        }
    )
    """
    Changed

    The medicine item has changed. The change may be described in an extension (not defined yet)
    """

    zero3 = CodeSystemConcept(
        {
            "code": "03",
            "definition": "The prescription for this medicine item was cancelled by an authorized health care provider. The patient may be advised to complete the course of the prescribed medicine. This advice is a clinical decision made based on assessment of the patient's clinical condition.",
            "display": "Cancelled",
        }
    )
    """
    Cancelled

    The prescription for this medicine item was cancelled by an authorized health care provider. The patient may be advised to complete the course of the prescribed medicine. This advice is a clinical decision made based on assessment of the patient's clinical condition.
    """

    zero4 = CodeSystemConcept(
        {
            "code": "04",
            "definition": "A new medicine item has been prescribed",
            "display": "Prescribed",
        }
    )
    """
    Prescribed

    A new medicine item has been prescribed
    """

    zero5 = CodeSystemConcept(
        {
            "code": "05",
            "definition": "Administration of this medication item that the patient is currently taking is stopped or recommended to be stopped (i.e. instructed to be ceased by a health care provider). This cessation is anticipated to be permanent. The Change Description should describe the reason for cessation. Example uses: the medication in question is considered ineffective or has caused serious adverse effects. This value applies both to the cessation of a medication that is prescribed by another healthcare provider or patient self-administration of OTC medicines.",
            "display": "Ceased",
        }
    )
    """
    Ceased

    Administration of this medication item that the patient is currently taking is stopped or recommended to be stopped (i.e. instructed to be ceased by a health care provider). This cessation is anticipated to be permanent. The Change Description should describe the reason for cessation. Example uses: the medication in question is considered ineffective or has caused serious adverse effects. This value applies both to the cessation of a medication that is prescribed by another healthcare provider or patient self-administration of OTC medicines.
    """

    zero6 = CodeSystemConcept(
        {
            "code": "06",
            "definition": "Administration of this medication item that the patient is currently taking is on hold, or instructed or recommended by a health care provider to be temporarily stopped, or subject to clinical review (i.e. the stop may be temporary or permanent depending on the outcome of clinical review), or temporarily suspended as a pre-requisite to certain surgical or diagnostic procedures.",
            "display": "Suspended",
        }
    )
    """
    Suspended

    Administration of this medication item that the patient is currently taking is on hold, or instructed or recommended by a health care provider to be temporarily stopped, or subject to clinical review (i.e. the stop may be temporary or permanent depending on the outcome of clinical review), or temporarily suspended as a pre-requisite to certain surgical or diagnostic procedures.
    """

    class Meta:
        resource = _resource
