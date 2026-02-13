from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class ExecutionEvent:
    step: int
    event_type: str          # call | line | return | exception
    filename: str
    lineno: int
    function_name: str
    locals_snapshot: Dict[str, Any]
    depth: int
    thread_id: int
    exception: Optional[str] = None
