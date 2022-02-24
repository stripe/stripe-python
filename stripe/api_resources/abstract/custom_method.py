from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.six.moves.urllib.parse import quote_plus


def custom_method(name, http_verb, http_path=None, is_streaming=False):
    if http_verb not in ["get", "post", "delete"]:
        raise ValueError(
            "Invalid http_verb: %s. Must be one of 'get', 'post' or 'delete'"
            % http_verb
        )
    if http_path is None:
        http_path = name

    def wrapper(cls):
        # Custom method can be defined on the resource class or TestHelpers class
        # In TestHelpers case, the _resource_cls attribute will contain the
        # resource implementation
        def get_resource_class(cls):
            resource_cls = getattr(cls, "_resource_cls", None)
            if resource_cls is None:
                resource_cls = cls
            return resource_cls

        def custom_method_request(cls, sid, **params):
            resource_cls = get_resource_class(cls)
            url = "%s/%s/%s" % (
                resource_cls.class_url(),
                quote_plus(util.utf8(sid)),
                http_path,
            )
            obj = resource_cls._static_request(http_verb, url, **params)

            # For list objects, we have to attach the parameters so that they
            # can be referenced in auto-pagination and ensure consistency.
            if "object" in obj and obj.object == "list":
                obj._retrieve_params = params

            return obj

        def custom_method_request_stream(cls, sid, **params):
            resource_cls = get_resource_class(cls)
            url = "%s/%s/%s" % (
                resource_cls.class_url(),
                quote_plus(util.utf8(sid)),
                http_path,
            )
            return resource_cls._static_request_stream(
                http_verb, url, **params
            )

        if is_streaming:
            class_method_impl = classmethod(custom_method_request_stream)
        else:
            class_method_impl = classmethod(custom_method_request)

        existing_method = getattr(cls, name, None)
        if existing_method is None:
            setattr(cls, name, class_method_impl)
        else:
            # If a method with the same name we want to use already exists on
            # the class, we assume it's an instance method. In this case, the
            # new class method is prefixed with `_cls_`, and the original
            # instance method is decorated with `util.class_method_variant` so
            # that the new class method is called when the original method is
            # called as a class method.
            setattr(cls, "_cls_" + name, class_method_impl)
            instance_method = util.class_method_variant("_cls_" + name)(
                existing_method
            )
            setattr(cls, name, instance_method)

        return cls

    return wrapper
