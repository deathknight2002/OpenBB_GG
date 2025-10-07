# OpenBB ClinicalTrials.gov Provider

This provider offers access to clinical trial data from ClinicalTrials.gov, the U.S. government's registry of clinical trials.

## Features

- Search for clinical trials by disease, intervention, phase, and status
- Retrieve detailed trial information including design, endpoints, and enrollment
- Access historical trial data for analysis

## Data Source

Data is sourced from ClinicalTrials.gov API (https://clinicaltrials.gov/api/v2/), which is publicly available and does not require authentication.

## Installation

```bash
pip install openbb-clinicaltrials
```

## Usage

```python
from openbb import obb

# Search for trials
trials = obb.biotech.trials.search(query="cancer", provider="clinicaltrials")

# Get trial details
details = obb.biotech.trials.details(nct_id="NCT04368728", provider="clinicaltrials")
```
