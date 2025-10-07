# pylint: disable=import-outside-toplevel, W0613:unused-argument
"""Biotech Router."""

from openbb_core.app.model.command_context import CommandContext
from openbb_core.app.model.example import APIEx
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.provider_interface import (
    ExtraParams,
    ProviderChoices,
    StandardParams,
)
from openbb_core.app.query import Query
from openbb_core.app.router import Router

from openbb_biotech.trials.trials_router import router as trials_router
from openbb_biotech.pipeline.pipeline_router import router as pipeline_router

router = Router(prefix="", description="Biotech and pharmaceutical industry data.")
router.include_router(trials_router)
router.include_router(pipeline_router)


@router.command(
    model="BiotechCompanyProfile",
    examples=[
        APIEx(parameters={"symbol": "MRNA", "provider": "fmp"}),
        APIEx(parameters={"symbol": "GILD", "provider": "fmp"}),
    ],
)
async def profile(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get biotech company profile.
    
    Retrieves detailed information about a biotech or pharmaceutical company,
    including their drug pipeline, clinical trials, and regulatory milestones.
    """
    return await OBBject.from_query(Query(**locals()))
