"""Provides the Result and Optional classes.

Typical usage of Result:

    def print_file(path: str) -> Result:
        try:
            with open(path, 'rb') as file:
                print(file.read().decode())
            return Result.ok()
        except OSError as exception:
            return Result.error(exception.strerror)

Typical usage of Optional:

    def read_file(path: str) -> Optional[str]:
        try:
            with open(path, 'rb') as file:
                return Optional.value(file.read().decode())
        except OSError as exception:
            return Optional.error("Failed to read file: " + exception.strerror)
"""

import inspect
from typing import Generic, TypeVar


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

    def trace(self, annotation: str | None = None) -> None:
        """Adds a trace to this error with an optional annotation.

        Args:
            annotation (str): Add a message annotating this trace.
                       (None): Do not add a message to this trace.
        """

        self._trace(inspect.currentframe(), annotation)


class BadOptionalAccess(Exception):
    """Raised when attempting to access a value from an Optional instance that
    does not contain a value or an error from an Optional instance that does
    not contain an error.
    """

    pass


class Result:
    """Represents a result that indicates either success or failure."""

    def __init__(self, error: None | Error) -> None:
        self._error: None | Error = error

    @classmethod
    def success(cls):
        """Returns a Result instance indicating success."""

        return cls(None)

    @classmethod
    def failure(cls, error: str):
        """Returns a Result instance indicating failure."""

        return cls(Error(error))

    def __str__(self) -> str:
        """Returns a string representation of the Error or None stored within this Result instance."""

        return str(self.get())

    def __bool__(self) -> bool:
        """Returns True if this Result instance indicates success and False if
        this result indicates failure."""

        return not isinstance(self._error, Error)

    def has_success(self) -> bool:
        """Returns True if this Result instance indicates success and False if
        this result indicates failure."""

        return not isinstance(self._error, Error)

    def has_failure(self) -> bool:
        """Returns True if this Result instance indicates failure and False if
        this result indicates success."""

        return isinstance(self._error, Error)

    def get(self) -> Error | None:
        """Returns the value or error stored within this Result instance.

        Returns:
            Error: If this Result instance indicates failure.
            None: If this Result instance indicates success.
        """

        return self._error

    def get_error(self) -> Error:
        """Returns the error stored within this Result instance.

        Raises:
            BadOptionalAccess: If this Result instance does not contain an
                error.
        """

        if not isinstance(self._error, Error):
            raise BadOptionalAccess(
                "This Result instance does not contain an error.  Error: "
                + str(self._error)
            )
        return self._error

    def trace(self, annotation: str | None = None) -> None:
        """Adds a trace to this error with an optional annotation.

        Args:
            annotation (str): Add a message annotating this trace.
                       (None): Do not add a message to this trace.
        """

        if self._error is None:
            raise BadOptionalAccess(
                "Failed to add a trace to a Result instance without an Error instance."
            )

        self._error._trace(inspect.currentframe(), annotation)


T = TypeVar("T")


class Optional(Generic[T]):
    """Represents a result that contains either a value or an error."""

    def __init__(self, result: T | Error) -> None:
        self._result: T | Error = result

    @classmethod
    def value(cls, value: T):
        """Returns an Optional instance indicating success."""

        return cls(value)

    @classmethod
    def error(cls, error: str):
        """Returns an Optional instance indicating failure."""

        return cls(Error(error))

    def __str__(self) -> str:
        return str(self.get())

    def __bool__(self) -> bool:
        """Returns True if this Optional instance contains a value and False if
        this instance contains an error."""

        return not isinstance(self._result, Error)

    def has_value(self) -> bool:
        """Returns True if this Optional instance contains a value and False if
        this instance contains an error."""

        return not isinstance(self._result, Error)

    def has_error(self) -> bool:
        """Returns True if this Optional instance contains an error and False
        if this instance contains a value."""

        return isinstance(self._result, Error)

    def get(self) -> T | Error:
        """Returns the value or error stored within this Optional instance.

        Returns:
            T: If this Optional instance contains a value.
            Error: If this Optional instance contains an error.
        """

        return self._result

    def get_value(self) -> T:
        """Returns the value stored within this Optional instance.

        Raises:
            BadOptionalAccess: If this Optional instance does not contain a
                value.
        """

        if isinstance(self._result, Error):
            raise BadOptionalAccess(
                "This Optional instance does not contain a value.  Error: "
                + str(self._result)
            )
        return self._result

    def get_error(self) -> Error:
        """Returns the error stored within this Optional instance.

        Raises:
            BadOptionalAccess: If this Optional instance does not contain an
                error.
        """

        if not isinstance(self._result, Error):
            raise BadOptionalAccess(
                "This Optional instance does not contain an error.  Value: "
                + str(self._result)
            )
        return self._result

    def trace(self, annotation: str | None = None) -> None:
        """Adds a trace to this error with an optional annotation.

        Args:
            annotation (str): Add a message annotating this trace.
                       (None): Do not add a message to this trace.
        """

        if not isinstance(self._result, Error):
            raise BadOptionalAccess(
                "Failed to add a trace to a Result instance without an Error instance."
            )

        self._result._trace(inspect.currentframe(), annotation)
