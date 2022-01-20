from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3ContextControl"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3ContextControl:
    """
    v3 Code System ContextControl

     A code that specifies how an ActRelationship or Participation
contributes to the context of an Act, and whether it may be propagated
to descendent Acts whose association allows such propagation (see also
attributes Participation.contextControlCode,
ActRelationship.contextControlCode,
ActRelationship.contextConductionInd).

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-ContextControl
    """

    underscore_context_control_additive = CodeSystemConcept(
        {
            "code": "_ContextControlAdditive",
            "concept": [
                {
                    "code": "AN",
                    "definition": "The association adds to the existing context associated with the Act, but will not propagate to any descendant Acts reached by conducting ActRelationships (see contextControlCode). Examples: If an 'Author' Participation were marked as \"Additive, Non-Propagating\" it means that the author will be added to the set of author participations that have propagated from ancestor Acts for the purpose of this Act. However only the previously propagated authors will propagate to any child Acts that allow context to be propagated.",
                    "display": "additive, non-propagating",
                },
                {
                    "code": "AP",
                    "definition": "The association adds to the existing context associated with the Act, and will propagate to any descendant Acts reached by conducting ActRelationships (see contextControlCode). Examples: If an 'Author' Participation were marked as \"Additive, Propagating\" it means that the author will be added to the set of author participations that have propagated from ancestor Acts, and will itself propagate with the other authors to any child Acts that allow context to be propagated.",
                    "display": "additive, propagating",
                },
            ],
            "definition": "The association adds to the existing context associated with the Act.  Both this association and any associations propagated from ancestor Acts are interpreted as being related to this Act.",
            "display": "ContextControlAdditive",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ContextControlAdditive

    The association adds to the existing context associated with the Act.  Both this association and any associations propagated from ancestor Acts are interpreted as being related to this Act.
    """

    underscore_context_control_non_propagating = CodeSystemConcept(
        {
            "code": "_ContextControlNonPropagating",
            "concept": [
                {
                    "code": "ON",
                    "definition": "The association is added to the existing context associated with the Act, but overrides an association with the same typeCode. However, this overriding association will not propagate to any descendant Acts reached by conducting ActRelationships (see contextControlCode). Examples: If an 'Author' Participation were marked as \"Overriding, Non-Propagating\" it means that the author will replace the set of author participations that have propagated from ancestor Acts. Furthermore, no author participations whatsoever will propagate to any child Acts that allow context to be propagated.",
                    "display": "overriding, non-propagating",
                }
            ],
            "definition": "The association applies only to the current Act and will not propagate to any child Acts that are related via a conducting ActRelationship (refer to contextConductionInd).",
            "display": "ContextControlNonPropagating",
            "property": [
                {"code": "notSelectable", "valueBoolean": True},
                {"code": "child", "valueCode": "AN"},
            ],
        }
    )
    """
    ContextControlNonPropagating

    The association applies only to the current Act and will not propagate to any child Acts that are related via a conducting ActRelationship (refer to contextConductionInd).
    """

    underscore_context_control_overriding = CodeSystemConcept(
        {
            "code": "_ContextControlOverriding",
            "concept": [
                {
                    "code": "OP",
                    "definition": "The association is added to the existing context associated with the Act, but overrides an association with the same typeCode. This overriding association will propagate to any descendant Acts reached by conducting ActRelationships (see contextControlCode). Examples: If an 'Author' Participation were marked as \"Overriding, Propagating\" it means that the author will replace the set of author participations that have propagated from ancestor Acts, and will itself be the only author to propagate to any child Acts that allow context to be propagated.",
                    "display": "overriding, propagating",
                }
            ],
            "definition": "The association adds to the existing context associated with the Act, but replaces associations propagated from ancestor Acts whose typeCodes are the same or more specific.",
            "display": "ContextControlOverriding",
            "property": [
                {"code": "notSelectable", "valueBoolean": True},
                {"code": "child", "valueCode": "ON"},
            ],
        }
    )
    """
    ContextControlOverriding

    The association adds to the existing context associated with the Act, but replaces associations propagated from ancestor Acts whose typeCodes are the same or more specific.
    """

    underscore_context_control_propagating = CodeSystemConcept(
        {
            "code": "_ContextControlPropagating",
            "definition": "The association propagates to any child Acts that are related via a conducting ActRelationship (refer to contextConductionInd).",
            "display": "ContextControlPropagating",
            "property": [
                {"code": "notSelectable", "valueBoolean": True},
                {"code": "child", "valueCode": "AP"},
                {"code": "child", "valueCode": "OP"},
            ],
        }
    )
    """
    ContextControlPropagating

    The association propagates to any child Acts that are related via a conducting ActRelationship (refer to contextConductionInd).
    """

    class Meta:
        resource = _resource
