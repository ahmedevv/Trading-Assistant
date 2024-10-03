import MetaTrader5 as mt5
import parameters
RED = '\033[31m'
GREEN = '\033[32m'
RESET = '\033[0m' # called to return to standard terminal text color
def OpenedPosition(Symbols):
    #print(RED + '----Managing the RR----' + RESET)
    mt5.initialize(parameters.path,login=parameters.login,      
   password=parameters.password,   
   server=parameters.server)
    for key,val in Symbols.items():
        position = mt5.positions_get(symbol=val)
        second_curr = val[3:-3]
        if position:
            for orders in position:
                symbol_info = mt5.symbol_info(val)
                min_lot_size = symbol_info.trade_contract_size
                # get position data
                order_type = orders.type
                price_open = orders.price_open
                profit = orders.profit
                sl = orders.sl
                tp = orders.tp
                vol = orders.volume
                #For Buy
                one_percent_of_trade = 0
                if order_type == 0:
                    one_percent_of_trade = (price_open - sl)
                elif order_type == 1: 
                    one_percent_of_trade = (sl - price_open)
                
                if val in ['USDJPY.sd','GBPJPY.sd','NZDJPY.sd','AUDJPY.sd','EURJPY.sd']:
                     one_percent_of_trade = one_percent_of_trade*0.01
    
                if second_curr == 'CHF':
                    one_percent = one_percent_of_trade * min_lot_size * vol * parameters.chf_pip_val
                elif second_curr == 'CAD':
                    one_percent = one_percent_of_trade * min_lot_size * vol * parameters.cad_pip_val
                elif second_curr == 'JPY' :
                    one_percent = one_percent_of_trade * min_lot_size * vol * parameters.jpy_pip_val
                else:
                    one_percent = one_percent_of_trade * min_lot_size * vol * 1
                
                
                 
                #Now if the balance is greater than 250$ it will change the SL to entry so we remain on safe side
                if order_type == 0:
                    #Profit is greater than 2 Percent SL goes to BreakEven
                    if profit >= one_percent : 
                            
                            sl_price = price_open   
                            request = {
                                        'action': mt5.TRADE_ACTION_SLTP,
                                        'position': orders.ticket,
                                        'sl': sl_price,
                                        'tp' : tp
                                    }
                            result = mt5.order_send(request)
                            
                            
                    
                            
                elif order_type == 1:
                    if profit >= one_percent :  
                            
                            sl_price = price_open 
                            request = {
                                        'action': mt5.TRADE_ACTION_SLTP,
                                        'position': orders.ticket,
                                        'sl': sl_price,
                                        'tp' : tp
                                    }
                            result = mt5.order_send(request)
                            
                            



#OpenedPosition(parameters.asset)