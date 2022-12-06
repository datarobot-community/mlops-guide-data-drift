**Please note:** The code in these repos is sourced from the DataRobot user community and is not owned or maintained by DataRobot, Inc. You may need to make edits or updates for this code to function properly in your environment.

# DataRobot MLOps guide - Data Drift

This repository corresponds to the guide in DataRobot Developers portal that shows you how to monitor data drift in models deployed or monitored with DataRobot MLOps.

You can find the guide at the DataRobot Developers portal: 

## Usage

- Follow the Setup/Installation steps to prepare environment and make sure you have the credentials set
- Run `python check_data_drift.py` to check the current data drift for features
- Run `python cause_data_drift.py` to make predictions with drifted data - which will cause data drift
- Run `python check_data_drift.py` again to compare results

## Repository Contents

Python scripts and datasets for monitoring data drift

## Setup/Installation

- DataRobot account with MLOps enabled. You can apply for a free account at https://datarobot.com/lp/trial
- The Auto MPG model trained and deployed. Follow the quick start guide if you haven't yet - https://api-docs.datarobot.com/docs/quickstart-guide
- Python 3 installed, `venv` created, and dependencies installed:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
- In `cause_data_drift.py` and `check_data_drift.py` replace missing values with your DataRobot values - API keys, deployment ID, and DataRobot URL.

## Development and Contributing

If you'd like to report an issue or bug, suggest improvements, or contribute code to this project, please refer to [CONTRIBUTING.md](CONTRIBUTING.md).


# Code of Conduct

This project has adopted the Contributor Covenant for its Code of Conduct. 
See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) to read it in full.

# License

Licensed under the Apache License 2.0. 
See [LICENSE](LICENSE) to read it in full.


