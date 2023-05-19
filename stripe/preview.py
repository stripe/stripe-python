from stripe import raw_request


class Preview(object):
    def _get_default_opts(self, params):
        if "api_mode" not in params:
            params["api_mode"] = "preview"
        return params

    def post(self, url, **params):
        return raw_request("post", url, **self._get_default_opts(params))

    def get(self, url, **params):
        return raw_request("get", url, **self._get_default_opts(params))

    def delete(self, url, **params):
        return raw_request("delete", url, **self._get_default_opts(params))


preview = Preview()
