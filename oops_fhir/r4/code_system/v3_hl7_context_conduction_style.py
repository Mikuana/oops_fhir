from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3HL7ContextConductionStyle"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3HL7ContextConductionStyle:
    """
    v3 Code System HL7ContextConductionStyle

    The styles of context conduction usable by relationships within a static
model derived from tyhe HL7 Reference Information Model.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-HL7ContextConductionStyle
    """

    c = CodeSystemConcept(
        {
            "code": "C",
            "definition": "Definition: Context conduction is defined using the contextConductionCode and contextConductionInd attributes on ActRelationship and Participation.\r\n\n                        \n                           UsageNotes: This approach is deprecated as of March, 2010.",
            "display": "conduction-indicator-based",
        }
    )
    """
    conduction-indicator-based

    Definition: Context conduction is defined using the contextConductionCode and contextConductionInd attributes on ActRelationship and Participation.

                        
                           UsageNotes: This approach is deprecated as of March, 2010.
    """

    i = CodeSystemConcept(
        {
            "code": "I",
            "definition": 'Definition: Context conduction is not explicitly defined.  The recipient of an instance must infer conduction based on the semantics of the model and what is deemed "reasonable".\r\n\n                        \n                           UsageNotes: Because this approach can lead to variation in instance interpretation, its use is discouraged.',
            "display": "inferred",
        }
    )
    """
    inferred

    Definition: Context conduction is not explicitly defined.  The recipient of an instance must infer conduction based on the semantics of the model and what is deemed "reasonable".

                        
                           UsageNotes: Because this approach can lead to variation in instance interpretation, its use is discouraged.
    """

    v = CodeSystemConcept(
        {
            "code": "V",
            "definition": 'Definition: Context conduction is defined using the ActRelationship.blockedContextActRelationshipType and blockedContextParticipationType attributes and the "conductible" property on the ActRelationshipType and ParticipationType code systems.',
            "display": "vocabulary-based",
        }
    )
    """
    vocabulary-based

    Definition: Context conduction is defined using the ActRelationship.blockedContextActRelationshipType and blockedContextParticipationType attributes and the "conductible" property on the ActRelationshipType and ParticipationType code systems.
    """

    class Meta:
        resource = _resource
