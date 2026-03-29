from fastapi import FastAPI
from env.environment import DataCleaningEnv
from env.models import Action
import json

app = FastAPI()

# Load dataset
with open("data/raw/sample_dataset.json") as f:
    dataset = json.load(f)

env = DataCleaningEnv(dataset)

# RESET
@app.post("/reset")
def reset():
    obs = env.reset()
    return {
        "dataset": obs.dataset,
        "missing_values": obs.missing_values,
        "duplicate_rows": obs.duplicate_rows,
        "columns": obs.columns,
        "step_count": obs.step_count
    }

#  STATE
@app.get("/state")
def state():
    return env.state()

# STEP
@app.post("/step")
def step(action: dict):
    action_obj = Action(**action)
    obs, reward, done, _ = env.step(action_obj)

    return {
        "observation": {
            "dataset": obs.dataset,
            "missing_values": obs.missing_values,
            "duplicate_rows": obs.duplicate_rows,
            "columns": obs.columns,
            "step_count": obs.step_count
        },
        "reward": {
            "score": reward.score,
            "message": reward.message
        },
        "done": done
    }
# server/app.py

def main():
    print("Server started")

# Standard Python entry point
if __name__ == "__main__":
    main()