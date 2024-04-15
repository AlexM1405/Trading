# region imports
from AlgorithmImports import *
# endregion

class DancingRedOrangeAntelope(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2022, 10, 9)

        self.SetCash(100000)
        
        self.Universe(self.ByVolumen)

    def OnData(self, data: Slice): 
        self.Log("Acciones con mayor volumen: {",".join([key.value for key in data.keys])}" )

        
    def ByVolumen(self,coarse):
        SortByVolumen = sorted(coarse, key = lambda x: x.DollarVolume, reverse=True)
        HoldingSorted = [x.Symbol for x in SortByVolumen if x.HasFundamentalData]

        return HoldingSorted[:10]