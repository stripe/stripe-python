# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import NotRequired, TypedDict


class DisputeSimulateNetworkLifecyclePreArbitrationResponseParams(
    RequestOptions,
):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    merchant_evidence_files: "DisputeSimulateNetworkLifecyclePreArbitrationResponseParamsMerchantEvidenceFiles"
    """
    Controls the acquiring merchant's simulated submitted evidence files for the pre-arbitration response stage.
    """


class DisputeSimulateNetworkLifecyclePreArbitrationResponseParamsMerchantEvidenceFiles(
    TypedDict,
):
    number_to_generate: int
    """
    How many simulated merchant evidence file tokens to attach (between 1 and 12).
    """
