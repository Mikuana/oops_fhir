from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["validationprocess"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class validationprocess:
    """
    Validation-process

    The primary process by which the target is validated

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/validation-process
    """

    edit_check = CodeSystemConcept({"code": "edit-check", "display": "edit check"})
    """
    edit check

    
    """

    valueset = CodeSystemConcept({"code": "valueset", "display": "value set"})
    """
    value set

    
    """

    primary = CodeSystemConcept({"code": "primary", "display": "primary source"})
    """
    primary source

    
    """

    multi = CodeSystemConcept({"code": "multi", "display": "multiple sources"})
    """
    multiple sources

    
    """

    standalone = CodeSystemConcept({"code": "standalone", "display": "standalone"})
    """
    standalone

    
    """

    in_context = CodeSystemConcept({"code": "in-context", "display": "in context"})
    """
    in context

    
    """

    class Meta:
        resource = _resource
