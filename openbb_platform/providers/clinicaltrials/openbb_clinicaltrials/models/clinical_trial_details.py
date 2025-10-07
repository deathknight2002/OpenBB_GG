"""ClinicalTrials.gov Details Fetcher."""

from typing import Any, Dict, List, Optional
import requests
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.clinical_trial_details import (
    ClinicalTrialDetailsData,
    ClinicalTrialDetailsQueryParams,
)


class ClinicalTrialsDetailsQueryParams(ClinicalTrialDetailsQueryParams):
    """ClinicalTrials.gov Details Query Parameters."""


class ClinicalTrialsDetailsData(ClinicalTrialDetailsData):
    """ClinicalTrials.gov Details Data."""


class ClinicalTrialsDetailsFetcher(
    Fetcher[
        ClinicalTrialsDetailsQueryParams,
        List[ClinicalTrialsDetailsData],
    ]
):
    """ClinicalTrials.gov Details Fetcher."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> ClinicalTrialsDetailsQueryParams:
        """Transform query parameters."""
        return ClinicalTrialsDetailsQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: ClinicalTrialsDetailsQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Extract data from ClinicalTrials.gov API."""
        base_url = f"https://clinicaltrials.gov/api/v2/studies/{query.nct_id}"
        
        params = {"format": "json"}
        
        try:
            response = requests.get(base_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            protocol = data.get("protocolSection", {})
            identification = protocol.get("identificationModule", {})
            description = protocol.get("descriptionModule", {})
            status_module = protocol.get("statusModule", {})
            design = protocol.get("designModule", {})
            conditions_module = protocol.get("conditionsModule", {})
            arms_module = protocol.get("armsInterventionsModule", {})
            outcomes = protocol.get("outcomesModule", {})
            sponsor_module = protocol.get("sponsorCollaboratorsModule", {})
            contacts_locations = protocol.get("contactsLocationsModule", {})
            
            result = {
                "nct_id": identification.get("nctId", ""),
                "title": identification.get("officialTitle", identification.get("briefTitle", "")),
                "brief_summary": description.get("briefSummary"),
                "detailed_description": description.get("detailedDescription"),
                "status": status_module.get("overallStatus"),
                "phase": ",".join(design.get("phases", [])) if design.get("phases") else None,
                "study_type": design.get("studyType"),
                "enrollment": status_module.get("enrollmentInfo", {}).get("count"),
                "conditions": ", ".join(conditions_module.get("conditions", [])),
                "interventions": ", ".join([
                    i.get("name", "") for i in arms_module.get("interventions", [])
                ]) if arms_module.get("interventions") else None,
                "primary_outcome": "; ".join([
                    o.get("measure", "") for o in outcomes.get("primaryOutcomes", [])
                ]) if outcomes.get("primaryOutcomes") else None,
                "secondary_outcome": "; ".join([
                    o.get("measure", "") for o in outcomes.get("secondaryOutcomes", [])
                ]) if outcomes.get("secondaryOutcomes") else None,
                "sponsor": sponsor_module.get("leadSponsor", {}).get("name"),
                "collaborators": ", ".join([
                    c.get("name", "") for c in sponsor_module.get("collaborators", [])
                ]) if sponsor_module.get("collaborators") else None,
                "start_date": status_module.get("startDateStruct", {}).get("date"),
                "completion_date": status_module.get("primaryCompletionDateStruct", {}).get("date"),
                "locations": ", ".join([
                    f"{l.get('facility', '')}, {l.get('city', '')}, {l.get('country', '')}"
                    for l in contacts_locations.get("locations", [])[:5]  # Limit to first 5 locations
                ]) if contacts_locations.get("locations") else None,
            }
            
            return [result]
        except Exception as e:
            # Return empty list on error
            return []

    @staticmethod
    def transform_data(
        query: ClinicalTrialsDetailsQueryParams,
        data: List[Dict],
        **kwargs: Any,
    ) -> List[ClinicalTrialsDetailsData]:
        """Transform data to standard format."""
        return [ClinicalTrialsDetailsData(**item) for item in data]
