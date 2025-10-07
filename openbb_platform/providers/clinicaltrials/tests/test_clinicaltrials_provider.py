"""Tests for ClinicalTrials.gov provider."""

import pytest


def test_clinicaltrials_provider_import():
    """Test that ClinicalTrials provider can be imported."""
    try:
        from openbb_clinicaltrials import clinicaltrials_provider
        assert clinicaltrials_provider is not None
        assert clinicaltrials_provider.name == "clinicaltrials"
    except ImportError:
        pytest.skip("openbb-clinicaltrials not installed")


def test_clinical_trial_search_fetcher():
    """Test ClinicalTrialSearchFetcher."""
    try:
        from openbb_clinicaltrials.models.clinical_trial_search import (
            ClinicalTrialsSearchFetcher,
            ClinicalTrialsClinicalTrialSearchQueryParams,
        )
        
        # Test query transformation
        params = {"query": "cancer", "limit": 10}
        query = ClinicalTrialsSearchFetcher.transform_query(params)
        assert isinstance(query, ClinicalTrialsClinicalTrialSearchQueryParams)
        assert query.query == "cancer"
        assert query.limit == 10
        
        # Test data extraction
        data = ClinicalTrialsSearchFetcher.extract_data(query, None)
        assert isinstance(data, list)
        assert len(data) > 0
        
        # Test data transformation
        transformed = ClinicalTrialsSearchFetcher.transform_data(query, data)
        assert isinstance(transformed, list)
        assert len(transformed) > 0
        assert hasattr(transformed[0], "nct_id")
        
    except ImportError:
        pytest.skip("openbb-clinicaltrials not installed")


def test_clinical_trial_details_fetcher():
    """Test ClinicalTrialDetailsFetcher."""
    try:
        from openbb_clinicaltrials.models.clinical_trial_details import (
            ClinicalTrialsDetailsFetcher,
            ClinicalTrialsClinicalTrialDetailsQueryParams,
        )
        
        # Test query transformation
        params = {"nct_id": "NCT04368728"}
        query = ClinicalTrialsDetailsFetcher.transform_query(params)
        assert isinstance(query, ClinicalTrialsClinicalTrialDetailsQueryParams)
        assert query.nct_id == "NCT04368728"
        
        # Test data extraction
        data = ClinicalTrialsDetailsFetcher.extract_data(query, None)
        assert isinstance(data, list)
        assert len(data) > 0
        
        # Test data transformation
        transformed = ClinicalTrialsDetailsFetcher.transform_data(query, data)
        assert isinstance(transformed, list)
        assert len(transformed) > 0
        assert hasattr(transformed[0], "nct_id")
        
    except ImportError:
        pytest.skip("openbb-clinicaltrials not installed")
