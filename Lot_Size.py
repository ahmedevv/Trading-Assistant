import MetaTrader5 as mt5


EQUITI_TO_IC_SYMBOL_MAP = {
        'EURUSD.sd' : 'EURUSD',
        'EURCHF.sd' : 'EURCHF',
        'GBPUSD.sd' : 'GBPUSD',
        'USDCAD.sd' : 'USDCAD',
        'USDJPY.sd' : 'USDJPY',
        'AUDUSD.sd' : 'AUDUSD',
        'USDCHF.sd' : 'USDCHF',
        'NZDUSD.sd' : 'NZDUSD',
        'GBPCHF.sd' : 'GBPCHF',
        'AUDJPY.sd' : 'AUDJPY',
        'GBPJPY.sd': 'GBPJPY',
        'EURJPY.sd' : 'EURJPY',
        'GBPCAD.sd' : 'GBPCAD',
        'EURCAD.sd' : 'EURCAD',
        'AUDCAD.sd' : 'AUDCAD', 
        'NZDCAD.sd' : 'NZDCAD',
        'US500Roll' : 'US500',
        'UT100Roll' : 'USTEC', 
        'US30Roll' : 'US30', 
        'XAUUSD.sd' : 'XAUUSD',
        'USOILRoll' : 'XTIUSD'
}
EQUITI_TO_PS_SYMBOL_MAP = {
        'EURUSD.sd' : 'EURUSD.a',
        'EURCHF.sd' : 'EURCHF.a',
        'GBPUSD.sd' : 'GBPUSD.a',
        'USDCAD.sd' : 'USDCAD.a',
        'USDJPY.sd' : 'USDJPY.a',
        'AUDUSD.sd' : 'AUDUSD.a',
        'USDCHF.sd' : 'USDCHF.a',
        'NZDUSD.sd' : 'NZDUSD.a',
        'GBPCHF.sd' : 'GBPCHF.a',
        'AUDJPY.sd' : 'AUDJPY.a',
        'GBPJPY.sd': 'GBPJPY.a',
        'EURJPY.sd' : 'EURJPY.a',
        'GBPCAD.sd' : 'GBPCAD.a',
        'EURCAD.sd' : 'EURCAD.a',
        'AUDCAD.sd' : 'AUDCAD.a', 
        'NZDCAD.sd' : 'NZDCAD.a',
        'US500Roll' : 'US500.a',
        'UT100Roll' : 'NAS100.a', 
        'US30Roll' : 'US30.a', 
        'XAUUSD.sd' : 'XAUUSD.a',
        'USOILRoll' : 'SpotCrude.a'
}
EQUITI_TO_NC_SYMBOL_MAP = {
        'EURUSD.sd' : 'EURUSDx',
        'EURCHF.sd' : 'EURCHFx',
        'GBPUSD.sd' : 'GBPUSDx',
        'USDCAD.sd' : 'USDCADx',
        'USDJPY.sd' : 'USDJPYx',
        'AUDUSD.sd' : 'AUDUSDx',
        'USDCHF.sd' : 'USDCHFx',
        'NZDUSD.sd' : 'NZDUSDx',
        'GBPCHF.sd' : 'GBPCHFx',
        'AUDJPY.sd' : 'AUDJPYx',
        'GBPJPY.sd': 'GBPJPYx',
        'EURJPY.sd' : 'EURJPYx',
        'GBPCAD.sd' : 'GBPCADx',
        'EURCAD.sd' : 'EURCADx',
        'AUDCAD.sd' : 'AUDCADx', 
        'NZDCAD.sd' : 'NZDCADx',
        'US500Roll' : 'US500Rollx',
        'UT100Roll' : 'UT100Rollx', 
        'US30Roll' : 'US30Rollx', 
        'XAUUSD.sd' : 'XAUUSDx',
        'USOILRoll' : 'USOUSD!'
}

CONTRACT_SIZES = {
    'default': 100000,
    'gold': 100,
    'silver': 5000,
    'index': 1,
    'oil': 1000
}

