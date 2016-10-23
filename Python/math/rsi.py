class RSI:
    aus = []
    ads = []
    days = 0
    au = 0
    ad = 0

    def __init__(self, aus, ads, days):
        assert(len(aus) >= days)
        assert(len(ads) >= days)

        self.aus = aus
        self.ads = ads
        self.days = days
        
        print("rsi")

    def cal(self):
        au = sum(aus) / len(aus)
        ad = sum(ads) / len(ads)
        
        print("au: %.1f, ad: %.1f" % (au, ad))

        rsi = round(au / (au + abs(ad)), 3)
        print("rsi: ", rsi)


if __name__ == "__main__":
    aus = [100, 300, 1500, 600, 0]
    ads = [0, 0, 0, 0, -1100]
    days = 5 
    
    rsi = RSI(aus, ads, days) 
    rsi.cal()
