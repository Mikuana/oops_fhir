from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["SNOMEDCT"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class SNOMEDCT:
    """
    SNOMED CT (all versions)

    SNOMED CT is the most comprehensive and precise clinical health
terminology product in the world, owned and distributed around the world
by The International Health Terminology Standards Development
Organisation (IHTSDO).

    Status: active - Version: None

    Copyright © 2002-2016 International Health Terminology Standards Development Organisation (IHTSDO). All rights reserved. SNOMED CT®, was originally created by The College of American Pathologists. "SNOMED" and "SNOMED CT" are registered trademarks of the IHTSDO http://www.ihtsdo.org/snomed-ct/get-snomed-ct

    http://snomed.info/sct
    """

    class Meta:
        resource = _resource
