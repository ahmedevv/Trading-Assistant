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


def timezoneTranslation(time_gap):

    """
        Given the time difference between different zones It'll convert the time to make sure the time is according to broker's time.

    """

    curr_time = datetime.datetime.now()
    if time_gap == 0:
        curr_time = datetime.datetime.now()
    elif time_gap > 0:
        curr_time = datetime.datetime.now()
        curr_time = curr_time + datetime.timedelta(hours=time_gap)
    elif time_gap < 0:
        curr_time = datetime.datetime.now()
        curr_time = curr_time - datetime.timedelta(hours=abs(time_gap))
    return curr_time




def getData(time_gap,timeframe,symbol,path,login,password,servername):
    try:
        initializeMetatrader(path,login,password,servername)
        data = mt5.copy_rates_from_pos(symbol,timeframe_dict.get(timeframe),0,500)
        df = pd.DataFrame(data)  
    
        df['time']  = pd.to_datetime(df['time'],unit='s')
        timestamp = df['time'].iloc[-1]
        curr_time = timezoneTranslation(time_gap)
        print(curr_time)
 
    # the name "GMT+2" is optional, the name does not appear in output of isoformat, only the offset

        
        if timeframe in ['H12','H4','H2','H1']:  

            if curr_time.hour == timestamp.hour:
                df = df[:-1]

        elif timeframe in ['D','W']:
           
            if curr_time.day == timestamp.day:
                df = df[:-1]

        elif timeframe in ['MN'] :
           
            if curr_time.month == timestamp.month:
                df = df[:-1]

        elif timeframe in ['M30','M15','M5','M1'] :
           
            if curr_time.minute == timestamp.minute:
                df = df[:-1]


        return df
    except Exception as e:
        
        print(e)
    
         

   

    


#df = getData(0,'H2','EURUSDx','C:/Program Files/Metatrader 5/terminal64.exe',5466445487,'XCdd!!9855','NoorCapital-Server')
