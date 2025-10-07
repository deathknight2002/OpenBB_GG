"""Clinical Trial Details Standard Model."""

from datetime import date as dateType
from typing import List, Optional

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from pydantic import Field


class ClinicalTrialDetailsQueryParams(QueryParams):
    """Clinical Trial Details Query Parameters."""

    nct_id: str = Field(
        description="NCT identifier for the clinical trial.",
    )


class ClinicalTrialDetailsData(Data):
    """Clinical Trial Details Data."""

    nct_id: str = Field(
        description="NCT identifier for the clinical trial."
    )
    title: str = Field(
        description="Official title of the clinical trial."
    )
    brief_summary: Optional[str] = Field(
        default=None,
        description="Brief summary of the trial."
    )
    status: Optional[str] = Field(
        default=None,
        description="Current recruitment status of the trial."
    )
    phase: Optional[str] = Field(
        default=None,
        description="Clinical trial phase."
    )
    study_type: Optional[str] = Field(
        default=None,
        description="Type of study (interventional, observational, etc.)."
    )
    conditions: Optional[List[str]] = Field(
        default=None,
        description="Medical conditions being studied."
    )
    interventions: Optional[List[str]] = Field(
        default=None,
        description="Interventions or treatments being tested."
    )
    primary_outcome: Optional[str] = Field(
        default=None,
        description="Primary outcome measure."
    )
    sponsor: Optional[str] = Field(
        default=None,
        description="Primary sponsor of the trial."
    )
    enrollment: Optional[int] = Field(
        default=None,
        description="Target or actual enrollment number."
    )
    start_date: Optional[dateType] = Field(
        default=None,
        description="Trial start date."
    )
    completion_date: Optional[dateType] = Field(
        default=None,
        description="Trial completion date."
    )
    location: Optional[str] = Field(
        default=None,
        description="Trial location(s)."
    )
