import MetaTrader5 as mt5
import pandas as pd
import datetime
import pandas_ta as ta
import datetime





timeframe_dict = {
                    'D' : mt5.TIMEFRAME_D1,
                    'W' : mt5.TIMEFRAME_W1,
                    'MN' : mt5.TIMEFRAME_MN1,
                    'H12' : mt5.TIMEFRAME_H12,
                    'H6' : mt5.TIMEFRAME_H6,
                    'H4' : mt5.TIMEFRAME_H4,
                    'H2' : mt5.TIMEFRAME_H2,
                    'H1' : mt5.TIMEFRAME_H1,
                    'M30' : mt5.TIMEFRAME_M30,
                    'M15' : mt5.TIMEFRAME_M15,
                    'M5' : mt5.TIMEFRAME_M5,
                    'M1' : mt5.TIMEFRAME_M1

}



def initializeMetatrader(path,login,password,servername):
        try:
            
            if not mt5.initialize(path=path,login=login,password=password,server=servername):
                print("initialize() failed, error code =",mt5.last_error())
                LoginFlag = False
                return(LoginFlag)
                #quit()
            #self.mt5.initialize(self.path,login=self.login,password=self.password,server=self.servername)
        except:
            print('Check Metatrader Credentials i.e. Login,Password,Server')







broker_time_zones = {
    "UTC-4": "Etc/GMT+4",  # UTC-4
    "UTC+2": "Etc/GMT-2"    # UTC+2
}


# def getData(timeframe, symbol, path, login, password, servername, broker_timezone):
#     try:
#         # Initialize MT5 connection
#         initializeMetatrader(path, login, password, servername)
        
#         # Fetch data from MT5
#         data = mt5.copy_rates_from_pos(symbol, timeframe_dict.get(timeframe), 0, 500)
#         df = pd.DataFrame(data)
        
#         # Convert timestamps to datetime and adjust to the broker's timezone
#         df['time'] = pd.to_datetime(df['time'], unit='s')
#         df['time'] = df['time'].dt.tz_localize(broker_time_zones[broker_timezone])  # Localize to broker's timezone
#         df['time'] = df['time'].dt.tz_convert('UTC')  # Convert to UTC

#         # Get the current UTC time
#         curr_time = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
#         #print(curr_time)
        
#         # Define the cutoff for each timeframe, making it timezone-aware
#         if timeframe == 'H12':
#             last_close_time = curr_time.replace(hour=12 * (curr_time.hour // 12), minute=0, second=0, microsecond=0)  - datetime.timedelta(hours=12)
#             print(last_close_time)
#         elif timeframe == 'H6':
#             last_close_time = curr_time.replace(hour=6 * (curr_time.hour // 6), minute=0, second=0, microsecond=0) - datetime.timedelta(hours=6)
#         elif timeframe == 'H4':
#             last_close_time = curr_time.replace(hour=4 * (curr_time.hour // 4), minute=0, second=0, microsecond=0) - datetime.timedelta(hours=4)
#         elif timeframe == 'H2':
#             last_close_time = curr_time.replace(hour=2 * (curr_time.hour // 2), minute=0, second=0, microsecond=0) - datetime.timedelta(hours=2)
#         elif timeframe == 'H1':
#             last_close_time = curr_time.replace(minute=0, second=0, microsecond=0) - datetime.timedelta(hours=1)
#         elif timeframe == 'D':
#             last_close_time = curr_time.replace(hour=22, minute=0, second=0, microsecond=0) - datetime.timedelta(days=1)
#         elif timeframe == 'W':
#             last_close_time = (curr_time - datetime.timedelta(days=curr_time.weekday())).replace(hour=0, minute=0, second=0, microsecond=0) - datetime.timedelta(weeks=1)
#         elif timeframe == 'MN':
#             last_close_time = (curr_time.replace(day=1, hour=0, minute=0, second=0, microsecond=0) - datetime.timedelta(days=1)).replace(day=1)
#         elif timeframe == 'M30':
#             last_close_time = curr_time.replace(minute=30 * (curr_time.minute // 30), second=0, microsecond=0) - datetime.timedelta(minutes=30)
#         elif timeframe == 'M15':
#             last_close_time = curr_time.replace(minute=15 * (curr_time.minute // 15), second=0, microsecond=0) - datetime.timedelta(minutes=15)
#         elif timeframe == 'M5':
#             last_close_time = curr_time.replace(minute=5 * (curr_time.minute // 5), second=0, microsecond=0) - datetime.timedelta(minutes=5)
#         elif timeframe == 'M1':
#             last_close_time = curr_time.replace(second=0, microsecond=0) - datetime.timedelta(minutes=1)

#         # Filter the DataFrame to include only closed candles
#         df = df[df['time'] <= last_close_time]

#         return df
#     except Exception as e:
#         print(e)       

   
import datetime

