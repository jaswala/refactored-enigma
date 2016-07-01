>>> import numpy as np
>>> import pandas as pd
>>> 
>>> from pandas import Series, DataFrame
>>> 
>>> import webbrowser
>>> website = 'https://en.wikipedia.org/wiki/NFL_win%E2%80%93loss_records'
>>> 
>>> webbrowser.open(website)
True
>>> 
>>> nfl_frame = pd.read_clipboard()
>>> 
>>> nfl_frame
   Rank                  Team  Won  Lost  Tied   Pct.  First NFL Season  \
0     1         Chicago Bears  741   555    42  0.570              1920   
1     2        Dallas Cowboys  480   364     6  0.568              1960   
2     3     Green Bay Packers  720   547    37  0.566              1921   
3     4        Miami Dolphins  429   335     4  0.561              1966   
4     5  New England Patriots  462   381     9  0.548              1960   

  Total Games   Division  
0       1,338  NFC North  
1         850   NFC East  
2       1,304  NFC North  
3         768   AFC East  
4         852   AFC East  
>>> 
>>> help(pandas)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'pandas' is not defined
>>> 
>>> nfl_frame.columns
Index([u'Rank', u'Team', u'Won', u'Lost', u'Tied', u'Pct.',
       u'First NFL Season', u'Total Games', u'Division'],
      dtype='object')
>>> 
>>> nfl_frame.Rank
0    1
1    2
2    3
3    4
4    5
Name: Rank, dtype: int64
>>> 
>>> nfl_frame.Team
0           Chicago Bears
1          Dallas Cowboys
2       Green Bay Packers
3          Miami Dolphins
4    New England Patriots
Name: Team, dtype: object
>>> 
>>> nfl_frame['First Season']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/pandas/core/frame.py", line 1992, in __getitem__
    return self._getitem_column(key)
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/pandas/core/frame.py", line 1999, in _getitem_column
    return self._get_item_cache(key)
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/pandas/core/generic.py", line 1345, in _get_item_cache
    values = self._data.get(item)
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/pandas/core/internals.py", line 3225, in get
    loc = self.items.get_loc(item)
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/pandas/indexes/base.py", line 1878, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas/index.pyx", line 137, in pandas.index.IndexEngine.get_loc (pandas/index.c:4027)
  File "pandas/index.pyx", line 157, in pandas.index.IndexEngine.get_loc (pandas/index.c:3891)
  File "pandas/hashtable.pyx", line 675, in pandas.hashtable.PyObjectHashTable.get_item (pandas/hashtable.c:12408)
  File "pandas/hashtable.pyx", line 683, in pandas.hashtable.PyObjectHashTable.get_item (pandas/hashtable.c:12359)
KeyError: 'First Season'
>>> nfl_frame['First NFL Season']
0    1920
1    1960
2    1921
3    1966
4    1960
Name: First NFL Season, dtype: int64

>>> import numpy as np
>>> import pandas as pd
>>> from pandas import Series, DataFrame
>>> 
>>> nfl_frame = pd.read_clipboard()
>>> nfl_frame
   Rank                  Team  Won  Lost  Tied   Pct.  First NFL Season  \
0     1         Chicago Bears  741   555    42  0.570              1920   
1     2        Dallas Cowboys  480   364     6  0.568              1960   
2     3     Green Bay Packers  720   547    37  0.566              1921   
3     4        Miami Dolphins  429   335     4  0.561              1966   
4     5  New England Patriots  462   381     9  0.548              1960   

  Total Games   Division  
0       1,338  NFC North  
1         850   NFC East  
2       1,304  NFC North  
3         768   AFC East  
4         852   AFC East  
>>> 
>>> 
>>> nfl_frame.columns
Index([u'Rank', u'Team', u'Won', u'Lost', u'Tied', u'Pct.',
       u'First NFL Season', u'Total Games', u'Division'],
      dtype='object')
>>> nfl_frame.Ranke
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/pandas/core/generic.py", line 2669, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'Ranke'
>>> nfl_frame.Rank
0    1
1    2
2    3
3    4
4    5
Name: Rank, dtype: int64
>>> 
>>> DataFrame(nfl_frame, columns=['Team','Rank', 'Total Games']
... 
... )
                   Team  Rank Total Games
0         Chicago Bears     1       1,338
1        Dallas Cowboys     2         850
2     Green Bay Packers     3       1,304
3        Miami Dolphins     4         768
4  New England Patriots     5         852
>>> 
>>> DataFrame(nfl_frame, columns=['Team','Rank', 'Total Games'])
                   Team  Rank Total Games
0         Chicago Bears     1       1,338
1        Dallas Cowboys     2         850
2     Green Bay Packers     3       1,304
3        Miami Dolphins     4         768
4  New England Patriots     5         852
>>> 
>>> 
>>> DataFrame(nfl_frame, columns=['Team','Rank', 'Total Games', 'Stadium'])
                   Team  Rank Total Games  Stadium
0         Chicago Bears     1       1,338      NaN
1        Dallas Cowboys     2         850      NaN
2     Green Bay Packers     3       1,304      NaN
3        Miami Dolphins     4         768      NaN
4  New England Patriots     5         852      NaN
>>> 
>>> 
>>> nfl_frame.head()
   Rank                  Team  Won  Lost  Tied   Pct.  First NFL Season  \
0     1         Chicago Bears  741   555    42  0.570              1920   
1     2        Dallas Cowboys  480   364     6  0.568              1960   
2     3     Green Bay Packers  720   547    37  0.566              1921   
3     4        Miami Dolphins  429   335     4  0.561              1966   
4     5  New England Patriots  462   381     9  0.548              1960   

  Total Games   Division  
0       1,338  NFC North  
1         850   NFC East  
2       1,304  NFC North  
3         768   AFC East  
4         852   AFC East  
>>> nfl_frame.tail()
   Rank                  Team  Won  Lost  Tied   Pct.  First NFL Season  \
0     1         Chicago Bears  741   555    42  0.570              1920   
1     2        Dallas Cowboys  480   364     6  0.568              1960   
2     3     Green Bay Packers  720   547    37  0.566              1921   
3     4        Miami Dolphins  429   335     4  0.561              1966   
4     5  New England Patriots  462   381     9  0.548              1960   

  Total Games   Division  
0       1,338  NFC North  
1         850   NFC East  
2       1,304  NFC North  
3         768   AFC East  
4         852   AFC East  
>>> 
>>> nfl_frame.tail(3P)
  File "<stdin>", line 1
    nfl_frame.tail(3P)
                    ^
SyntaxError: invalid syntax
>>> nfl_frame.tail(3)
   Rank                  Team  Won  Lost  Tied   Pct.  First NFL Season  \
2     3     Green Bay Packers  720   547    37  0.566              1921   
3     4        Miami Dolphins  429   335     4  0.561              1966   
4     5  New England Patriots  462   381     9  0.548              1960   

  Total Games   Division  