IC_CONTRACT_SIZES = {
    'default': 100000,
    'gold': 100,
    'silver': 5000,
    'index': 1,
    'oil': 100
}




OIL_PAIR = ['USOILRoll']
GOLD_PAIR = ['XAUUSD.sd']
SILVER_PAIR = ['XAGUSD.sd']
CHF_PAIRS = ['USDCHF.sd', 'CADCHF.sd', 'GBPCHF.sd']
JPY_PAIRS = ['USDJPY.sd', 'GBPJPY.sd', 'NZDJPY.sd', 'AUDJPY.sd', 'EURJPY.sd']
INDEX_PAIRS = ['UT100Roll', 'US30Roll', 'DE40Roll', 'UK100Roll', 'US500Roll']
CAD_PAIRS = ['AUDCAD.sd','GBPCAD.sd', 'EURCAD.sd', 'USDCAD.sd', 'NZDCAD.sd']
NZD_PAIRS = ['GBPNZD.sd','AUDNZD.sd','USDNZD.sd','EURNZD.sd']
AUD_PAIRS = ['GBPAUD.sd','EURAUD.sd','NZDAUD.sd']

def calculate_quote_usd_indirect(common_usd, common_quote):
    """
    Calculate Quote/USD using a common currency (e.g., EUR or GBP).
    
    Args:
        common_usd (float): Exchange rate of Common/USD (e.g., EUR/USD).
        common_quote (float): Exchange rate of Common/Quote (e.g., EUR/CHF).
    
    Returns:
        float: Derived Quote/USD rate (e.g., CHF/USD).
    """
    if common_quote == 0:
        raise ValueError("Common/Quote exchange rate cannot be zero.")
    
    return common_usd / common_quote

def get_broker_symbol(equiti_symbol, broker):
    """Retrieve the Equiti symbol from the given IC symbol."""
    if broker == 'IC':
        return EQUITI_TO_IC_SYMBOL_MAP.get(equiti_symbol)
    elif broker == 'PS':
        return EQUITI_TO_PS_SYMBOL_MAP.get(equiti_symbol)
    elif broker == 'NC' : 
        return EQUITI_TO_NC_SYMBOL_MAP.get(equiti_symbol)



def get_quote_price(equiti_symbol,  broker=None):
    eur_usd_symbol = 'EURUSD.sd'
    eur_chf_symbol = 'EURCHF.sd'
    eur_cad_symbol = 'EURCAD.sd'
    eur_jpy_symbol = 'EURJPY.sd'
    aud_usd_symbol = 'AUDUSD.sd'
    nzd_usd_symbol = 'NZDUSD.sd'

    if broker:
        eur_usd_symbol = get_broker_symbol(eur_usd_symbol, broker)
        eur_chf_symbol = get_broker_symbol(eur_chf_symbol, broker)
        eur_cad_symbol = get_broker_symbol(eur_cad_symbol, broker)
        eur_jpy_symbol = get_broker_symbol(eur_jpy_symbol, broker)
        aud_usd_symbol = get_broker_symbol(aud_usd_symbol, broker)
        nzd_usd_symbol = get_broker_symbol(nzd_usd_symbol, broker)

    if equiti_symbol in CHF_PAIRS:
        print(eur_chf_symbol)
        return calculate_quote_usd_indirect(mt5.symbol_info_tick(eur_usd_symbol).bid,mt5.symbol_info_tick(eur_chf_symbol).bid)
    elif equiti_symbol in CAD_PAIRS:
        return calculate_quote_usd_indirect(mt5.symbol_info_tick(eur_usd_symbol).bid,mt5.symbol_info_tick(eur_cad_symbol).bid)
    elif equiti_symbol in JPY_PAIRS:
        value =  calculate_quote_usd_indirect(mt5.symbol_info_tick(eur_usd_symbol).bid,mt5.symbol_info_tick(eur_jpy_symbol).bid)
        value = value * 100
        return value
    elif equiti_symbol in AUD_PAIRS:
        return mt5.symbol_info_tick(aud_usd_symbol).bid
    elif equiti_symbol in NZD_PAIRS:
        return mt5.symbol_info_tick(nzd_usd_symbol).bid
    else:
        return 1.00

