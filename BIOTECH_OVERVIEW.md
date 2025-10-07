# OpenBB Biotech/Pharma Platform - Complete Overview

## Introduction

This is a **100% open-source** financial platform specialized for biotech and pharmaceutical investing, built on the OpenBB Platform. All components are licensed under AGPL-3.0 with no proprietary modules or closed-source code.

## Why Biotech/Pharma Focus?

Biotech and pharmaceutical investing requires specialized data and analytics:

- **Clinical Trials**: Track drug development progress through trial phases
- **Regulatory Milestones**: Monitor FDA/EMA decisions and approvals
- **Pipeline Analysis**: Evaluate company drug portfolios and competitive positioning
- **Success Analytics**: Assess probability of success based on historical data
- **Investment Research**: Comprehensive tools for biotech due diligence

Traditional financial platforms lack this domain-specific functionality. OpenBB fills this gap with a fully open-source solution.

## What Has Been Built

### 1. Biotech Extension (`openbb-biotech`)

**Location**: `openbb_platform/extensions/biotech/`

A complete extension providing:

#### Company Profiles
```python
obb.biotech.profile(symbol="MRNA", provider="fmp")
```

#### Clinical Trials
- **Search**: Find trials by disease, phase, status
- **Details**: Get comprehensive trial information
- **Success Rates**: Analyze historical success probabilities

```python
obb.biotech.trials.search(query="cancer", phase="3", provider="clinicaltrials")
obb.biotech.trials.details(nct_id="NCT04368728", provider="clinicaltrials")
obb.biotech.trials.success_rates(indication="oncology", provider="analytics")
```

#### Drug Pipeline
- **Company Pipeline**: Track drugs in development
- **Competitive Landscape**: Compare pipelines across companies
- **Milestones**: Monitor upcoming catalysts

```python
obb.biotech.pipeline.company(symbol="GILD", provider="fmp")
obb.biotech.pipeline.competitive_landscape(indication="oncology", provider="analytics")
obb.biotech.pipeline.milestones(symbol="MRNA", provider="fmp")
```

### 2. ClinicalTrials.gov Provider (`openbb-clinicaltrials`)

**Location**: `openbb_platform/providers/clinicaltrials/`

Open-source provider for ClinicalTrials.gov:
- **No API key required** - uses public data
- Real-time access to 400,000+ clinical trials
- Search and detailed information fetchers
- Compliant with ClinicalTrials.gov API v2

### 3. Standard Models

**Location**: `openbb_platform/core/openbb_core/provider/standard_models/`

Data standardization layer:
- `clinical_trial_search.py`: Trial search parameters and results
- `clinical_trial_details.py`: Detailed trial information

Ensures interoperability between different data providers.

## Architecture

```
┌──────────────────────────┐
│ Data Sources             │  ← ClinicalTrials.gov, FDA, EMA
└────────────┬─────────────┘
             │
┌────────────▼─────────────┐
│ Providers                │  ← clinicaltrials, fmp, analytics
└────────────┬─────────────┘
             │
┌────────────▼─────────────┐
│ Standard Models          │  ← Query/Data schemas
└────────────┬─────────────┘
             │
┌────────────▼─────────────┐
│ Extensions/Routers       │  ← biotech extension
└────────────┬─────────────┘
             │
┌────────────▼─────────────┐
│ Python/REST/CLI API      │  ← User interfaces
└──────────────────────────┘
```

### Key Design Principles

1. **Modularity**: Each component is independent and replaceable
2. **Standardization**: Common data models ensure provider interoperability
3. **Extensibility**: Easy to add new providers and analytics
4. **Open Source**: AGPL-3.0 license ensures community ownership

## Installation

### Quick Start

```bash
pip install openbb[biotech]
```

### From Source

```bash
# Clone repository
git clone https://github.com/deathknight2002/OpenBB_GG.git
cd OpenBB_GG

# Install biotech extension
cd openbb_platform/extensions/biotech
pip install -e .

# Install clinicaltrials provider
cd ../../providers/clinicaltrials
pip install -e .
```

