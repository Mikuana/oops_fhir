from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3IdentifierScope"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3IdentifierScope:
    """
    v3 Code System IdentifierScope

      Description:  Codes to specify the scope in which the identifier
applies to the object with which it is associated, and used in the
datatype property II.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-IdentifierScope
    """

    busn = CodeSystemConcept(
        {
            "code": "BUSN",
            "definition": "Description: An identifier whose scope is defined by the business practices associated with the object. In contrast to the other scope identifiers, the scope of the use of the id is not necessarily restricted to a single object, but may be reused for other objects closely associated with the object due to business practice.",
            "display": "Business Identifier",
        }
    )
    """
    Business Identifier

    Description: An identifier whose scope is defined by the business practices associated with the object. In contrast to the other scope identifiers, the scope of the use of the id is not necessarily restricted to a single object, but may be reused for other objects closely associated with the object due to business practice.
    """

    obj = CodeSystemConcept(
        {
            "code": "OBJ",
            "definition": "Description: The identifier associated with a particular object. It remains consistent as the object undergoes state transitions.",
            "display": "Object Identifier",
        }
    )
    """
    Object Identifier

    Description: The identifier associated with a particular object. It remains consistent as the object undergoes state transitions.
    """

    ver = CodeSystemConcept(
        {
            "code": "VER",
            "definition": "Description: An identifier that references a particular object as it existed at a given point in time. The identifier SHALL change with each state transition on the object. I.e. The version identifier of an object prior to a 'suspend' state transition is distinct from the identifier of the object after the state transition. Each version identifier can be tied to exactly one ControlAct event which brought that version into being (though the control act may never be instantiated).\r\n\n                        \n                            NOTE: Applications that do not support versioning of objects must ignore and not persist these ids to avoid confusion resulting from leaving the same identifier on an object that undergoes changes.",
            "display": "Version Identifier",
        }
    )
    """
    Version Identifier

    Description: An identifier that references a particular object as it existed at a given point in time. The identifier SHALL change with each state transition on the object. I.e. The version identifier of an object prior to a 'suspend' state transition is distinct from the identifier of the object after the state transition. Each version identifier can be tied to exactly one ControlAct event which brought that version into being (though the control act may never be instantiated).

                        
                            NOTE: Applications that do not support versioning of objects must ignore and not persist these ids to avoid confusion resulting from leaving the same identifier on an object that undergoes changes.
    """

    vw = CodeSystemConcept(
        {
            "code": "VW",
            "definition": "Description: An identifier that references a particular object as it existed at a given point in time. The identifier SHALL change with each state transition on the object.\r\n\n                        \n                           Example The version identifier of an object prior to a 'suspend' state transition is distinct from the identifier of the object after the state transition. Each version identifier can be tied to exactly one ControlAct event which brought that version into being (though the control act may never be instantiated).\r\n\n                        \n                            NOTE: Applications that do not support versioning of objects must ignore and not persist these ids to avoid confusion resulting from leaving the same identifier on an object that undergoes changes.",
            "display": "View Specific Identifier",
        }
    )
    """
    View Specific Identifier

    Description: An identifier that references a particular object as it existed at a given point in time. The identifier SHALL change with each state transition on the object.

                        
                           Example The version identifier of an object prior to a 'suspend' state transition is distinct from the identifier of the object after the state transition. Each version identifier can be tied to exactly one ControlAct event which brought that version into being (though the control act may never be instantiated).

                        
                            NOTE: Applications that do not support versioning of objects must ignore and not persist these ids to avoid confusion resulting from leaving the same identifier on an object that undergoes changes.
    """

    class Meta:
        resource = _resource
