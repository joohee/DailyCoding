from os import listdir
from os.path import isfile, join, basename, splitext

class StockItem(object):
    code = ''
    name = ''
    date = ''
    time = ''
    sprice = 0 
    hprice = 0  
    lprice = 0 
    eprice = 0 
    delta = 0
    amount = 0
    def __init__(self, arys):
        if (len(arys) == 10):
            self.code = arys[0]
            self.name = arys[1]
            self.date = arys[2]
            self.time = arys[3]
            self.sprice = arys[4]
            self.hprice = arys[5]
            self.price = arys[6]
            self.eprice = arys[7]
            self.delta = int(arys[8])
            self.amount = int(arys[9])
        else:
            raise Exception("argument is wrong")

    def __str__(self):
        return "delta={}".format(self.delta)


if __name__ == "__main__":
    print("with rsi")
    mypath = "."
    #files = [f for f in listdir(mypath) if isfile(join(mypath, f) and basename(f).lower().endswith('.csv'))]
    files = [f for f in listdir(mypath) if basename(f).lower().endswith('.csv')]
    #kfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    min_index = 3
    max_index = 29

    for f in files:
        print(basename(f))

        count = 0
        with open(f, 'r', encoding="utf-8") as fp:
            code = splitext(f)[0]
            results = [] 

            with open('result_'+code+'.csv2', 'w', encoding="utf-8") as wf:
                updowns = []
                for line in reversed(fp.readlines()):
                    item = line.split('\t')
                    target = item[0:10]
		
                    if item[0] == code:
                        stockItem = StockItem(target)
                        updowns.insert(0, stockItem.delta)
	                #print("updowns: ", updowns)
	
                        if len(updowns) >= min_index:
                            for idx in range(min_index, len(updowns)+1):
                                if idx > max_index:
                                    break 
                                
                                ups = [i for i in updowns[0:idx] if i > 0]
                                downs = [i for i in updowns[0:idx] if i < 0]
	                        #print("idx: ", idx)
	                        #print("\tups: %s, sum(ups): %d" % (ups, sum(ups)))
	                        #print("\tdowns: %s, sum(downs): %d" % (downs, sum(downs))) 
                                au = round(sum(ups)/idx, 2)
                                ad = round(sum(downs)/idx, 2)
                                rsi = 0
                                try:
                                    rsi = round(100*au/(au+abs(ad)), 2)
                                except ZeroDivisionError:
                                    print("sum is zero...")
	
	                        #print("idx: %d, au: %f, ad: %f, rsi: %f" % (idx, au, ad, rsi))
                                target.append(str(au))
                                target.append(str(ad))
                                target.append(str(rsi))

                            #print("\t".join(target))
                            #wf.write("\t".join(target))
                            #wf.write("\n")
                        else:
                            print("len(updowns) is %d, pass..." % len(updowns))

                        #wf.write("\t".join(target))
                        #wf.write("\n")
                        results.append("\t".join(target)+"\n")
                        
                    else:
                        for i in range(3, 30):
                            target.append("AU"+str(i))
                            target.append("AD"+str(i))
                            target.append("RSI"+str(i))

                        #print(target)
                        #wf.write("\t".join(target))
                        #wf.write("\n")
                        results.insert(0, "\t".join(target) + "\n")
                        
                   #print(target)
                wf.writelines(results)
                results.clear()
                   #wf.write('\n')

