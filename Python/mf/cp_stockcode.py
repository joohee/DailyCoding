import win32com.client
import os
import datetime

def get_code_name(instCpStockCode, today, filename, index_no=2):
    print(instCpStockCode.GetCount())
    instCpStockCount = instCpStockCode.GetCount()

    dirname = os.path.dirname(__file__)
    fullpath = os.path.join(dirname, today+'_'+filename)
    with open(fullpath, "w", encoding='utf-8') as f:
        for i in range(0, instCpStockCount):
            line = str(i)
            for idx in range(0, index_no):
                line += "\t{0}".format(instCpStockCode.GetData(idx, i))
            #f.write("%d\t%s\t%s\n" % (i, instCpStockCode.GetData(0,i), instCpStockCode.GetData(1,i)))
            f.write(line+"\n")

    print("saved...")

if __name__ == '__main__':
    today = datetime.datetime.now().strftime('%y%m%d')
    instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
    instCpFutureCode = win32com.client.Dispatch("CpUtil.CpFutureCode")
    instCpKFutureCode = win32com.client.Dispatch("CpUtil.CpKFutureCode")
    instCpOptionCode = win32com.client.Dispatch("CpUtil.CpOptionCode")
    instCpSoptionCode = win32com.client.Dispatch("CpUtil.CpSOptionCode")
    instCpElwCode = win32com.client.Dispatch("CpUtil.CpElwCode")

    get_code_name(instCpStockCode, today, 'stock_code_name.csv')
    get_code_name(instCpFutureCode, today, 'future_code_name.csv')
    get_code_name(instCpKFutureCode, today, 'kfuture_code_name.csv')
    get_code_name(instCpOptionCode, today, 'option_code_name.csv', 5)
    get_code_name(instCpSOptionCode, today, 'soption_code_name.csv', 5)
    get_code_name(instCpElwCode, today, 'elw_code_name.csv', 7)

