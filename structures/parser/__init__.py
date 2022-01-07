from typing import Dict, Callable

from structures.parser import code_system

process_lookup: Dict[str, Callable] = {
    'code_system': code_system.concepts
}
