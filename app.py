from fastapi import FastAPI
from env.environment import DataCleaningEnv
from env.models import Action

app = FastAPI()

# Load dataset
import json
with open("data/raw/sample_dataset.json") as f:
    dataset = json.load(f)

env = DataCleaningEnv(dataset)

# RESET
@app.post("/reset")
def reset():
    obs = env.reset()
    return obs.dict()

# STATE
@app.get("/state")
def state():
    return env.state()

# STEP
@app.post("/step")
def step(action: Action):
    obs, reward, done, _ = env.step(action)
    return {
        "observation": obs.dict(),
        "reward": reward.dict(),
        "done": done
    }