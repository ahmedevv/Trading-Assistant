import MetaTrader5 as mt5
import pandas as pd
import datetime
import pandas_ta as ta
import datetime



HOURS_2 = 2
HOURS_3 = 3
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
    "UTC+2": "Etc/GMT-2",  # UTC+2
    "UTC+3" : "Etc/GMT-3" 
} 

dst_cutoffs = [
    (pd.to_datetime("2025-03-09T00:00:00"), pd.to_datetime("2025-11-02T00:00:00")),
]

def convert_to_utc(timestamp):
    """Convert broker time to UTC based on DST periods."""
    for start, end in dst_cutoffs:
        if start <= timestamp <= end:
            return 'UTC+3'  # UTC+3 during DST
    return 'UTC+2' # UTC+2 otherwise

def getData(timeframe, symbol, path, login, password, servername):
    try:
        # Initialize MT5 connection
        mt5.shutdown()
        initializeMetatrader(path, login, password, servername)

        current_dst = convert_to_utc(datetime.datetime.now())
        timezone = broker_time_zones.get(current_dst)
        data = mt5.copy_rates_from_pos(symbol, timeframe_dict.get(timeframe), 0, 500)
        df = pd.DataFrame(data)
        
        # Convert timestamps to datetime and adjust to the broker's timezone
        df['time'] = pd.to_datetime(df['time'], unit='s')
        df['time'] = df['time'].dt.tz_localize(timezone)  # Localize to broker's timezone
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
            if current_dst == 'UTC+3':
                if curr_time.hour >= 21:  
                    last_close_time = curr_time.replace(hour=17, minute=0, second=0, microsecond=0)
                if curr_time.hour >= 17:
                    last_close_time = curr_time.replace(hour=17, minute=0, second=0, microsecond=0) - datetime.timedelta(hours=4)
                elif curr_time.hour >= 13:
                    last_close_time = curr_time.replace(hour=13, minute=0, second=0, microsecond=0)- datetime.timedelta(hours=4)
                elif curr_time.hour >= 9:
                    last_close_time = curr_time.replace(hour=9, minute=0, second=0, microsecond=0) - datetime.timedelta(hours=4)
                elif curr_time.hour >= 5:
                    last_close_time = curr_time.replace(hour=5, minute=0, second=0, microsecond=0) - datetime.timedelta(hours=4)
                elif curr_time.hour >= 1:
                    last_close_time = curr_time.replace(hour=1, minute=0, second=0, microsecond=0) - datetime.timedelta(hours=4)
                else:
                    last_close_time = curr_time.replace(hour=21, minute=0, second=0, microsecond=0) - datetime.timedelta(days=1,hours=4)
                    
                
            if current_dst == 'UTC+2':
                if curr_time.hour >= 22:  
                    last_close_time = curr_time.replace(hour=18, minute=0, second=0, microsecond=0)
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
                    last_close_time = curr_time.replace(hour=22, minute=0, second=0, microsecond=0) - datetime.timedelta(days=1,hours=4)
        
        elif timeframe == 'H2':
            last_close_time = curr_time.replace(hour=2 * (curr_time.hour // 2), minute=0, second=0, microsecond=0) - datetime.timedelta(hours=2)
        
        elif timeframe == 'H1':
            last_close_time = curr_time.replace(minute=0, second=0, microsecond=0) - datetime.timedelta(hours=1)
        
        elif timeframe == 'D':
            # if curr_time.weekday() == 0:
            #     last_close_time = curr_time.replace(hour=22, minute=0, second=0, microsecond=0) - datetime.timedelta(days=2)
            # else:
            if current_dst == 'UTC+3':
                last_close_time = curr_time.replace(hour=21, minute=0, second=0, microsecond=0) - datetime.timedelta(days=1, hours = 3)
            if current_dst == 'UTC+2':
                last_close_time = curr_time.replace(hour=22, minute=0, second=0, microsecond=0) - datetime.timedelta(days=1, hours = 2)
        
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
        #print(last_close_time)
        df = df[df['time'] <= last_close_time]

        return df
    except Exception as e:
        print(e)



    

#Useage Example

# df = getData('H4','EURUSD.sd','C:/Program Files/Metatrader 5/terminal64.exe',276521,'Forex_2023#','EquitiBrokerageSC-Demo')
# print(df)