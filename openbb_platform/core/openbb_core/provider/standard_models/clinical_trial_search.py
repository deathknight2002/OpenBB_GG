"""Clinical Trial Search Standard Model."""

from datetime import date as dateType
from typing import Optional

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, NonNegativeInt


class ClinicalTrialSearchQueryParams(QueryParams):
    """Clinical Trial Search Query Parameters."""

    query: Optional[str] = Field(
        default=None,
        description="Search query for condition, intervention, or other trial characteristics.",
    )
    phase: Optional[str] = Field(
        default=None,
        description="Clinical trial phase (1, 2, 3, 4).",
    )
    status: Optional[str] = Field(
        default=None,
        description="Recruitment status (recruiting, completed, terminated, etc.).",
    )
    limit: Optional[NonNegativeInt] = Field(
        default=100,
        description=QUERY_DESCRIPTIONS.get("limit", ""),
    )


class ClinicalTrialSearchData(Data):
    """Clinical Trial Search Data."""

    nct_id: str = Field(
        description="NCT identifier for the clinical trial."
    )
    title: str = Field(
        description="Official title of the clinical trial."
    )
    status: Optional[str] = Field(
        default=None,
        description="Current recruitment status of the trial."
    )
    phase: Optional[str] = Field(
        default=None,
        description="Clinical trial phase."
    )
    condition: Optional[str] = Field(
        default=None,
        description="Medical condition being studied."
    )
    intervention: Optional[str] = Field(
        default=None,
        description="Intervention or treatment being tested."
    )
    sponsor: Optional[str] = Field(
        default=None,
        description="Primary sponsor of the trial."
    )
    start_date: Optional[dateType] = Field(
        default=None,
        description="Trial start date."
    )
    completion_date: Optional[dateType] = Field(
        default=None,
        description="Trial completion date."
    )
