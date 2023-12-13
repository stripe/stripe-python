# Hint: if you're developing this plugin, test changes with:
#   venv/bin/tox -e lint -r
# so that tox re-installs the plugin from the local directory
import ast
from typing import Iterator, Tuple


class TypingImportsChecker:
    name = __name__
    version = "0.1.0"

    # Rules:
    # * typing_extensions v4.1.1 is the latest that supports Python 3.6
    # so don't depend on anything from a more recent version than that.
    #
    # If we need something newer, maybe we can provide it for users on
    # newer versions with a conditional import, but we'll cross that
    # bridge when we come to it.

    # If a symbol exists in both `typing` and `typing_extensions`, which
    # should you use? Prefer `typing_extensions` if the symbol available there.
    # in 4.1.1. In typing_extensions 4.7.0, `typing_extensions` started re-exporting
    # EVERYTHING from `typing` but this is not the case in v4.1.1.
    allowed_typing_extensions_imports = [
        "Literal",
        "NoReturn",
        "Protocol",
        "TYPE_CHECKING",
        "Type",
        "TypedDict",
        "NotRequired",
        "Self",
        "Unpack",
        "Awaitable",
        "Never",
    ]

    allowed_typing_imports = [
        "Any",
        "ClassVar",
        "Optional",
        "TypeVar",
        "Union",
        "cast",
        "overload",
        "Dict",
        "Tuple",
        "List",
        "Generic",
        "Mapping",
        "Tuple",
        "Iterator",
        "Mapping",
        "Set",
        "Callable",
        "Generator",
    ]

    def __init__(self, tree: ast.AST):
        self.tree = tree

        intersection = set(self.allowed_typing_imports) & set(
            self.allowed_typing_extensions_imports
        )
        if len(intersection) > 0:
            raise AssertionError(
                "TypingImportsChecker: allowed_typing_imports and allowed_typing_extensions_imports must not overlap. Both entries contained: %s"
                % (intersection)
            )

    def run(self) -> Iterator[Tuple[int, int, str, type]]:
        for node in ast.walk(self.tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == "typing":
                    for name in node.names:
                        if name.name not in self.allowed_typing_imports:
                            msg = None
                            if (
                                name.name
                                in self.allowed_typing_extensions_imports
                            ):
                                msg = (
                                    "SPY100 Don't import %s from 'typing', instead import from 'typing_extensions'"
                                    % (name.name)
                                )
                            else:
                                msg = (
                                    "SPY101 Importing %s from 'typing' is prohibited. Do you need to add to the allowlist in flake8_stripe.py?"
                                    % (name.name)
                                )
                            yield (
                                name.lineno,
                                name.col_offset,
                                msg,
                                type(self),
                            )
                elif node.module == "typing_extensions":
                    for name in node.names:
                        if (
                            name.name
                            not in self.allowed_typing_extensions_imports
                        ):
                            msg = None
                            if name.name in self.allowed_typing_imports:
                                msg = (
                                    "SPY102 Don't import '%s' from 'typing_extensions', instead import from 'typing'"
                                    % (name.name)
                                )
                            else:
                                msg = (
                                    "SPY103 Importing '%s' from 'typing_extensions' is prohibited. Do you need to add to the allowlist in flake8_stripe.py?"
                                    % (name.name)
                                )
                            yield (
                                name.lineno,
                                name.col_offset,
                                msg,
                                type(self),
                            )


class StripeImportsChecker:
    name = __name__
    version = "0.1.0"

    def __init__(self, tree: ast.AST, filename: str):
        self.tree = tree
        self.filename = filename

    def run(self) -> Iterator[Tuple[int, int, str, type]]:
        if not self.filename.split("/")[-1].startswith("_"):
            backcompat = False
            for node in ast.walk(self.tree):
                # check node is a constant string that contains package is deprecated
                if (
                    isinstance(node, ast.Constant)
                    and isinstance(node.value, str)
                    and "is deprecated" in node.value
                ):
                    backcompat = True

            if not backcompat:
                yield (
                    0,
                    0,
                    "IMP102 Do not create non-private modules",
                    type(self),
                )

        for node in ast.walk(self.tree):
            if isinstance(node, ast.Import):
                # Forbid: import stripe
                if any(alias.name == "stripe" for alias in node.names):
                    msg = "IMP101 Do not `import stripe` unless you are accessing the global variable or breaking circular dependency"
                    yield (
                        node.lineno,
                        node.col_offset,
                        msg,
                        type(self),
                    )
            if isinstance(node, ast.ImportFrom):
                # Forbid: from stripe...module import Type
                parts = node.module.split(".")
                if (
                    len(parts) > 1
                    and parts[0] == "stripe"
                    and not parts[-1].startswith("_")
                ):
                    msg = "IMP100 Import from private implementation modules that start with _."
                    yield (
                        node.lineno,
                        node.col_offset,
                        msg,
                        type(self),
                    )
