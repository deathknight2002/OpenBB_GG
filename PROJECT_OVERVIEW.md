# OpenBB Biotech Extension - Project Overview

## Introduction

This project implements a biotech and pharmaceutical data analytics extension for the OpenBB Platform, following the architectural blueprint outlined in the problem statement for building an "OpenBB for biotech/pharma investing."

## Project Structure

```
OpenBB_GG/
├── IMPLEMENTATION_SUMMARY.md                    # Maps implementation to requirements
│
├── openbb_platform/
│   ├── extensions/biotech/                      # BIOTECH EXTENSION
│   │   ├── openbb_biotech/
│   │   │   ├── biotech_router.py               # Main router (company profiles)
│   │   │   ├── trials/
│   │   │   │   └── trials_router.py            # Clinical trials endpoints
│   │   │   └── pipeline/
│   │   │       └── pipeline_router.py          # Drug pipeline endpoints
│   │   ├── tests/
│   │   │   └── test_biotech_extension.py       # Extension tests
│   │   ├── pyproject.toml                      # Package configuration
│   │   ├── README.md                           # User documentation
│   │   ├── ARCHITECTURE.md                     # Technical architecture
│   │   └── GETTING_STARTED.md                  # Implementation guide
│   │
│   ├── providers/clinicaltrials/                # CLINICAL TRIALS PROVIDER
│   │   ├── openbb_clinicaltrials/
│   │   │   ├── __init__.py                     # Provider registration
│   │   │   ├── models/
│   │   │   │   ├── clinical_trial_search.py    # Search fetcher
│   │   │   │   └── clinical_trial_details.py   # Details fetcher
│   │   │   └── utils/
│   │   │       └── helpers.py                  # Utility functions
│   │   ├── tests/
│   │   │   └── test_clinicaltrials_provider.py # Provider tests
│   │   ├── pyproject.toml                      # Package configuration
│   │   └── README.md                           # Provider documentation
│   │
│   └── core/openbb_core/provider/
│       └── standard_models/                     # STANDARD MODELS
│           ├── clinical_trial_search.py         # Trial search data schema
│           └── clinical_trial_details.py        # Trial details data schema
```

## Key Components

### 1. Biotech Extension (openbb-biotech)

**Purpose**: Provides domain-specific API endpoints for biotech/pharma data

**Endpoints**:
- `obb.biotech.profile(symbol)` - Company profile
- `obb.biotech.trials.search(query, phase, status)` - Search clinical trials
- `obb.biotech.trials.details(nct_id)` - Get trial details
- `obb.biotech.trials.success_rates(indication, phase)` - Analyze success rates
- `obb.biotech.pipeline.company(symbol)` - Get drug pipeline
- `obb.biotech.pipeline.competitive_landscape(indication)` - Competitive analysis
- `obb.biotech.pipeline.milestones(symbol)` - Track development milestones

**Key Files**:
- `biotech_router.py` - Main router with company profile endpoint
- `trials/trials_router.py` - Clinical trials functionality (3 endpoints)
- `pipeline/pipeline_router.py` - Drug pipeline functionality (3 endpoints)

### 2. ClinicalTrials.gov Provider (openbb-clinicaltrials)

**Purpose**: Fetches clinical trial data from ClinicalTrials.gov API

**Fetchers**:
- `ClinicalTrialsSearchFetcher` - Search for trials by criteria
- `ClinicalTrialsDetailsFetcher` - Get detailed trial information

**Key Files**:
- `__init__.py` - Registers provider with OpenBB Platform
- `models/clinical_trial_search.py` - Search implementation
- `models/clinical_trial_details.py` - Details implementation

### 3. Standard Models

**Purpose**: Defines standardized data schemas for interoperability

**Models**:
- `ClinicalTrialSearchQueryParams` + `ClinicalTrialSearchData`
- `ClinicalTrialDetailsQueryParams` + `ClinicalTrialDetailsData`

**Key Files**:
- `clinical_trial_search.py` - Search query params and data schema
- `clinical_trial_details.py` - Details query params and data schema

## Architecture Principles

### Modularity
Each component is independent:
- **Extension**: Defines API surface and commands
- **Provider**: Implements data fetching from sources
- **Standard Models**: Ensure data consistency

### Extensibility
Easy to add:
- New data sources (add providers)
- New analytics (add router commands)
- New data types (add standard models)

### Standardization
Standard models ensure:
- Consistent data schemas
- Type safety with Pydantic
- Interoperability between providers

### Plugin Architecture
Supports:
- Open-source components (public data, basic analytics)
- Proprietary components (advanced ML, internal data)
- Independent development and deployment

## Usage Examples

### Python Interface

```python
from openbb import obb

# Search for cancer trials in Phase 3
trials = obb.biotech.trials.search(
    query="lung cancer",
    phase="3",
    status="recruiting",
    provider="clinicaltrials"
)

# Get details for a specific trial
details = obb.biotech.trials.details(
    nct_id="NCT04368728",
    provider="clinicaltrials"
)

# Get Moderna's drug pipeline
pipeline = obb.biotech.pipeline.company(
    symbol="MRNA",
    provider="fmp"
)

# Analyze trial success rates in oncology
success = obb.biotech.trials.success_rates(
    indication="oncology",
    phase="2",
    provider="analytics"
)
```

### REST API

```bash
# Start OpenBB API server
openbb-api

# Search for trials
curl "http://localhost:6900/api/v1/biotech/trials/search?query=cancer&provider=clinicaltrials"

# Get company pipeline
curl "http://localhost:6900/api/v1/biotech/pipeline/company?symbol=MRNA&provider=fmp"

# Get company profile
curl "http://localhost:6900/api/v1/biotech/profile?symbol=GILD&provider=fmp"
```

