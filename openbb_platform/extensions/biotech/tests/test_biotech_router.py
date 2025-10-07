"""Tests for biotech extension."""

import pytest


def test_biotech_router_import():
    """Test that biotech router can be imported."""
    from openbb_biotech.biotech_router import router
    
    assert router is not None
    assert router.prefix == ""
    assert "biotech" in router.description.lower() or "pharmaceutical" in router.description.lower()


def test_trials_router_import():
    """Test that trials router can be imported."""
    from openbb_biotech.trials.trials_router import router
    
    assert router is not None
    assert router.prefix == "/trials"


def test_pipeline_router_import():
    """Test that pipeline router can be imported."""
    from openbb_biotech.pipeline.pipeline_router import router
    
    assert router is not None
    assert router.prefix == "/pipeline"


def test_biotech_router_commands():
    """Test that biotech router has expected commands."""
    from openbb_biotech.biotech_router import router
    
    # Check that router includes sub-routers
    assert len(router.routers) >= 2  # trials and pipeline routers
