# core/timer.py
import asyncio
from abc import ABC, abstractmethod
from typing import Awaitable


class Timer(ABC):
    """Abstract interface for timing operations."""

    @abstractmethod
    def sleep(self, seconds: int) -> None:
        """Sleep for the given number of seconds (synchronous)."""
        pass

    @abstractmethod
    def monotonic(self) -> float:
        """Return monotonic time (synchronous)."""
        pass

    @abstractmethod
    def async_sleep(self, seconds: int) -> Awaitable[None]:
        """Sleep for the given number of seconds (asynchronous)."""
        pass

    @abstractmethod
    def async_time(self) -> float:
        """Return event loop time (asynchronous)."""
        pass


class DefaultTimer(Timer):
    """Default implementation using time and asyncio modules."""

    def sleep(self, seconds: int) -> None:
        import time

        time.sleep(seconds)

    def monotonic(self) -> float:
        import time

        return time.monotonic()

    async def async_sleep(self, seconds: int) -> None:
        await asyncio.sleep(seconds)

    def async_time(self) -> float:
        return asyncio.get_running_loop().time()
