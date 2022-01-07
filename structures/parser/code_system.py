import json
from textwrap import dedent

from fhir.resources.codesystem import CodeSystem

from structures.utils import snake_case

__all__ = ['concepts']


def concepts(code_system: CodeSystem):
    chunks = []
    for concept in code_system.concept:
        chunk = dedent(f'''
        {snake_case(concept.code)} = {concept.json()}
        """ {concept.definition} """
        ''')
        chunks.append(chunk)

    return '\n'.join(chunks)
