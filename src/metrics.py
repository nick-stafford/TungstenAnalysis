"""
Risk-Adjusted Performance Metrics
Tungsten Analysis - Quantitative Finance Toolkit
"""

import numpy as np
import pandas as pd
from typing import Tuple


def calculate_returns(prices: pd.Series) -> pd.Series:
    """Calculate daily returns from price series."""
    return prices.pct_change().dropna()


def annualized_return(returns: pd.Series, periods: int = 252) -> float:
    """Calculate annualized return from daily returns."""
    total_return = (1 + returns).prod()
    n_years = len(returns) / periods
    return total_return ** (1 / n_years) - 1


def annualized_volatility(returns: pd.Series, periods: int = 252) -> float:
    """Calculate annualized volatility from daily returns."""
    return returns.std() * np.sqrt(periods)


def sharpe_ratio(returns: pd.Series, risk_free: float = 0.05, periods: int = 252) -> float:
    """
    Calculate Sharpe Ratio.

    Args:
        returns: Daily return series
        risk_free: Annual risk-free rate (default 5%)
        periods: Trading days per year

    Returns:
        Sharpe ratio (annualized)
    """
    ann_return = annualized_return(returns, periods)
    ann_vol = annualized_volatility(returns, periods)

    if ann_vol == 0:
        return 0.0

    return (ann_return - risk_free) / ann_vol


def sortino_ratio(returns: pd.Series, risk_free: float = 0.05, periods: int = 252) -> float:
    """
    Calculate Sortino Ratio (downside risk only).

    Uses downside deviation instead of standard deviation,
    focusing only on negative returns.
    """
    ann_return = annualized_return(returns, periods)

    # Calculate downside deviation
    downside_returns = returns[returns < 0]
    if len(downside_returns) == 0:
        return np.inf

    downside_std = downside_returns.std() * np.sqrt(periods)

    if downside_std == 0:
        return 0.0

    return (ann_return - risk_free) / downside_std


def max_drawdown(prices: pd.Series) -> Tuple[float, pd.Timestamp, pd.Timestamp]:
    """
    Calculate maximum drawdown.

    Returns:
        Tuple of (max_drawdown_pct, peak_date, trough_date)
    """
    rolling_max = prices.expanding().max()
    drawdown = (prices - rolling_max) / rolling_max

    max_dd = drawdown.min()
    trough_date = drawdown.idxmin()
    peak_date = prices[:trough_date].idxmax()

    return max_dd, peak_date, trough_date


def calmar_ratio(returns: pd.Series, prices: pd.Series, periods: int = 252) -> float:
    """
    Calculate Calmar Ratio.

    Annualized return divided by maximum drawdown.
    """
    ann_return = annualized_return(returns, periods)
    max_dd, _, _ = max_drawdown(prices)

    if max_dd == 0:
        return 0.0

    return ann_return / abs(max_dd)


def calculate_all_metrics(prices: pd.Series, risk_free: float = 0.05) -> dict:
    """
    Calculate all risk metrics for a price series.

    Returns:
        Dictionary with all metrics
    """
    returns = calculate_returns(prices)
    max_dd, peak, trough = max_drawdown(prices)

    return {
        'annualized_return': annualized_return(returns),
        'annualized_volatility': annualized_volatility(returns),
        'sharpe_ratio': sharpe_ratio(returns, risk_free),
        'sortino_ratio': sortino_ratio(returns, risk_free),
        'calmar_ratio': calmar_ratio(returns, prices),
        'max_drawdown': max_dd,
        'max_dd_peak': peak,
        'max_dd_trough': trough,
    }
