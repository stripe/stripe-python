# Hint: if you're developing this plugin, test changes with:
#   venv/bin/tox -e lint -r
# so that tox re-installs the plugin from the local directory
import ast
from typing import Iterator, Tuple


class TypingImportsChecker:
    name = __name__
    version = "0.1.0"

    allowed_typing_extensions_imports = [
        "Literal",
        "NoReturn",
        "Protocol",
        "TYPE_CHECKING",
        "Type",
        "TypedDict",
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
