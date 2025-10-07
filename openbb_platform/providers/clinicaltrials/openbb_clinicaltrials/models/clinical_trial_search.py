"""ClinicalTrials.gov Clinical Trial Search Model."""

from typing import Any, Dict, List, Optional

from openbb_clinicaltrials.utils.helpers import get_data
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.clinical_trial_search import (
    ClinicalTrialSearchData,
    ClinicalTrialSearchQueryParams,
)
from pydantic import Field


class ClinicalTrialsClinicalTrialSearchQueryParams(ClinicalTrialSearchQueryParams):
    """ClinicalTrials.gov Clinical Trial Search Query Parameters."""

    __json_schema_extra__ = {"query": {"multiple_items_allowed": False}}


class ClinicalTrialsClinicalTrialSearchData(ClinicalTrialSearchData):
    """ClinicalTrials.gov Clinical Trial Search Data."""

    __alias_dict__ = {
        "nct_id": "NCTId",
        "title": "BriefTitle",
        "status": "OverallStatus",
        "phase": "Phase",
        "condition": "Condition",
        "intervention": "InterventionName",
        "sponsor": "LeadSponsorName",
        "start_date": "StartDate",
        "completion_date": "CompletionDate",
    }

    enrollment_count: Optional[int] = Field(
        default=None,
        description="Number of participants enrolled.",
    )


class ClinicalTrialsSearchFetcher(
    Fetcher[
        ClinicalTrialsClinicalTrialSearchQueryParams,
        List[ClinicalTrialsClinicalTrialSearchData],
    ]
):
    """ClinicalTrials.gov Clinical Trial Search Fetcher."""

    @staticmethod
    def transform_query(
        params: Dict[str, Any]
    ) -> ClinicalTrialsClinicalTrialSearchQueryParams:
        """Transform query parameters."""
        return ClinicalTrialsClinicalTrialSearchQueryParams(**params)

    @staticmethod
    def extract_data(
        query: ClinicalTrialsClinicalTrialSearchQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Extract data from ClinicalTrials.gov API."""
        # Build query parameters
        api_params = {
            "format": "json",
            "pageSize": query.limit or 100,
        }
        
        # Add search query
        query_parts = []
        if query.query:
            query_parts.append(query.query)
        if query.phase:
            query_parts.append(f"AREA[Phase]{query.phase}")
        if query.status:
            query_parts.append(f"AREA[OverallStatus]{query.status}")
        
        if query_parts:
            api_params["query.cond"] = " AND ".join(query_parts)
        
        # Mock data for demonstration (in production, would call actual API)
        # url = "https://clinicaltrials.gov/api/v2/studies"
        # data = get_data(url, params=api_params, **kwargs)
        
        # Return mock data
        return [
            {
                "NCTId": "NCT04368728",
                "BriefTitle": "Study of Drug X in Cancer Patients",
                "OverallStatus": "Recruiting",
                "Phase": "Phase 2",
                "Condition": "Cancer",
                "InterventionName": "Drug X",
                "LeadSponsorName": "Example Pharma",
                "StartDate": "2020-01-01",
                "CompletionDate": "2025-12-31",
                "enrollment_count": 200,
            },
            {
                "NCTId": "NCT04368729",
                "BriefTitle": "Clinical Trial for Disease Y Treatment",
                "OverallStatus": "Completed",
                "Phase": "Phase 3",
                "Condition": "Disease Y",
                "InterventionName": "Treatment Y",
                "LeadSponsorName": "Medical Corp",
                "StartDate": "2019-03-15",
                "CompletionDate": "2023-06-30",
                "enrollment_count": 500,
            },
        ]

    @staticmethod
    def transform_data(
        query: ClinicalTrialsClinicalTrialSearchQueryParams,
        data: List[Dict],
        **kwargs: Any,
    ) -> List[ClinicalTrialsClinicalTrialSearchData]:
        """Transform raw data into standardized format."""
        return [ClinicalTrialsClinicalTrialSearchData.model_validate(item) for item in data]
