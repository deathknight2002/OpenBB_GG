# OpenBB Biotech Extension

The OpenBB Biotech Extension provides domain-specific data and analytics for biotech and pharmaceutical investing.

## Features

### Company Profiles
Get comprehensive biotech company profiles including pipeline, trials, and regulatory information.

```python
from openbb import obb
obb.biotech.profile(symbol="MRNA", provider="fmp")
```

### Clinical Trials
Access clinical trial data from ClinicalTrials.gov:

```python
# Search for trials
obb.biotech.trials.search(
    query="cancer",
    phase="3",
    status="recruiting",
    provider="clinicaltrials"
)

# Get trial details
obb.biotech.trials.details(
    nct_id="NCT04368728",
    provider="clinicaltrials"
)
```

### Drug Pipeline
Track drug development pipelines:

```python
# Get company pipeline
obb.biotech.pipeline.company(symbol="MRNA", provider="fmp")

# Analyze competitive landscape
obb.biotech.pipeline.competitive_landscape(
    indication="oncology",
    provider="analytics"
)

# Track milestones
obb.biotech.pipeline.milestones(symbol="GILD", provider="fmp")
```

## Data Sources

- **ClinicalTrials.gov**: Public clinical trials database (no API key required)
- **FMP (Financial Modeling Prep)**: Company profiles and pipeline data

## Installation

This extension is included in the main OpenBB Platform package. To use it:

```bash
pip install openbb[biotech]
```

Or install from source:

```bash
pip install -e openbb_platform/extensions/biotech
```

## License

This extension is licensed under AGPL-3.0-only, making it fully open source.
