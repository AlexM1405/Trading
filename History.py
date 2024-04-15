# region imports
from AlgorithmImports import *
# endregion

class DancingRedOrangeAntelope(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2022, 10, 9)
        self.SetCash(100000)
        
        self.AddEquity("AAPL", resolution.daily)

        slices = self.History(5)

        for s in slices:
            self.Log(str(self.time)+ "APPL"+ str(s.Bars[self.Symbol("AAPL")].close))


    def OnData(self, data: Slice): 
       pass

    