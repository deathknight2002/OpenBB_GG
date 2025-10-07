"""Clinical Trial Details Standard Model."""

from typing import Optional
from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from pydantic import Field


class ClinicalTrialDetailsQueryParams(QueryParams):
    """Clinical Trial Details Query Parameters."""

    nct_id: str = Field(
        description="ClinicalTrials.gov NCT identifier.",
    )


class ClinicalTrialDetailsData(Data):
    """Clinical Trial Details Data."""

    nct_id: str = Field(
        description="ClinicalTrials.gov NCT identifier.",
    )
    title: str = Field(
        description="Official title of the clinical trial.",
    )
    brief_summary: Optional[str] = Field(
        default=None,
        description="Brief summary of the trial.",
    )
    detailed_description: Optional[str] = Field(
        default=None,
        description="Detailed description of the trial.",
    )
    status: Optional[str] = Field(
        default=None,
        description="Current recruitment status.",
    )
    phase: Optional[str] = Field(
        default=None,
        description="Trial phase.",
    )
    study_type: Optional[str] = Field(
        default=None,
        description="Type of study (Interventional, Observational, etc.).",
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
    primary_outcome: Optional[str] = Field(
        default=None,
        description="Primary outcome measures.",
    )
    secondary_outcome: Optional[str] = Field(
        default=None,
        description="Secondary outcome measures.",
    )
    sponsor: Optional[str] = Field(
        default=None,
        description="Primary sponsor name.",
    )
    collaborators: Optional[str] = Field(
        default=None,
        description="Collaborating organizations.",
    )
    start_date: Optional[str] = Field(
        default=None,
        description="Trial start date.",
    )
    completion_date: Optional[str] = Field(
        default=None,
        description="Primary completion date.",
    )
    locations: Optional[str] = Field(
        default=None,
        description="Trial locations.",
    )
