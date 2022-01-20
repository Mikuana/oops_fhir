from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ActionGroupingBehavior"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ActionGroupingBehavior:
    """
    ActionGroupingBehavior

    Defines organization behavior of a group.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/action-grouping-behavior
    """

    visual_group = CodeSystemConcept(
        {
            "code": "visual-group",
            "definition": "Any group marked with this behavior should be displayed as a visual group to the end user.",
            "display": "Visual Group",
        }
    )
    """
    Visual Group

    Any group marked with this behavior should be displayed as a visual group to the end user.
    """

    logical_group = CodeSystemConcept(
        {
            "code": "logical-group",
            "definition": "A group with this behavior logically groups its sub-elements, and may be shown as a visual group to the end user, but it is not required to do so.",
            "display": "Logical Group",
        }
    )
    """
    Logical Group

    A group with this behavior logically groups its sub-elements, and may be shown as a visual group to the end user, but it is not required to do so.
    """

    sentence_group = CodeSystemConcept(
        {
            "code": "sentence-group",
            "definition": 'A group of related alternative actions is a sentence group if the target referenced by the action is the same in all the actions and each action simply constitutes a different variation on how to specify the details for the target. For example, two actions that could be in a SentenceGroup are "aspirin, 500 mg, 2 times per day" and "aspirin, 300 mg, 3 times per day". In both cases, aspirin is the target referenced by the action, and the two actions represent different options for how aspirin might be ordered for the patient. Note that a SentenceGroup would almost always have an associated selection behavior of "AtMostOne", unless it\'s a required action, in which case, it would be "ExactlyOne".',
            "display": "Sentence Group",
        }
    )
    """
    Sentence Group

    A group of related alternative actions is a sentence group if the target referenced by the action is the same in all the actions and each action simply constitutes a different variation on how to specify the details for the target. For example, two actions that could be in a SentenceGroup are "aspirin, 500 mg, 2 times per day" and "aspirin, 300 mg, 3 times per day". In both cases, aspirin is the target referenced by the action, and the two actions represent different options for how aspirin might be ordered for the patient. Note that a SentenceGroup would almost always have an associated selection behavior of "AtMostOne", unless it's a required action, in which case, it would be "ExactlyOne".
    """

    class Meta:
        resource = _resource
