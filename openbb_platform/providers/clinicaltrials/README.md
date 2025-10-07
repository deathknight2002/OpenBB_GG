# ClinicalTrials.gov Provider for OpenBB

Open-source provider for accessing clinical trial data from ClinicalTrials.gov.

## Features

- Search clinical trials by disease, intervention, phase, and status
- Get detailed trial information including study design, endpoints, and outcomes
- No API key required (public data)
- Real-time access to global clinical trial database

## Data Source

**ClinicalTrials.gov** is a database of privately and publicly funded clinical studies conducted around the world, maintained by the U.S. National Library of Medicine.

- **Website**: https://clinicaltrials.gov
- **API Documentation**: https://clinicaltrials.gov/api/
- **Coverage**: Over 400,000 research studies in 220 countries

## Supported Models

### ClinicalTrialSearch
Search for clinical trials by criteria.

**Query Parameters:**
- `query` (required): Search query (disease, intervention, etc.)
- `phase`: Trial phase (1, 2, 3, 4)
- `status`: Recruitment status (recruiting, completed, etc.)
- `max_results`: Maximum results to return (default: 20)

**Data Fields:**
- NCT ID
- Title
- Status
- Phase
- Enrollment
- Conditions
- Interventions
- Sponsor
- Start date

### ClinicalTrialDetails
Get detailed information about a specific trial.

**Query Parameters:**
- `nct_id` (required): ClinicalTrials.gov NCT identifier

**Data Fields:**
- All search fields plus:
- Brief summary
- Detailed description
- Study type
- Primary and secondary outcomes
- Collaborators
- Completion date
- Locations

## Usage

```python
from openbb import obb

# Search for trials
trials = obb.biotech.trials.search(
    query="cancer",
    phase="3",
    status="recruiting",
    provider="clinicaltrials"
)

# Get trial details
details = obb.biotech.trials.details(
    nct_id="NCT04368728",
    provider="clinicaltrials"
)
```

## Installation

Included with the biotech extension:

```bash
pip install openbb[biotech]
```

Or install directly:

```bash
pip install -e openbb_platform/providers/clinicaltrials
```

## License

Licensed under AGPL-3.0-only, making it fully open source.

## Data Licensing

Data from ClinicalTrials.gov is public domain and can be freely used, redistributed, and built upon.
