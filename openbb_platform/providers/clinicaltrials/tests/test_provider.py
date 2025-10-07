"""Tests for clinicaltrials provider."""

import pytest


def test_provider_import():
    """Test that clinicaltrials provider can be imported."""
    from openbb_clinicaltrials import clinicaltrials_provider
    
    assert clinicaltrials_provider is not None
    assert clinicaltrials_provider.name == "clinicaltrials"


def test_provider_fetchers():
    """Test that provider has expected fetchers."""
    from openbb_clinicaltrials import clinicaltrials_provider
    
    assert "ClinicalTrialSearch" in clinicaltrials_provider.fetcher_dict
    assert "ClinicalTrialDetails" in clinicaltrials_provider.fetcher_dict


def test_search_fetcher_import():
    """Test that search fetcher can be imported."""
    from openbb_clinicaltrials.models.clinical_trial_search import (
        ClinicalTrialsSearchFetcher,
    )
    
    assert ClinicalTrialsSearchFetcher is not None


def test_details_fetcher_import():
    """Test that details fetcher can be imported."""
    from openbb_clinicaltrials.models.clinical_trial_details import (
        ClinicalTrialsDetailsFetcher,
    )
    
    assert ClinicalTrialsDetailsFetcher is not None
