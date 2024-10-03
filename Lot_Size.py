import parameters
def calculate_lot_size(symbol,order_type,balance,stoploss,open_price,risk_pct):
    try:
      second_curr = symbol[3:-3]
      risk_balance = float(risk_pct)
      account_balance = balance
      contract_size = 100000
      gold_contract = 100
      silver_contract = 5000
      index_contract = 1
      oil_contract = 1000
      lot = 0.0
      #Equation for Calculating lot Size
      #1. risked = (balance * risk) / 100 gives the percent of risk we want 
      #2. Determine SL 
      #3. (SL*Symbol_Contract_Size)*Lotsize(Find) = Risked
      #4. Lotsize = risked/(SL*100)
      # calculate the lot size based on the specified risk percentage and account balance
      #risk_percent = (risk_balance * 100) / account_balance
      
      risked = (account_balance * risk_pct) / 100
      if second_curr == 'CHF':
         risked = risked/parameters.chf_pip_val
      elif second_curr == 'CAD':
         risked = risked / parameters.cad_pip_val
      elif second_curr == 'JPY' :
         risked = risked / parameters.jpy_pip_val
      print(risked)
      if order_type == "Buy":
          if symbol in ['USDJPY.sd','GBPJPY.sd','NZDJPY.sd','AUDJPY.sd','EURJPY.sd']:
            SL = (open_price - stoploss) / 100
            lotSize = risked / (SL*contract_size)
            lot = float("{:.2f}".format(lotSize))
            
          elif symbol in ['XAUUSD.sd']:
            SL = (open_price - stoploss) 
            
            lotSize = risked / (SL*gold_contract)
            lot = float("{:.2f}".format(lotSize))
            
          elif symbol in ['UT100Roll','US30Roll','DE40Roll','UK100Roll','UT100Roll']:
            SL = (open_price - stoploss) 
            lotSize = risked / (SL*index_contract)
            lot = float("{:.1f}".format(lotSize))


          elif symbol in ['XAGUSD.sd']:
            SL = (open_price - stoploss) 
            lotSize = risked / (SL*silver_contract)
            lot = float("{:.2f}".format(lotSize))

          elif symbol == 'USOILRoll':
            
            SL = (open_price - stoploss) 
            lotSize = risked / (SL*oil_contract)
            lot = float("{:.2f}".format(lotSize))
            
          else:
            SL = (open_price - stoploss) 
            lotSize = risked / (SL*contract_size)
            lot = float("{:.2f}".format(lotSize))
            
        

      elif order_type == "Sell":
          if symbol in ['USDJPY.sd','GBPJPY.sd','NZDJPY.sd','AUDJPY.sd','EURJPY.sd']:
            print(risked)
            SL = (stoploss - open_price) / 100
            print(stoploss,open_price)
            print(SL)
            lotSize = risked / (SL*contract_size)
            print(lotSize)
            lot = float("{:.2f}".format(lotSize))
            
          elif symbol in ['XAUUSD.sd']:
            SL = (stoploss - open_price) 
            lotSize = risked / (SL*gold_contract)
            lot = float("{:.2f}".format(lotSize))
            
          elif symbol in ['UT100Roll','US30Roll','DE40Roll','UK100Roll','UT100Roll']:
            SL = (stoploss - open_price) 
            lotSize = risked / (SL*index_contract)
            lot = float("{:.1f}".format(lotSize))


          elif symbol in ['XAGUSD.sd']:
            SL = (stoploss - open_price) 
            lotSize = risked / (SL*silver_contract)
            lot = float("{:.2f}".format(lotSize))

          elif symbol == 'USOILRoll':
            SL = (stoploss - open_price) 
            lotSize = risked / (SL*oil_contract)
            lot = float("{:.2f}".format(lotSize))
            
          else:
              SL = (stoploss - open_price)
              lotSize = risked / (SL*contract_size)
              lot = float("{:.2f}".format(lotSize))
              

      return abs(lot)
    except Exception as e:
        print(e)






