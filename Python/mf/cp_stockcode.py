import win32com.client

def get_stock_code():
    instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
    print(instCpStockCode.GetCount())
    instCpStockCount = instCpStockCode.GetCount()

    for i in range(0, instCpStockCount):
        print("%d\t%s\t%s" % (i, instCpStockCode.GetData(0,i), instCpStockCode.GetData(1,i)))
        #print("code: ", instCpStockCode.GetData(0,i))
        #print("name: ", instCpStockCode.GetData(1,i))

if __name__ == '__main__':
    get_stock_code()

