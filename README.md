# MetaTrader 5 Trading Automation

This project provides a set of tools for automated trading using MetaTrader 5 (MT5). It includes functionality for data fetching, position management, lot size calculation, and Fair Value Gap (FVG) detection.

## Features

- **Data Fetching**: Retrieve historical and real-time market data from MT5
- **Position Management**: Automate position management including break-even functionality
- **Lot Size Calculation**: Calculate appropriate lot sizes based on risk management parameters
- **FVG Detection**: Identify Fair Value Gaps in price action for trading opportunities

## Components

### 1. fetch_data.py
- Handles MT5 initialization and connection
- Retrieves historical price data for various timeframes
- Manages timezone conversions and DST adjustments
- Supports multiple timeframes (M1, M5, M15, M30, H1, H4, D1, etc.)

### 2. Lot_Size.py
- Calculates appropriate lot sizes based on:
  - Account balance
  - Risk percentage
  - Stop loss distance
  - Symbol-specific contract sizes
- Supports multiple brokers (IC Markets, Pepperstone, etc.)
- Handles different currency pairs and their specific requirements

### 3. fvg.py
- Identifies Fair Value Gaps in price action
- Supports multiple FVG patterns
- Returns FVG direction and price levels

### 4. breakeven.py
- Manages open positions
- Implements break-even functionality
- Adjusts stop-loss levels based on profit targets

### 5. parameters.py
- Contains configuration parameters
- Defines trading pairs and their mappings
- Stores broker-specific settings

## Requirements

- Python 3.x
- MetaTrader 5
- Required Python packages:
  - MetaTrader5
  - pandas
  - pandas_ta

## Usage

1. **Data Fetching**:
```python
from fetch_data import getData

# Initialize MT5 connection and fetch data
df = getData('H4', 'EURUSD.sd', 'path_to_mt5', login, password, server)
```

2. **Lot Size Calculation**:
```python
from Lot_Size import calculate_lot_size

# Calculate lot size for a trade
lot_size = calculate_lot_size('EURUSD.sd', 'Buy', 100000, 0.0010, 1.0800, 1.0)
```

3. **FVG Detection**:
```python
from fvg import identifyFVG

# Identify FVG in price data
fvg_flag, fvg_candle, high, low, direction, date = identifyFVG(df)
```

4. **Position Management**:
```python
from breakeven import OpenedPosition

# Manage open positions
OpenedPosition(symbols_dict, mt5_path, login, password, server)
```

## Configuration

Before using the system:
1. Configure your MT5 credentials in the relevant functions
2. Set up your broker mappings in `parameters.py`
3. Adjust risk parameters according to your trading strategy

## Notes

- The system supports multiple brokers with different symbol mappings
- Timezone handling is implemented for accurate data synchronization
- Risk management is built into the lot size calculations
- The FVG detection supports multiple market conditions

## Disclaimer

This software is for educational purposes only. Trading involves risk of loss. Use at your own risk.