2       1,304  NFC North  
3         768   AFC East  
4         852   AFC East  
>>> 
>>> 
>>> 
>>> nfl_frame.ix[2] # using index to call values
Rank                                3
Team                Green Bay Packers
Won                               720
Lost                              547
Tied                               37
Pct.                            0.566
First NFL Season                 1921
Total Games                     1,304
Division                    NFC North
Name: 2, dtype: object
>>> 
>>> nfl_frame.ix[3] # using index to call values
Rank                             4
Team                Miami Dolphins
Won                            429
Lost                           335
Tied                             4
Pct.                         0.561
First NFL Season              1966
Total Games                    768
Division                  AFC East
Name: 3, dtype: object
>>> 
>>> nfl_frame['Stadium'] = "Levi's Stadium"
>>> 
>>> nfl_frame
   Rank                  Team  Won  Lost  Tied   Pct.  First NFL Season  \
0     1         Chicago Bears  741   555    42  0.570              1920   
1     2        Dallas Cowboys  480   364     6  0.568              1960   
2     3     Green Bay Packers  720   547    37  0.566              1921   
3     4        Miami Dolphins  429   335     4  0.561              1966   
4     5  New England Patriots  462   381     9  0.548              1960   

  Total Games   Division         Stadium  
0       1,338  NFC North  Levi's Stadium  
1         850   NFC East  Levi's Stadium  
2       1,304  NFC North  Levi's Stadium  
3         768   AFC East  Levi's Stadium  
4         852   AFC East  Levi's Stadium  
>>> 
>>> nfl_frame['Stadium'] = np.arange(6)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/pandas/core/frame.py", line 2348, in __setitem__
    self._set_item(key, value)
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/pandas/core/frame.py", line 2414, in _set_item
    value = self._sanitize_column(key, value)
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/pandas/core/frame.py", line 2572, in _sanitize_column
    value = _sanitize_index(value, self.index, copy=False)
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/pandas/core/series.py", line 2821, in _sanitize_index
    raise ValueError('Length of values does not match length of ' 'index')
ValueError: Length of values does not match length of index
>>> 
>>> nfl_frame['Stadium'] = np.arange(5)
>>> 
>>> nfl_frame['Stadium'] = np.arange(5) # passing value to statidum
>>> 
>>> nfl_frame
   Rank                  Team  Won  Lost  Tied   Pct.  First NFL Season  \
0     1         Chicago Bears  741   555    42  0.570              1920   
1     2        Dallas Cowboys  480   364     6  0.568              1960   
2     3     Green Bay Packers  720   547    37  0.566              1921   
3     4        Miami Dolphins  429   335     4  0.561              1966   
4     5  New England Patriots  462   381     9  0.548              1960   

  Total Games   Division  Stadium  
0       1,338  NFC North        0  
1         850   NFC East        1  
2       1,304  NFC North        2  
3         768   AFC East        3  
4         852   AFC East        4  
>>> 
>>> stadiums = Series(["Levi's Stadium", "ATT Stadium"], index[5,0])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'index' is not defined
>>> stadiums = Series(["Levi's Stadium", "ATT Stadium"], index[5,0])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'index' is not defined
>>> stadiums = Series(["Levi's Stadium", "ATT Stadium"], index=[5,0])
>>> 
>>> stadiums
5    Levi's Stadium
0       ATT Stadium
dtype: object
>>> 
>>> nfl_frame['Stadium'] = stadiums
>>> 
>>> nfl_frame
   Rank                  Team  Won  Lost  Tied   Pct.  First NFL Season  \
0     1         Chicago Bears  741   555    42  0.570              1920   
1     2        Dallas Cowboys  480   364     6  0.568              1960   
2     3     Green Bay Packers  720   547    37  0.566              1921   
3     4        Miami Dolphins  429   335     4  0.561              1966   
4     5  New England Patriots  462   381     9  0.548              1960   

  Total Games   Division      Stadium  
0       1,338  NFC North  ATT Stadium  
1         850   NFC East          NaN  
2       1,304  NFC North          NaN  
3         768   AFC East          NaN  
4         852   AFC East          NaN  
>>> 
>>> 
>>> stadiums = Series(["Levi's Stadium", "ATT Stadium"], index=[4,0])
>>> 
>>> nfl_frame['Stadium'] = stadiums
>>> 
>>> nfl_frame
   Rank                  Team  Won  Lost  Tied   Pct.  First NFL Season  \
0     1         Chicago Bears  741   555    42  0.570              1920   
1     2        Dallas Cowboys  480   364     6  0.568              1960   
2     3     Green Bay Packers  720   547    37  0.566              1921   
3     4        Miami Dolphins  429   335     4  0.561              1966   
4     5  New England Patriots  462   381     9  0.548              1960   

  Total Games   Division         Stadium  
0       1,338  NFC North     ATT Stadium  
1         850   NFC East             NaN  
2       1,304  NFC North             NaN  
3         768   AFC East             NaN  
4         852   AFC East  Levi's Stadium  
>>> 
>>> 
>>> del nfl_frame['Stadium']
>>> del nfl_frame['Stadium'] # delting column
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/pandas/core/generic.py", line 1601, in __delitem__
    self._data.delete(key)
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/pandas/core/internals.py", line 3284, in delete
    indexer = self.items.get_loc(item)
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/pandas/indexes/base.py", line 1878, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas/index.pyx", line 137, in pandas.index.IndexEngine.get_loc (pandas/index.c:4027)
  File "pandas/index.pyx", line 157, in pandas.index.IndexEngine.get_loc (pandas/index.c:3891)
  File "pandas/hashtable.pyx", line 675, in pandas.hashtable.PyObjectHashTable.get_item (pandas/hashtable.c:12408)
  File "pandas/hashtable.pyx", line 683, in pandas.hashtable.PyObjectHashTable.get_item (pandas/hashtable.c:12359)
KeyError: 'Stadium'
>>> 
>>> nfl_frame
   Rank                  Team  Won  Lost  Tied   Pct.  First NFL Season  \
0     1         Chicago Bears  741   555    42  0.570              1920   
1     2        Dallas Cowboys  480   364     6  0.568              1960   
2     3     Green Bay Packers  720   547    37  0.566              1921   
3     4        Miami Dolphins  429   335     4  0.561              1966   
4     5  New England Patriots  462   381     9  0.548              1960   

  Total Games   Division  
0       1,338  NFC North  
1         850   NFC East  
2       1,304  NFC North  
3         768   AFC East  
4         852   AFC East  
>>> 
>>> 
>>> data = {'City':[ 'SF','LA','NYC'], 'Popluation':[837000,3888800,8400000]}
>>> 
>>> 
>>> data = {'City':[ 'SF','LA','NYC'], 'Popluation':[837000,3888800,8400000]} # Dict 
>>> 
>>> data
{'City': ['SF', 'LA', 'NYC'], 'Popluation': [837000, 3888800, 8400000]}
>>> 
>>> city_frame = DataFrame(data)
>>> 
>>> city_frame
  City  Popluation
0   SF      837000
1   LA     3888800
2  NYC     8400000
>>> 
>>> # contrcuted data fraome from dict
... 
>>> 
>>> # http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html
... 
>>> 
>>> # more library from pandas dataframe look up the link http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html
... 
>>> 

