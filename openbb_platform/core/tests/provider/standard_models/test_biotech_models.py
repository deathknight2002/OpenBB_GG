"""Tests for biotech standard models."""

import pytest


def test_clinical_trial_search_models():
    """Test ClinicalTrialSearch standard models."""
    try:
        from openbb_core.provider.standard_models.clinical_trial_search import (
            ClinicalTrialSearchQueryParams,
            ClinicalTrialSearchData,
        )
        
        # Test QueryParams
        query = ClinicalTrialSearchQueryParams(
            query="cancer",
            phase="2",
            status="recruiting",
            limit=50
        )
        assert query.query == "cancer"
        assert query.phase == "2"
        assert query.status == "recruiting"
        assert query.limit == 50
        
        # Test Data
        data = ClinicalTrialSearchData(
            nct_id="NCT12345678",
            title="Test Trial",
            status="Recruiting",
            phase="Phase 2",
        )
        assert data.nct_id == "NCT12345678"
        assert data.title == "Test Trial"
        
    except ImportError as e:
        pytest.skip(f"Standard models not available: {e}")


def test_clinical_trial_details_models():
    """Test ClinicalTrialDetails standard models."""
    try:
        from openbb_core.provider.standard_models.clinical_trial_details import (
            ClinicalTrialDetailsQueryParams,
            ClinicalTrialDetailsData,
        )
        
        # Test QueryParams
        query = ClinicalTrialDetailsQueryParams(nct_id="NCT12345678")
        assert query.nct_id == "NCT12345678"
        
        # Test Data
        data = ClinicalTrialDetailsData(
            nct_id="NCT12345678",
            title="Test Trial Details",
            status="Recruiting",
            phase="Phase 2",
        )
        assert data.nct_id == "NCT12345678"
        assert data.title == "Test Trial Details"
        
    except ImportError as e:
        pytest.skip(f"Standard models not available: {e}")
