from stripe import _util


class _RequestMetrics(object):
    def __init__(self, request_id, request_duration_ms):
        self.request_id = request_id
        self.request_duration_ms = request_duration_ms

    def payload(self):
        return {
            "request_id": self.request_id,
            "request_duration_ms": self.request_duration_ms,
        }


@_util.deprecated(
    "This class is for internal stripe-python use only. The public interface will be removed in a future version."
)
class RequestMetrics(_RequestMetrics):
    pass
