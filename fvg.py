import pandas as pd



def identifyFVG(df):
    ''' Return the FVG Flag if a FVG is occured in given Candles
        Different Scenarios for FVG in Order 1st Candle - 2nd Candle - 3rd Candle
        # 1. Bearish - Bearish - Bullish
        # 2. Bearish - Bearish - Bearish
        # 3. Bearish - Bullish - Bearish
        # 4. Bearish - Bullish - Bullish
        # 5. Bullish - Bullish - Bullish
        # 6. Bullish - Bearish - Bearish
        # 7. Bullish - Bullish - Bearish
        # 8. Bullish - Bearish - Bullish
        Indexes : j-2 Candle is First, j-1 Second Candle, j Third Candle
        Bullish and Bearish : if open-close < 0 then Bullish, open-close > 0 Bearish'''
    
    if df.empty:
        print(df)
        return False,df
    fvg_flag = False
    fvg_candle = df.iloc[0] 
    high = 0
    low = 0
    direction = ''
    date = ''
    for j in range(2,len(df)):
        
        print((df['open'].iloc[j-2] - df['close'].iloc[j-2]))
        print((df['open'].iloc[j-1] - df['close'].iloc[j-1]))
        print((df['open'].iloc[j] - df['close'].iloc[j]))
        print((df['high'].iloc[j-2] - df['low'].iloc[j]))
        #
        # Bearish - Bearish - Bullish
        if (df['open'].iloc[j-2] - df['close'].iloc[j-2]) > 0 and (df['open'].iloc[j-1] - df['close'].iloc[j-1]) > 0 and (df['open'].iloc[j] - df['close'].iloc[j]) < 0: 
            if (df['low'].iloc[j-2] - df['high'].iloc[j]) > 0:
                fvg_flag = True
                fvg_candle = df.iloc[j-2] 
                high = df['high'].iloc[j]
                low = df['low'].iloc[j-2]
                date = df['time'].iloc[j]
                direction = 'Bearish'
                print('case 1')

                break

        # Bearish - Bearish - Bearish
        elif (df['open'].iloc[j-2] - df['close'].iloc[j-2]) > 0 and (df['open'].iloc[j-1] - df['close'].iloc[j-1]) > 0 and (df['open'].iloc[j] - df['close'].iloc[j]) > 0 :
            if (df['low'].iloc[j-2] - df['high'].iloc[j]) > 0:
                fvg_flag = True
                fvg_candle = df.iloc[j-2]
                high = df['high'].iloc[j]
                low = df['low'].iloc[j-2]
                date = df['time'].iloc[j]
                direction = 'Bearish' 
                print('case 2')
                break
        # check direction for this particular condition
        # Bearish - Bullish - Bearish
        elif (df['open'].iloc[j-2] - df['close'].iloc[j-2]) > 0 and (df['open'].iloc[j-1] - df['close'].iloc[j-1]) < 0 and (df['open'].iloc[j] - df['close'].iloc[j]) > 0:
            if (df['high'].iloc[j-2] - df['low'].iloc[j]) < 0:
                fvg_flag = True
                fvg_candle = df.iloc[j-2] 
                high = df['high'].iloc[j-2]
                low = df['low'].iloc[j]
                date = df['time'].iloc[j]
                direction = 'Bullish'
                print('case 3')
                break
        
        # Bearish - Bullish - Bullish
        elif (df['open'].iloc[j-2] - df['close'].iloc[j-2]) > 0 and (df['open'].iloc[j-1] - df['close'].iloc[j-1]) < 0 and (df['open'].iloc[j] - df['close'].iloc[j]) < 0:
            if (df['high'].iloc[j-2] - df['low'].iloc[j]) < 0:
                fvg_flag = True
                fvg_candle = df.iloc[j-2] 
                high = df['high'].iloc[j-2]
                low = df['low'].iloc[j]
                date = df['time'].iloc[j]
                direction = 'Bullish'
                print('case 4')
                break
        

        # Bullish - Bullish - Bullish
        elif (df['open'].iloc[j-2] - df['close'].iloc[j-2]) < 0 and (df['open'].iloc[j-1] - df['close'].iloc[j-1]) < 0 and (df['open'].iloc[j] - df['close'].iloc[j]) < 0:
            if (df['high'].iloc[j-2] - df['low'].iloc[j]) < 0:
                fvg_flag = True
                fvg_candle = df.iloc[j-2] 
                high = df['high'].iloc[j-2]
                low = df['low'].iloc[j]
                date = df['time'].iloc[j]
                direction = 'Bullish'
                print('case 5')
                break

        # Bullish - Bearish - Bearish
        elif (df['open'].iloc[j-2] - df['close'].iloc[j-2]) < 0 and (df['open'].iloc[j-1] - df['close'].iloc[j-1]) > 0 and (df['open'].iloc[j] - df['close'].iloc[j]) > 0:
            if (df['low'].iloc[j-2] - df['high'].iloc[j]) > 0:
                fvg_flag = True
                fvg_candle = df.iloc[j-2] 
                high = df['high'].iloc[j]
                low = df['low'].iloc[j-2]
                date = df['time'].iloc[j]
                direction = 'Bearish'
                print('case 6')
                break

        # Bullish - Bullish - Bearish
        elif (df['open'].iloc[j-2] - df['close'].iloc[j-2]) < 0 and (df['open'].iloc[j-1] - df['close'].iloc[j-1]) < 0 and (df['open'].iloc[j] - df['close'].iloc[j]) > 0:
            if (df['high'].iloc[j-2] - df['low'].iloc[j]) < 0:
                fvg_flag = True
                fvg_candle = df.iloc[j-2] 
                high = df['high'].iloc[j-2]
                low = df['low'].iloc[j]
                date = df['time'].iloc[j]
                direction = 'Bullish'
                print('case 7')
                break
        

        # Bullish - Bearish - Bullish
        elif (df['open'].iloc[j-2] - df['close'].iloc[j-2]) < 0 and (df['open'].iloc[j-1] - df['close'].iloc[j-1]) > 0 and (df['open'].iloc[j] - df['close'].iloc[j]) < 0:
            if (df['high'].iloc[j] - df['low'].iloc[j-2]) < 0:
                fvg_flag = True
                fvg_candle = df.iloc[j-2] 
                high = df['high'].iloc[j]
                low = df['low'].iloc[j-2]
                date = df['time'].iloc[j]
                direction = 'Bearish'
                print('case 8')
                break
    if high < low:
        high , low = low , high
    
    return fvg_flag,fvg_candle,high,low,direction,date









# df = pd.DataFrame(columns=['time','open','high','low','close'])
# df['time'] = ['2024-10-16 06:00:00','2024-10-16 08:00:00','2024-10-16 10:00:00']
# df['open'] = [1.62362,1.62883,1.61682]
# df['high'] = [1.63269,1.63036,1.62112]
# df['low'] = [1.62349,1.61487,1.61331]
# df['close'] = [1.62924,1.61731,1.62025]        
# print(df) 
# fvg_flag,fvg_candle,high,low,direction,date = identifyFVG(df)  
# print(fvg_flag)               