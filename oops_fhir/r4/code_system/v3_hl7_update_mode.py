from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3HL7UpdateMode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3HL7UpdateMode:
    """
    v3 Code System HL7UpdateMode

     The possible modes of updating that occur when an attribute is received
by a system that already contains values for that attribute.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-HL7UpdateMode
    """

    a = CodeSystemConcept(
        {
            "code": "A",
            "definition": "Description:The item was (or is to be) added, having not been present immediately before. (If it is already present, this may be treated as an error condition.)",
            "display": "Add",
        }
    )
    """
    Add

    Description:The item was (or is to be) added, having not been present immediately before. (If it is already present, this may be treated as an error condition.)
    """

    ar = CodeSystemConcept(
        {
            "code": "AR",
            "definition": "Description:The item was (or is to be) either added or replaced.",
            "display": "Add or Replace",
        }
    )
    """
    Add or Replace

    Description:The item was (or is to be) either added or replaced.
    """

    d = CodeSystemConcept(
        {
            "code": "D",
            "definition": "Description:The item was (or is to be) removed (sometimes referred to as deleted). If the item is part of a collection, delete any matching items.",
            "display": "Remove",
        }
    )
    """
    Remove

    Description:The item was (or is to be) removed (sometimes referred to as deleted). If the item is part of a collection, delete any matching items.
    """

    k = CodeSystemConcept(
        {
            "code": "K",
            "definition": "Description:This item is part of the identifying information for this object.",
            "display": "Key",
        }
    )
    """
    Key

    Description:This item is part of the identifying information for this object.
    """

    n = CodeSystemConcept(
        {
            "code": "N",
            "definition": "Description:There was (or is to be) no change to the item. This is primarily used when this element has not changed, but other attributes in the instance have changed.",
            "display": "No Change",
        }
    )
    """
    No Change

    Description:There was (or is to be) no change to the item. This is primarily used when this element has not changed, but other attributes in the instance have changed.
    """

    r = CodeSystemConcept(
        {
            "code": "R",
            "definition": "Description:The item existed previously and has (or is to be) revised. (If an item does not already exist, this may be treated as an error condition.)",
            "display": "Replace",
        }
    )
    """
    Replace

    Description:The item existed previously and has (or is to be) revised. (If an item does not already exist, this may be treated as an error condition.)
    """

    ref = CodeSystemConcept(
        {
            "code": "REF",
            "definition": "Description:This item provides enough information to allow a processing system to locate the full applicable record by identifying the object.",
            "display": "Reference",
        }
    )
    """
    Reference

    Description:This item provides enough information to allow a processing system to locate the full applicable record by identifying the object.
    """

    u = CodeSystemConcept(
        {
            "code": "U",
            "definition": "Description:Description:</b>It is not specified whether or what kind of change has occurred to the item, or whether the item is present as a reference or identifying property.",
            "display": "Unknown",
        }
    )
    """
    Unknown

    Description:Description:</b>It is not specified whether or what kind of change has occurred to the item, or whether the item is present as a reference or identifying property.
    """

    underscore_set_update_mode = CodeSystemConcept(
        {
            "code": "_SetUpdateMode",
            "concept": [
                {
                    "code": "ESA",
                    "definition": "Add the message element to the collection of items on the receiving system that correspond to the message element.",
                    "display": "Set Add",
                    "property": [{"code": "status", "valueCode": "retired"}],
                },
                {
                    "code": "ESAC",
                    "definition": "Change the item on the receiving system that corresponds to this message element; if a matching element does not exist, add a new one created with the values in the message.",
                    "display": "Set Add or Change",
                    "property": [{"code": "status", "valueCode": "retired"}],
                },
                {
                    "code": "ESC",
                    "definition": "Change the item on the receiving system that corresponds to this message element; do not process if a matching element does not exist.",
                    "display": "Set Change",
                    "property": [{"code": "status", "valueCode": "retired"}],
                },
                {
                    "code": "ESD",
                    "definition": "Delete the item on the receiving system that corresponds to this message element.",
                    "display": "Set Delete",
                    "property": [{"code": "status", "valueCode": "retired"}],
                },
            ],
            "definition": "These concepts apply when the element and/or message is updating a set of items.",
            "display": "SetUpdateMode",
            "property": [
                {"code": "notSelectable", "valueBoolean": True},
                {"code": "status", "valueCode": "retired"},
            ],
        }
    )
    """
    SetUpdateMode

    These concepts apply when the element and/or message is updating a set of items.
    """

    au = CodeSystemConcept(
        {
            "code": "AU",
            "definition": "Description: AU: If this item exists, update it with these values. If it does not exist, create it with these values. If the item is part of the collection, update each item that matches this item, and if no items match, add a new item to the collection.",
            "display": "Add or Update",
            "property": [{"code": "status", "valueCode": "retired"}],
        }
    )
    """
    Add or Update

    Description: AU: If this item exists, update it with these values. If it does not exist, create it with these values. If the item is part of the collection, update each item that matches this item, and if no items match, add a new item to the collection.
    """

    i = CodeSystemConcept(
        {
            "code": "I",
            "definition": "Ignore this role, it is not relevant to the update.",
            "display": "Ignore",
            "property": [{"code": "status", "valueCode": "retired"}],
        }
    )
    """
    Ignore

    Ignore this role, it is not relevant to the update.
    """

    v = CodeSystemConcept(
        {
            "code": "V",
            "definition": "Verify - this message element must match a value already in the receiving systems database in order to process the message.",
            "display": "Verify",
            "property": [{"code": "status", "valueCode": "retired"}],
        }
    )
    """
    Verify

    Verify - this message element must match a value already in the receiving systems database in order to process the message.
    """

    class Meta:
        resource = _resource
