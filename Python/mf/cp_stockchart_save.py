import win32com.client as wc
import datetime
from cp_codes import Codes
import datetime
import os

def get_code_dic(code):
    code_dic = {
        "0":"날짜",
        "1":"시간",
        "2":"고가",
        "3":"저가",
        "4":"저가",
        "5":"종가",
        "6":"전일대비",
        "7":"거래량",
        "8":"거래대금",
        "9":"누적체결매도수량",
        "10":"누적체결매수수량",
        "11":"상장주식수",
        "12":"시가총액",
        "13":"외국인주문한도수량",
        "14":"외국인주문가능수량",
        "15":"외국인현보유수량",
        "16":"외국인현보유비율",
        "17":"수정주가일자(YYYYMMDD)",
        "18":"수정주가비율",
        "19":"기관순매수",
        "20":"기관누적순매수",
        "21":"등락주선",
        "22":"등락비율",
        "23":"예탁금",
        "24":"주식회전율",
        "25":"거래성립률",
        "26":"대비부호"
    }
    return code_dic.get(code)

def getStockChart(code):
    print ("=== stockChart for", code, "===")

    today = datetime.datetime.now()
    yyyymmdd = today.strftime('%Y%m%d')
    start_date = today - datetime.timedelta(days=7)
    print(start_date)
    print(yyyymmdd)
    count = 20
    
    reqObj = wc.Dispatch("CpSysDib.StockChart")
    reqObj.SetInputValue(0, code)
    #reqObj.SetInputValue(1, '2')        # date
    #reqObj.SetInputValue(2, yyyymmdd)     # end date
    #reqObj.SetInputValue(3, start_date.strftime('%Y%m%d'))     # start date
    #reqObj.SetInputValue(6, ord('D'))        # day
    reqObj.SetInputValue(1, '1')        # count
    reqObj.SetInputValue(2, '0')        # lastest
    reqObj.SetInputValue(3, yyyymmdd)
    reqObj.SetInputValue(6, ord('m'))        # minute

    reqObj.SetInputValue(4, count)
    reqObj.SetInputValue(5, [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 37])
    reqObj.SetInputValue(9, '1')

    ret = reqObj.BlockRequest()

    if ret == 0:
        # success
        codes = Codes()
        dirname = os.path.dirname(__file__)
        fullpath = os.path.join(dirname, yyyymmdd+'_StockChart.csv')

        str_list = []
        with open(fullpath, 'w', encoding='utf-8') as f:
            #for i in range(0, 24):
                #str_list.append(reqObj.GetHeaderValue(i))
            header_list = []
            for i in range(0, 27):
                header_list.append(get_code_dic(str(i)))
            print(header_list)
            f.write('\t'.join(header_list))
            f.write('\n')

            num = reqObj.GetHeaderValue(3)
            print("received count: {}".format(num))
            for i in range(num):
                for j in range(0, 27):
                    str_list.append(str(reqObj.GetDataValue(j, i)))
                print(str_list)
                f.write('\t'.join(str_list))
                f.write('\n')
                del str_list[:]

    else:
        print("error = ", ret)

if __name__ == '__main__':
    print("code 1 means {}".format(get_code_dic("1")))
    getStockChart('A067160')

