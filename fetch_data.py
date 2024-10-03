import MetaTrader5 as mt5
import pandas as pd
import datetime
import pandas_ta as ta
import datetime

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


def getDailyData(symbol,path,login,password,servername):
    try:
        initializeMetatrader(path,login,password,servername)
        gmt2 = datetime.timezone(datetime.timedelta(hours=3), "GMT+3")
        
    # the name "GMT+2" is optional, the name does not appear in output of isoformat, only the offset
       
        
           
        daily = mt5.copy_rates_from_pos(symbol,mt5.TIMEFRAME_D1,0,500)
        df = pd.DataFrame(daily)  
        
        df['time']  = pd.to_datetime(df['time'],unit='s')
        timestamp = df['time'].iloc[-1]
        if datetime.datetime.now(gmt2).day == timestamp.day:
            df = df[:-1]



        return df
    except Exception as e:
        
        print(e)
    
         

   
def getMonthlyData(symbol,path,login,password,servername):
    try:
        initializeMetatrader(path,login,password,servername)
        gmt2 = datetime.timezone(datetime.timedelta(hours=3), "GMT+3")
        today = False
    # the name "GMT+2" is optional, the name does not appear in output of isoformat, only the offset
        hour = datetime.datetime.now(gmt2).hour
        
           
        daily = mt5.copy_rates_from_pos(symbol,mt5.TIMEFRAME_MN1,0,500)
        df = pd.DataFrame(daily)  
        
        df['time']  = pd.to_datetime(df['time'],unit='s')
        timestamp = df['time'].iloc[-1]
        if datetime.datetime.now(gmt2).month == timestamp.month:
            today = True
            df = df[:-1]



        return df,today
    except Exception as e:
        
        print(e)
    


def getWeeklyData(symbol,path,login,password,servername):
    try:
        initializeMetatrader(path,login,password,servername)
        gmt2 = datetime.timezone(datetime.timedelta(hours=3), "GMT+3")
        today = False
    # the name "GMT+2" is optional, the name does not appear in output of isoformat, only the offset
        hour = datetime.datetime.now(gmt2).hour
        
           
        daily = mt5.copy_rates_from_pos(symbol,mt5.TIMEFRAME_W1,0,500)
        df = pd.DataFrame(daily)  
        
        df['time']  = pd.to_datetime(df['time'],unit='s')
        timestamp = df['time'].iloc[-1]
        if datetime.datetime.now(gmt2).day == timestamp.day:
            today = True
            df = df[:-1]



        return df
    except Exception as e:
        
        print(e)
    

def get4hData(symbol,path,login,password,servername):
    try:
        initializeMetatrader(path,login,password,servername)
        gmt2 = datetime.timezone(datetime.timedelta(hours=3), "GMT+3")
        today = False
    # the name "GMT+2" is optional, the name does not appear in output of isoformat, only the offset
        hour = datetime.datetime.now(gmt2).hour
        
           
        daily = mt5.copy_rates_from_pos(symbol,mt5.TIMEFRAME_H4,0,500)
        df = pd.DataFrame(daily)  
        
        df['time']  = pd.to_datetime(df['time'],unit='s')
        timestamp = df['time'].iloc[-1]
        if datetime.datetime.now(gmt2).hour == timestamp.hour:
            today = True
            df = df[:-1]



        return df
    except Exception as e:
        
        print(e)
    


def get1HData(symbol,path,login,password,servername):
    try:
        initializeMetatrader(path,login,password,servername)
        gmt2 = datetime.timezone(datetime.timedelta(hours=3), "GMT+3")
        today = False
    # the name "GMT+2" is optional, the name does not appear in output of isoformat, only the offset
        hour = datetime.datetime.now(gmt2).hour
        
           
        daily = mt5.copy_rates_from_pos(symbol,mt5.TIMEFRAME_H1,0,500)
        df = pd.DataFrame(daily)  
        
        df['time']  = pd.to_datetime(df['time'],unit='s')
        timestamp = df['time'].iloc[-1]
        if datetime.datetime.now(gmt2).hour == timestamp.hour:
            today = True
            df = df[:-1]



        return df
    except Exception as e:
        
        print(e)
    


def get5MData(symbol,path,login,password,servername):
    try:
        initializeMetatrader(path,login,password,servername)
        gmt2 = datetime.timezone(datetime.timedelta(hours=3), "GMT+3")
        today = False
    # the name "GMT+2" is optional, the name does not appear in output of isoformat, only the offset
        hour = datetime.datetime.now(gmt2).hour
        
           
        daily = mt5.copy_rates_from_pos(symbol,mt5.TIMEFRAME_M5,0,500)
        df = pd.DataFrame(daily)  
        
        df['time']  = pd.to_datetime(df['time'],unit='s')
        timestamp = df['time'].iloc[-1]
        if datetime.datetime.now(gmt2).minute == timestamp.minute:
            today = True
            df = df[:-1]


        return df
    except Exception as e:
        
        print(e)



def get15MData(symbol,path,login,password,servername):
    try:
        initializeMetatrader(path,login,password,servername)
        gmt2 = datetime.timezone(datetime.timedelta(hours=3), "GMT+3")
        today = False
    # the name "GMT+2" is optional, the name does not appear in output of isoformat, only the offset
        hour = datetime.datetime.now(gmt2).hour
        
           
        daily = mt5.copy_rates_from_pos(symbol,mt5.TIMEFRAME_M15,0,500)
        df = pd.DataFrame(daily)  
        
        df['time']  = pd.to_datetime(df['time'],unit='s')
        timestamp = df['time'].iloc[-1]
        if datetime.datetime.now(gmt2).minute == timestamp.minute:
            today = True
            df = df[:-1]



        return df
    except Exception as e:
        
        print(e)
    