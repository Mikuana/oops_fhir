from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["medicationKnowledgePackageTypeCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class medicationKnowledgePackageTypeCodes:
    """
    Medication knowledge  package  type  codes

    MedicationKnowledge Package Type Codes

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/medicationknowledge-package-type
    """

    amp = CodeSystemConcept({"code": "amp", "display": "Ampule"})
    """
    Ampule

    
    """

    bag = CodeSystemConcept({"code": "bag", "display": "Bag"})
    """
    Bag

    
    """

    blstrpk = CodeSystemConcept({"code": "blstrpk", "display": "Blister Pack"})
    """
    Blister Pack

    
    """

    bot = CodeSystemConcept({"code": "bot", "display": "Bottle"})
    """
    Bottle

    
    """

    box = CodeSystemConcept({"code": "box", "display": "Box"})
    """
    Box

    
    """

    can = CodeSystemConcept({"code": "can", "display": "Can"})
    """
    Can

    
    """

    cart = CodeSystemConcept({"code": "cart", "display": "Cartridge"})
    """
    Cartridge

    
    """

    disk = CodeSystemConcept({"code": "disk", "display": "Disk"})
    """
    Disk

    
    """

    doset = CodeSystemConcept({"code": "doset", "display": "Dosette"})
    """
    Dosette

    
    """

    jar = CodeSystemConcept({"code": "jar", "display": "Jar"})
    """
    Jar

    
    """

    jug = CodeSystemConcept({"code": "jug", "display": "Jug"})
    """
    Jug

    
    """

    minim = CodeSystemConcept({"code": "minim", "display": "Minim"})
    """
    Minim

    
    """

    nebamp = CodeSystemConcept({"code": "nebamp", "display": "Nebule Amp"})
    """
    Nebule Amp

    
    """

    ovul = CodeSystemConcept({"code": "ovul", "display": "Ovule"})
    """
    Ovule

    
    """

    pch = CodeSystemConcept({"code": "pch", "display": "Pouch"})
    """
    Pouch

    
    """

    pkt = CodeSystemConcept({"code": "pkt", "display": "Packet"})
    """
    Packet

    
    """

    sash = CodeSystemConcept({"code": "sash", "display": "Sashet"})
    """
    Sashet

    
    """

    strip = CodeSystemConcept({"code": "strip", "display": "Strip"})
    """
    Strip

    
    """

    tin = CodeSystemConcept({"code": "tin", "display": "Tin"})
    """
    Tin

    
    """

    tub = CodeSystemConcept({"code": "tub", "display": "Tub"})
    """
    Tub

    
    """

    tube = CodeSystemConcept({"code": "tube", "display": "Tube"})
    """
    Tube

    
    """

    vial = CodeSystemConcept({"code": "vial", "display": "Vial"})
    """
    Vial

    
    """

    class Meta:
        resource = _resource
