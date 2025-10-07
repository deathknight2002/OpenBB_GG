# OpenBB Biotech Extension

This extension provides biotech and pharmaceutical industry data and analytics for the OpenBB Platform.

## Features

### Clinical Trials Data
- Search and retrieve clinical trial information
- Track trial progress and milestones
- Analyze trial success rates by phase and indication

### Drug Pipeline Analytics
- Company pipeline analysis
- Competitive landscape mapping
- Drug development stage tracking

### Company Profiles
- Biotech company information
- Pipeline and product portfolio
- Regulatory filings and milestones

## Installation

```bash
pip install openbb-biotech
```

## Usage

```python
from openbb import obb

# Search for clinical trials
trials = obb.biotech.trials.search(query="cancer")

# Get company pipeline
pipeline = obb.biotech.pipeline.company(symbol="MRNA")

# Get company profile
profile = obb.biotech.profile(symbol="GILD")
```

## Data Sources

This extension integrates with:
- ClinicalTrials.gov (public clinical trial data)
- FDA regulatory databases
- SEC filings for biotech companies
- PubMed for scientific publications

## Architecture

The extension follows OpenBB Platform conventions:
- Standard data models for interoperability
- Provider-based architecture for multiple data sources
- Extensible analytics layer for domain-specific calculations

## Contributing

See the main OpenBB Platform [contributing guide](../../CONTRIBUTING.md) for information on how to contribute to this extension.
