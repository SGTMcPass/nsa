import pytest
import time
import random
from unittest.mock import patch, MagicMock
from pathlib import Path

from embedding_lib.retry_utils import (
    retry_with_backoff,
    CircuitBreaker,
    CircuitBreakerError
)

# Test retry_with_backoff

def test_retry_success():
    """Test that a successful function returns immediately."""
    mock_func = MagicMock(return_value="success")
    decorated = retry_with_backoff()(mock_func)
    
    result = decorated()
    
    assert result == "success"
    mock_func.assert_called_once()


def test_retry_eventual_success():
    """Test that a function succeeds after some retries."""
    mock_func = MagicMock()
    mock_func.__name__ = "mock_func"
    mock_func.side_effect = [Exception("Fail"), Exception("Fail"), "success"]
    
    decorated = retry_with_backoff(max_retries=3, initial_delay=0.01)(mock_func)
    
    result = decorated()
    assert result == "success"
    assert mock_func.call_count == 3


def test_retry_exhausted():
    """Test that all retries are exhausted before giving up."""
    mock_func = MagicMock()
    mock_func.__name__ = "mock_func"
    mock_func.side_effect = Exception("Fail")
    
    decorated = retry_with_backoff(max_retries=2, initial_delay=0.01)(mock_func)
    
    with pytest.raises(Exception, match="Fail"):
        decorated()
    
    assert mock_func.call_count == 3  # Initial + 2 retries


def test_retry_specific_exceptions():
    """Test that only specified exceptions trigger a retry."""
    class MyError(Exception):
        pass
    
    mock_func = MagicMock()
    mock_func.__name__ = "mock_func"
    mock_func.side_effect = [MyError(), "success"]
    
    # Should retry on MyError
    decorated = retry_with_backoff(
        exceptions=(MyError,),
        max_retries=1,
        initial_delay=0.01
    )(mock_func)
    
    result = decorated()
    assert result == "success"
    assert mock_func.call_count == 2
    
    # Should not retry on other exceptions
    mock_func.reset_mock()
    mock_func.side_effect = [ValueError("Other error")]
    
    with pytest.raises(ValueError):
        decorated()
    
    assert mock_func.call_count == 1


# Test CircuitBreaker

def test_circuit_breaker_closed_state():
    """Test circuit in closed state allows calls to pass through."""
    cb = CircuitBreaker(failure_threshold=2, recovery_timeout=0.1)
    mock_func = MagicMock(return_value="success")
    
    result = cb.call(mock_func)
    
    assert result == "success"
    assert cb.state == "CLOSED"
    assert cb.failure_count == 0


def test_circuit_breaker_opens_after_threshold():
    """Test circuit opens after failure threshold is reached."""
    cb = CircuitBreaker(failure_threshold=2, recovery_timeout=0.1)
    mock_func = MagicMock(side_effect=Exception("Service down"))
    
    # First failure
    with pytest.raises(Exception):
        cb.call(mock_func)
    assert cb.state == "CLOSED"
    assert cb.failure_count == 1
    
    # Second failure - should open the circuit
    with pytest.raises(Exception):
        cb.call(mock_func)
    assert cb.state == "OPEN"
    assert cb.failure_count == 2
    
    # Third attempt should fail fast with CircuitBreakerError
    with pytest.raises(CircuitBreakerError):
        cb.call(mock_func)
    assert mock_func.call_count == 2  # Only called twice, fails fast on third


def test_circuit_breaker_reset_after_timeout():
    """Test circuit moves to half-open after recovery timeout."""
    with patch('time.time') as mock_time:
        mock_time.return_value = 0
        cb = CircuitBreaker(failure_threshold=1, recovery_timeout=10)
        
        # Make it fail once to open the circuit
        with pytest.raises(Exception):
            cb.call(lambda: 1/0)
        assert cb.state == "OPEN"
        
        # Fast forward past recovery timeout
        mock_time.return_value = 11
        
        # Next call should be allowed (half-open state)
        def failing_func():
            raise Exception("Still failing")
            
        with pytest.raises(Exception):
            cb.call(failing_func)
        
        # Should be open again after the failed attempt
        assert cb.state == "OPEN"
        
        # Fast forward again
        mock_time.return_value = 22
        
        # This time it should work and reset the circuit
        def working_func():
            return "success"
            
        result = cb.call(working_func)
        assert result == "success"
        assert cb.state == "CLOSED"
        assert cb.failure_count == 0


def test_circuit_breaker_decorator():
    """Test using CircuitBreaker as a decorator."""
    cb = CircuitBreaker(failure_threshold=1, recovery_timeout=0.1)
    
    @cb
    def failing_func():
        raise Exception("Fail")
    
    with pytest.raises(Exception):
        failing_func()
    
    with pytest.raises(CircuitBreakerError):
        failing_func()
    
    assert cb.state == "OPEN"
    assert cb.failure_count == 1


def test_circuit_breaker_reset():
    """Test manually resetting the circuit breaker."""
    cb = CircuitBreaker(failure_threshold=1, recovery_timeout=10)
    
    # Make it fail once to open the circuit
    with pytest.raises(Exception):
        cb.call(lambda: 1/0)
    assert cb.state == "OPEN"
    
    # Reset it
    cb.reset()
    assert cb.state == "CLOSED"
    assert cb.failure_count == 0
    
    # Should work again
    result = cb.call(lambda: "success")
    assert result == "success"
    assert cb.state == "CLOSED"
