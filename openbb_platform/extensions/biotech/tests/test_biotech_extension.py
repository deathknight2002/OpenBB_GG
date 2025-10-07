"""Tests for biotech extension."""

import pytest


def test_biotech_extension_import():
    """Test that biotech extension can be imported."""
    try:
        import openbb_biotech
        assert openbb_biotech is not None
    except ImportError:
        pytest.skip("openbb-biotech not installed")


def test_biotech_router_import():
    """Test that biotech router can be imported."""
    try:
        from openbb_biotech.biotech_router import router
        assert router is not None
        assert router.prefix == ""
    except ImportError:
        pytest.skip("openbb-biotech not installed")


def test_trials_router_import():
    """Test that trials router can be imported."""
    try:
        from openbb_biotech.trials.trials_router import router
        assert router is not None
        assert router.prefix == "/trials"
    except ImportError:
        pytest.skip("openbb-biotech not installed")


def test_pipeline_router_import():
    """Test that pipeline router can be imported."""
    try:
        from openbb_biotech.pipeline.pipeline_router import router
        assert router is not None
        assert router.prefix == "/pipeline"
    except ImportError:
        pytest.skip("openbb-biotech not installed")
