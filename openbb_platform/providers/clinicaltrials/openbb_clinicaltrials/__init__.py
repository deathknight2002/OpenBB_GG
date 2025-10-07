"""ClinicalTrials.gov Provider for OpenBB."""

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
    description="ClinicalTrials.gov is a database of privately and publicly funded"
    " clinical studies conducted around the world.",
    fetcher_dict={
        "ClinicalTrialSearch": ClinicalTrialsSearchFetcher,
        "ClinicalTrialDetails": ClinicalTrialsDetailsFetcher,
    },
    repr_name="ClinicalTrials.gov",
)