## Implementation Status

### ✅ Completed

1. **Core Architecture**
   - Modular extension structure
   - Provider pattern implementation
   - Standard models for data validation
   - API integration via FastAPI

2. **Biotech Extension**
   - 7 API endpoints across 3 routers
   - Company profiles, trials, pipeline
   - Analytics framework (success rates, competitive landscape)

3. **ClinicalTrials.gov Provider**
   - Search and details fetchers
   - Query parameter validation
   - Data transformation pipeline

4. **Documentation**
   - User guide (README.md)
   - Architecture guide (ARCHITECTURE.md)
   - Getting started guide (GETTING_STARTED.md)
   - Implementation summary (IMPLEMENTATION_SUMMARY.md)
   - This overview document

5. **Testing**
   - Extension import tests
   - Provider functionality tests
   - Standard model validation tests

### ⚠️ Ready for Implementation

1. **API Integration**
   - Replace mock data with actual ClinicalTrials.gov API calls
   - Implement HTTP request handling
   - Add error handling and retry logic

2. **Additional Providers**
   - FDA regulatory database
   - PubMed scientific publications
   - Patent databases (USPTO, EPO)
   - SEC filings for biotech companies

3. **Advanced Analytics**
   - Machine learning models for trial success prediction
   - Bayesian probability models
   - Time-to-event analysis
   - Competitive intelligence algorithms

4. **Visualization**
   - Kaplan-Meier survival curves
   - Clinical trial timelines
   - Pipeline comparison charts
   - Development stage visualizations

## How to Use This Project

### For Users

1. **Read User Documentation**
   - Start with `openbb_platform/extensions/biotech/README.md`
   - Review usage examples and API reference

2. **Install the Extension**
   ```bash
   pip install openbb-biotech openbb-clinicaltrials
   ```

3. **Use in Python or REST API**
   - See usage examples above
   - Access OpenAPI docs at http://localhost:6900/docs

### For Developers

1. **Understand the Architecture**
   - Read `openbb_platform/extensions/biotech/ARCHITECTURE.md`
   - Review the modular design principles

2. **Get Started with Development**
   - Read `openbb_platform/extensions/biotech/GETTING_STARTED.md`
   - Follow extension patterns and examples

3. **Add New Features**
   - New data sources: Create providers
   - New endpoints: Add router commands
   - New analytics: Implement fetchers

### For Contributors

1. **Review Implementation**
   - Read `IMPLEMENTATION_SUMMARY.md` for alignment with requirements
   - Check code quality and standards compliance

2. **Run Tests**
   ```bash
   pytest openbb_platform/extensions/biotech/tests/
   pytest openbb_platform/providers/clinicaltrials/tests/
   ```

3. **Extend the Platform**
   - Follow OpenBB contributing guidelines
   - Add your data sources or analytics
   - Submit pull requests

## Key Documents

| Document | Purpose | Location |
|----------|---------|----------|
| README.md | User documentation | `extensions/biotech/README.md` |
| ARCHITECTURE.md | Technical design | `extensions/biotech/ARCHITECTURE.md` |
| GETTING_STARTED.md | Implementation guide | `extensions/biotech/GETTING_STARTED.md` |
| IMPLEMENTATION_SUMMARY.md | Requirement mapping | Root directory |
| PROJECT_OVERVIEW.md | This document | Root directory |

## Technology Stack

- **Language**: Python 3.9.21+
- **Framework**: FastAPI (via OpenBB Core)
- **Validation**: Pydantic v2
- **Testing**: pytest
- **Package Management**: Poetry
- **License**: AGPL-3.0 (with dual-licensing support)

## Design Decisions

### Why Separate Extension and Provider?

- **Extension**: Defines the API surface (what endpoints exist)
- **Provider**: Implements data fetching (where data comes from)
- **Benefit**: Multiple providers can serve the same endpoint

### Why Standard Models?

- Ensures consistency across providers
- Enables type safety and validation
- Makes it easy to switch providers
- Supports data standardization

### Why Mock Data in Provider?

- Demonstrates the pattern without API dependencies
- Allows testing of structure and integration
- Easy to replace with real implementation
- No API rate limiting during development

## Future Roadmap

### Phase 1 (Current) ✅
- Core architecture and framework
- Basic endpoints and routers
- ClinicalTrials.gov provider structure
- Comprehensive documentation

### Phase 2 (Short-term)
- Implement actual API calls
- Add FDA and PubMed providers
- Enhance analytics functions
- Integration testing

### Phase 3 (Medium-term)
- Machine learning models
- Advanced visualizations
- Knowledge graph integration
- Real-time alerts

### Phase 4 (Long-term)
- AI agents for research
- Proprietary data sources
- Advanced scenario modeling
- Enterprise features

## Success Metrics

This implementation successfully delivers:

1. ✅ **Complete architectural foundation** following problem statement
2. ✅ **Modular, extensible design** for independent development
3. ✅ **Standard conventions** aligned with OpenBB Platform
4. ✅ **Comprehensive documentation** for users and developers
5. ✅ **Working skeleton** ready for production implementation

## Contact & Support

- **Documentation**: See files listed above
- **Issues**: Report on GitHub
- **Community**: OpenBB Discord
- **Contributing**: See OpenBB contributing guidelines

## License

AGPL-3.0 (following OpenBB Platform)

With support for:
- Open-source components (core framework, public data)
- Proprietary components (advanced models, internal data)
- Dual licensing for commercial use

---

**Note**: This is a foundational implementation that demonstrates the architecture and provides a working skeleton. The next step is to implement actual API calls and add real analytics models to transform this into a production-ready biotech analytics platform.
