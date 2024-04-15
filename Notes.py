# region imports
from AlgorithmImports import *
# endregion

class FocusedFluorescentPinkSalamander(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2023, 1, 4)
        self.SetEndDate(2024, 1, 4)
        self.SetCash(100000)

        self.SetBrokerageModel(BrokerageName.InteractiveBrokersBrokerage, AccountType.Margin)
        self.SetTimeZone(TimeZones.NewYork)

        self.AddEquity( "AAPL", resolution=Hour),
        self.Bitcoin = self.AddCrypto( "BTC-USD", resolution=Daily ).Symbol,
        self.AddCrypto( "ETH-USD", resolution=Daily ),
        self.AddForex( "EURUSD" , resolution=Second),
        self.AddFuture("^GSPC", resolution=Second)
        self.AddFuture("^IXIC", resolution=Second)

    def OnData(self, data: Slice):
        self.Log(data[self.Bitcoin].Close)