from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3DataOperation"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3DataOperation:
    """
    v3 Code System DataOperation

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-DataOperation
    """

    operate = CodeSystemConcept(
        {
            "code": "OPERATE",
            "concept": [
                {
                    "code": "CREATE",
                    "definition": "Description:Fundamental operation in an Information System (IS) that results only in the act of bringing an object into existence. Note: The preceding definition is taken from the HL7 RBAC specification.  There is no restriction on how the operation is invoked, e.g., via a user interface. For an HL7 Act, the state transitions per the HL7 Reference Information Model.",
                    "display": "create",
                },
                {
                    "code": "DELETE",
                    "definition": "Description:Fundamental operation in an Information System (IS) that results only in the removal of information about an object from memory or storage. Note: The preceding definition is taken from the HL7 RBAC specification.  There is no restriction on how the operation is invoked, e.g., via a user interface.",
                    "display": "delete",
                },
                {
                    "code": "EXECUTE",
                    "definition": "Description:Fundamental operation in an IS that results only in initiating performance of a single or set of programs (i.e., software objects). Note: The preceding definition is taken from the HL7 RBAC specification.  There is no restriction on how the operation is invoked, e.g., via a user interface.",
                    "display": "execute",
                },
                {
                    "code": "READ",
                    "definition": "Description:Fundamental operation in an Information System (IS) that results only in the flow of information about an object to a subject. Note: The preceding definition is taken from the HL7 RBAC specification.  There is no restriction on how the operation is invoked, e.g., via a user interface.",
                    "display": "read",
                },
                {
                    "code": "UPDATE",
                    "concept": [
                        {
                            "code": "APPEND",
                            "definition": "Description:Fundamental operation in an Information System (IS) that results only in the addition of information to an object already in existence. Note: The preceding definition is taken from the HL7 RBAC specification.  There is no restriction on how the operation is invoked, e.g., via a user interface.",
                            "display": "append",
                        },
                        {
                            "code": "MODIFYSTATUS",
                            "concept": [
                                {
                                    "code": "ABORT",
                                    "definition": 'Description:Change the status of an object representing an Act to "aborted", i.e., terminated prior to the originally intended completion. For an HL7 Act, the state transitions per the HL7 Reference Information Model.',
                                    "display": "abort",
                                },
                                {
                                    "code": "ACTIVATE",
                                    "definition": 'Description:Change the status of an object representing an Act to "active", i.e., so it can be performed or is being performed, for the first time. (Contrast with REACTIVATE.) For an HL7 Act, the state transitions per the HL7 Reference Information Model.',
                                    "display": "activate",
                                },
                                {
                                    "code": "CANCEL",
                                    "definition": 'Description:Change the status of an object representing an Act to "cancelled", i.e., abandoned before activation. For an HL7 Act, the state transitions per the HL7 Reference Information Model.',
                                    "display": "cancel",
                                },
                                {
                                    "code": "COMPLETE",
                                    "definition": 'Description:Change the status of an object representing an Act to "completed", i.e., terminated normally after all of its constituents have been performed. For an HL7 Act, the state transitions per the HL7 Reference Information Model.',
                                    "display": "complete",
                                },
                                {
                                    "code": "HOLD",
                                    "definition": 'Description:Change the status of an object representing an Act to "held", i.e., put aside an Act that is still in preparatory stages.  No action can occur until the Act is released. For an HL7 Act, the state transitions per the HL7 Reference Information Model.',
                                    "display": "hold",
                                },
                                {
                                    "code": "JUMP",
                                    "definition": "Description:Change the status of an object representing an Act to a normal state. For an HL7 Act, the state transitions per the HL7 Reference Information Model.",
                                    "display": "jump",
                                },
                                {
                                    "code": "NULLIFY",
                                    "definition": 'Description:Change the status of an object representing an Act to "nullified", i.e., treat as though it never existed. For an HL7 Act, the state transitions per the HL7 Reference Information Model.',
                                    "display": "nullify",
                                },
                                {
                                    "code": "OBSOLETE",
                                    "definition": 'Description:Change the status of an object representing an Act to "obsolete" when it has been replaced by a new instance. For an HL7 Act, the state transitions per the HL7 Reference Information Model.',
                                    "display": "obsolete",
                                },
                                {
                                    "code": "REACTIVATE",
                                    "definition": 'Description:Change the status of a formerly active object representing an Act to "active", i.e., so it can again be performed or is being performed. (Contrast with ACTIVATE.) For an HL7 Act, the state transitions per the HL7 Reference Information Model.',
                                    "display": "reactivate",
                                },
                                {
                                    "code": "RELEASE",
                                    "definition": 'Description:Change the status of an object representing an Act so it is no longer "held", i.e., allow action to occur. For an HL7 Act, the state transitions per the HL7 Reference Information Model.',
                                    "display": "release",
                                },
                                {
                                    "code": "RESUME",
                                    "definition": 'Description:Change the status of a suspended object representing an Act to "active", i.e., so it can be performed or is being performed. For an HL7 Act, the state transitions per the HL7 Reference Information Model.',
                                    "display": "resume",
                                },
                                {
                                    "code": "SUSPEND",
                                    "definition": "Definition:Change the status of an object representing an Act to suspended, i.e., so it is temporarily not in service.",
                                    "display": "suspend",
                                },
                            ],
                            "definition": "Description:Change the status of an object representing an Act.",
                            "display": "modify status",
                        },
                    ],
                    "definition": "Definition:Fundamental operation in an Information System (IS) that results only in the revision or alteration of an object. Note: The preceding definition is taken from the HL7 RBAC specification. There is no restriction on how the operation is invoked, e.g., via a user interface.",
                    "display": "revise",
                },
            ],
            "definition": "Description:Act on an object or objects.",
            "display": "operate",
        }
    )
    """
    operate

    Description:Act on an object or objects.
    """

    class Meta:
        resource = _resource