def calculate_quote_usd_indirect(common_usd, common_quote):
    """
    Calculate Quote/USD using a common currency (e.g., EUR or GBP).
    
    Args:
        common_usd (float): Exchange rate of Common/USD (e.g., EUR/USD).
        common_quote (float): Exchange rate of Common/Quote (e.g., EUR/CHF).
    
    Returns:
        float: Derived Quote/USD rate (e.g., CHF/USD).
    """
    if common_quote == 0:
        raise ValueError("Common/Quote exchange rate cannot be zero.")
    
    return common_usd / common_quote


def calculate_risked_amount(balance, risk_pct, symbol, broker=None):
    """Calculate the risked amount based on the balance, risk percentage, and symbol."""
    risked = (balance * risk_pct) / 100
    quote_symbol_price = get_quote_price(symbol, broker)
    if symbol in CHF_PAIRS:
        return risked / quote_symbol_price 
    elif symbol in CAD_PAIRS:
        return risked / quote_symbol_price
    elif symbol in JPY_PAIRS:
        return risked / quote_symbol_price
    elif symbol in AUD_PAIRS:
        return risked / quote_symbol_price
    elif symbol in NZD_PAIRS:
        return risked / quote_symbol_price

    return risked

def get_contract_size(symbol, broker=None):
    """Return the appropriate contract size for the given symbol."""
    if symbol in GOLD_PAIR:
        return CONTRACT_SIZES['gold']
    elif symbol in INDEX_PAIRS:
        return CONTRACT_SIZES['index']
    elif symbol in SILVER_PAIR:
        return CONTRACT_SIZES['silver']
    elif symbol in OIL_PAIR:
        if broker and broker == 'IC':
            return IC_CONTRACT_SIZES['oil']
        elif broker and broker == 'PS':
            return IC_CONTRACT_SIZES['oil']
        elif broker and broker == 'NC':
            return CONTRACT_SIZES['oil']
        return CONTRACT_SIZES['oil']
    return CONTRACT_SIZES['default']


def get_pip_value(symbol):
    if symbol in JPY_PAIRS:
        return get_quote_price('EURJPY.sd')
    elif symbol in CAD_PAIRS:
        return get_quote_price('USDCAD.sd')
    elif symbol in CHF_PAIRS:
        return get_quote_price('USDCHF.sd')
    elif symbol in AUD_PAIRS:
        return get_quote_price('GBPAUD.sd')
    elif symbol in NZD_PAIRS: 
        return get_quote_price('AUDNZD.sd')
    return 1.00


def calculate_lot_size(symbol, entry_type, balance, stoploss, open_price, risk_pct, broker=None):
    """Calculate lot size based on the specified risk percentage and account balance."""
    try:
        risked = calculate_risked_amount(balance, risk_pct, symbol, broker)
        contract_size = get_contract_size(symbol, broker)
        
        if entry_type == "Buy":
            SL = open_price - stoploss
        elif entry_type == "Sell":
            SL = stoploss - open_price
        else:
            raise ValueError("Invalid entry type. Must be 'Buy' or 'Sell'.")

        # Adjust for JPY pairs
        if symbol in JPY_PAIRS:
            SL /= 100
        
        # Calculate lot size
        lot_size = risked / (SL * contract_size)
        precision = 1 if symbol in INDEX_PAIRS else 2  # Different precision for index pairs
        lot = float(f"{lot_size:.{precision}f}")
        
        return abs(lot)

    except Exception as e:
        print(e)



# x = calculate_lot_size('USOILRoll', 'Buy', 100000, 71, 72, 0.25, broker='IC')
# print(x)