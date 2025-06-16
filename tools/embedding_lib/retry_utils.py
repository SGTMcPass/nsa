"""
retry_utils.py — Retry and circuit breaking utilities for NASA Simulation Agents.
Implements the Stark Protocol: Modular, resilient, CLI-ready.

Key features:
- Exponential backoff with jitter for retries
- Circuit breaker pattern for external service calls
- Configurable retry policies
"""

import time
import random
import logging
from functools import wraps
from typing import Callable, Type, Tuple, Optional, TypeVar, Any

# Type variable for generic function typing
T = TypeVar('T')

# Default logger
logger = logging.getLogger(__name__)


def retry_with_backoff(
    exceptions: Tuple[Type[Exception], ...] = (Exception,),
    max_retries: int = 3,
    initial_delay: float = 0.1,
    max_delay: float = 10.0,
    backoff_factor: float = 2.0,
    jitter: bool = True,
    logger: Optional[logging.Logger] = None
) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """
    Decorator that retries the wrapped function with exponential backoff.

    Args:
        exceptions: Tuple of exceptions to catch and retry on
        max_retries: Maximum number of retry attempts
        initial_delay: Initial delay between retries in seconds
        max_delay: Maximum delay between retries in seconds
        backoff_factor: Factor to multiply delay by after each retry
        jitter: If True, adds random jitter to delay times
        logger: Optional logger instance for logging retries

    Returns:
        Decorated function with retry logic
    """
    if logger is None:
        logger = logging.getLogger(__name__)

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            delay = initial_delay
            last_exception = None

            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt == max_retries:
                        logger.error(
                            f"Max retries ({max_retries}) exceeded for {func.__name__}"
                        )
                        raise

                    # Calculate delay with jitter if enabled
                    current_delay = delay * (backoff_factor ** attempt)
                    if jitter:
                        current_delay = random.uniform(0, current_delay)
                    current_delay = min(current_delay, max_delay)

                    logger.warning(
                        f"Attempt {attempt + 1}/{max_retries} failed for {func.__name__} "
                        f"with error: {str(e)}. Retrying in {current_delay:.2f}s..."
                    )

                    time.sleep(current_delay)

            # This line should theoretically never be reached due to the raise in the except block
            raise last_exception  # type: ignore

        return wrapper
    return decorator


class CircuitBreakerError(Exception):
    """Exception raised when the circuit is open/breaker is tripped."""
    pass


class CircuitBreaker:
    """
    Circuit breaker pattern implementation for external service calls.
    
    The circuit breaker has three states:
    - CLOSED: Normal operation, requests pass through
    - OPEN: Circuit is open, all requests fail fast
    - HALF-OPEN: Limited requests allowed to test if service has recovered
    """
    
    def __init__(
        self,
        failure_threshold: int = 5,
        recovery_timeout: float = 60.0,
        name: str = "unnamed",
        logger: Optional[logging.Logger] = None
    ):
        """
        Initialize the circuit breaker.
        
        Args:
            failure_threshold: Number of failures before opening the circuit
            recovery_timeout: Time in seconds before moving to HALF-OPEN state
            name: Name of the circuit breaker for logging
            logger: Optional logger instance
        """
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.name = name
        self.logger = logger or logging.getLogger(__name__)
        
        self._failure_count = 0
        self._last_failure_time = 0.0
        self._state = "CLOSED"
    
    def __call__(self, func: Callable[..., T]) -> Callable[..., T]:
        """Use the circuit breaker as a decorator."""
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            return self.call(func, *args, **kwargs)
        return wrapper
    
    def call(self, func: Callable[..., T], *args: Any, **kwargs: Any) -> T:
        """
        Execute the function with circuit breaker logic.
        
        Returns:
            The result of the function call if successful
            
        Raises:
            CircuitBreakerError: If the circuit is open
            Exception: The original exception if the call fails and the circuit is not open
        """
        if self._state == "OPEN":
            # Check if we should try to recover
            if time.time() - self._last_failure_time > self.recovery_timeout:
                self._state = "HALF_OPEN"
                self.logger.info(f"Circuit {self.name} moved to HALF_OPEN state")
            else:
                raise CircuitBreakerError(
                    f"Circuit {self.name} is OPEN (failures: {self._failure_count})"
                )
        
        try:
            result = func(*args, **kwargs)
            
            # On success, reset the circuit if it was HALF_OPEN
            if self._state == "HALF_OPEN":
                self.reset()
                
            return result
            
        except Exception as e:
            self._record_failure()
            raise  # Re-raise the original exception
    
    def _record_failure(self) -> None:
        """Record a failure and update the circuit state."""
        self._failure_count += 1
        self._last_failure_time = time.time()
        
        if self._state == "HALF_OPEN" or \
           (self._state == "CLOSED" and self._failure_count >= self.failure_threshold):
            self._state = "OPEN"
            self.logger.error(
                f"Circuit {self.name} is now OPEN "
                f"(failures: {self._failure_count}, "
                f"last failure: {self._last_failure_time})"
            )
    
    def reset(self) -> None:
        """Reset the circuit to CLOSED state."""
        self._state = "CLOSED"
        self._failure_count = 0
        self.logger.info(f"Circuit {self.name} has been reset to CLOSED state")
    
    @property
    def state(self) -> str:
        """Get the current state of the circuit breaker."""
        return self._state
    
    @property
    def failure_count(self) -> int:
        """Get the current failure count."""
        return self._failure_count
    
    @property
    def last_failure_time(self) -> float:
        """Get the timestamp of the last failure."""
        return self._last_failure_time
