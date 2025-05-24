"""Provides the Error class and the TraceError exception.

Typical usage of Error:

    def print_file(path: str) -> Error[None]:
        try:
            with open(path, 'rb') as file:
                print(file.read().decode())
            return None
        except OSError as exception:
            return Error("Failed to read file: " + str(exception))

    def read_file(path: str) -> Error[str]:
        try:
            with open(path, 'rb') as file:
                return file.read().decode()
        except OSError as exception:
            return Error("Failed to read file: " + str(exception))
"""

import inspect
from typing import TypeAlias, TypeVar


class TraceError(Exception):
    """Raised when a trace could not be generated."""

    pass


class Error:
    """Represents an error message with traces."""

    def __init__(self, annotation: str | BaseException | None = None) -> None:
        """Initialize a new Error instance.

        Args:
            annotation (str): Annotate the first trace with the given string.
                       (BaseException): Replicate the traceback of an exception.
                       (None): Create the first trace without an annotation.
        """

        self._error: str = ""
        self._trace(inspect.currentframe(), annotation)

    def __str__(self) -> str:
        return self._error

    def _trace(
        self,
        current_frame: inspect.types.FrameType | None,
        annotation: str | BaseException | None,
    ) -> None:
        if current_frame is None:
            raise TraceError("Failed to retrieve the current frame.")

        prev_frame: None | inspect.types.FrameType = current_frame.f_back
        if prev_frame is None:
            raise TraceError("Failed to retrieve the previous frame.")

        file: str = prev_frame.f_code.co_filename
        func: str = prev_frame.f_code.co_name
        line: str = prev_frame.f_lineno

        self._error += f"{file}:{func}():{line}"

        if issubclass(type(annotation), BaseException):
            self._error += f" -> Exception: {type(annotation)}: {annotation}\n"
            traceback = annotation.__traceback__
            while traceback is not None:
                self._error += f" | {traceback.tb_frame}\n"
                traceback = traceback.tb_next
        elif type(annotation) is str:
            self._error += f" -> {annotation}\n"
        else:
            self._error += "\n"

    def trace(self, annotation: str | BaseException | None = None) -> "Error":
        """Adds a trace to this error with an optional annotation.

        Args:
            annotation (str): Add a message annotating this trace.
                       (BaseException): Replicate the traceback of an exception.
                       (None): Do not add a message to this trace.

        Returns:
            Error: A reference to this error.
        """

        self._trace(inspect.currentframe(), annotation)

        return self

    def concat(self, next_error: "Error") -> "Error":
        """Generates a new error from this error and another subsequent error.
        This method is used to combine two separate traces when an
        error (next_error) is encountered while handling a prior error (self).

        Args:
            next_error (Error): The error to concatenate with this error.

        Returns:
            Error: A reference to a new error containing the traces from both
                   this error and the given error.
        """

        new_error = Error()
        new_error._error = (
            self._error
            + "\nEncountered another error while handling the previous error:"
            + next_error._error
        )

        return new_error


T = TypeVar("T")

Result: TypeAlias = Error | T


def is_error(result: Result) -> bool:
    """Return True if the given Result indicates failure and False otherwise."""

    return type(result) is Error