## Usage Examples

### Python API

```python
from openbb import obb

# Search trials
trials = obb.biotech.trials.search(
    query="cancer",
    phase="3",
    status="recruiting",
    provider="clinicaltrials"
)
df = trials.to_dataframe()

# Get trial details
details = obb.biotech.trials.details(
    nct_id="NCT04368728",
    provider="clinicaltrials"
)
```

### REST API

```bash
# Start server
openbb-api

# Query endpoint
curl http://localhost:6900/api/v1/biotech/trials/search?query=cancer&phase=3
```

### CLI

```bash
/biotech/trials/search --query cancer --phase 3 --provider clinicaltrials
```

## Examples

- **Notebook**: `examples/biotechResearch.ipynb` - Comprehensive Jupyter notebook
- **Script**: `examples/biotech_trials_example.py` - Standalone Python script

## Documentation

- `README.md` - Main project overview (this file)
- `openbb_platform/extensions/biotech/README.md` - Extension documentation
- `openbb_platform/extensions/biotech/ARCHITECTURE.md` - Technical architecture
- `openbb_platform/extensions/biotech/GETTING_STARTED.md` - Getting started guide
- `openbb_platform/providers/clinicaltrials/README.md` - Provider documentation

## Testing

Basic tests are included to verify structure:

```bash
# Extension tests
pytest openbb_platform/extensions/biotech/tests/

# Provider tests
pytest openbb_platform/providers/clinicaltrials/tests/
```

## Future Enhancements

### Data Sources
- FDA databases (approvals, REMS, adverse events)
- EMA regulatory data
- PubMed publications
- Patent databases (USPTO, EPO)
- Commercial data (BioMedTracker, EvaluatePharma)

### Analytics
- ML-based trial success prediction
- Portfolio risk analysis
- Drug development cost estimation
- Market size analysis
- Competitive intelligence

### Features
- Real-time alerts for trial readouts
- Automated research reports
- Portfolio tracking
- Regulatory calendar
- Conference monitoring

## Contributing

We welcome contributions! All contributions remain open source under AGPL-3.0.

### How to Contribute

1. **Fork the repository**
2. **Create a feature branch**
3. **Make your changes**
4. **Add tests**
5. **Submit a pull request**

See `CONTRIBUTING.md` for detailed guidelines.

## License

**100% Open Source - AGPL-3.0**

This project is entirely open source under the GNU Affero General Public License v3.0:

- ✅ All code is publicly available
- ✅ No proprietary components
- ✅ No closed-source modules
- ✅ Free to use, modify, and distribute
- ✅ Network copyleft ensures modifications stay open

See [LICENSE](LICENSE) for full text.

### Why AGPL-3.0?

- **Community-driven**: Everyone can contribute
- **Transparency**: All code is open for review
- **Network copyleft**: Even SaaS deployments must share source
- **Freedom**: Use without restrictions

## Data Licensing

- **ClinicalTrials.gov**: Public domain data, freely usable
- **Provider implementations**: AGPL-3.0 (open source)
- **Commercial providers**: Require API keys (user-provided)

## Support

- **Documentation**: [OpenBB Docs](https://docs.openbb.co)
- **Discord**: [OpenBB Community](https://openbb.co/discord)
- **GitHub Issues**: [Report bugs or request features](https://github.com/deathknight2002/OpenBB_GG/issues)
- **Email**: support@openbb.co

## Credits

Built on the OpenBB Platform by the OpenBB community.

### Technologies Used

- **Python**: Core programming language
- **FastAPI**: REST API framework
- **Pydantic**: Data validation
- **Poetry**: Dependency management
- **ClinicalTrials.gov API**: Clinical trial data

## Acknowledgments

- OpenBB community for the platform foundation
- ClinicalTrials.gov for open data access
- Contributors and users of this biotech extension

---

**Built with ❤️ by the open-source community**

*100% open source. No proprietary code. No vendor lock-in.*
