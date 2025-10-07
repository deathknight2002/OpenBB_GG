# Getting Started with OpenBB Biotech Extension

## Overview

The OpenBB Biotech Extension provides domain-specific data and analytics for biotech and pharmaceutical investing, following an open-source architectural blueprint.

## Quick Start

### Installation

```bash
pip install openbb[biotech]
```

### Basic Usage

```python
from openbb import obb

# Search for cancer trials
trials = obb.biotech.trials.search(
    query="cancer",
    phase="3",
    provider="clinicaltrials"
)
print(trials.to_dataframe())

# Get detailed trial information
details = obb.biotech.trials.details(
    nct_id="NCT04368728",
    provider="clinicaltrials"
)
print(details.to_dict())
```

## What Has Been Implemented

### 1. Core Extension (`openbb-biotech`)

**Location**: `openbb_platform/extensions/biotech/`

The biotech extension provides three main areas of functionality:

#### Company Profiles
```python
# Get biotech company profile
obb.biotech.profile(symbol="MRNA", provider="fmp")
```

#### Clinical Trials
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

# Analyze success rates
obb.biotech.trials.success_rates(
    indication="oncology",
    phase="2",
    provider="analytics"
)
```

#### Drug Pipeline
```python
# Get company pipeline
obb.biotech.pipeline.company(symbol="MRNA", provider="fmp")

# Competitive landscape analysis
obb.biotech.pipeline.competitive_landscape(
    indication="oncology",
    symbols="MRNA,GILD,PFE",
    provider="analytics"
)

# Track milestones
obb.biotech.pipeline.milestones(
    symbol="GILD",
    months_ahead=6,
    provider="fmp"
)
```

### 2. ClinicalTrials.gov Provider (`openbb-clinicaltrials`)

**Location**: `openbb_platform/providers/clinicaltrials/`

Open-source provider for ClinicalTrials.gov data:
- No API key required
- Public data access
- Real-time trial information
- Comprehensive trial details

### 3. Standard Models

**Location**: `openbb_platform/core/openbb_core/provider/standard_models/`

Data models ensuring interoperability:
- `clinical_trial_search.py`: Trial search parameters and results
- `clinical_trial_details.py`: Detailed trial information

## How to Extend

### Adding a New Data Source

1. Create a new provider package:
```bash
mkdir -p openbb_platform/providers/newprovider/openbb_newprovider/models
```

2. Implement fetchers following the pattern in `clinicaltrials` provider

3. Register the provider in `__init__.py`

### Adding a New Endpoint

1. Define the standard model
2. Add a command to the appropriate router:
   ```python
   @router.command(model="FDAApproval")
   async def approvals(cc, provider_choices, standard_params, extra_params):
       return await OBBject.from_query(Query(**locals()))
   ```

### Adding Proprietary Analytics

For proprietary models that should remain private:

1. Create a separate provider (not in the main repository)
2. Use the plugin architecture:
   ```python
   proprietary_provider = Provider(
       name="analytics",
       fetcher_dict={
           "TrialSuccessRates": ProprietarySuccessRatesFetcher
       }
   )
   ```
3. Install privately: `pip install /path/to/proprietary/provider`

## Key Files Reference

```
openbb_platform/
├── extensions/biotech/
│   ├── openbb_biotech/
│   │   ├── biotech_router.py          # Main router
│   │   ├── trials/trials_router.py     # Clinical trials endpoints
│   │   └── pipeline/pipeline_router.py # Drug pipeline endpoints
│   ├── tests/                          # Extension tests
│   ├── pyproject.toml                  # Package configuration
│   ├── README.md                       # User documentation
│   └── ARCHITECTURE.md                 # Architecture guide
│
├── providers/clinicaltrials/
│   ├── openbb_clinicaltrials/
│   │   ├── __init__.py                 # Provider registration
│   │   └── models/
│   │       ├── clinical_trial_search.py    # Search fetcher
│   │       └── clinical_trial_details.py   # Details fetcher
│   ├── pyproject.toml                  # Provider package config
│   └── README.md                       # Provider documentation
│
└── core/openbb_core/provider/standard_models/
    ├── clinical_trial_search.py        # Standard search model
    └── clinical_trial_details.py       # Standard details model
```

## Architecture Alignment

This implementation follows the modular architecture from the problem statement:

```
Data Sources (ClinicalTrials.gov)
        ↓
Data Ingestion (Provider Fetchers)
        ↓
Data Storage (Standard Models)
        ↓
Analytics Layer (Success Rates, Competitive Analysis)
        ↓
API Layer (FastAPI via OpenBB Core)
        ↓
User Interface (Python API, REST API, CLI)
```

### Key Design Principles

1. **Modularity**: Extensions, providers, and models are independent
2. **Standardization**: Standard models ensure interoperability
3. **Extensibility**: Easy to add new data sources and analytics
4. **Plugin Architecture**: Proprietary components can be added separately

## Common Use Cases

### 1. Trial Discovery & Analysis

```python
# Find all Phase 3 oncology trials
trials = obb.biotech.trials.search(
    query="cancer",
    phase="3",
    status="recruiting",
    provider="clinicaltrials"
)

# Analyze each trial
for trial in trials.results:
    details = obb.biotech.trials.details(
        nct_id=trial.nct_id,
        provider="clinicaltrials"
    )
    print(f"{details.results[0].title}: {details.results[0].enrollment} patients")
```

### 2. Company Pipeline Analysis

```python
# Compare pipeline across companies
landscape = obb.biotech.pipeline.competitive_landscape(
    indication="diabetes",
    symbols="MRNA,GILD,PFE",
    provider="analytics"
)

# Track upcoming catalysts
milestones = obb.biotech.pipeline.milestones(
    symbol="MRNA",
    months_ahead=6,
    provider="fmp"
)
```

### 3. Investment Research Workflow

```python
# Step 1: Identify trials
trials = obb.biotech.trials.search(
    query="alzheimer",
    phase="3",
    provider="clinicaltrials"
)

# Step 2: Get success probability
success_rates = obb.biotech.trials.success_rates(
    indication="neurology",
    phase="3",
    provider="analytics"
)

# Step 3: Analyze company
profile = obb.biotech.profile(
    symbol="BIIB",
    provider="fmp"
)

# Step 4: Track milestones
milestones = obb.biotech.pipeline.milestones(
    symbol="BIIB",
    provider="fmp"
)
```

## FAQ

### Q: Do I need API keys?
A: ClinicalTrials.gov provider requires no API key. Other providers (FMP, analytics) may require keys.

### Q: Is all data open source?
A: Yes! The ClinicalTrials.gov provider uses public data. All code is AGPL-3.0 licensed.

### Q: Can I add my own data sources?
A: Yes! Follow the provider pattern and create your own fetchers.

### Q: How do I contribute?
A: See CONTRIBUTING.md in the repository root. All contributions are welcome!

## Support

- **Documentation**: https://docs.openbb.co
- **Discord**: https://openbb.co/discord
- **GitHub Issues**: https://github.com/OpenBB-finance/OpenBB/issues
- **Email**: support@openbb.co

## License

This extension is licensed under AGPL-3.0-only, ensuring it remains fully open source.
