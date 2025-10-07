"""ClinicalTrials.gov Provider Module."""

from openbb_core.provider.abstract.provider import Provider
from openbb_clinicaltrials.models.clinical_trial_search import (
    ClinicalTrialsSearchFetcher,
)
from openbb_clinicaltrials.models.clinical_trial_details import (
    ClinicalTrialsDetailsFetcher,
)

clinicaltrials_provider = Provider(
    name="clinicaltrials",
    website="https://clinicaltrials.gov",
    description="""ClinicalTrials.gov is a database of clinical studies conducted 
    around the world, maintained by the U.S. National Library of Medicine.""",
    credentials=None,  # Public API, no credentials required
    fetcher_dict={
        "ClinicalTrialSearch": ClinicalTrialsSearchFetcher,
        "ClinicalTrialDetails": ClinicalTrialsDetailsFetcher,
    },
    repr_name="ClinicalTrials.gov",
)
