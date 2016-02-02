from collections import Counter
class AnnualStats:
    def __init__(self, year_measure):
        self.year_measure = list(year_measure)
        print(self.year_measure)
        self.data = list(v for yr, v in self.year_measure)
        self.counter = Counter(self.data)

    def __repr__(self):
        return repr(self.year_measure)

    def min_year(self):
        return min(yr for yr, v in self.year_measure)

    def max_year(self):
        return max(yr for yr, v in self.year_measure)

    def mean(self):
        return sum(self.data)/len(self.data)

    def median(self):
        mid, odd = divmod(len(self.data), 2)
        if odd:
            return sorted(self.data)[mid]
        else:
            pair = sorted(self.data[mid-1:mid+1])
            return sum(pair)/2

    def mode(self):
        value, count = self.counter.most_common()[0]
        return value

if __name__ == "__main__":
    target = input("please insert data: (enter: default data)")
    if len(target) == 0:
        target = [(2000, 29.87), (2001, 30.12), (2002, 30.6), (2003, 30.66),
            (2004, 31.33), (2005, 32.62), (2006, 32.73), (2007, 33.5),
            (2008, 32.84), (2009, 33.02), (2010, 32.92), (2011, 33.27),
            (2012, 33.51)]


    # if you don't use eval function, input data will be accepted as string. It's not our intention.
    stats = AnnualStats(eval(target))
    print("target", stats)
    print("min_year", stats.min_year())
    print("max_year", stats.max_year())
    print("mean", stats.mean())
    print("median", stats.median())
    print("mode", stats.mode())
