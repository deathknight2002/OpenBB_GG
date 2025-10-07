# pylint: disable=import-outside-toplevel, W0613:unused-argument
"""Clinical Trials Router."""

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

router = Router(prefix="/trials", description="Clinical trials data.")


@router.command(
    model="ClinicalTrialSearch",
    examples=[
        APIEx(parameters={"query": "cancer", "provider": "clinicaltrials"}),
        APIEx(
            description="Search for Phase 3 trials",
            parameters={"query": "diabetes", "phase": "3", "provider": "clinicaltrials"}
        ),
        APIEx(
            description="Search for active recruiting trials",
            parameters={"query": "alzheimer", "status": "recruiting", "provider": "clinicaltrials"}
        ),
    ],
)
async def search(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Search for clinical trials.
    
    Search and retrieve clinical trial data based on various criteria such as
    disease, intervention, phase, and recruitment status.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="ClinicalTrialDetails",
    examples=[
        APIEx(parameters={"nct_id": "NCT04368728", "provider": "clinicaltrials"}),
    ],
)
async def details(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get detailed information about a specific clinical trial.
    
    Retrieve comprehensive details including study design, endpoints,
    enrollment, and timeline for a clinical trial identified by NCT ID.
    """
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="TrialSuccessRates",
    examples=[
        APIEx(parameters={"indication": "oncology", "provider": "analytics"}),
        APIEx(
            description="Get success rates by phase",
            parameters={"indication": "cardiovascular", "phase": "2", "provider": "analytics"}
        ),
    ],
)
async def success_rates(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get clinical trial success rates by indication and phase.
    
    Provides statistical analysis of trial success rates based on historical data,
    segmented by disease indication, trial phase, and other factors.
    """
    return await OBBject.from_query(Query(**locals()))
