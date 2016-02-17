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

    def ex2(self):
        import os
        encoding = 'latin1'
        upath = os.path.expanduser('ch2_movielens/users.dat')
        rpath = os.path.expanduser('ch2_movielens/ratings.dat')
        mpath = os.path.expanduser('ch2_movielens/movies.dat')

        unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
        rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
        mnames = ['movie_id', 'title', 'genres']

        users = pd.read_csv(upath, sep='::', header=None, names=unames, encoding=encoding)
        ratings = pd.read_csv(rpath, sep='::', header=None, names=rnames, encoding=encoding)
        movies = pd.read_csv(mpath, sep='::', header=None, names=mnames, encoding=encoding)

        print(users[:5])
        print(ratings[:5])
        print(movies[:5])

        # 두 테이블 병합. 중복되는 열의 이름을 key로 사용한다. 
        data = pd.merge(pd.merge(ratings, users), movies)
        print(data[:10])
        print(data.ix[0])
        
        # 성별에 따른 영화의 평균 평점 정보 
        mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')
        print(mean_ratings[:5])

        # 제목 별 평점 정보 
        # size() 함수를 이용해서 Series 객체로 얻어냄. 
        ratings_by_title = data.groupby('title').size()
        print(ratings_by_title[:5])

        # 제목 별 평점 정보에서 250건 이상 평점 정보가 있는 영화만 추리기.
        active_titles = ratings_by_title.index[ratings_by_title >= 250]
        print(active_titles[:5])

        # 250 건 이상의 평점 정보가 있는 영화에 대한 색인은 mean_ratings에서 항목을 선택하기 위해 사용됨. 
        mean_ratings = mean_ratings.ix[active_titles]
        print(mean_ratings[:5])

        # 여성에게 높은 평점을 받은 영화 목록을 확인하기 위해 F열을 내림차순으로 정렬.
        top_female_ratings = mean_ratings.sort_values(by='F', ascending=False)
        print(top_female_ratings[:5])

        # 평균 평점의 차이에 따라 정렬하기 
        mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
        sorted_by_diff = mean_ratings.sort_values(by='diff')
        print(sorted_by_diff[:5])

        # 정렬된 행에서 역순으로 15개를 잘라낸다. 
        print(sorted_by_diff[::-1][:5])

        # 성별에 관계없이 영화에 대한 호불호가 극명하게 나뉘는 영화를 구한다. 
        # 평점의 표준편차
        ratings_std_by_title = data.groupby('title')['rating'].std()
        # active_titles 만 선택 
        ratings_std_by_title = ratings_std_by_title.ix[active_titles]
        print(ratings_std_by_title.sort_values(ascending=False)[:10])

    def ex3(self):
        names1880 = pd.read_csv('ch2_names/yob1880.txt', names=['name', 'sex', 'births'])
        print(names1880[:10])

        names1880.groupby('sex').births.sum()

        # 모든 데이터를 DataFrame 하나로 취합 후 year 항목을 추가한다. 
        years = range(1880, 2015)
        pieces = []
        columns = ['name', 'sex', 'births']
        
        for year in years:
            path = 'ch2_names/yob%d.txt' % year
            frame = pd.read_csv(path, names=columns)

            frame['year'] = year
            pieces.append(frame)

        # 모두 하나의 DataFrame으로 취합한다. 
        names = pd.concat(pieces, ignore_index=True)
        print(names[:10])

        total_births = names.pivot_table('births', index='year', columns='sex', aggfunc=sum)
        print(total_births.tail())

        # prop열을 추가해서 각 이름이 전체 출생수에서 차지하는 비율을 계산한다.
        # prop값이 0.02라면 100명중 2명의 이름이 같다는 뜻이다. 
        def add_prop(group):
            # Integer division floors
            births = group.births.astype(float)
            group['prop'] = births / births.sum()
            return group

        names = names.groupby(['year', 'sex']).apply(add_prop)
        print(names[:10])
    
        # 모든 그룹에서 prop열의 합이 1이 맞는지 확인하는 sanity check를 하는것이 좋다. 
        result = np.allclose(names.groupby(['year', 'sex']).prop.sum(), 1)
        print(result)

        def get_top1000(group):
            return group.sort_values(by='births', ascending=True)[:1000]

        grouped = names.groupby(['year', 'sex'])
        top1000 = grouped.apply(get_top1000)
        top1000.index = np.arange(len(top1000))
        print(top1000[:10])

        # 이름 유형 분석 
        boys = top1000[top1000.sex == 'M']
        girls = top1000[top1000.sex == 'F']

        # 연도별로 John이나 Mary라는 이름의 추이를 간단하게 그래프로 만들 수 있다. 
        # 그 전에 데이터를 약간 변경하도록 한다. 
        total_births = top1000.pivot_table('births', index='year', columns='name', aggfunc=sum)
        print(total_births.info())
        
        # %matplotlib inline - ipython에서 그래프를 보여주기 위한 예약 함수. 
        subset = total_births[['John', 'Harry', 'Mary', 'Marilyn']]
        # .plot 함수는 그래프를 그려주지만 console에서는 안되는 듯 하다. 
        subset.plot(subplots=True, figsize=(12,10), grid=False, title="Number of births per year")



if __name__ == "__main__":
    pfda = PfDA()
    #pfda.ex1()
    #pfda.ex2()
    pfda.ex3()


