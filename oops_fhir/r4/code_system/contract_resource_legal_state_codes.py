from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ContractResourceLegalStateCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ContractResourceLegalStateCodes:
    """
    Contract Resource Legal State codes

    This value set contract specific codes for status.

    Status: draft - Version: 4.0.1

    Copyright HL7 International.

    http://hl7.org/fhir/contract-legalstate
    """

    amended = CodeSystemConcept(
        {
            "code": "amended",
            "definition": "Contract is augmented with additional information to correct errors in a predecessor or to updated values in a predecessor. Usage: Contract altered within effective time. Precedence Order = 9. Comparable FHIR and v.3 status codes: revised; replaced.",
            "display": "Amended",
        }
    )
    """
    Amended

    Contract is augmented with additional information to correct errors in a predecessor or to updated values in a predecessor. Usage: Contract altered within effective time. Precedence Order = 9. Comparable FHIR and v.3 status codes: revised; replaced.
    """

    appended = CodeSystemConcept(
        {
            "code": "appended",
            "definition": "Contract is augmented with additional information that was missing from a predecessor Contract. Usage: Contract altered within effective time. Precedence Order = 9. Comparable FHIR and v.3 status codes: updated, replaced.",
            "display": "Appended",
        }
    )
    """
    Appended

    Contract is augmented with additional information that was missing from a predecessor Contract. Usage: Contract altered within effective time. Precedence Order = 9. Comparable FHIR and v.3 status codes: updated, replaced.
    """

    cancelled = CodeSystemConcept(
        {
            "code": "cancelled",
            "definition": "Contract is terminated due to failure of the Grantor and/or the Grantee to fulfil one or more contract provisions. Usage: Abnormal contract termination. Precedence Order = 10. Comparable FHIR and v.3 status codes: stopped; failed; aborted.",
            "display": "Cancelled",
        }
    )
    """
    Cancelled

    Contract is terminated due to failure of the Grantor and/or the Grantee to fulfil one or more contract provisions. Usage: Abnormal contract termination. Precedence Order = 10. Comparable FHIR and v.3 status codes: stopped; failed; aborted.
    """

    disputed = CodeSystemConcept(
        {
            "code": "disputed",
            "definition": "Contract is pended to rectify failure of the Grantor or the Grantee to fulfil contract provision(s). E.g., Grantee complaint about Grantor's failure to comply with contract provisions. Usage: Contract pended. Precedence Order = 7. Comparable FHIR and v.3 status codes: on hold; pended; suspended.",
            "display": "Disputed",
        }
    )
    """
    Disputed

    Contract is pended to rectify failure of the Grantor or the Grantee to fulfil contract provision(s). E.g., Grantee complaint about Grantor's failure to comply with contract provisions. Usage: Contract pended. Precedence Order = 7. Comparable FHIR and v.3 status codes: on hold; pended; suspended.
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": "Contract was created in error. No Precedence Order.  Status may be applied to a Contract with any status.",
            "display": "Entered in Error",
        }
    )
    """
    Entered in Error

    Contract was created in error. No Precedence Order.  Status may be applied to a Contract with any status.
    """

    executable = CodeSystemConcept(
        {
            "code": "executable",
            "definition": "Contract execution pending; may be executed when either the Grantor or the Grantee accepts the contract provisions by signing. I.e., where either the Grantor or the Grantee has signed, but not both. E.g., when an insurance applicant signs the insurers application, which references the policy.\xa0Usage: Optional first step of contract execution activity.  May be skipped and contracting activity moves directly to executed state. Precedence Order = 3. Comparable FHIR and v.3 status codes: draft; preliminary; planned; intended; active.",
            "display": "Executable",
        }
    )
    """
    Executable

    Contract execution pending; may be executed when either the Grantor or the Grantee accepts the contract provisions by signing. I.e., where either the Grantor or the Grantee has signed, but not both. E.g., when an insurance applicant signs the insurers application, which references the policy. Usage: Optional first step of contract execution activity.  May be skipped and contracting activity moves directly to executed state. Precedence Order = 3. Comparable FHIR and v.3 status codes: draft; preliminary; planned; intended; active.
    """

    executed = CodeSystemConcept(
        {
            "code": "executed",
            "definition": "Contract is activated for period stipulated when both the Grantor and Grantee have signed it. Usage: Required state for normal completion of contracting activity.  Precedence Order = 6. Comparable FHIR and v.3 status codes: accepted; completed.",
            "display": "Executed",
        }
    )
    """
    Executed

    Contract is activated for period stipulated when both the Grantor and Grantee have signed it. Usage: Required state for normal completion of contracting activity.  Precedence Order = 6. Comparable FHIR and v.3 status codes: accepted; completed.
    """

    negotiable = CodeSystemConcept(
        {
            "code": "negotiable",
            "definition": "Contract execution is suspended while either or both the Grantor and Grantee propose and consider new or revised contract provisions. I.e., where the party which has not signed proposes changes to the terms.  E .g., a life insurer declines to agree to the signed application because the life insurer has evidence that the applicant, who asserted to being younger or a non-smoker to get a lower premium rate - but offers instead to agree to a higher premium based on the applicants actual age or smoking status. Usage: Optional contract activity between executable and executed state. Precedence Order = 4. Comparable FHIR and v.3 status codes: in progress; review; held.",
            "display": "Negotiable",
        }
    )
    """
    Negotiable

    Contract execution is suspended while either or both the Grantor and Grantee propose and consider new or revised contract provisions. I.e., where the party which has not signed proposes changes to the terms.  E .g., a life insurer declines to agree to the signed application because the life insurer has evidence that the applicant, who asserted to being younger or a non-smoker to get a lower premium rate - but offers instead to agree to a higher premium based on the applicants actual age or smoking status. Usage: Optional contract activity between executable and executed state. Precedence Order = 4. Comparable FHIR and v.3 status codes: in progress; review; held.
    """

    offered = CodeSystemConcept(
        {
            "code": "offered",
            "definition": "Contract is a proposal by either the Grantor or the Grantee. Aka - A Contract hard copy or electronic 'template', 'form' or 'application'. E.g., health insurance application; consent directive form. Usage: Beginning of contract negotiation, which may have been completed as a precondition because used for 0..* contracts. Precedence Order = 2. Comparable FHIR and v.3 status codes: requested; new.",
            "display": "Offered",
        }
    )
    """
    Offered

    Contract is a proposal by either the Grantor or the Grantee. Aka - A Contract hard copy or electronic 'template', 'form' or 'application'. E.g., health insurance application; consent directive form. Usage: Beginning of contract negotiation, which may have been completed as a precondition because used for 0..* contracts. Precedence Order = 2. Comparable FHIR and v.3 status codes: requested; new.
    """

    policy = CodeSystemConcept(
        {
            "code": "policy",
            "definition": "Contract template is available as the basis for an application or offer by the Grantor or Grantee. E.g., health insurance policy; consent directive policy.  Usage: Required initial contract activity, which may have been completed as a precondition because used for 0..* contracts. Precedence Order = 1. Comparable FHIR and v.3 status codes: proposed; intended.",
            "display": "Policy",
        }
    )
    """
    Policy

    Contract template is available as the basis for an application or offer by the Grantor or Grantee. E.g., health insurance policy; consent directive policy.  Usage: Required initial contract activity, which may have been completed as a precondition because used for 0..* contracts. Precedence Order = 1. Comparable FHIR and v.3 status codes: proposed; intended.
    """

    rejected = CodeSystemConcept(
        {
            "code": "rejected",
            "definition": " Execution of the Contract is not completed because either or both the Grantor and Grantee decline to accept some or all of the contract provisions. Usage: Optional contract activity between executable and abnormal termination. Precedence Order = 5. Comparable FHIR and v.3 status codes:  stopped; cancelled.",
            "display": "Rejected",
        }
    )
    """
    Rejected

     Execution of the Contract is not completed because either or both the Grantor and Grantee decline to accept some or all of the contract provisions. Usage: Optional contract activity between executable and abnormal termination. Precedence Order = 5. Comparable FHIR and v.3 status codes:  stopped; cancelled.
    """

    renewed = CodeSystemConcept(
        {
            "code": "renewed",
            "definition": "Beginning of a successor Contract at the termination of predecessor Contract lifecycle. Usage: Follows termination of a preceding Contract that has reached its expiry date. Precedence Order = 13. Comparable FHIR and v.3 status codes: superseded.",
            "display": "Renewed",
        }
    )
    """
    Renewed

    Beginning of a successor Contract at the termination of predecessor Contract lifecycle. Usage: Follows termination of a preceding Contract that has reached its expiry date. Precedence Order = 13. Comparable FHIR and v.3 status codes: superseded.
    """

    revoked = CodeSystemConcept(
        {
            "code": "revoked",
            "definition": "A Contract that is rescinded.  May be required prior to replacing with an updated Contract. Comparable FHIR and v.3 status codes: nullified.",
            "display": "Revoked",
        }
    )
    """
    Revoked

    A Contract that is rescinded.  May be required prior to replacing with an updated Contract. Comparable FHIR and v.3 status codes: nullified.
    """

    resolved = CodeSystemConcept(
        {
            "code": "resolved",
            "definition": "Contract is reactivated after being pended because of faulty execution. *E.g., competency of the signer(s), or where the policy is substantially different from and did not accompany the application/form so that the applicant could not compare them. Aka - ''reactivated''. Usage: Optional stage where a pended contract is reactivated. Precedence Order = 8. Comparable FHIR and v.3 status codes: reactivated.",
            "display": "Resolved",
        }
    )
    """
    Resolved

    Contract is reactivated after being pended because of faulty execution. *E.g., competency of the signer(s), or where the policy is substantially different from and did not accompany the application/form so that the applicant could not compare them. Aka - ''reactivated''. Usage: Optional stage where a pended contract is reactivated. Precedence Order = 8. Comparable FHIR and v.3 status codes: reactivated.
    """

    terminated = CodeSystemConcept(
        {
            "code": "terminated",
            "definition": "Contract reaches its expiry date.\xa0It might or might not be renewed or renegotiated. Usage: Normal end of contract period. Precedence Order = 12. Comparable FHIR and v.3 status codes: Obsoleted.",
            "display": "Terminated",
        }
    )
    """
    Terminated

    Contract reaches its expiry date. It might or might not be renewed or renegotiated. Usage: Normal end of contract period. Precedence Order = 12. Comparable FHIR and v.3 status codes: Obsoleted.
    """

    class Meta:
        resource = _resource