>>> import numpy as np
>>> import pandas
>>> import pandas as pd
>>> from pandas import Series, DataFrame
>>> 
>>> ## index objects
... 
>>> 
>>> my_ser = Series([1,2,3,4], index=['A','B','C','D'])
>>> 
>>> my_ser
A    1
B    2
C    3
D    4
dtype: int64
>>> 
>>> my_index = myserie.index
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'myserie' is not defined
>>> 
>>> my_index = myseries.index
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'myseries' is not defined
>>> my_index = myser.index
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'myser' is not defined
>>> my_index = my_ser.index
>>> my_index
Index([u'A', u'B', u'C', u'D'], dtype='object')
>>> 
>>> 
>>> my_index[2]
'C'
>>> 
>>> my_index[2:]
Index([u'C', u'D'], dtype='object')
>>> 
>>> my_index[0]
'A'
>>> 
>>> my_index[0] = 'Z'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/pandas/indexes/base.py", line 1237, in __setitem__
    raise TypeError("Index does not support mutable operations")
TypeError: Index does not support mutable operations
>>> 
>>> # CANT CHANGE THE INDEX ; IMMUTABLE
... 
>>> 
>>>  ## RE-INDEXING
... 
>>> import numpy as np
>>> from pandas import Series, DataFrame
>>> 
>>> import pandas as pd
>>> 
>>> from numpy.radom import randn
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named radom
>>> 
>>> from numpy.random import randn
>>> 
>>> 
>>> seri = Series([1,2,3,4], index=['A','B','C','D'])
>>> 
>>> seri
A    1
B    2
C    3
D    4
dtype: int64
>>> 
>>> ser2 = ser1.reindex(['A','B','C','D','E','F'))
  File "<stdin>", line 1
    ser2 = ser1.reindex(['A','B','C','D','E','F'))
                                                ^
