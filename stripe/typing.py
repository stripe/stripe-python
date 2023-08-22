# Centralized place for typing imports.

# The last version supported by Python 3.6 is typing_extensions 4.1.1. Unfortunately,
# typing_extensions didn't decide to re-export all of the types from typing until 4.7.0.
# TODO (major): if we drop support for Python 3.6, we can remove this file and just import
# everything from typing_extensions.

# Rules: don't depend on anything only in typing_extensions > 4.1.1. If we need something
# newer, we might be able to provide a better type for some users with a conditional import
# but we'll cross that bridge when we come to it.

# Note: we can't re-export *everything* here, unfortunately. Some special
# forms can't be aliased.

# > The following special forms cannot be re-exported: Final, ClassVar, and InitVar in pyright.
# (https://github.com/microsoft/pyright/discussions/4845#discussioncomment-5440032)

# Also aliasing @typing.overload will confuse pyflakes so needs to
# be imported directly to avoid spurious "redefinition" F811 linter errors.
# https://github.com/PyCQA/flake8/issues/1575#issuecomment-1075451224

from typing import Optional as Optional  # noqa: F401
from typing import cast as cast  # noqa: F401
from typing import Dict as Dict  # noqa: F401
from typing import Any as Any  # noqa: F401
from typing import TypeVar as TypeVar  # noqa: F401
from typing import Union as Union  # noqa: F401
from typing_extensions import TYPE_CHECKING as TYPE_CHECKING  # noqa: F401
from typing_extensions import Literal as Literal  # noqa: F401
from typing_extensions import NoReturn as NoReturn  # noqa: F401
from typing_extensions import Protocol as Protocol  # noqa: F401
from typing_extensions import Type as Type  # noqa: F401
from typing_extensions import TypedDict as TypedDict  # noqa: F401
