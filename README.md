# openenv-data-cleaning-env
Data Cleaning & Preprocessing Environment (OpenEnv)<br>
This project implements a **real-world OpenEnv environment** where an AI agent learns to clean and preprocess messy datasets — a critical task in data science and machine learning pipelines.<br>
 Problem Motivation
In real-world systems used by companies like Microsoft, Google, and Snowflake, raw data is often:<br>
* Incomplete (missing values)<br>
* Inconsistent (different formats)<br>
* Noisy (invalid entries)<br>
* Redundant (duplicate rows)<br>
Before any meaningful analysis or machine learning can be performed, this data must be cleaned.<br>

This environment simulates that process
 Objective

The goal of the agent is to:
* Improve dataset quality step-by-step
* Apply correct data cleaning operations
* Avoid destructive or unnecessary transformations
* Produce a clean dataset efficiently
 Environment Overview

The environment follows the **OpenEnv standard API**:
* `reset()` → loads a new dataset
* `step(action)` → applies a transformation
* `state()` → returns current environment state

Each step updates the dataset and returns a reward based on improvement.

 Observation Space
At each step, the agent receives:
* Dataset snapshot (rows & columns)
* Column metadata:
  * data types
  * missing value counts
  * duplicate counts
* Data quality metrics:
  * % missing values
  * % duplicates
  * format consistency score
 Action Space
The agent can perform:
* `fill_missing(column, method)`
* `drop_missing(column)`
* `remove_duplicates()`
* `standardise_format(column, type)`
* `rename_column(old, new)`
* `filter_rows(condition)`
* `finish()`


 Reward System
The environment uses a **dense reward function**:
Positive Rewards
* Reduce missing values → +0.2
* Remove duplicates → +0.2
* Improve formatting → +0.2
* Fully clean dataset → +0.4 Partial Rewards
* Partial improvements → +0.1 to +0.3

 Penalties

* Incorrect operations → −0.2
* Data loss → −0.3
* Redundant actions → −0.1
* Too many steps → penalty
Tasks
 Easy — Missing Value Handling
* Clean missing values in a single column
Medium — Duplicate + Format Cleaning
* Remove duplicates
* Standardise date formats
Hard — Full Cleaning Pipeline
Handle missing data, duplicates, formats, and noise
 Setup Instructions

 1. Clone Repository

```bash
git clone https://github.com/your-username/openenv-data-cleaning-env.git
cd openenv-data-cleaning-env
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Environment

```bash
python scripts/run_baseline.py
```

---

## 🐳 Docker Support

```bash
docker build -t data-cleaning-env .
docker run data-cleaning-env
```

---

## 📊 Baseline Performance (Initial)

| Task   | Score |
| ------ | ----- |
| Easy   | 1.0   |
| Medium | 0.7   |
| Hard   | 0.5   |

---

 OpenEnv Compliance

* Typed Observation, Action, Reward models
* step(), reset(), state() implemented
* openenv.yaml included
* Agent-based task graders
* Continuous reward shaping

---

Real-World Relevance

This environment reflects workflows in:

* Data science pipelines
* Business analytics
* Machine learning preprocessing

---

 Why This Project Matters

Data cleaning accounts for a significant portion of real-world AI workflows. This environment enables training AI agents to:

* Understand messy data
* Apply structured transformations
* Optimise multi-step workflows

 Author
shan 
