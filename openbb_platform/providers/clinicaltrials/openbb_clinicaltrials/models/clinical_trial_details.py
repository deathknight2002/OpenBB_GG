"""ClinicalTrials.gov Clinical Trial Details Model."""

from typing import Any, Dict, List, Optional

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.clinical_trial_details import (
    ClinicalTrialDetailsData,
    ClinicalTrialDetailsQueryParams,
)
from pydantic import Field


class ClinicalTrialsClinicalTrialDetailsQueryParams(ClinicalTrialDetailsQueryParams):
    """ClinicalTrials.gov Clinical Trial Details Query Parameters."""

    __json_schema_extra__ = {"nct_id": {"multiple_items_allowed": False}}


class ClinicalTrialsClinicalTrialDetailsData(ClinicalTrialDetailsData):
    """ClinicalTrials.gov Clinical Trial Details Data."""

    __alias_dict__ = {
        "nct_id": "NCTId",
        "title": "OfficialTitle",
        "brief_summary": "BriefSummary",
        "status": "OverallStatus",
        "phase": "Phase",
        "study_type": "StudyType",
        "sponsor": "LeadSponsorName",
        "enrollment": "EnrollmentCount",
        "start_date": "StartDate",
        "completion_date": "CompletionDate",
        "location": "LocationFacility",
    }

    url: Optional[str] = Field(
        default=None,
        description="URL to the trial on ClinicalTrials.gov",
    )


class ClinicalTrialsDetailsFetcher(
    Fetcher[
        ClinicalTrialsClinicalTrialDetailsQueryParams,
        List[ClinicalTrialsClinicalTrialDetailsData],
    ]
):
    """ClinicalTrials.gov Clinical Trial Details Fetcher."""

    @staticmethod
    def transform_query(
        params: Dict[str, Any]
    ) -> ClinicalTrialsClinicalTrialDetailsQueryParams:
        """Transform query parameters."""
        return ClinicalTrialsClinicalTrialDetailsQueryParams(**params)

    @staticmethod
    def extract_data(
        query: ClinicalTrialsClinicalTrialDetailsQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Extract data from ClinicalTrials.gov API."""
        # Mock data for demonstration (in production, would call actual API)
        # url = f"https://clinicaltrials.gov/api/v2/studies/{query.nct_id}"
        # data = get_data(url, **kwargs)
        
        # Return mock data
        return [
            {
                "NCTId": query.nct_id,
                "OfficialTitle": "A Phase 2 Study of Drug X in Patients with Advanced Cancer",
                "BriefSummary": "This study evaluates the safety and efficacy of Drug X...",
                "OverallStatus": "Recruiting",
                "Phase": "Phase 2",
                "StudyType": "Interventional",
                "conditions": ["Cancer", "Advanced Solid Tumors"],
                "interventions": ["Drug X", "Placebo"],
                "primary_outcome": "Overall Response Rate",
                "LeadSponsorName": "Example Pharma",
                "EnrollmentCount": 200,
                "StartDate": "2020-01-01",
                "CompletionDate": "2025-12-31",
                "LocationFacility": "Multiple Sites",
                "url": f"https://clinicaltrials.gov/study/{query.nct_id}",
            }
        ]

    @staticmethod
    def transform_data(
        query: ClinicalTrialsClinicalTrialDetailsQueryParams,
        data: List[Dict],
        **kwargs: Any,
    ) -> List[ClinicalTrialsClinicalTrialDetailsData]:
        """Transform raw data into standardized format."""
        return [ClinicalTrialsClinicalTrialDetailsData.model_validate(item) for item in data]
