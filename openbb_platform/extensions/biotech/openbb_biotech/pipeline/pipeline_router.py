# pylint: disable=import-outside-toplevel, W0613:unused-argument
"""Drug Pipeline Router."""

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

router = Router(prefix="/pipeline", description="Drug development pipeline data.")


@router.command(
    model="CompanyPipeline",
    examples=[
        APIEx(parameters={"symbol": "MRNA", "provider": "fmp"}),
        APIEx(parameters={"symbol": "GILD,MRNA", "provider": "fmp"}),
    ],
)
async def company(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get company drug development pipeline.
    
    Retrieves information about drugs in development including indication,
    development phase, trial status, and expected timelines.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="PipelineCompetitiveLandscape",
    examples=[
        APIEx(parameters={"indication": "oncology", "provider": "analytics"}),
        APIEx(
            description="Compare multiple companies",
            parameters={"indication": "diabetes", "symbols": "MRNA,GILD,PFE", "provider": "analytics"}
        ),
    ],
)
async def competitive_landscape(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Analyze competitive landscape for a disease indication.
    
    Compares drug pipelines across multiple companies for a specific indication,
    showing development phases, mechanism of action, and competitive positioning.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="DrugMilestones",
    examples=[
        APIEx(parameters={"symbol": "MRNA", "provider": "fmp"}),
        APIEx(
            description="Get upcoming milestones in next 6 months",
            parameters={"symbol": "GILD", "months_ahead": 6, "provider": "fmp"}
        ),
    ],
)
async def milestones(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get upcoming regulatory and development milestones.
    
    Retrieves expected milestones including trial readouts, FDA decisions,
    and regulatory filings for drugs in development.
    """
    return await OBBject.from_query(Query(**locals()))
