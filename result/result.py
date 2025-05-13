"""Provides the Error class and the TraceError exception.

Typical usage of Error:

    def print_file(path: str) -> Error[None]:
        try:
            with open(path, 'rb') as file:
                print(file.read().decode())
            return None
        except OSError as exception:
            return Error("Failed to read file: " + exception.strerror)

    def read_file(path: str) -> Error[str]:
        try:
            with open(path, 'rb') as file:
                return file.read().decode()
        except OSError as exception:
            return Error("Failed to read file: " + exception.strerror)
"""

import inspect
from typing import TypeAlias, TypeVar


class TraceError(Exception):
    """Raised when a trace could not be generated."""

    pass


class Error:
    """Represents an error message with traces.

    This type is used to distinguish between errors and result values.
    """

    def __init__(self, annotation: str) -> None:
        self._error: str = ""
        self._trace(inspect.currentframe(), annotation)

    def __str__(self) -> str:
        return self._error

    def _trace(
        self,
        current_frame: inspect.types.FrameType | None,
        annotation: str | None = None,
    ) -> None:
        if current_frame is None:
            raise TraceError("Failed to retrieve the current frame.")

        prev_frame: None | inspect.types.FrameType = current_frame.f_back
        if prev_frame is None:
            raise TraceError("Failed to retrieve the previous frame.")

        file: str = prev_frame.f_code.co_filename
        func: str = prev_frame.f_code.co_name
        line: str = prev_frame.f_lineno

        self._error += f"\n{file}:{func}():{line}"

        if annotation is not None:
            self._error += f" -> {annotation}"

    def trace(self, annotation: str | None = None):
        """Adds a trace to this error with an optional annotation.

        Args:
            annotation (str): Add a message annotating this trace.
                       (None): Do not add a message to this trace.
        """

        self._trace(inspect.currentframe(), annotation)

        return self


T = TypeVar("T")
Result: TypeAlias = Error | T
