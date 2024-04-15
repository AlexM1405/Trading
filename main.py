# region imports
from AlgorithmImports import *
# endregion

class CalculatingBlackWhale(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020, 1, 10)  # Set Start Date
        self.SetEndDate(2021,1,10)
        self.SetCash(100000)  # Set Strategy Cash

        #Acceder a los datos del mercado
        #self.bitcoin = self.AddCrypto("BTCUSD",Resolution.Daily).Symbol
        #self.AddEquity("AAPL",Resoltion.Hour)
        #self.AddForex("EURUSD",Resolution.Second)
        #self.AddCfd("",Resolution.Minute)
        #self.AddOption("",Resolution.Tick)
        
    def OnData(self, data):
        self.Log(data[self.bitcoin].Close)