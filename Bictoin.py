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
        self.AddCrypto( "ETH-USD", resolution.Daily ),
        self.AddForex( "EURUSD" , resolution.Second),
        self.AddFuture("^GSPC", resolution=Second)
        self.AddFuture("^IXIC", resolution=Second)

        self.TakeProfit = None
        self.StopLoss = None

    def OnData(self, data: Slice):
        self.Log(data[self.Bitcoin].Close)

        if not (self.Portfolio.Invested and self.Transactions.GetOpenOrders):
            self.order = self.MarketOrder(self.Bitcoin, 1)
            self.TakeProfit = self.LimitOrder(self.Bitcoin, 1, price*1.03)
            self.StopLoss = self.StopMarketOrder(self.Bitcoin, 1, price*0.97)
        elif (price > self.PreviousPrice ):
            self.StopLoss.UpdateStopPrice(price*0.97)

        self.PreviousPrice = price
    def OnOrderEvent(self, orderEvent):
        order = self.Transactions.GetOrderById(orderEvent.orderId)
        if orderEvent.Status !=  OrdenStatus.Filled:
            return 
        
        if self.TakeProfit == None or self.StopLoss == None:
            return 

        if (Orden.Id == self.TakeProfit.OrderId):
            self.StopLoss.Cancel()
        
        if (Orden.Id == self.StopLoss.OrderId):
            self.TakeProfit.Cancel()