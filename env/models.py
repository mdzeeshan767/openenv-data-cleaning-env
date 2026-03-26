from pydantic import BaseModel
from typing import List, Optional, Dict, Any


# 📥 Observation (what agent sees)
class Observation(BaseModel):
    dataset: List[Dict[str, Any]]  # table data
    missing_values: int
    duplicate_rows: int
    columns: List[str]
    step_count: int


# 🎮 Action (what agent does)
class Action(BaseModel):
    action_type: str  # e.g., fill_missing, remove_duplicates, etc.
    column: Optional[str] = None
    method: Optional[str] = None
    value: Optional[Any] = None


# 🏆 Reward (feedback)
class Reward(BaseModel):
    score: float  # between 0.0 and 1.0
    message: str