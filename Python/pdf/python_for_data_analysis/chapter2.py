import json
from collections import Counter
import numpy as np
from pandas import DataFrame, Series
import pandas as pd

class PfDA():
    def __init__(self):
        pass

    def ex1(self):
        # data from http://developer.usa.gov/1usagov
        path = '1usagov.1'
        records = [json.loads(rec) for rec in open(path)]
        #print(records[:5])

        time_zones = [rec['tz'] for rec in records if 'tz' in rec]
        #print(time_zones[:5])
    
        counts = Counter(time_zones)
        #print(counts.most_common())

        frame = DataFrame(records)
        #print(frame.info())

        # %matplotlib info -> only in ipython notebook
        clean_tz = frame['tz'].fillna('Missing')
        clean_tz[clean_tz == ''] = 'Unknown'
        tz_counts = clean_tz.value_counts()
        #print(tz_counts)

        results = Series([x.split()[0] for x in frame.a.dropna()])
        #print(results[:5])
        #print(results.value_counts()[:8])

        cframe = frame[frame.a.notnull()]
        #print(cframe)           # show like a table

        operating_system = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')
        #print(operating_system)

        by_tz_os = cframe.groupby(['tz', operating_system])
        agg_counts = by_tz_os.size().unstack().fillna(0)
        print(agg_counts[:10])

        # sort ascending.
        indexer = agg_counts.sum(1).argsort()
        print(indexer[:10])

        count_subset = agg_counts.take(indexer)[-10:]
        print(count_subset)

        # graph
        count_subset.plot(kind='barh', stacked=True)
        #count_subset.plot(kind='barh', stacked=True)    # notebook can show the graph only.

        normed_subset = count_subset.div(count_subset.sum(1), axis=0)
        # normed_subset.plot(kind='barh', stacked=True)         # notebook can show the graph only.

if __name__ == "__main__":
    pfda = PfDA()
    pfda.ex1()


