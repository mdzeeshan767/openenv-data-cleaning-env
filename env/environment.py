from typing import Tuple, Dict, Any
from copy import deepcopy
from env.models import Observation, Action, Reward


class DataCleaningEnv:
    def __init__(self, dataset: list):
        self.original_data = dataset
        self.data = deepcopy(dataset)
        self.step_count = 0
        self.max_steps = 10

    # Reset environment
    def reset(self) -> Observation:
        self.data = deepcopy(self.original_data)
        self.step_count = 0
        return self._get_observation()

    #  Current state
    def state(self) -> Dict[str, Any]:
        return {
            "data": self.data,
            "step_count": self.step_count
        }

    #  Step function
    def step(self, action: Action) -> Tuple[Observation, Reward, bool, Dict]:
        self.step_count += 1

        if action.action_type == "remove_duplicates":
            self._remove_duplicates()

        elif action.action_type == "fill_missing":
            self._fill_missing(action.column, action.value)

        elif action.action_type == "drop_column":
            self._drop_column(action.column)

        #  Calculate reward
        reward = self._calculate_reward()

        # Done condition
        done = self.step_count >= self.max_steps or reward.score >= 0.95

        return self._get_observation(), reward, done, {}

    #  Helper Functions
 

    def _get_observation(self) -> Observation:
        return Observation(
            dataset=self.data,
            missing_values=self._count_missing(),
            duplicate_rows=self._count_duplicates(),
            columns=list(self.data[0].keys()) if self.data else [],
            step_count=self.step_count
        )

    def _count_missing(self) -> int:
        count = 0
        for row in self.data:
            for value in row.values():
                if value is None:
                    count += 1
        return count

    def _count_duplicates(self) -> int:
        seen = []
        duplicates = 0
        for row in self.data:
            if row in seen:
                duplicates += 1
            else:
                seen.append(row)
        return duplicates

    def _remove_duplicates(self):
        unique = []
        for row in self.data:
            if row not in unique:
                unique.append(row)
        self.data = unique

    def _fill_missing(self, column, value):
        if column is None:
            return
        for row in self.data:
            if row.get(column) is None:
                row[column] = value

    def _drop_column(self, column):
        if column is None:
            return
        for row in self.data:
            row.pop(column, None)

    def _calculate_reward(self) -> Reward:
        missing = self._count_missing()
        duplicates = self._count_duplicates()

        # Simple scoring logic
        score = 1.0 - (0.1 * missing + 0.2 * duplicates)
        score = max(0.0, min(1.0, score))

        return Reward(
            score=score,
            message=f"Missing: {missing}, Duplicates: {duplicates}"
        )