"""Clinical Trial Search Standard Model."""

from typing import Optional
from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from pydantic import Field


class ClinicalTrialSearchQueryParams(QueryParams):
    """Clinical Trial Search Query Parameters."""

    query: str = Field(
        description="Search query for clinical trials (disease, intervention, etc.)."
    )
    phase: Optional[str] = Field(
        default=None,
        description="Trial phase (1, 2, 3, 4).",
    )
    status: Optional[str] = Field(
        default=None,
        description="Trial status (recruiting, completed, terminated, etc.).",
    )


class ClinicalTrialSearchData(Data):
    """Clinical Trial Search Data."""

    nct_id: str = Field(
        description="ClinicalTrials.gov NCT identifier.",
    )
    title: str = Field(
        description="Official title of the clinical trial.",
    )
    status: Optional[str] = Field(
        default=None,
        description="Current recruitment status.",
    )
    phase: Optional[str] = Field(
        default=None,
        description="Trial phase.",
    )
    enrollment: Optional[int] = Field(
        default=None,
        description="Planned or actual enrollment count.",
    )
    conditions: Optional[str] = Field(
        default=None,
        description="Conditions or diseases studied.",
    )
    interventions: Optional[str] = Field(
        default=None,
        description="Interventions or treatments.",
    )
    sponsor: Optional[str] = Field(
        default=None,
        description="Primary sponsor name.",
    )
    start_date: Optional[str] = Field(
        default=None,
        description="Trial start date.",
    )
