"""ClinicalTrials.gov Search Fetcher."""

from typing import Any, Dict, List, Optional
import requests
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.clinical_trial_search import (
    ClinicalTrialSearchData,
    ClinicalTrialSearchQueryParams,
)
from pydantic import Field


class ClinicalTrialsSearchQueryParams(ClinicalTrialSearchQueryParams):
    """ClinicalTrials.gov Search Query Parameters."""

    max_results: Optional[int] = Field(
        default=20,
        description="Maximum number of results to return.",
    )


class ClinicalTrialsSearchData(ClinicalTrialSearchData):
    """ClinicalTrials.gov Search Data."""


class ClinicalTrialsSearchFetcher(
    Fetcher[
        ClinicalTrialsSearchQueryParams,
        List[ClinicalTrialsSearchData],
    ]
):
    """ClinicalTrials.gov Search Fetcher."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> ClinicalTrialsSearchQueryParams:
        """Transform query parameters."""
        return ClinicalTrialsSearchQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: ClinicalTrialsSearchQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Extract data from ClinicalTrials.gov API."""
        # Build the API request
        base_url = "https://clinicaltrials.gov/api/v2/studies"
        
        # Build query string
        query_parts = [query.query]
        if query.phase:
            query_parts.append(f"PHASE:{query.phase}")
        if query.status:
            query_parts.append(f"STATUS:{query.status}")
        
        params = {
            "query.term": " AND ".join(query_parts),
            "pageSize": query.max_results,
            "format": "json",
        }
        
        try:
            response = requests.get(base_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            studies = data.get("studies", [])
            results = []
            
            for study in studies:
                protocol = study.get("protocolSection", {})
                identification = protocol.get("identificationModule", {})
                status_module = protocol.get("statusModule", {})
                design = protocol.get("designModule", {})
                conditions_module = protocol.get("conditionsModule", {})
                arms_module = protocol.get("armsInterventionsModule", {})
                sponsor_module = protocol.get("sponsorCollaboratorsModule", {})
                
                result = {
                    "nct_id": identification.get("nctId", ""),
                    "title": identification.get("briefTitle", ""),
                    "status": status_module.get("overallStatus", ""),
                    "phase": ",".join(design.get("phases", [])) if design.get("phases") else None,
                    "enrollment": status_module.get("enrollmentInfo", {}).get("count"),
                    "conditions": ", ".join(conditions_module.get("conditions", [])),
                    "interventions": ", ".join([
                        i.get("name", "") for i in arms_module.get("interventions", [])
                    ]) if arms_module.get("interventions") else None,
                    "sponsor": sponsor_module.get("leadSponsor", {}).get("name"),
                    "start_date": status_module.get("startDateStruct", {}).get("date"),
                }
                results.append(result)
            
            return results
        except Exception as e:
            # Return empty list on error for now
            return []

    @staticmethod
    def transform_data(
        query: ClinicalTrialsSearchQueryParams,
        data: List[Dict],
        **kwargs: Any,
    ) -> List[ClinicalTrialsSearchData]:
        """Transform data to standard format."""
        return [ClinicalTrialsSearchData(**item) for item in data]
