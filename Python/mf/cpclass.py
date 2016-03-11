import win32com
import win32com.client
import pythoncom
import threading
import time

class CpClass:
    cnt = 0

    @classmethod
    def Bind(self, usr_obj):
        handler = type('CpClass_%s'%CpClass.cnt, (CpClass,),{})
        handler.idx = CpClass.cnt
        handler.com_obj = win32com.client.Dispatch(usr_obj.com_str)
        handler.usr_obj = usr_obj
        win32com.client.WithEvents(handler.com_obj, handler)
        CpClass.cnt = CpClass.cnt + 1
        return handler

    @classmethod
    def Request(self):
        self.usr_obj.request(self.com_obj)

    def OnReceived(self):
        self.usr_obj.response(self.com_obj)

class StkMst:
    def __init__(self):
        self.com_str = "dscbo1.StockMst"

    def request(self, com_obj):
        com_obj.SetInputValue(0, "A000660")
        com_obj.Request()
        print ('rq [%s]'%self.__class__.__name__)

    def response(self, com_obj):
        print ('rp [%s]'%self.__class__.__name__)
        print (com_obj.GetHeaderValue(1))

class CpChart:
    def __init__(self):
        self.com_str = "CpSysDib.StockChart"

    def request(self, com_obj):
        com_obj.SetInputValue(0, "A003540")
        com_obj.SetInputValue(1, '2')
        com_obj.SetInputValue(4, 10)
        com_obj.SetInputValue(5, 5)
        com_obj.SetInputValue(6, ord('D'))
        com_obj.Request()
        print ('rq [%s]'%self.__class__.__name__)

    def response(self, com_obj):
        print ('rp [%s]'%self.__class__.__name__)
        print ('received count: [%s]'%com_obj.GetHeaderValue(3))

class StockChart:
    def __init__(self):
        self.com_str = "CpSysDib.StockChart"

    def request(self, com_obj):
        com_obj.SetInputValue(0, 'A067160')
        com_obj.SetInputValue(1, '1')        # count
        com_obj.SetInputValue(2, '0')        # lastest 
        com_obj.SetInputValue(3, '20160310')
        com_obj.SetInputValue(4, 10)        # request count
        com_obj.SetInputValue(5, [0, 1, 2, 3, 4, 5, 6, 8, 9, 37])
        com_obj.SetInputValue(6, ord('m'))        # minute
        com_obj.SetInputValue(9, '1')
        com_obj.Request()
        print ('rq [%s]'%self.__class__.__name__)

    def response(self, com_obj):
        print ('rp [%s]'%self.__class__.__name__)
        
        print ("code = ", com_obj.GetHeaderValue(0))
        print ("field count = ", com_obj.GetHeaderValue(1))
        print ("received count = ", com_obj.GetHeaderValue(3))
        print ("date = ", com_obj.GetHeaderValue(4))
        print ("end price of yesterday = ", com_obj.GetHeaderValue(6))
        print ("current price = ", com_obj.GetHeaderValue(7))
        print ("compare mark = ", chr(com_obj.GetHeaderValue(8)))
        print ("trade amount", com_obj.GetHeaderValue(10))
        print ("asking price for sale = ", com_obj.GetHeaderValue(11))
        print ("asking price for purchase = ", com_obj.GetHeaderValue(12))
        print ("start price = ", com_obj.GetHeaderValue(13))
        print ("top price = ", com_obj.GetHeaderValue(14))
        print ("bottom price = ", com_obj.GetHeaderValue(15))
        print ("trade price", com_obj.GetHeaderValue(16))
        print ("status", chr(com_obj.GetHeaderValue(17)))
        print ("maximum price", com_obj.GetHeaderValue(22))
        print ("minimum price", com_obj.GetHeaderValue(23))

        num = com_obj.GetHeaderValue(3)
        for i in range(num):
            print("\tdate: ", com_obj.GetDataValue(0,i))
            print("\ttime ", com_obj.GetDataValue(1,i))
            print("\tstart price: ", com_obj.GetDataValue(2,i))
            print("\ttop price: ", com_obj.GetDataValue(3,i))
            print("\tbottom price: ", com_obj.GetDataValue(4,i))
            print("\tend price: ", com_obj.GetDataValue(5,i))
            print("\tdiff via yesterday: ", com_obj.GetDataValue(6,i))
            print("\ttrade amount: ", com_obj.GetDataValue(7,i))
            print("\ttrade price: ", com_obj.GetDataValue(8,i))
            print("\tcompare mark: ", chr(com_obj.GetDataValue(9,i)))
            print("\t==============")

if __name__ == '__main__':
    stkmst = CpClass.Bind(StkMst())
    stkmst.Request()

    #cpchart = CpClass.Bind(CpChart())
    #cpchart.Request()

    stockchart = CpClass.Bind(StockChart())
    stockchart.Request()

    while True:
        pythoncom.PumpWaitingMessages()
        time.sleep(0.01)