SyntaxError: invalid syntax
>>> ser2 = ser1.reindex(['A','B','C','D','E','F'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ser1' is not defined
>>> 
>>> ser2 = seri.reindex(['A','B','C','D','E','F'])
>>> 
>>> ser2
A    1.0
B    2.0
C    3.0
D    4.0
E    NaN
F    NaN
dtype: float64
>>> 
>>> seri.reindex(['A','B','C','D','E','F','G'], fill_value=0)
A    1
B    2
C    3
D    4
E    0
F    0
G    0
dtype: int64
>>> ser2.reindex(['A','B','C','D','E','F','G'], fill_value=0)
A    1.0
B    2.0
C    3.0
D    4.0
E    NaN
F    NaN
G    0.0
dtype: float64
>>> 
>>> ser3= Series(['USA','Mexico','Canada'],index=[0,5,10])
>>> 
>>> ser3
0        USA
5     Mexico
10    Canada
dtype: object
>>> 
>>> ranger = range(15)
>>> ranger
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
>>> 
>>> ser3.reindex(ranger,method='ffill') # forward fill reindex with previous values
0        USA
1        USA
2        USA
3        USA
4        USA
5     Mexico
6     Mexico
7     Mexico
8     Mexico
9     Mexico
10    Canada
11    Canada
12    Canada
13    Canada
14    Canada
dtype: object
>>> 
>>> 
>>> dframe = DataFrame(randn(25).reshape((5,5)), index=['A','B','D','E','F'], columns=['col1','col2',col3','col4',col5'])
  File "<stdin>", line 1
    dframe = DataFrame(randn(25).reshape((5,5)), index=['A','B','D','E','F'], columns=['col1','col2',col3','col4',col5'])
                                                                                                           ^
SyntaxError: invalid syntax
>>> 
>>> dframe = DataFrame(randn(25).reshape((5,5)), index=['A','B','D','E','F'], columns=['col1','col2','col3','col4',col5'])
  File "<stdin>", line 1
    dframe = DataFrame(randn(25).reshape((5,5)), index=['A','B','D','E','F'], columns=['col1','col2','col3','col4',col5'])
                                                                                                                         ^
SyntaxError: EOL while scanning string literal
>>> 
>>> dframe = DataFrame(randn(25).reshape((5,5)), index=['A','B','D','E','F'], columns=['col1','col2','col3','col4','col5'])
>>> 
>>> dframe
       col1      col2      col3      col4      col5
A  0.947795  1.021343 -0.706050 -0.234731  0.120617
B  0.259542  0.110539  0.821890 -0.480243 -0.348446
D -0.598554  0.454436 -0.413844 -1.090275 -1.721833
E -2.490846 -0.114459 -2.058151  0.795029 -0.460813
F -1.405506 -0.119085 -0.843312  0.253352 -0.293726
>>> 
>>> dframe2=dframe.reindex(['A','B','C','D','E','F'])
>>> 
>>> dframe2
       col1      col2      col3      col4      col5
A  0.947795  1.021343 -0.706050 -0.234731  0.120617
B  0.259542  0.110539  0.821890 -0.480243 -0.348446
C       NaN       NaN       NaN       NaN       NaN
D -0.598554  0.454436 -0.413844 -1.090275 -1.721833
E -2.490846 -0.114459 -2.058151  0.795029 -0.460813
F -1.405506 -0.119085 -0.843312  0.253352 -0.293726
>>> 
>>> new_columns= ['col1','col2','col3','col4','col5','col6')
  File "<stdin>", line 1
    new_columns= ['col1','col2','col3','col4','col5','col6')
                                                           ^
SyntaxError: invalid syntax
>>> 
>>> new_columns= ['col1','col2','col3','col4','col5','col6']
>>> 
>>> dframe2.reindex(columns=new_columns)
       col1      col2      col3      col4      col5  col6
A  0.947795  1.021343 -0.706050 -0.234731  0.120617   NaN
B  0.259542  0.110539  0.821890 -0.480243 -0.348446   NaN
C       NaN       NaN       NaN       NaN       NaN   NaN
D -0.598554  0.454436 -0.413844 -1.090275 -1.721833   NaN
E -2.490846 -0.114459 -2.058151  0.795029 -0.460813   NaN
F -1.405506 -0.119085 -0.843312  0.253352 -0.293726   NaN
>>> 
>>> dframe
       col1      col2      col3      col4      col5
A  0.947795  1.021343 -0.706050 -0.234731  0.120617
B  0.259542  0.110539  0.821890 -0.480243 -0.348446
D -0.598554  0.454436 -0.413844 -1.090275 -1.721833
E -2.490846 -0.114459 -2.058151  0.795029 -0.460813
F -1.405506 -0.119085 -0.843312  0.253352 -0.293726
>>> 
>>> dframe.ix[['A','B','C','D','E','F'], new_columns]
       col1      col2      col3      col4      col5  col6
A  0.947795  1.021343 -0.706050 -0.234731  0.120617   NaN
B  0.259542  0.110539  0.821890 -0.480243 -0.348446   NaN
C       NaN       NaN       NaN       NaN       NaN   NaN
D -0.598554  0.454436 -0.413844 -1.090275 -1.721833   NaN
E -2.490846 -0.114459 -2.058151  0.795029 -0.460813   NaN
F -1.405506 -0.119085 -0.843312  0.253352 -0.293726   NaN
>>> 


>>> ## lecture 18
... 
>>> ## Drop Entries
... 
>>> 
>>> import numpy as np
>>> import pandas 
>>> import pandas as pd
>>> 
>>> from pandas import Series, DataFrame
>>> 
>>> ser1 = Series(np.arange(3), index=['a','b','c'])
>>> 
>>> ser1
a    0
b    1
c    2
dtype: int64
>>> 
>>> 
>>> ser1.drop('b')
a    0
c    2
dtype: int64
>>> 
>>> 
>>> dframe1 = DataFrame(np.arange(9).reshape((3,3)), index=['SF','LA','NYC'], columns=['pop','size','year'])
>>> 
>>> dframe1
     pop  size  year
SF     0     1     2
LA     3     4     5
NYC    6     7     8
>>> 
>>> 
>>> dframe1.drop('LA')
     pop  size  year
SF     0     1     2
NYC    6     7     8
>>> 
>>> 
>>> dframe1
     pop  size  year
SF     0     1     2
LA     3     4     5
NYC    6     7     8
>>> 
>>> dframe2 = dframe1.drop('LA')
>>> 
>>> dframe2
     pop  size  year
SF     0     1     2
NYC    6     7     8
>>> 
>>> 
>>> dframe1.drop('year', axis=1)
     pop  size
SF     0     1
LA     3     4
NYC    6     7
>>> 



>>> ## lecture 18
... 
>>> ## Drop Entries
... 
>>> 
>>> import numpy as np
>>> import pandas 
>>> import pandas as pd
>>> 
>>> from pandas import Series, DataFrame
>>> 
>>> ser1 = Series(np.arange(3), index=['a','b','c'])
>>> 
>>> ser1
a    0
b    1
c    2
dtype: int64
>>> 
>>> 
>>> ser1.drop('b')
a    0
c    2
dtype: int64
>>> 
>>> 
>>> dframe1 = DataFrame(np.arange(9).reshape((3,3)), index=['SF','LA','NYC'], columns=['pop','size','year'])
>>> 
>>> dframe1
     pop  size  year
SF     0     1     2
LA     3     4     5
NYC    6     7     8
>>> 
>>> 
>>> dframe1.drop('LA')
     pop  size  year
SF     0     1     2
NYC    6     7     8
>>> 
>>> 
>>> dframe1
     pop  size  year
SF     0     1     2
LA     3     4     5
NYC    6     7     8
>>> 
>>> dframe2 = dframe1.drop('LA')
>>> 
>>> dframe2
     pop  size  year
SF     0     1     2
NYC    6     7     8
>>> 
>>> 
>>> dframe1.drop('year', axis=1)
     pop  size
SF     0     1
LA     3     4
NYC    6     7
>>> 
>>> 
>>> 
>>> quit()
sea-jaswala-m:~ jaswala$ 
sea-jaswala-m:~ jaswala$ 
sea-jaswala-m:~ jaswala$ python
Python 2.7.11 |Anaconda 4.0.0 (x86_64)| (default, Dec  6 2015, 18:57:58) 
[GCC 4.2.1 (Apple Inc. build 5577)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
Anaconda is brought to you by Continuum Analytics.
Please check out: http://continuum.io/thanks and https://anaconda.org
>>> 
>>> 
>>> import numpy as np
>>> import pandas as pd
>>> from pandas import Series, DataFrame
>>> 
>>> ser1 = Series(np.arange(3), index=['A','B','C'])
>>> 
>>> ser1
A    0
B    1
C    2
dtype: int64
>>> 
>>> 
>>> ser1 = 2*ser1
>>> 
>>> ser1
A    0
B    2
C    4
dtype: int64
>>> 
>>> ser1
A    0
B    2
C    4
dtype: int64
>>> 
>>> ser1['B']
2
>>> 
>>> ser1[1]
2
>>> ser1[0:3]
A    0
B    2
C    4
dtype: int64
>>> 
>>> 
>>> ser1[['A','B']]
A    0
B    2
dtype: int64
>>> 
>>> ser1[ser1>3]
C    4
dtype: int64
>>> ser1[ser1>3] = 10
>>> 
>>> dframe = DataFrame(np.arange(25).reshape((5,5)), index=['nyc','la','sf','dc','chi'], columns=['A','B','C','D','E'])
>>> 
>>> dframe
      A   B   C   D   E
nyc   0   1   2   3   4
la    5   6   7   8   9
sf   10  11  12  13  14
dc   15  16  17  18  19
chi  20  21  22  23  24
>>> 
>>> 
>>> 
>>> 
>>> dframe['B']
nyc     1
la      6
sf     11
dc     16
chi    21
Name: B, dtype: int64
>>> 
>>> 
>>> dframe['B','C']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/pandas/core/frame.py", line 1992, in __getitem__
    return self._getitem_column(key)
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/pandas/core/frame.py", line 1999, in _getitem_column
    return self._get_item_cache(key)
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/pandas/core/generic.py", line 1345, in _get_item_cache
    values = self._data.get(item)
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/pandas/core/internals.py", line 3225, in get
    loc = self.items.get_loc(item)
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/pandas/indexes/base.py", line 1878, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas/index.pyx", line 137, in pandas.index.IndexEngine.get_loc (pandas/index.c:4027)
  File "pandas/index.pyx", line 157, in pandas.index.IndexEngine.get_loc (pandas/index.c:3891)
  File "pandas/hashtable.pyx", line 675, in pandas.hashtable.PyObjectHashTable.get_item (pandas/hashtable.c:12408)
  File "pandas/hashtable.pyx", line 683, in pandas.hashtable.PyObjectHashTable.get_item (pandas/hashtable.c:12359)
KeyError: ('B', 'C')
>>> 
>>> 
>>> dframe[['B','C']]
      B   C
nyc   1   2
la    6   7
sf   11  12
dc   16  17
chi  21  22
>>> 
>>> 
>>> dframe[dframe['C']>8
... 
... 
... 
... 
... 
... L
  File "<stdin>", line 7
    L
    ^
SyntaxError: invalid syntax
>>> 
>>> dframe[dframe['C']>8]
      A   B   C   D   E
sf   10  11  12  13  14
dc   15  16  17  18  19
chi  20  21  22  23  24
>>> 
>>> 
>>> ## GIVES ALL VALUE WHERE C >8 IN ALL ROWS
... 
>>> 
>>> dframe
      A   B   C   D   E
nyc   0   1   2   3   4
la    5   6   7   8   9
sf   10  11  12  13  14
dc   15  16  17  18  19
chi  20  21  22  23  24
>>> 
>>> dframe >10
         A      B      C      D      E
nyc  False  False  False  False  False
la   False  False  False  False  False
sf   False   True   True   True   True
dc    True   True   True   True   True
chi   True   True   True   True   True
>>> 
>>> 
>>> 
>>> dframe.ix['LA']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/pandas/core/indexing.py", line 78, in __getitem__
    return self._getitem_axis(key, axis=0)
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/pandas/core/indexing.py", line 1014, in _getitem_axis
    return self._get_label(key, axis=axis)
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/pandas/core/indexing.py", line 93, in _get_label
    return self.obj._xs(label, axis=axis)
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/pandas/core/generic.py", line 1744, in xs
    loc = self.index.get_loc(key)
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/pandas/indexes/base.py", line 1878, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas/index.pyx", line 137, in pandas.index.IndexEngine.get_loc (pandas/index.c:4027)
  File "pandas/index.pyx", line 157, in pandas.index.IndexEngine.get_loc (pandas/index.c:3891)
  File "pandas/hashtable.pyx", line 675, in pandas.hashtable.PyObjectHashTable.get_item (pandas/hashtable.c:12408)
  File "pandas/hashtable.pyx", line 683, in pandas.hashtable.PyObjectHashTable.get_item (pandas/hashtable.c:12359)
KeyError: 'LA'
>>> 
>>> 
>>> dframe.ix['LA']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/pandas/core/indexing.py", line 78, in __getitem__
    return self._getitem_axis(key, axis=0)
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/pandas/core/indexing.py", line 1014, in _getitem_axis
    return self._get_label(key, axis=axis)
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/pandas/core/indexing.py", line 93, in _get_label
    return self.obj._xs(label, axis=axis)
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/pandas/core/generic.py", line 1744, in xs
    loc = self.index.get_loc(key)
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/pandas/indexes/base.py", line 1878, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas/index.pyx", line 137, in pandas.index.IndexEngine.get_loc (pandas/index.c:4027)
  File "pandas/index.pyx", line 157, in pandas.index.IndexEngine.get_loc (pandas/index.c:3891)
  File "pandas/hashtable.pyx", line 675, in pandas.hashtable.PyObjectHashTable.get_item (pandas/hashtable.c:12408)
  File "pandas/hashtable.pyx", line 683, in pandas.hashtable.PyObjectHashTable.get_item (pandas/hashtable.c:12359)
KeyError: 'LA'
>>> dframe.ix['la']
A    5
B    6
C    7
D    8
E    9
Name: la, dtype: int64
>>> 
>>> 
>>> dframe.ix['1']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/pandas/core/indexing.py", line 78, in __getitem__
    return self._getitem_axis(key, axis=0)
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/pandas/core/indexing.py", line 1014, in _getitem_axis
    return self._get_label(key, axis=axis)
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/pandas/core/indexing.py", line 93, in _get_label
    return self.obj._xs(label, axis=axis)
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/pandas/core/generic.py", line 1744, in xs
    loc = self.index.get_loc(key)
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/pandas/indexes/base.py", line 1878, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas/index.pyx", line 137, in pandas.index.IndexEngine.get_loc (pandas/index.c:4027)
  File "pandas/index.pyx", line 157, in pandas.index.IndexEngine.get_loc (pandas/index.c:3891)
  File "pandas/hashtable.pyx", line 675, in pandas.hashtable.PyObjectHashTable.get_item (pandas/hashtable.c:12408)
  File "pandas/hashtable.pyx", line 683, in pandas.hashtable.PyObjectHashTable.get_item (pandas/hashtable.c:12359)
KeyError: '1'
>>> dframe.ix[1]
A    5
B    6
C    7
D    8
E    9
Name: la, dtype: int64


>>> ##lecture 20
... 
>>> data alignment
  File "<stdin>", line 1
    data alignment
                 ^
SyntaxError: invalid syntax
>>> 
>>> ## data alignment
... 
>>> 
>>> import numpy as np
>>> import pandas as pd
>>> from pandas import Series, DataFrame
>>> 
>>> 
>>> ser1= Series([0,1,2], index=['A','B',C'])
  File "<stdin>", line 1
    ser1= Series([0,1,2], index=['A','B',C'])
                                            ^
SyntaxError: EOL while scanning string literal
>>> 
>>> ser1= Series([0,1,2], index=['A','B','C'])
>>> 
>>> ser1
A    0
B    1
C    2
dtype: int64
>>> 
>>> ser2 = Series([3,4,5,6], index=['A','B','C','D'])
>>> 
>>> ser2
A    3
B    4
C    5
D    6
dtype: int64
>>> 
>>> ser1 + ser2
A    3.0
B    5.0
C    7.0
D    NaN
dtype: float64
>>> 
>>> 
>>> 
>>> ## data frame
... 
>>>  dframe1 = DataFrame(np.arange(4).reshape((2,2)), columns=list('AB'))
  File "<stdin>", line 1
    dframe1 = DataFrame(np.arange(4).reshape((2,2)), columns=list('AB'))
    ^
IndentationError: unexpected indent
>>> 
>>>  dframe1 = DataFrame(np.arange(4).reshape((2,2)), columns=list('AB'), index=['la','nyc']))
  File "<stdin>", line 1
    dframe1 = DataFrame(np.arange(4).reshape((2,2)), columns=list('AB'), index=['la','nyc']))
    ^
IndentationError: unexpected indent
>>>  dframe1 = DataFrame(np.arange(4).reshape((2,2)), columns=list('AB'), index=['la','nyc'])
  File "<stdin>", line 1
    dframe1 = DataFrame(np.arange(4).reshape((2,2)), columns=list('AB'), index=['la','nyc'])


>>> ser1 = Series(range(3),index=['C','A','B'])
>>> ser1
C    0
A    1
B    2
dtype: int64
>>> ser1.sort_index()
A    1
B    2
C    0
dtype: int64
>>> 
>>> 
>>> ser1.order()
__main__:1: FutureWarning: order is deprecated, use sort_values(...)
C    0
A    1
B    2
dtype: int64
>>> 
>>> 
>>> ser1.sortvalues()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/pandas/core/generic.py", line 2669, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'Series' object has no attribute 'sortvalues'
>>> ser1.sort_values()
C    0
A    1
B    2
dtype: int64
>>> 
>>> 
>>> 
>>> from numpy.random import randn
>>> 
>>> ser2 = Series(randn(10))
>>> 
>>> ser2
0   -0.271551
1   -0.275873
2    0.038348
3    0.994169
4    1.393251
5   -0.968238
6   -0.717568
7   -0.229250
8    0.973946
9   -1.076439
dtype: float64
>>> 
>>> ser2.sort()
__main__:1: FutureWarning: sort is deprecated, use sort_values(inplace=True) for INPLACE sorting
>>> 
>>> ser2.sort_values()
9   -1.076439
5   -0.968238
6   -0.717568
1   -0.275873
0   -0.271551
7   -0.229250
2    0.038348
8    0.973946
3    0.994169
4    1.393251
dtype: float64
>>> 
>>> ser2.rank()
9     1.0
5     2.0
6     3.0
1     4.0
0     5.0
7     6.0
2     7.0
8     8.0
3     9.0
4    10.0
dtype: float64
>>> 
>>> 
>>> ser3 = Series(randn(10))
>>> ser3
0   -1.713711
1    0.446762
2    0.041463
3    0.182776
4   -1.096859
5   -0.936046
6   -0.122769
7   -0.515086
8    0.851559
9   -0.000485
dtype: float64
>>> 
>>> ser.rank()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ser' is not defined
>>> 
>>> ser3.rank()
0     1.0
1     9.0
2     7.0
3     8.0
4     2.0
5     3.0
6     5.0
7     4.0
8    10.0
9     6.0
dtype: float64
>>> 
>>> 
>>> ser3
0   -1.713711
1    0.446762
2    0.041463
3    0.182776
4   -1.096859
5   -0.936046
6   -0.122769
7   -0.515086
8    0.851559
9   -0.000485
dtype: float64
>>> 
>>> 
>>> 
>>> ## summary statistics
... 
>>> import numpy as np
>>> 
>>> from pandas import Series, DataFrame
>>> 
>>> import pandas as pd
>>> 
>>> 
>>> arr = np.array([[1,2,np.nan],[np.nan,3,4]])
>>> 
>>> arr
array([[  1.,   2.,  nan],
       [ nan,   3.,   4.]])
>>> 
>>> 
>>> dframe1=DataFrame(arr,index=['A','B'],columns=['One','Two','Three'])
>>> 
>>> dframe
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'dframe' is not defined
>>> 
>>> dframe12
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'dframe12' is not defined
>>> dframe1
   One  Two  Three
A  1.0  2.0    NaN
B  NaN  3.0    4.0
>>> 
>>> 
>>> dframe1.sum()
One      1.0
Two      5.0
Three    4.0
dtype: float64
>>> 
>>> 
>>> dframe1.sum(axis=1)
A    3.0
B    7.0
dtype: float64
>>> 
>>> 
>>> 
>>> dframe.min()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'dframe' is not defined
>>>  ## min function
... 
>>> dframe1.min()
One      1.0
Two      2.0
Three    4.0
dtype: float64
>>> 
>>> dframe1.max()
One      1.0
Two      3.0
Three    4.0
dtype: float64
>>> 
>>> 
>>> dframe1.idxmin()
One      A
Two      A
Three    B
dtype: object
>>> 
>>> 
>>> 
>>> 
>>> dframe1.idxmax()
One      A
Two      B
Three    B
dtype: object
>>> 
>>> dfram1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'dfram1' is not defined
>>> dframe1
   One  Two  Three
A  1.0  2.0    NaN
B  NaN  3.0    4.0
>>> 
>>> 
>>> dframe1.cumsum()
   One  Two  Three
A  1.0  2.0    NaN
B  NaN  5.0    4.0
>>> 
>>> dframe1.describe()
       One       Two  Three
count  1.0  2.000000    1.0
mean   1.0  2.500000    4.0
std    NaN  0.707107    NaN
min    1.0  2.000000    4.0
25%    1.0  2.250000    4.0
50%    1.0  2.500000    4.0
75%    1.0  2.750000    4.0
max    1.0  3.000000    4.0

##### Sumary statistics


>>> ## Summary Statistics 
... 
>>> import numpy as no
>>> from pandas import Series, DataFrame

>>> 
>>> import pandas as pd
>>> 
>>> arr= no.array([1,2,np.nan], [np.nan,3,4])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'np' is not defined
>>> arr= no.array([1,2,no.nan], [no.nan,3,4])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: data type not understood
>>> 
>>> arr= no.array([[1,2,no.nan], [no.nan,3,4]])
>>> 
>>> dframe1 = DataFrame(arr, index['A','B'], columns=['One', 'Two', 'Three'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'index' is not defined
>>> 
>>> dframe1 = DataFrame(arr, index=['A','B'], columns=['One', 'Two', 'Three'])
>>> 
>>> dframe1
   One  Two  Three
A  1.0  2.0    NaN
B  NaN  3.0    4.0
>>> 
>>> 
>>> dframe1.sum()
One      1.0
Two      5.0
Three    4.0
dtype: float64
>>> 
>>> dframe(axis=1) # summing rows
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'dframe' is not defined
>>> 
>>> dframe.sum(axis=1) # summing rows
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'dframe' is not defined
>>> dframe1.sum(axis=1) # suming rows
A    3.0
B    7.0
dtype: float64
>>> 
>>> 
>>> frame.min()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'frame' is not defined
>>> dframe1.min()
One      1.0
Two      2.0
Three    4.0
dtype: float64
>>> 
>>> dframe.idxmin()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'dframe' is not defined
>>> 
>>> dframe1.idxmin()
One      A
Two      A
Three    B
dtype: object
>>> 
>>> 
>>> dframe1.describe()  # summary 
       One       Two  Three
count  1.0  2.000000    1.0
mean   1.0  2.500000    4.0
std    NaN  0.707107    NaN
min    1.0  2.000000    4.0
25%    1.0  2.250000    4.0
50%    1.0  2.500000    4.0
75%    1.0  2.750000    4.0
max    1.0  3.000000    4.0
>>> 
>>> 
>>> from IPython.display import YouTubeVideo
>>> 
>>> 
>>> YouTubeVideo(()
... 
... )
<IPython.lib.display.YouTubeVideo object at 0x112a29650>
>>> 
>>> 
>>> YouTubeVideo()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __init__() takes at least 2 arguments (1 given)
>>> 
>>> 
>>> # learning covariance, correlations
... 
>>> 
>>> 
>>> import pandas.io.data as pdweb
/Users/jaswala/anaconda/lib/python2.7/site-packages/pandas/io/data.py:35: FutureWarning: 
The pandas.io.data module is moved to a separate package (pandas-datareader) and will be removed from pandas in a future version.
After installing the pandas-datareader package (https://github.com/pydata/pandas-datareader), you can change the import ``from pandas.io import data, wb`` to ``from pandas_datareader import data, wb``.
  FutureWarning)
>>> 
>>> import datatime
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named datatime
>>> import datetime
>>> 
>>> 
>>> 
>>> import pandas.io.data as pdweb
>>> import datetime
>>> 
>>> prices = pdweb.get_data_yahoo(['CVX','XOM','BP'], start=datetime.datetime(2015,1,1), end=datetime.datetime(2016,1,1)) ['Adj Close']
>>> 
>>> prices.head()
                   BP         CVX        XOM
Date                                        
2015-01-02  34.457313  105.234582  88.202638
2015-01-05  32.631401  101.028190  85.789250
2015-01-06  32.387346  100.981449  85.333174
2015-01-07  32.468695  100.897325  86.197816
2015-01-08  33.200869  103.206168  87.632548
>>> 
>>> volumes = pdweb.get_data_yahoo(['CVX','XOM','BP'], start=datetime.datetime(2015,1,1), end=datetime.datetime(2016,1,1)) ['Volume']
>>> 
>>> volumes.head()
                    BP         CVX         XOM
Date                                          
2015-01-02   6290100.0   5898800.0  10220400.0
2015-01-05  16126000.0  11758100.0  18502400.0
2015-01-06  11575800.0  11591600.0  16670700.0
2015-01-07   9192400.0  10353800.0  13590700.0
2015-01-08  10789700.0   8650800.0  15487500.0
>>> 
>>> rets = prices.pct_change()
>>> 
>>> rets.head()
                  BP       CVX       XOM
Date                                    
2015-01-02       NaN       NaN       NaN
2015-01-05 -0.052991 -0.039972 -0.027362
2015-01-06 -0.007479 -0.000463 -0.005316
2015-01-07  0.002512 -0.000833  0.010133
2015-01-08  0.022550  0.022883  0.016645
>>> 
>>> 
>>> # correlation of stocks
... 
>>> corr = rets.corr
>>> 
>>> corr
<bound method DataFrame.corr of                   BP       CVX       XOM
Date                                    
2015-01-02       NaN       NaN       NaN
2015-01-05 -0.052991 -0.039972 -0.027362
2015-01-06 -0.007479 -0.000463 -0.005316
2015-01-07  0.002512 -0.000833  0.010133
2015-01-08  0.022550  0.022883  0.016645
2015-01-09 -0.004084 -0.019926 -0.001410
2015-01-12 -0.014489 -0.021532 -0.019218
2015-01-13 -0.002497 -0.015867 -0.003653
2015-01-14 -0.008065 -0.002879 -0.002889
2015-01-15  0.001682 -0.011838 -0.008692
2015-01-16  0.059614  0.023863  0.024281
2015-01-20 -0.004490  0.012842 -0.000329
2015-01-21  0.029981  0.015873  0.008563
2015-01-22  0.004122  0.007027  0.010885
2015-01-23 -0.002052 -0.019005 -0.021320
2015-01-26  0.026221  0.018999  0.009572
2015-01-27  0.007265 -0.005694 -0.008827
2015-01-28 -0.033076 -0.042028 -0.032985
2015-01-29 -0.003344 -0.006846 -0.004207
2015-01-30  0.002065 -0.004563 -0.001827
2015-02-02  0.026526  0.034429  0.024708
2015-02-03  0.031109  0.032717  0.029806
2015-02-04 -0.015815 -0.010773 -0.008564
2015-02-05  0.022991  0.008860  0.009840
2015-02-06 -0.005075  0.002745 -0.001854
2015-02-09  0.010687  0.007481  0.000656
2015-02-10 -0.008652 -0.002264 -0.006007
2015-02-11 -0.007380 -0.001815 -0.004505
2015-02-12  0.024535  0.017905  0.019536
2015-02-13  0.014272  0.017319  0.010826
...              ...       ...       ...
2015-11-18  0.026916  0.012963  0.009755
2015-11-19  0.004274 -0.014966 -0.005450
2015-11-20 -0.023262 -0.020037 -0.006351
2015-11-23 -0.000291  0.011235  0.006141
2015-11-24  0.016560  0.014887  0.019930
2015-11-25  0.000000 -0.005254 -0.007694
2015-11-27 -0.004573 -0.005502 -0.000246
2015-11-30 -0.006604  0.010512  0.005294
2015-12-01  0.004913  0.012703  0.002817
2015-12-02 -0.027322 -0.024113 -0.028575
2015-12-03 -0.016558 -0.015512 -0.014331
2015-12-04 -0.017739  0.009679  0.005739
2015-12-07 -0.043159 -0.027087 -0.026122
2015-12-08  0.000320 -0.009624 -0.028255
2015-12-09  0.017269  0.013420  0.013399
2015-12-10 -0.000314  0.019406  0.000793
2015-12-11 -0.031761 -0.032027 -0.017836
2015-12-14 -0.018513  0.033434  0.022733
2015-12-15  0.017538  0.038397  0.044719
2015-12-16  0.003902  0.007331 -0.003525
2015-12-17 -0.016845 -0.031036 -0.015035
2015-12-18 -0.006590 -0.008063 -0.008722
2015-12-21 -0.000663 -0.006347 -0.000259
2015-12-22  0.021905  0.011542  0.005048
2015-12-23  0.050666  0.039216  0.032711
2015-12-24 -0.007110 -0.018761 -0.010725
2015-12-28 -0.012765 -0.018360 -0.007437
2015-12-29  0.005046  0.009849  0.005334
2015-12-30 -0.017571 -0.012712 -0.013264
2015-12-31 -0.001597 -0.001443 -0.002048

[252 rows x 3 columns]>
>>> corr.head()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'function' object has no attribute 'head'
>>> 
>>> 
>>> ## ploting method
... 
>>> prices.plot()
<matplotlib.axes._subplots.AxesSubplot object at 0x1167985d0>
>>> 
>>> %matplotlib inline prices.plot()
  File "<stdin>", line 1
    %matplotlib inline prices.plot()
    ^
SyntaxError: invalid syntax
>>> %matplotlib inline prices.plot()
  File "<stdin>", line 1
    %matplotlib inline prices.plot()
    ^
SyntaxError: invalid syntax
>>> 
>>> import seaborn as sns
>>> import matplotlib.pyplot as plt
>>> 
>>> 
>>> sns.corrplot(rets, annot=False, diag_name=False)
/Users/jaswala/anaconda/lib/python2.7/site-packages/seaborn/linearmodels.py:1285: UserWarning: The `corrplot` function has been deprecated in favor of `heatmap` and will be removed in a forthcoming release. Please update your code.
  warnings.warn(("The `corrplot` function has been deprecated in favor "
/Users/jaswala/anaconda/lib/python2.7/site-packages/seaborn/linearmodels.py:1351: UserWarning: The `symmatplot` function has been deprecated in favor of `heatmap` and will be removed in a forthcoming release. Please update your code.
  warnings.warn(("The `symmatplot` function has been deprecated in favor "
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/seaborn/linearmodels.py", line 1338, in corrplot
    cbar, annot, diag_names, ax, **kwargs)
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/seaborn/linearmodels.py", line 1374, in symmatplot
    mat_img = ax.matshow(plotmat, cmap=cmap, vmin=vmin, vmax=vmax, **kwargs)
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/matplotlib/axes/_axes.py", line 7207, in matshow
    im = self.imshow(Z, **kw)
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py", line 1812, in inner
    return func(ax, *args, **kwargs)
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/matplotlib/axes/_axes.py", line 4945, in imshow
    resample=resample, **kwargs)
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/matplotlib/image.py", line 597, in __init__
    **kwargs
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/matplotlib/image.py", line 130, in __init__
    self.update(kwargs)
  File "/Users/jaswala/anaconda/lib/python2.7/site-packages/matplotlib/artist.py", line 856, in update
    raise AttributeError('Unknown property %s' % k)
AttributeError: Unknown property diag_name
>>> 
>>> sns.corrplot(rets, annot=False, diag_names=False)
<matplotlib.axes._subplots.AxesSubplot object at 0x1167985d0>
>>> %matplotlib inline
  File "<stdin>", line 1
    %matplotlib inline
    ^
SyntaxError: invalid syntax
>>> import pylab 
>>> pylab.show()
>>> pylab.show()
>>> pylab.show()
>>> sns.corrplot(rets, annot=False, diag_names=False)
<matplotlib.axes._subplots.AxesSubplot object at 0x11c7dccd0>
>>> pylab.show()
>>> 
>>> 
>>> ser1=Series(['w','w','x','y','z'.'w','x','a'])
  File "<stdin>", line 1
    ser1=Series(['w','w','x','y','z'.'w','x','a'])
                                       ^
SyntaxError: invalid syntax
>>> ser1=Series(['w','w','x','y','z','w','x','a'])
>>> 
>>> ser1.unique
<bound method Series.unique of 0    w
1    w
2    x
3    y
4    z
5    w
6    x
7    a
dtype: object>
>>> 
>>> ser1.value_counts()
w    3
x    2
a    1
z    1
y    1
dtype: int64
>>> 

>>> ## reading and writing text files 
... 
>>> import numpy as np
>>> import pandas as pd
>>> from pandas import DataFrame, Series
>>> 
>>> 
>>> dframe= pd.read_csv(/Users/jaswala/Desktop/reading-file.csv)
  File "<stdin>", line 1
    dframe= pd.read_csv(/Users/jaswala/Desktop/reading-file.csv)
                        ^
SyntaxError: invalid syntax
>>> 
>>> dframe= pd.read_csv('/Users/jaswala/Desktop/reading-file.csv')
>>> 
>>> dframe
  arshpreet jaswa;
0     1 2 4 5 5 5 
1          hshshsh
>>> 
>>> 
>>> dframe = pd.read_csv('/Users/jaswala/Desktop/reading-file.csv', header=None) # no column names
>>> 
>>> dframe
                  0
0  arshpreet jaswa;
1      1 2 4 5 5 5 
2           hshshsh
>>> 
>>> dframe = pd.read_table('/Users/jaswala/Desktop/reading-file.csv', sep=',', header=None) # read table more generic methohd
>>> 
>>> dframe
                  0
0  arshpreet jaswa;
1      1 2 4 5 5 5 
2           hshshsh
>>> 
>>> 
>>> pd.read_csv('/Users/jaswala/Desktop/reading-file.csv',header=None, nrow=2) # reading 2 rows
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: parser_f() got an unexpected keyword argument 'nrow'
>>> pd.read_csv('/Users/jaswala/Desktop/reading-file.csv',header=None, nrows=2) # reading 2 rows
                  0
0  arshpreet jaswa;
1      1 2 4 5 5 5 
>>> 
>>> 
>>> 
>>> dframe.to_csv('mytextdata_out.csv')
>>> 
>>> 
>>> dframe.to_csv('/Users/jaswala/Desktop/mytextdata_out.csv')


>>> ## JAVASCRIT OBJECT NOTATION
... 
>>> ## Looks like python dictornary 
... 
>>> import json 
>>> 
>>> data = json.loads(json_obj) # loading json
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/jaswala/anaconda/lib/python2.7/json/__init__.py", line 339, in loads
    return _default_decoder.decode(s)
  File "/Users/jaswala/anaconda/lib/python2.7/json/decoder.py", line 367, in decode
    raise ValueError(errmsg("Extra data", s, end, len(s)))
ValueError: Extra data: line 1 column 17 - line 5 column 73 (char 16 - 183)
>>> 
>>> data=json.loads(json_obj)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/jaswala/anaconda/lib/python2.7/json/__init__.py", line 339, in loads
    return _default_decoder.decode(s)
  File "/Users/jaswala/anaconda/lib/python2.7/json/decoder.py", line 367, in decode
    raise ValueError(errmsg("Extra data", s, end, len(s)))
ValueError: Extra data: line 1 column 17 - line 5 column 73 (char 16 - 183)
>>> 
>>> 
>>> 
>>> # Heres an example of what a JSON (JavaScript Object Notation) looks like:
... json_obj = """
... {   "zoo_animal": "Lion",
...     "food": ["Meat", "Veggies", "Honey"],
...     "fur": "Golden",
...     "clothes": null, 
...     "diet": [{"zoo_animal": "Gazelle", "food":"grass", "fur": "Brown"}]
... }
... """
>>> 
>>> json_obj
'\n{   "zoo_animal": "Lion",\n    "food": ["Meat", "Veggies", "Honey"],\n    "fur": "Golden",\n    "clothes": null, \n    "diet": [{"zoo_animal": "Gazelle", "food":"grass", "fur": "Brown"}]\n}\n'
>>> 
>>> 
>>> # Heres an example of what a JSON (JavaScript Object Notation) looks like:
... json_obj = """
... {   "zoo_animal": "Lion",
...     "food": ["Meat", "Veggies", "Honey"],
...     "fur": "Golden",
...     "clothes": null, 
...     "diet": [{"zoo_animal": "Gazelle", "food":"grass", "fur": "Brown"}]
... }
... """
>>> 
>>> import json
>>> 
>>> data=json.loads(json_obj)
>>> 
>>> data
{u'food': [u'Meat', u'Veggies', u'Honey'], u'zoo_animal': u'Lion', u'fur': u'Golden', u'diet': [{u'food': u'grass', u'zoo_animal': u'Gazelle', u'fur': u'Brown'}], u'clothes': None}
>>> \
... 
>>> json.dumps(data)  
'{"food": ["Meat", "Veggies", "Honey"], "zoo_animal": "Lion", "fur": "Golden", "diet": [{"food": "grass", "zoo_animal": "Gazelle", "fur": "Brown"}], "clothes": null}'
>>> 
>>> dframe = DataFrame(data['diet'])  # into dataframe
>>> 
>>> dframe
    food    fur zoo_animal
0  grass  Brown    Gazelle
>>> 
>>> 
>>> dframe = DataFrame(data['food'])  # into dataframe
>>> 
>>> 
>>> dframe
         0
0     Meat
1  Veggies
2    Honey


>>> # working with Excel
... 
>>> import pandas as pd

>>> 
>>> xlsfile=pd.ExcelFile('/Users/jaswala/Documents/results/AAG-230.xlsx')
>>> 
>>> dframe=xlsfile.parse('AAG-230.txt') 
>>> 
>>> dframe.head()
                           web_id                         site_name  \
0  toyd-autonation-corpus-christi  AutoNation Toyota Corpus Christi   
1                      gmps-brown      AutoNation Chevrolet Gilbert   
2                  gmps-wdadechev        AutoNation Chevrolet Doral   
3                  lex-palm-beach               Lexus of Palm Beach   
4      scion-autonation-las-vegas        AutoNation Scion Las Vegas   

    cal_date                vin  certified c_page_group1_name first_name  \
0 2015-01-19  1FMEU74EX7UB13784       used    Vehicle Details    Unknown   
1 2015-01-19  1G1PA5SH8E7254946        new    Vehicle Details    Unknown   
2 2015-01-19  1HGCG564XYA135168       used    Vehicle Details    Unknown   
3 2015-01-19  2T2ZK1BAXBC057744  certified    Vehicle Details    Unknown   
4 2015-01-19  WBANW13568CZ70573       used    Vehicle Details    Unknown   

  last_name day_phone_number evening_phone_number email_address  
0   Unknown          unknown              unknown       unknown  
1   Unknown          unknown              unknown       unknown  
2   Unknown          unknown              unknown       unknown  
3   Unknown          unknown              unknown       unknown  
4   Unknown          unknown              unknown       unknown  