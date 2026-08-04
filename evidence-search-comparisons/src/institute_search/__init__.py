"""Reusable evidence-search orchestration core.

The package is intentionally domain-agnostic. Scientific questions, competing
models, temporal ontologies, phenotype layers, genetics, BPSD, and other domain
constructs live in configuration files or optional hooks.
"""

from .config import RunConfig, load_config
from .engine import EvidenceSearchEngine
from .state import RunState

__all__ = ["RunConfig", "RunState", "EvidenceSearchEngine", "load_config"]
__version__ = "0.1.0"
