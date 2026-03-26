from env.environment import DataCleaningEnv
from env.tasks import TASKS
from env.models import Action


# Simple rule-based agent
def simple_agent(env: DataCleaningEnv):
    observation = env.reset()
    done = False

    while not done:
        # Strategy:
        # 1. Fill missing values
        if observation.missing_values > 0:
            action = Action(
                action_type="fill_missing",
                column="age",
                value=0
            )

        # 2. Remove duplicates
        elif observation.duplicate_rows > 0:
            action = Action(
                action_type="remove_duplicates"
            )

        # 3. Drop useless column (for hard task)
        elif "temp" in observation.columns:
            action = Action(
                action_type="drop_column",
                column="temp"
            )

        else:
            break

        observation, reward, done, _ = env.step(action)

    return env


# Run all tasks
def run():
    results = {}

    for task_name, task in TASKS.items():
        print(f"\nRunning task: {task_name}")

        env = DataCleaningEnv(task["dataset"])
        env = simple_agent(env)

        score = task["grader"](env)
        results[task_name] = score

        print(f"Score: {score}")

    print("\nFinal Results:", results)


if __name__ == "__main__":
    run()