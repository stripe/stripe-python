from typing import List, Optional


class StripeContext:
    """
    StripeContext represents a context path for Stripe API requests.

    The context is used to access child accounts by adding segments,
    or parent accounts by removing segments. This class provides an
    immutable interface for manipulating context paths.
    """

    def __init__(self, segments: Optional[List[str]] = None) -> None:
        """
        Initialize a StripeContext with the given segments.

        Args:
            segments: List of context path segments. Defaults to empty list.
        """
        self._segments = segments[:] if segments else []

    @classmethod
    def parse(cls, context_string: str) -> "StripeContext":
        """
        Parse a context string into a StripeContext instance.

        Args:
            context_string: A string like "a/b/c" to be split on "/"

        Returns:
            A new StripeContext instance with the parsed segments
        """
        if not context_string:
            return cls([])
        return cls(context_string.split("/"))

    def parent(self) -> "StripeContext":
        """
        Create a new StripeContext with the last segment removed.

        Returns:
            A new StripeContext instance with one fewer segment

        Raises:
            ValueError: If context has no segments to remove
        """
        if not self._segments:
            raise ValueError("Cannot get parent of empty context")
        return StripeContext(self._segments[:-1])

    def child(self, segment: str) -> "StripeContext":
        """
        Create a new StripeContext with an additional segment appended.

        Args:
            segment: The segment to append to the context path

        Returns:
            A new StripeContext instance with the new segment added
        """
        return StripeContext(self._segments + [segment])

    def __str__(self) -> str:
        """
        Convert the StripeContext to its string representation.

        Returns:
            A string with segments joined by "/"
        """
        return "/".join(self._segments)

    def __repr__(self) -> str:
        """
        Return a string representation of the StripeContext for debugging.
        """
        return f"StripeContext({self._segments!r})"
