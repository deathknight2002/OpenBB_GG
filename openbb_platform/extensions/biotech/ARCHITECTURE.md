# OpenBB Biotech Extension - Architecture & Implementation Guide

## Overview

The OpenBB Biotech Extension brings domain-specific biotech and pharmaceutical data analytics to the OpenBB Platform. This implementation follows the problem statement's blueprint for building an "OpenBB for biotech/pharma investing."

## Architecture

This implementation follows the modular architecture proposed in the problem statement:

```
┌──────────────────────────┐
│ Data Ingestion /         │  ← ClinicalTrials.gov Provider
│ Connectors               │
└──────────────────────────┘
            ↓
┌──────────────────────────┐
│ Data Storage &           │  ← Standard Models (QueryParams + Data)
│ Preprocessing            │
└──────────────────────────┘
            ↓
┌──────────────────────────┐
│ Domain Models &          │  ← Biotech-specific analytics
│ Analytics Layer          │     (success rates, competitive landscape)
└──────────────────────────┘
            ↓
┌──────────────────────────┐
│ API Layer /              │  ← FastAPI integration via OpenBB Core
│ Microservices            │
└──────────────────────────┘
            ↓
┌──────────────────────────┐
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

## Key Design Principles

### Modularity
Each component (extension, provider, model) is independent and can be:
- Developed separately
- Tested in isolation
- Updated without breaking others
- Extended with new functionality

### Standardization
Standard models ensure:
- Consistent data schemas across providers
- Type safety and validation
- Easy integration of new data sources
- Provider interoperability

### Extensibility
The architecture supports:
- **New data sources**: Add providers for FDA, EMA, PubMed, etc.
- **New analytics**: Extend with ML models for trial success prediction
- **New endpoints**: Add routers for patents, publications, molecules
- **Domain models**: Build proprietary analytics as plugins

## Implementation Phases

This initial implementation represents **Phase 1** of the roadmap:

### ✅ Phase 1: MVP Foundation (Current)
- [x] Core extension structure
- [x] Clinical trials search and details
- [x] Drug pipeline tracking
- [x] ClinicalTrials.gov provider
- [x] Standard data models
- [x] Basic architecture documentation

### 🔄 Phase 2: Enhanced Data Sources (Future)
- [ ] FDA regulatory data integration
- [ ] PubMed scientific publications
- [ ] SEC filings for biotech companies
- [ ] Patent database integration
- [ ] Additional provider implementations

### 🔄 Phase 3: Advanced Analytics (Future)
- [ ] Trial success probability models (Bayesian/ML)
- [ ] Competitive landscape analytics
- [ ] Time-to-event predictions
- [ ] Risk scoring algorithms
- [ ] Scenario simulation tools

### 🔄 Phase 4: Visualization & UI (Future)
- [ ] Kaplan-Meier survival curves
- [ ] Clinical timeline visualizations
- [ ] Pipeline comparison charts
- [ ] Dose-response curves
- [ ] Dashboard integration

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
6. **Proprietary Data**: Internal research, deal flow

## Security & Licensing Considerations

### Open vs. Closed Components

Following the problem statement's guidance on dual licensing:

**Open Source (AGPL-3.0):**
- Core extension framework
- Standard data models
- Public data providers (ClinicalTrials.gov)
- Basic analytics functions

**Proprietary (Future):**
- Advanced ML models (trial success prediction)
- Proprietary data connectors
- Internal research integrations
- Custom risk scoring algorithms

### Plugin Architecture
The design supports separate proprietary modules:
- Loaded via plugin system
- Gated by authentication/permissions
- Not included in open-source distribution
- Maintained independently

## Usage Examples

### Python Interface

```python
from openbb import obb

# Search for oncology trials
trials = obb.biotech.trials.search(
    query="lung cancer",
    phase="3",
    status="recruiting",
    provider="clinicaltrials"
)

# Get detailed trial information
details = obb.biotech.trials.details(
    nct_id="NCT04368728",
    provider="clinicaltrials"
)

# Get company pipeline
pipeline = obb.biotech.pipeline.company(
    symbol="MRNA",
    provider="fmp"
)

# Analyze trial success rates
success_rates = obb.biotech.trials.success_rates(
    indication="oncology",
    phase="2",
    provider="analytics"
)

# Company profile
profile = obb.biotech.profile(
    symbol="GILD",
    provider="fmp"
)
```

### REST API Interface

```bash
# Start OpenBB API server
openbb-api

# Query endpoints
curl http://localhost:6900/api/v1/biotech/trials/search?query=cancer&provider=clinicaltrials
curl http://localhost:6900/api/v1/biotech/pipeline/company?symbol=MRNA&provider=fmp
curl http://localhost:6900/api/v1/biotech/profile?symbol=GILD&provider=fmp
```

## Technical Stack

- **Language**: Python 3.9.21+
- **Framework**: FastAPI (via OpenBB Core)
- **Data Validation**: Pydantic v2
- **Testing**: pytest
- **Type Checking**: mypy
- **Code Quality**: ruff, pylint
- **Documentation**: Markdown, docstrings

## Development Workflow

1. **Add New Data Source**:
   - Create provider in `providers/`
   - Implement Fetcher with transform/extract/transform methods
   - Register in provider's `__init__.py`

2. **Add New Endpoint**:
   - Define standard models in `standard_models/`
   - Create router command in extension
   - Link to provider via `@router.command(model="...")`

3. **Add Analytics**:
   - Create analytics provider
   - Implement domain-specific calculations
   - Expose via router commands

## Testing Strategy

### Unit Tests
- Provider data extraction and transformation
- Query parameter validation
- Data model validation

### Integration Tests
- End-to-end command execution
- Provider integration
- API endpoint responses

### Validation Tests
- Data quality checks
- Schema compliance
- Historical accuracy

## Contributing

To extend this implementation:

1. **New Providers**: Follow OpenBB provider conventions
2. **New Analytics**: Use plugin architecture for proprietary models
3. **New Data Sources**: Add standard models first, then providers
4. **Documentation**: Update this guide with new capabilities

## References

- [OpenBB Platform Documentation](https://docs.openbb.co/platform)
- [Contributing Guide](../../CONTRIBUTING.md)
- [Provider Development](../../CONTRIBUTING.md#how-to-add-custom-data-sources)
- [Extension Development](../../CONTRIBUTING.md#how-to-build-openbb-extensions)

## Future Enhancements

### Short Term
- Implement actual ClinicalTrials.gov API calls (currently mock data)
- Add more provider implementations
- Expand trial analytics functions
- Add data caching layer

### Medium Term
- ML models for trial success prediction
- Patent analysis integration
- Publication citation networks
- Real-time milestone alerts

### Long Term
- Knowledge graph for biotech entities
- Advanced scenario modeling
- Integration with lab data systems
- AI agents for research assistance

## Conclusion

This implementation provides a solid foundation for biotech/pharma analytics on the OpenBB Platform. It follows the architectural principles outlined in the problem statement while maintaining OpenBB's conventions for modularity, standardization, and extensibility.

The design allows for incremental enhancement while keeping the core open-source. Proprietary analytics and data sources can be added as plugins without modifying the base framework.
