# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.issuing._dispute import Dispute
    from stripe.params.test_helpers.issuing._dispute_simulate_network_lifecycle_dispute_response_params import (
        DisputeSimulateNetworkLifecycleDisputeResponseParams,
    )
    from stripe.params.test_helpers.issuing._dispute_simulate_network_lifecycle_pre_arbitration_response_params import (
        DisputeSimulateNetworkLifecyclePreArbitrationResponseParams,
    )
    from stripe.params.test_helpers.issuing._dispute_simulate_network_lifecycle_pre_arbitration_submission_params import (
        DisputeSimulateNetworkLifecyclePreArbitrationSubmissionParams,
    )


class DisputeService(StripeService):
    def simulate_network_lifecycle_dispute_response(
        self,
        dispute: str,
        params: "DisputeSimulateNetworkLifecycleDisputeResponseParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Dispute":
        """
        Test helper: populates network_lifecycle.dispute_response on a test-mode Visa Issuing Dispute using placeholder file tokens. Only supported for Visa disputes.
        """
        return cast(
            "Dispute",
            self._request(
                "post",
                "/v1/test_helpers/issuing/disputes/{dispute}/simulate_network_lifecycle_dispute_response".format(
                    dispute=sanitize_id(dispute),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def simulate_network_lifecycle_dispute_response_async(
        self,
        dispute: str,
        params: "DisputeSimulateNetworkLifecycleDisputeResponseParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Dispute":
        """
        Test helper: populates network_lifecycle.dispute_response on a test-mode Visa Issuing Dispute using placeholder file tokens. Only supported for Visa disputes.
        """
        return cast(
            "Dispute",
            await self._request_async(
                "post",
                "/v1/test_helpers/issuing/disputes/{dispute}/simulate_network_lifecycle_dispute_response".format(
                    dispute=sanitize_id(dispute),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def simulate_network_lifecycle_pre_arbitration_response(
        self,
        dispute: str,
        params: "DisputeSimulateNetworkLifecyclePreArbitrationResponseParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Dispute":
        """
        Test helper: populates network_lifecycle.pre_arbitration_response on a test-mode Visa Issuing Dispute using placeholder file tokens. Only supported for Visa disputes in the collaboration flow.
        """
        return cast(
            "Dispute",
            self._request(
                "post",
                "/v1/test_helpers/issuing/disputes/{dispute}/simulate_network_lifecycle_pre_arbitration_response".format(
                    dispute=sanitize_id(dispute),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def simulate_network_lifecycle_pre_arbitration_response_async(
        self,
        dispute: str,
        params: "DisputeSimulateNetworkLifecyclePreArbitrationResponseParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Dispute":
        """
        Test helper: populates network_lifecycle.pre_arbitration_response on a test-mode Visa Issuing Dispute using placeholder file tokens. Only supported for Visa disputes in the collaboration flow.
        """
        return cast(
            "Dispute",
            await self._request_async(
                "post",
                "/v1/test_helpers/issuing/disputes/{dispute}/simulate_network_lifecycle_pre_arbitration_response".format(
                    dispute=sanitize_id(dispute),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def simulate_network_lifecycle_pre_arbitration_submission(
        self,
        dispute: str,
        params: "DisputeSimulateNetworkLifecyclePreArbitrationSubmissionParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Dispute":
        """
        Test helper: populates network_lifecycle.pre_arbitration_submission on a test-mode Visa Issuing Dispute using placeholder file tokens. Only supported for Visa disputes.
        """
        return cast(
            "Dispute",
            self._request(
                "post",
                "/v1/test_helpers/issuing/disputes/{dispute}/simulate_network_lifecycle_pre_arbitration_submission".format(
                    dispute=sanitize_id(dispute),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def simulate_network_lifecycle_pre_arbitration_submission_async(
        self,
        dispute: str,
        params: "DisputeSimulateNetworkLifecyclePreArbitrationSubmissionParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Dispute":
        """
        Test helper: populates network_lifecycle.pre_arbitration_submission on a test-mode Visa Issuing Dispute using placeholder file tokens. Only supported for Visa disputes.
        """
        return cast(
            "Dispute",
            await self._request_async(
                "post",
                "/v1/test_helpers/issuing/disputes/{dispute}/simulate_network_lifecycle_pre_arbitration_submission".format(
                    dispute=sanitize_id(dispute),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
