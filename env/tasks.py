from typing import Dict, Any, Callable
from env.environment import DataCleaningEnv


#  Sample datasets for tasks

# EASY: Only missing values
easy_dataset = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": None},
    {"name": "Charlie", "age": None},
]

# MEDIUM: Missing + duplicates
medium_dataset = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": None},
    {"name": "Bob", "age": None},  # duplicate
    {"name": "Charlie", "age": 30},
]

# HARD: Missing + duplicates + useless column
hard_dataset = [
    {"name": "Alice", "age": None, "temp": "x"},
    {"name": "Bob", "age": None, "temp": "y"},
    {"name": "Bob", "age": None, "temp": "y"},  # duplicate
    {"name": "Charlie", "age": 30, "temp": "z"},
]


# Graders

def easy_grader(env: DataCleaningEnv) -> float:
    if env._count_missing() == 0:
        return 1.0
    return 0.5


def medium_grader(env: DataCleaningEnv) -> float:
    missing = env._count_missing()
    duplicates = env._count_duplicates()

    if missing == 0 and duplicates == 0:
        return 1.0
    elif missing == 0 or duplicates == 0:
        return 0.6
    return 0.2


def hard_grader(env: DataCleaningEnv) -> float:
    missing = env._count_missing()
    duplicates = env._count_duplicates()
    columns = list(env.data[0].keys())

    if missing == 0 and duplicates == 0 and "temp" not in columns:
        return 1.0
    elif missing == 0 and duplicates == 0:
        return 0.7
    return 0.3


#  Task registry

TASKS: Dict[str, Dict[str, Any]] = {
    "easy": {
        "dataset": easy_dataset,
        "grader": easy_grader,
        "description": "Fill missing values in dataset"
    },
    "medium": {
        "dataset": medium_dataset,
        "grader": medium_grader,
        "description": "Remove duplicates and fill missing values"
    },
    "hard": {
        "dataset": hard_dataset,
        "grader": hard_grader,
        "description": "Clean dataset fully (missing, duplicates, useless column)"
    }
}