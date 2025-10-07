# Getting Started with OpenBB Biotech Extension

## Overview

The OpenBB Biotech Extension provides domain-specific data and analytics for biotech and pharmaceutical investing, following the architectural blueprint described in the problem statement.

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
obb.biotech.pipeline.company(
    symbol="MRNA",
    provider="fmp"
)

# Competitive landscape
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

Provides access to clinical trial data from ClinicalTrials.gov:

- **Clinical Trial Search**: Query trials by condition, intervention, phase, status
- **Clinical Trial Details**: Detailed information for specific trials (by NCT ID)

**Note**: Currently uses mock data. See "Next Steps" below for implementing actual API calls.

### 3. Standard Models

**Location**: `openbb_platform/core/openbb_core/provider/standard_models/`

Two new standard models for data standardization:

- `clinical_trial_search.py`: Query params and data schema for trial search
- `clinical_trial_details.py`: Query params and data schema for trial details

These models ensure consistent data structures across different providers.

## Installation (Development Mode)

To install the biotech extension in development mode:

```bash
cd openbb_platform/extensions/biotech
pip install -e .
```

To install the ClinicalTrials.gov provider:

```bash
cd openbb_platform/providers/clinicaltrials
pip install -e .
```

For full platform development setup:

```bash
cd openbb_platform
python dev_install.py
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

## Next Steps for Implementation

### Immediate Tasks

1. **Implement Actual API Calls**
   
   Current implementation uses mock data. To integrate real ClinicalTrials.gov data:
   
   ```python
   # In openbb_clinicaltrials/models/clinical_trial_search.py
   # Replace mock data with actual API call:
   
   import requests
   
   url = "https://clinicaltrials.gov/api/v2/studies"
   response = requests.get(url, params=api_params)
   data = response.json()
   ```

2. **Add to Platform Development Dependencies**
   
   Edit `openbb_platform/dev_install.py` to include:
   
   ```python
   openbb-biotech = { path = "./extensions/biotech", develop = true }
   openbb-clinicaltrials = { path = "./providers/clinicaltrials", develop = true }
   ```

3. **Run Tests**
   
   ```bash
   cd openbb_platform
   pytest extensions/biotech/tests/
   pytest providers/clinicaltrials/tests/
   ```

### Short-Term Enhancements

1. **Add More Providers**
   - FDA regulatory database provider
   - PubMed scientific publications provider
   - SEC filings provider (for biotech companies)

2. **Implement Analytics Functions**
   - Trial success probability models
   - Competitive landscape analytics
   - Patent analysis integration

3. **Enhance Data Models**
   - Add more biotech-specific standard models
   - Patent data models
   - Regulatory milestone models
   - Drug molecule models

### Medium-Term Goals

1. **Machine Learning Models**
   - Bayesian trial success prediction
   - Time-to-approval models
   - Market opportunity estimation

2. **Advanced Visualizations**
   - Kaplan-Meier survival curves
   - Clinical trial timelines
   - Pipeline comparison charts

3. **Knowledge Graph**
   - Entity relationships (drugs, targets, diseases)
   - Citation networks
   - Patent dependencies

## How to Extend

### Adding a New Data Source

1. Create a new provider directory:
   ```bash
   mkdir -p openbb_platform/providers/fda/openbb_fda/models
   ```

2. Define standard models (if needed):
   ```python
   # In openbb_core/provider/standard_models/fda_approval.py
   class FDAApprovalQueryParams(QueryParams):
       drug_name: Optional[str] = Field(default=None)
   
   class FDAApprovalData(Data):
       drug_name: str
       approval_date: date
       indication: str
   ```

3. Implement the provider fetcher:
   ```python
   # In openbb_fda/models/fda_approval.py
   class FDAApprovalFetcher(Fetcher[...]):
       @staticmethod
       def transform_query(params): ...
       
       @staticmethod
       def extract_data(query, credentials): ...
       
       @staticmethod
       def transform_data(query, data): ...
   ```

4. Register the provider:
   ```python
   # In openbb_fda/__init__.py
   fda_provider = Provider(
       name="fda",
       fetcher_dict={"FDAApproval": FDAApprovalFetcher}
   )
   ```

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

## Testing

Run the test suite:

```bash
# Test extension
pytest openbb_platform/extensions/biotech/tests/

# Test provider
pytest openbb_platform/providers/clinicaltrials/tests/

# Test standard models
pytest openbb_platform/core/tests/provider/standard_models/test_biotech_models.py
```

## API Documentation

Once installed, the REST API automatically includes biotech endpoints:

```bash
# Start the API server
openbb-api

# Access documentation
open http://localhost:6900/docs

# Endpoints available:
# GET /api/v1/biotech/profile
# GET /api/v1/biotech/trials/search
# GET /api/v1/biotech/trials/details
# GET /api/v1/biotech/trials/success_rates
# GET /api/v1/biotech/pipeline/company
# GET /api/v1/biotech/pipeline/competitive_landscape
# GET /api/v1/biotech/pipeline/milestones
```

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
│   ├── tests/                          # Provider tests
│   └── pyproject.toml                  # Package configuration
│
└── core/openbb_core/provider/standard_models/
    ├── clinical_trial_search.py        # Standard search model
    └── clinical_trial_details.py       # Standard details model
```

## Contributing

To contribute to the biotech extension:

1. Follow OpenBB's [contributing guidelines](../../CONTRIBUTING.md)
2. Ensure tests pass
3. Update documentation
4. Submit a pull request

## Questions & Support

- Documentation: See `ARCHITECTURE.md` for detailed technical information
- Issues: Report on GitHub
- Community: Join OpenBB Discord for discussions

## License

This extension follows OpenBB Platform's AGPL-3.0 license. Proprietary extensions can use separate licensing as needed.
