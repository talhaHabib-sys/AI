Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas
>>> from sklearn.datasets import load_iris
>>> iris=load_iris()
>>> dir(iris)
['DESCR', 'data', 'feature_names', 'filename', 'frame', 'target', 'target_names']
>>> iris.feature_names
['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
>>> df=pandas.DataFrame(iris.data,colum=iris.feature_names)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    df=pandas.DataFrame(iris.data,colum=iris.feature_names)
TypeError: __init__() got an unexpected keyword argument 'colum'
>>> df=pandas.DataFrame(iris.data,columns=iris.feature_names)
>>> df.head()
   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
0                5.1               3.5                1.4               0.2                                          
1                4.9               3.0                1.4               0.2
2                4.7               3.2                1.3               0.2
3                4.6               3.1                1.5               0.2
4                5.0               3.6                1.4               0.2
>>> df['target']=iris.target
>>> df.head()
   sepal length (cm)  sepal width (cm)  ...  petal width (cm)  target
0                5.1               3.5  ...               0.2       0
1                4.9               3.0  ...               0.2       0
2                4.7               3.2  ...               0.2       0
3                4.6               3.1  ...               0.2       0
4                5.0               3.6  ...               0.2       0

[5 rows x 5 columns]
>>> iris.target_names
array(['setosa', 'versicolor', 'virginica'], dtype='<U10')
>>> df[df.target==1].head()
    sepal length (cm)  sepal width (cm)  ...  petal width (cm)  target
50                7.0               3.2  ...               1.4       1
51                6.4               3.2  ...               1.5       1
52                6.9               3.1  ...               1.5       1
53                5.5               2.3  ...               1.3       1
54                6.5               2.8  ...               1.5       1

[5 rows x 5 columns]
>>> df['flowers_name']=df.target.apply(lambda x:iris.target_names[x])
>>> df.head()
   sepal length (cm)  sepal width (cm)  ...  target  flowers_name
0                5.1               3.5  ...       0        setosa
1                4.9               3.0  ...       0        setosa
2                4.7               3.2  ...       0        setosa
3                4.6               3.1  ...       0        setosa
4                5.0               3.6  ...       0        setosa

[5 rows x 6 columns]
>>> df[df.flowers_name=='virginica'].head()
     sepal length (cm)  sepal width (cm)  ...  target  flowers_name
100                6.3               3.3  ...       2     virginica
101                5.8               2.7  ...       2     virginica
102                7.1               3.0  ...       2     virginica
103                6.3               2.9  ...       2     virginica
104                6.5               3.0  ...       2     virginica

[5 rows x 6 columns]
>>> from matplotlib import pyplot as plt
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    from matplotlib import pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'
>>>  from matplotlib import pyplot as plt
SyntaxError: unexpected indent
>>> from matplotlib import pyplot as plt
>>> df0=df[df.target==0]
>>> df1=df[df.target==1]
>>> df2=df[df.target==2]
>>> df1.head()
    sepal length (cm)  sepal width (cm)  ...  target  flowers_name
50                7.0               3.2  ...       1    versicolor
51                6.4               3.2  ...       1    versicolor
52                6.9               3.1  ...       1    versicolor
53                5.5               2.3  ...       1    versicolor
54                6.5               2.8  ...       1    versicolor

[5 rows x 6 columns]
>>> plt.scatter(df0['sepal length (cm)'],df1['sepal width (cm)'],color='green',marker='+')
<matplotlib.collections.PathCollection object at 0x000001B7C5A5B9B0>
>>> from sklearn.model_selection import train_test_split
>>> x=dF.drop(['tarGget','flower_name'],axis='columns')
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    x=dF.drop(['tarGget','flower_name'],axis='columns')
NameError: name 'dF' is not defined
>>> x=df.drop(['tarGget','flower_name'],axis='columns')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    x=df.drop(['tarGget','flower_name'],axis='columns')
  File "C:\Users\Talha Habib\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\frame.py", line 3997, in drop
    errors=errors,
  File "C:\Users\Talha Habib\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\generic.py", line 3936, in drop
    obj = obj._drop_axis(labels, axis, level=level, errors=errors)
  File "C:\Users\Talha Habib\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\generic.py", line 3970, in _drop_axis
    new_axis = axis.drop(labels, errors=errors)
  File "C:\Users\Talha Habib\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\indexes\base.py", line 5018, in drop
    raise KeyError(f"{labels[mask]} not found in axis")
KeyError: "['tarGget' 'flower_name'] not found in axis"
>>> 
>>> x=df.drop(['target','flower_name'],axis='columns')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    x=df.drop(['target','flower_name'],axis='columns')
  File "C:\Users\Talha Habib\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\frame.py", line 3997, in drop
    errors=errors,
  File "C:\Users\Talha Habib\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\generic.py", line 3936, in drop
    obj = obj._drop_axis(labels, axis, level=level, errors=errors)
  File "C:\Users\Talha Habib\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\generic.py", line 3970, in _drop_axis
    new_axis = axis.drop(labels, errors=errors)
  File "C:\Users\Talha Habib\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\indexes\base.py", line 5018, in drop
    raise KeyError(f"{labels[mask]} not found in axis")
KeyError: "['flower_name'] not found in axis"
>>> x=df.drop(['tarGget','flower_names'],axis='columns')
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    x=df.drop(['tarGget','flower_names'],axis='columns')
  File "C:\Users\Talha Habib\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\frame.py", line 3997, in drop
    errors=errors,
  File "C:\Users\Talha Habib\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\generic.py", line 3936, in drop
    obj = obj._drop_axis(labels, axis, level=level, errors=errors)
  File "C:\Users\Talha Habib\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\generic.py", line 3970, in _drop_axis
    new_axis = axis.drop(labels, errors=errors)
  File "C:\Users\Talha Habib\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\indexes\base.py", line 5018, in drop
    raise KeyError(f"{labels[mask]} not found in axis")
KeyError: "['tarGget' 'flower_names'] not found in axis"
>>> x=df.drop(['target','flower_name'],axis='columns')
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    x=df.drop(['target','flower_name'],axis='columns')
  File "C:\Users\Talha Habib\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\frame.py", line 3997, in drop
    errors=errors,
  File "C:\Users\Talha Habib\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\generic.py", line 3936, in drop
    obj = obj._drop_axis(labels, axis, level=level, errors=errors)
  File "C:\Users\Talha Habib\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\generic.py", line 3970, in _drop_axis
    new_axis = axis.drop(labels, errors=errors)
  File "C:\Users\Talha Habib\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\indexes\base.py", line 5018, in drop
    raise KeyError(f"{labels[mask]} not found in axis")
KeyError: "['flower_name'] not found in axis"
>>> x=df.drop(['target','flowers_name'],axis='columns')
>>> x.head()
   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
0                5.1               3.5                1.4               0.2
1                4.9               3.0                1.4               0.2
2                4.7               3.2                1.3               0.2
3                4.6               3.1                1.5               0.2
4                5.0               3.6                1.4               0.2
>>> y=df.target
>>> x_train,x_train,y_train,y_test=train_test_split(x,y,test_size=0.2)
>>> len(x_train)
30
>>> len(y_train)
120
>>> len(x_test)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    len(x_test)
NameError: name 'x_test' is not defined
>>> x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
>>> len(x_train)
120
>>> len(x_test)
30
>>> len(y_train)
120
>>> len(y_test)
30
>>> from sklearn.svn import SVC
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    from sklearn.svn import SVC
ModuleNotFoundError: No module named 'sklearn.svn'
>>> from sklearn.svm import SVC
>>> model=SVC()
>>> model.fit(x_train,y_train)
SVC()
>>> model.score(x_test,y_test)
0.8666666666666667
>>> model=SVC(c=10)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    model=SVC(c=10)
  File "C:\Users\Talha Habib\AppData\Local\Programs\Python\Python37\lib\site-packages\sklearn\utils\validation.py", line 73, in inner_f
    return f(**kwargs)
TypeError: __init__() got an unexpected keyword argument 'c'
>>> model=SVC(C=10)
>>> model.fit(x_test,y_test)
SVC(C=10)
>>> model.score()
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    model.score()
TypeError: score() missing 2 required positional arguments: 'X' and 'y'
>>> model.fit(x_train,y_train)
SVC(C=10)
>>> model.score(x_test,y_test)
0.9333333333333333
>>> Y_predict=model.predict(x_test)
>>> Y_predict
array([0, 0, 2, 2, 2, 1, 2, 0, 2, 2, 1, 2, 2, 1, 2, 2, 0, 2, 2, 1, 1, 2,
       2, 2, 1, 1, 2, 1, 0, 1])
>>> Y_predict[0]
0
>>> Y_predict[2]
2
>>> Y_predict[3]
2
>>> Y_predict[51]
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    Y_predict[51]
IndexError: index 51 is out of bounds for axis 0 with size 30
>>> Y_predict[4]
2
>>> X.head()
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    X.head()
NameError: name 'X' is not defined
>>> 
