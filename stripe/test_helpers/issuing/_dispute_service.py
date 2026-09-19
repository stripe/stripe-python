# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.issuing._dispute import Dispute
    from stripe.params.test_helpers.issuing._dispute_close_params import (
        DisputeCloseParams,
    )
    from stripe.params.test_helpers.issuing._dispute_provisional_credit_params import (
        DisputeProvisionalCreditParams,
    )
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
    def close(
        self,
        id: str,
        /,
        params: "DisputeCloseParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Dispute":
        """
        Test helper: closes a test-mode Issuing dispute as won or lost.
        """
        return cast(
            "Dispute",
            self._request(
                "post",
                "/v1/test_helpers/issuing/disputes/{id}/close".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def close_async(
        self,
        id: str,
        /,
        params: "DisputeCloseParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Dispute":
        """
        Test helper: closes a test-mode Issuing dispute as won or lost.
        """
        return cast(
            "Dispute",
            await self._request_async(
                "post",
                "/v1/test_helpers/issuing/disputes/{id}/close".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def provisional_credit(
        self,
        id: str,
        /,
        params: Optional["DisputeProvisionalCreditParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Dispute":
        """
        Test helper: overrides the grant_deadline and revocable_after timestamps on a test-mode Issuing dispute's provisional credit, allowing tests to simulate timer-driven status transitions without waiting for real regulatory deadlines to pass.
        """
        return cast(
            "Dispute",
            self._request(
                "post",
                "/v1/test_helpers/issuing/disputes/{id}/provisional_credit".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def provisional_credit_async(
        self,
        id: str,
        /,
        params: Optional["DisputeProvisionalCreditParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Dispute":
        """
        Test helper: overrides the grant_deadline and revocable_after timestamps on a test-mode Issuing dispute's provisional credit, allowing tests to simulate timer-driven status transitions without waiting for real regulatory deadlines to pass.
        """
        return cast(
            "Dispute",
            await self._request_async(
                "post",
                "/v1/test_helpers/issuing/disputes/{id}/provisional_credit".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def simulate_network_lifecycle_dispute_response(
        self,
        id: str,
        /,
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
                "/v1/test_helpers/issuing/disputes/{id}/simulate_network_lifecycle_dispute_response".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def simulate_network_lifecycle_dispute_response_async(
        self,
        id: str,
        /,
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
                "/v1/test_helpers/issuing/disputes/{id}/simulate_network_lifecycle_dispute_response".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def simulate_network_lifecycle_pre_arbitration_response(
        self,
        id: str,
        /,
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
                "/v1/test_helpers/issuing/disputes/{id}/simulate_network_lifecycle_pre_arbitration_response".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def simulate_network_lifecycle_pre_arbitration_response_async(
        self,
        id: str,
        /,
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
                "/v1/test_helpers/issuing/disputes/{id}/simulate_network_lifecycle_pre_arbitration_response".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def simulate_network_lifecycle_pre_arbitration_submission(
        self,
        id: str,
        /,
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
                "/v1/test_helpers/issuing/disputes/{id}/simulate_network_lifecycle_pre_arbitration_submission".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def simulate_network_lifecycle_pre_arbitration_submission_async(
        self,
        id: str,
        /,
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
                "/v1/test_helpers/issuing/disputes/{id}/simulate_network_lifecycle_pre_arbitration_submission".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
