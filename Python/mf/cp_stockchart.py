import win32com.client as wc
from cp_codes import Codes

def getStockChart(code):
    print ("=== stockChart for", code, "===")

    reqObj = wc.Dispatch("CpSysDib.StockChart")
    reqObj.SetInputValue(0, code)
    reqObj.SetInputValue(1, '1')        # count
    reqObj.SetInputValue(2, '0')        # lastest 
    reqObj.SetInputValue(3, '20160310')
    reqObj.SetInputValue(4, 20)
    reqObj.SetInputValue(5, [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 37])
    reqObj.SetInputValue(6, ord('m'))        # minute
    reqObj.SetInputValue(9, '1')
    
    ret = reqObj.BlockRequest()

    if ret == 0:
        # success
        codes = Codes()
        print ("종목코드 = ", reqObj.GetHeaderValue(0))
        print ("필드 개수 = ", reqObj.GetHeaderValue(1))
        print ("수신 개수 = ", reqObj.GetHeaderValue(3))
        print ("시간 = ", reqObj.GetHeaderValue(4))
        print ("전일종가 = ", reqObj.GetHeaderValue(6))
        print ("현재가 = ", reqObj.GetHeaderValue(7))
        print ("대비부호 = ", chr(reqObj.GetHeaderValue(8)))
        print ("거래량", reqObj.GetHeaderValue(10))
        print ("매도호가 = ", reqObj.GetHeaderValue(11))
        print ("매수호가 = ", reqObj.GetHeaderValue(12))
        print ("시가 = ", reqObj.GetHeaderValue(13))
        print ("고가 = ", reqObj.GetHeaderValue(14))
        print ("저가 = ", reqObj.GetHeaderValue(15))
        print ("거래대금 = ", reqObj.GetHeaderValue(16))
        print ("종목상태 = ", codes.get_stock_status(chr(reqObj.GetHeaderValue(17))))
        print ("상한가 = ", reqObj.GetHeaderValue(22))
        print ("하한가 = ", reqObj.GetHeaderValue(23))

        num = reqObj.GetHeaderValue(3)
        for i in range(num):
            print("\t날짜: ", reqObj.GetDataValue(0,i))
            print("\t시간: ", reqObj.GetDataValue(1,i))
            print("\t시가: ", reqObj.GetDataValue(2,i))
            print("\t고가: ", reqObj.GetDataValue(3,i))
            print("\t저가: ", reqObj.GetDataValue(4,i))
            print("\t종가: ", reqObj.GetDataValue(5,i))
            print("\t전일대비: ", reqObj.GetDataValue(6,i))
            print("\t거래량: ", reqObj.GetDataValue(7,i))
            print("\t거래대금: ", reqObj.GetDataValue(8,i))
            print("\t누적체결매도수량: ", reqObj.GetDataValue(9,i))
            print("\t누적체결매수수량: ", reqObj.GetDataValue(10,i))
            print("\t상장주식수: ", reqObj.GetDataValue(11,i))
            print("\t시가총액: ", reqObj.GetDataValue(12,i))
            print("\t외국인주문한도수량: ", reqObj.GetDataValue(13,i))
            print("\t외국인주문가능수량: ", reqObj.GetDataValue(14,i))
            print("\t외국인현보유수량: ", reqObj.GetDataValue(15,i))
            print("\t외국인현보유비율: ", reqObj.GetDataValue(15,i))
            print("\t수정주가일자(YYYYMMDD): ", reqObj.GetDataValue(17,i))
            print("\t수정주가비율: ", reqObj.GetDataValue(18,i))
            print("\t기관순매수: ", reqObj.GetDataValue(19,i))
            print("\t기관누적순매수: ", reqObj.GetDataValue(20,i))
            print("\t등락주선: ", reqObj.GetDataValue(21,i))
            print("\t등락비율: ", reqObj.GetDataValue(22,i))
            print("\t예탁금: ", reqObj.GetDataValue(23,i))
            print("\t주식회전율: ", reqObj.GetDataValue(24,i))
            print("\t거래성립률: ", reqObj.GetDataValue(25,i))
            print("\t:대비부호(종목상태와 동일) ", codes.get_stock_status(chr(reqObj.GetDataValue(26,i))))
            
            print("\t==============")
    else:
        print("error = ", ret)

if __name__ == '__main__':
    getStockChart('A067160')

