# OpenBB Biotech Extension - Architecture & Implementation Guide

## Overview

The OpenBB Biotech Extension brings domain-specific biotech and pharmaceutical data analytics to the OpenBB Platform. This implementation follows a modular, open-source architecture for biotech/pharma investing.

## Architecture

```
┌──────────────────────────┐
│ Data Sources             │  ← ClinicalTrials.gov, FDA, EMA, PubMed
└────────────┬─────────────┘
             │
┌────────────▼─────────────┐
│ Data Ingestion Layer     │  ← Provider Fetchers (clinicaltrials, fmp)
│ (Providers)              │
└────────────┬─────────────┘
             │
┌────────────▼─────────────┐
│ Data Storage Layer       │  ← Standard Models (QueryParams, Data)
│ (Standard Models)        │
└────────────┬─────────────┘
             │
┌────────────▼─────────────┐
│ Analytics Layer          │  ← Success Rates, Competitive Analysis
│ (Business Logic)         │
└────────────┬─────────────┘
             │
┌────────────▼─────────────┐
│ API Layer                │  ← FastAPI via OpenBB Core
│ (Extensions/Routers)     │
└────────────┬─────────────┘
             │
┌────────────▼─────────────┐
│ UI / Dashboard /         │  ← Python API, REST API, CLI
│ CLI / Notebooks          │
└──────────────────────────┘
```

## Module Structure

### 1. Extensions (`openbb_platform/extensions/biotech/`)

The biotech extension provides domain-specific routers and commands:

- **biotech_router.py**: Main router with company profile endpoint
- **trials/trials_router.py**: Clinical trials data endpoints
  - `search`: Search for clinical trials by criteria
  - `details`: Get detailed trial information
  - `success_rates`: Analyze trial success rates by indication/phase
- **pipeline/pipeline_router.py**: Drug pipeline endpoints
  - `company`: Get company drug pipeline
  - `competitive_landscape`: Compare pipelines across companies
  - `milestones`: Track regulatory and development milestones

### 2. Providers (`openbb_platform/providers/clinicaltrials/`)

Data source connectors following OpenBB's provider pattern:

- **ClinicalTrialsSearchFetcher**: Fetches clinical trial search results
- **ClinicalTrialsDetailsFetcher**: Fetches detailed trial information

The provider architecture uses the Fetcher pattern with three key methods:
1. `transform_query`: Validates and transforms query parameters
2. `extract_data`: Retrieves data from external source
3. `transform_data`: Transforms raw data to standard format

### 3. Standard Models (`openbb_platform/core/.../standard_models/`)

Data standardization layer ensuring interoperability:

- **clinical_trial_search.py**: Query params and data models for trial search
- **clinical_trial_details.py**: Query params and data models for trial details

Standard models define:
- `QueryParams`: Input parameters with validation
- `Data`: Output data schema with type checking

## Data Sources & Integration

### Current: ClinicalTrials.gov
- **Type**: Public API
- **Authentication**: None required
- **Data**: Clinical trials, study design, enrollment, outcomes
- **Coverage**: Global trials registered in US system

### Planned Future Sources
1. **FDA Databases**: Regulatory decisions, approvals, REMS
2. **EMA**: European regulatory data
3. **PubMed**: Scientific literature, clinical publications
4. **Patent Databases**: USPTO, EPO patent data
5. **Commercial Sources**: BioMedTracker, EvaluatePharma (optional)

## Security & Licensing Considerations

### Open Source (AGPL-3.0)
All components in this repository are licensed under AGPL-3.0-only:
- Core extension framework
- Standard data models
- Public data providers (ClinicalTrials.gov)
- Basic analytics functions

This ensures:
- Complete transparency
- Community collaboration
- Free access to biotech data analytics
- No proprietary lock-in

### Plugin Architecture
The design supports extending with proprietary modules if needed:
- Loaded via plugin system
- Gated by authentication/permissions
- Not included in open-source distribution
- Maintained independently

## Development Guidelines

### Adding New Endpoints

1. Define standard model in `openbb_core/provider/standard_models/`
2. Create fetcher in appropriate provider
3. Add command to router
4. Update documentation

### Adding New Providers

1. Create provider package in `openbb_platform/providers/`
2. Implement fetchers for each data model
3. Register provider in `__init__.py`
4. Add provider to extension dependencies

## Testing

Tests are located in `openbb_platform/extensions/biotech/tests/`

Run tests:
```bash
pytest openbb_platform/extensions/biotech/tests/
```

## API Usage Examples

### Python API
```python
from openbb import obb

# Search trials
results = obb.biotech.trials.search(
    query="cancer", 
    phase="3",
    provider="clinicaltrials"
)

# Get company profile
profile = obb.biotech.profile(symbol="MRNA", provider="fmp")
```

### REST API
```bash
# Start API server
openbb-api

# Query via REST
curl http://localhost:6900/api/v1/biotech/trials/search?query=cancer&phase=3
```

### CLI
```bash
/biotech/trials/search --query cancer --phase 3 --provider clinicaltrials
```

## Future Enhancements

1. **Additional Data Sources**: FDA, EMA, PubMed integration
2. **Advanced Analytics**: ML-based trial success prediction
3. **Portfolio Analysis**: Track biotech holdings and pipeline
4. **Risk Scoring**: Automated assessment of drug development risk
5. **Alert System**: Notifications for trial readouts and regulatory decisions