def getData(timeframe, symbol, path, login, password, servername, broker_timezone):
    try:
        # Initialize MT5 connection
        initializeMetatrader(path, login, password, servername)
       
        # Fetch data from MT5
        data = mt5.copy_rates_from_pos(symbol, timeframe_dict.get(timeframe), 0, 500)
        df = pd.DataFrame(data)
        
        # Convert timestamps to datetime and adjust to the broker's timezone
        df['time'] = pd.to_datetime(df['time'], unit='s')
        df['time'] = df['time'].dt.tz_localize(broker_time_zones[broker_timezone])  # Localize to broker's timezone
        df['time'] = df['time'].dt.tz_convert('UTC')  # Convert to UTC

        # Get the current UTC time
        curr_time = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
        
        
        # Define the cutoff for each timeframe, ensuring the last fully closed candle is used
        if timeframe == 'H12':
            # H12 candles close at 10:00 and 22:00 UTC
            if 10 <= curr_time.hour < 22:
                last_close_time = curr_time.replace(hour=10, minute=0, second=0, microsecond=0) - datetime.timedelta(hours=12)
            else:
                last_close_time = curr_time.replace(hour=22, minute=0, second=0, microsecond=0) - datetime.timedelta(days=12)
        
        elif timeframe == 'H6':
            # H6 candles close at 04:00, 10:00, 16:00, and 22:00 UTC
            if curr_time.hour >= 16:
                last_close_time = curr_time.replace(hour=16, minute=0, second=0, microsecond=0) - datetime.timedelta(hours=6)
            elif curr_time.hour >= 10:
                last_close_time = curr_time.replace(hour=10, minute=0, second=0, microsecond=0) - datetime.timedelta(hours=6)
            elif curr_time.hour >= 4:
                last_close_time = curr_time.replace(hour=4, minute=0, second=0, microsecond=0) - datetime.timedelta(hours=6)
            else:
                last_close_time = curr_time.replace(hour=22, minute=0, second=0, microsecond=0) - datetime.timedelta(hours=6)

        elif timeframe == 'H4':
            # H4 candles close at 02:00, 06:00, 10:00, 14:00, 18:00, and 22:00 UTC
            if curr_time.hour >= 18:
                last_close_time = curr_time.replace(hour=18, minute=0, second=0, microsecond=0) - datetime.timedelta(hours=4)
            elif curr_time.hour >= 14:
                last_close_time = curr_time.replace(hour=14, minute=0, second=0, microsecond=0)- datetime.timedelta(hours=4)
            elif curr_time.hour >= 10:
                last_close_time = curr_time.replace(hour=10, minute=0, second=0, microsecond=0) - datetime.timedelta(hours=4)
            elif curr_time.hour >= 6:
                last_close_time = curr_time.replace(hour=6, minute=0, second=0, microsecond=0) - datetime.timedelta(hours=4)
            elif curr_time.hour >= 2:
                last_close_time = curr_time.replace(hour=2, minute=0, second=0, microsecond=0) - datetime.timedelta(hours=4)
            else:
                last_close_time = curr_time.replace(hour=22, minute=0, second=0, microsecond=0) - datetime.timedelta(days=4)
        
        elif timeframe == 'H2':
            last_close_time = curr_time.replace(hour=2 * (curr_time.hour // 2), minute=0, second=0, microsecond=0) - datetime.timedelta(hours=2)
        
        elif timeframe == 'H1':
            last_close_time = curr_time.replace(minute=0, second=0, microsecond=0) - datetime.timedelta(hours=1)
        
        elif timeframe == 'D':
            # if curr_time.weekday() == 0:
            #     last_close_time = curr_time.replace(hour=22, minute=0, second=0, microsecond=0) - datetime.timedelta(days=2)
            # else:
                last_close_time = curr_time.replace(hour=22, minute=0, second=0, microsecond=0) - datetime.timedelta(days=1)
        
        elif timeframe == 'W':
            last_close_time = (curr_time - datetime.timedelta(days=curr_time.weekday())).replace(hour=0, minute=0, second=0, microsecond=0) - datetime.timedelta(weeks=1)
        
        elif timeframe == 'MN':
            last_close_time = (curr_time.replace(day=1, hour=0, minute=0, second=0, microsecond=0) - datetime.timedelta(days=1)).replace(day=1)
        
        elif timeframe == 'M30':
            last_close_time = curr_time.replace(minute=30 * (curr_time.minute // 30), second=0, microsecond=0) - datetime.timedelta(minutes=30)
        
        elif timeframe == 'M15':
            last_close_time = curr_time.replace(minute=15 * (curr_time.minute // 15), second=0, microsecond=0) - datetime.timedelta(minutes=15)
        
        elif timeframe == 'M5':
            last_close_time = curr_time.replace(minute=5 * (curr_time.minute // 5), second=0, microsecond=0) - datetime.timedelta(minutes=5)
        
        elif timeframe == 'M1':
            last_close_time = curr_time.replace(second=0, microsecond=0) - datetime.timedelta(minutes=1)

        # Filter the DataFrame to include only closed candles
        print(last_close_time)
        df = df[df['time'] <= last_close_time]

        return df
    except Exception as e:
        print(e)



    

#Useage Example

# df = getData('H1','EURUSD.sd','C:/Program Files/MT5-1/terminal64.exe',276521,'Forex_2023#','EquitiBrokerageSC-Demo','UTC+2')
# print(df)