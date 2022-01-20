from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["primarysourcetype"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class primarysourcetype:
    """
    Primary-source-type

    Type of the validation primary source

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/primary-source-type
    """

    lic_board = CodeSystemConcept({"code": "lic-board", "display": "License Board"})
    """
    License Board

    
    """

    prim = CodeSystemConcept({"code": "prim", "display": "Primary Education"})
    """
    Primary Education

    
    """

    cont_ed = CodeSystemConcept({"code": "cont-ed", "display": "Continuing Education"})
    """
    Continuing Education

    
    """

    post_serv = CodeSystemConcept({"code": "post-serv", "display": "Postal Service"})
    """
    Postal Service

    
    """

    rel_own = CodeSystemConcept({"code": "rel-own", "display": "Relationship owner"})
    """
    Relationship owner

    
    """

    reg_auth = CodeSystemConcept(
        {"code": "reg-auth", "display": "Registration Authority"}
    )
    """
    Registration Authority

    
    """

    legal = CodeSystemConcept({"code": "legal", "display": "Legal source"})
    """
    Legal source

    
    """

    issuer = CodeSystemConcept({"code": "issuer", "display": "Issuing source"})
    """
    Issuing source

    
    """

    auth_source = CodeSystemConcept(
        {"code": "auth-source", "display": "Authoritative source"}
    )
    """
    Authoritative source

    
    """

    class Meta:
        resource = _resource
