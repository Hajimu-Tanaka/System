
##################################################################################
# セクション３　Pythonの基本 Todo
##################################################################################

################################
# 文字列のメソッド
################################
s = 'My name is Mike. Hi Mike'

print(s.startswith('My')) #指定の文字列で始まっているか
print(s.find('Mike')) #指定の文字列が何文字目にあるか
print(s)
print(s.rfind('Mike')) #指定の文字列が後の何文字目にあるか
print(s.count('Mike')) #指定の文字列が、検索対象に何個入っているか
print(s.capitalize()) #対象の文字列の最初の文字を大文字に、それ以降を小文字にする
print(s.title()) #対象の文字列の各単語の最初の文字を大文字にする
print(s.upper()) #対象の文字列をすべて大文字にする
print(s.lower()) #対象の文字列をすべて小文字にする
print(s.replace('Mike','Nancy')) #指定の文字列を、別の文字列に置換する

################################
# 文字の代入
################################
print('a is {}'.format('test'))
print('a is {} {} {}'.format(1,2,3))
print('a is {2} {1} {0}'.format(1,2,3))

print('My name is {0} {1} watasshi wa {1} {0}'.format('Taro','Yamada'))
print('My name is {name} {family} watasshi wa {family} {name}'.format(name='Taro',family='Yamada'))

#f-strings py3.6以降 処理も早い
x,y,z = 1,2,3
print(f'a is {x} {y} {z}')


##################################################################################
# セクション４　データ構造 Todo
##################################################################################

################################
# リストの操作
################################
s = ['a','b','c','d','e','f','g']
s[2:5]=['C','D','E']
print(s)

################################
# リストのメソッド
################################
r = [1,2,3,4,5,1,2,3]

print(r.index(3)) #指定の文字が、先頭から何番目の要素にあるかを調べる
print(r.index(4,3)) #第一引数の要素番号から、第二引数の文字が何番目にあるか調べる
print(r.count(3)) #指定の文字がリストに何個あるか

r.sort() #リスト内の文字を昇順で並べる
print(r)
r.reverse() #リスト内の文字を降順で並べる
print(r)

#特定の値（例：５）が含まれているか確認
if 5 in r:
    print()

#指定の文字を区切りにして分割し、リストに格納する
s = 'My name is Mike.'
to_split = s.split(' ')
print(to_split)

#リスト内の要素を左記の文字列で結合する
x = ' ####### '.join(to_split)
print(x)


################################
# リストのコピー
################################
#参照渡し
i = [1,2,3,4,5]
j = i
print('j =', j)
print('i =', i)

#値渡し
x = [1,2,3,4,5]
y = x.copy()
y[0] = 100
print('y =', y)
print('x =', x)


################################
# リストの使い所
################################
#座席の空きがあるかを判定する
seat = []
min = 0
max = 5
print(min <= len(seat) < max) #論理和の判定：True

seat.append('p')
seat.append('p')
seat.append('p')
seat.append('p')
seat.append('p')

print(min <= len(seat) < max) #False 空きなし



################################
# タプル
################################
t = (1,2,3,4,5,6)
print(t)
#t[0] = 100 値を後から入力できない

################################
# タプルの使い所
################################
#例：質問をユーザーに投げかけて、３つの選択肢のうち２つ選ばせる
chose_from_two = ('A','B','C')

answer = []
answer.append('A')
answer.append('B')

print(chose_from_two)
print(answer)

################################
# 辞書型
################################
d = {'x':10, 'y':20}
print(d)
print(d['x'])

print(d.keys())    #キーを表示
print(d.values())   #バリューを表示

#上書き更新ができる
d2 = {'x':1000, 'j':2000}
d.update(d2)
print(d)

print(d.get('x'))  #値を取り出す 存在しないキーを入れるとNoneを返す

#指定の値を取り出して、除去
print(d.pop('x'))
print(d)

#指定のキーの要素を削除する
del d['y']
print(d)

#中身を空にする
d.clear()
print(d)

#キー・バリューを同時に取り出す
persons_name = {'tanaka':34,
                'yamada':33,
                'takahasshi':42,
                'onizuka':50}

for key,value in persons_name.items():
    print(key , ':' , value)


################################
# 辞書型のコピー
################################
#参照渡し
x = {'a':1}
y = x
y['a'] = 1000
print(x)
print(y)

#値渡し
x = {'a':1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)


################################
# 辞書型の使い所
################################
#何か指定したものの、情報を取得できるようにする
#リストは検索に時間かかる、辞書型はハッシュ値で検索するため早い
fruits = {
    'apple':100,
    'banana':200,
    'orange':300
}
print(fruits['orange'])


################################
# 集合型
################################
a = {1,2,3,4,5,6}
print(type(a))
print(a)

b={2,3,4}
print(b)

print(a-b)
print(a & b) #論理和

s = {1,2,3,4,5}
print(s)

#指定の値を加える
s.add(6)
print(s)
#指定の値を削除する
s.remove(6)
print(s)
#中身を空にする
s.clear()
print(s)

################################
# 集合型の使い所
################################
#例：友達との共通点を探すときに使える
#何かと共通点がないかを調べる
my_friends = {'A','C','D'}
A_friends = {'B','D','E',"F"}
print(my_friends & A_friends)

#重複を排除する
f = ['apple','banana','apple','banana']
kind = set(f)
print(kind)


##################################################################################
# セクション５　制御フローとコード構造 Todo
##################################################################################


################################
# １行が長くなるとき
################################
#バックスラッシュを付けること
#１行８０文字が基本ルール
s = 'aaaaaaaaaaaaaaaaaaaa' \
    + 'bbbbbbbbbbbbbb'
print(s)

#パレンティスのカッコを使うと、以下でもいける
s = ('aaaaaaaaaaaaaaaaaaaa' 
     'bbbbbbbbbbbbbb')
print(s)

x = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1  \
    + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
print(x)


################################
# if文
################################
#elifが複数ある場合、上の方の判定が優先される
x = 0
if x < 0:
    print('negative')
elif x == 0:
    print('zero')
else:
    print('positive')

a = 5
b = 10
if a > 0:
    print('positive')
    if b > 0:
        print('b is positive')

################################
# in と　Notの使い所
################################
y = [1,2,3]
x = 1

if x in y:
    print('in')

if 100 not in y:
    print('not in')

a = 1
b = 2

#非推奨
#if not a == b:
#    print('Not equal')
if a != b:
    print('Not equal')

#以下のようにis判定でnotは使う
is_ok = True
if not is_ok:
    print('hello')


################################
# 値が入っていない判定をする方法
################################
#is_ok = []
is_ok = '' #False
is_ok = 'aaaa' #True

if is_ok:
    print('OK!')
else:
    print('No!')

################################
# Noneを判定
################################
is_empty = None

if is_empty is not None:
    print('None')

################################
# input関数
################################
while True:
    word = input('Enter:')
    num = int(word)
#    if word == 'ok':
    if num == 100:
        break
    print('next')

################################
# for文とbreak文とcontinue文
################################
some_list = [1,2,3,4,5]

# i = 0
# while i < len(some_list):
#     print(some_list[i])
#     i += 1

# for i in some_list:
#     print(i)

# for s in 'abcde':
#     print(s)

# for word in ['My','name','is','Mike']:
#     if word == 'name':
#         break
#     print(word)

for word in ['My','name','is','Mike']:
    if word == 'name':
        continue
    print(word)

################################
# 名前空間とスコープ
################################
animal = 'cat'

def f():
#    print(animal)  #後続でローカル変数を作るとエラー。しかし無ければグローバル変数を参照する
    animal = 'dog'
    print(animal) #dog
    print('locals', locals())

f()

print(animal) #cat
print('globals', globals())
print(__name__)
print(__builtins__)

#################################
# 例外処理
################################
l = [1,2,3]
i = 5
#l[i]
#del l

try:
    l[1]
except IndexError as ex:
    print("don't worry:{}".format((ex)))
except NameError as ex:
    print(ex)
except Exception as ex:
    print('other:{}'.format(ex))
else:
    print('done')
finally:
    print('clean up')

#elseは例外が発生しなかった場合のみ実行される
#exceptなしで実行しても、finallyは実行される
#以下は例外の一覧
#https://docs.python.org/ja/3/library/exceptions.html


################################
# 独自例外の作成
################################
#自分で独自例外を作っておけば、すぐに自分たちのものだとわかり原因特定しやすい
#こういった例外に対して、こういった対応が必要ではないか？となったときに独自例外を作るとよい

class UppercaseError(Exception):
    pass

def check():
    words = ['APPLE','orange','banana']
    for word in words:
        if word.isupper():
            raise UppercaseError

try:
    check()
except UppercaseError as exec:
    print('This is my fault. Go next')


##################################################################################
# セクション６　モジュールとパッケージ Todo
##################################################################################

################################
#コマンドライン引数
################################
#ターミナルで「python main.py option1 option2」　と実行してみると以下のように表示
"""
['lesson.py', 'option1', 'option2']
lesson.py
option1
option2
"""
import sys

print(sys.argv)
for i in sys.argv:
    print(i)

###########################
#import文とas
################################
#__init__.py を作る必要がある
#__init__.py が先に読み込まれる

#import lesson_package.utils
from lesson_package import utils #このモジュールを書く書き方のほうが推奨されている。他のところからインポートしているのがわかりやすい。
#from lesson_package import utils as u   #この書き方も推奨はされていない。
#from lesson_package.utils import say_twice #どこのモジュールか分かりにくいため非推奨


################################
#絶対パスと相対パスのインポート
################################
from lesson_package.talk import human

print(human.sing())
print(human.cry())

#human.py
# from lesson_package import utils
#
# def sing():
#     return 'sing'
#
# def cry():
#     return utils.say_twice('cry')

################################
#seup.pyでパッケージ化して配布する
################################
"""
１、「ツール」から「setup.pyの作成」
２、必要情報を入力する
３、「ツール」から「setup.pyタスクの実行」 例：sdist
"""

################################
#組み込み関数 (インポートしなくても使える関数)
# https://docs.python.org/ja/3/library/functions.html
################################

#よく使われる組込関数
#sorted()

ranking = {
    'A' : 100,
    'B' : 85,
    'C' : 95
}

print(sorted(ranking, key=ranking.get))               #昇順 ['B', 'C', 'A']
print(sorted(ranking, key=ranking.get, reverse=True)) #降順 ['A', 'C', 'B']

################################
#標準ライブラリ
################################
#importして利用するライブラリ

s = 'dadadasdadadcadcadcasdcadcadcasdcadcdsaca'
# d = {}
# for c in s:
#     if c not in d:
#         d[c] = 0
#     d[c] += 1
# print(d)
#
# d = {'f':10}
# for c in s:
#     d.setdefault(c,0)
#     d[c] += 1
# print(d)

#代表のライブラリの一つ
#指定の文字列に含まれる文字の数をそれぞれ算出する
from collections import defaultdict
d = defaultdict(int)
for c in s:
    d[c] += 1
print(d)
print(d['s'])

################################
#importする際の注意点
################################
#import collections, sys ,os  こういう書き方は非推奨
#アルファベット順
#上から標準ライブラリ、サードパーティ、自分たちのパッケージ、ローカルファイルの順で。
import collections
import os
import sys

#import termcolor

import lesson_package

#import config

#以下で各ライブラリが存在する__init__.pyの場所を示す
print(collections.__file__)
print(lesson_package.__file__)


################################
#__name__　と　__main__
################################
import lesson_package.talk.animal

import config

def main():
    lesson_package.talk.animal.sing()

if __name__ == '__main__':
    main()


##################################################################################
# セクション７　オブジェクトとクラス Todo
##################################################################################

################################
#クラスの定義
################################
class Person(object):
    def say_somthing(self):
        print('hello')

person = Person()
person.say_somthing()


################################
#クラスの初期化とクラス変数
################################
class Person(object):

    def __init__(self,name):
        self.name = name
        print(self.name)

    def say_somthing(self):
        print('I am {}. hello'.format(self.name))
        self.run(10)

    def run(self, num):
        print('run' * num)

person = Person('TANAKA')
person.say_somthing()


################################
#コンストラクタとデストラクタ
################################
class Person(object):

    #コンストラクタ
    def __init__(self,name):
        self.name = name
        print(self.name)

    def say_somthing(self):
        print('I am {}. hello'.format(self.name))
        self.run(10)

    def run(self, num):
        print('run' * num)

    #デストラクタ
    def __del__(self):
        print('good bye')

person = Person('TANAKA')
person.say_somthing()

#del person #先に明示的に削除したい場合

print('#########')

################################
#クラスの継承
################################
class Car(object):
    def run(self):
        print('run')

class ToyotaCar(Car):
    pass

class TeslaCar(Car):
    def auto_run(self):
        print('auto run')

car = Car()
car.run()
print('##################')
toyota_car = ToyotaCar()
toyota_car.run()
print('##################')
tesla_car = TeslaCar()
tesla_car.run()
tesla_car.auto_run()


################################
#メソッドのオーバライドとsuperによる親のメソッド
################################
class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

class ToyotaCar(Car):
    def run(self):
        print('fast')

class TeslaCar(Car):
    #コンストラクタで親のメソッドを呼び出す
    def __init__(self, model='Model S', enable_auto_run=False):
        super().__init__(model)
        self.enable_auto_run =  enable_auto_run

    def run(self):
        print('super fast')

    def auto_run(self):
        print('auto run')

car = Car()
car.run()

print('##################')
toyota_car = ToyotaCar('Lexus')
toyota_car.run()
print('##################')
tesla_car = TeslaCar('Model S')
tesla_car.run()
tesla_car.auto_run()

################################
#プロパティを使った属性の設定
################################
class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

class ToyotaCar(Car):
    def run(self):
        print('fast')

class TeslaCar(Car):
    #コンストラクタで親のメソッドを呼び出す
    def __init__(self, model='Model S', enable_auto_run=False, passed='123'):
        super().__init__(model)
        self._enable_auto_run =  enable_auto_run #明示的に隠す
        self.passed = passed

    #getter
    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    #setter ある特定の条件で書き換えるといったときに使える
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.passed == '456':
            self._enable_auto_run = is_enable
        else:
            raise ValueError

    def run(self):
        print('super fast')

    def auto_run(self):
        print('auto run')

tesla_car = TeslaCar('Model S', passed='111')
#tesla_car.enable_auto_run = True
print(tesla_car.enable_auto_run)

################################
#ダックタイピング
################################
class Person(object):
    def __init__(self, age=1):
        self.age = age

    def drive(self):
        if self.age >= 18:
            print('OK')
        else:
            raise Exception('No drive')

class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

    def ride(self,person):
        person.drive()

baby = Baby()
adult = Adult()

car = Car()
#car.ride(baby)
car.ride(adult)

################################
#抽象クラス
################################
#car.drive()を使う場合、Personを継承するクラスは全てdrive()実装要と明示
#無理に作る必要がない
import abc

class Person(metaclass=abc.ABCMeta):
    def __init__(self, age=1):
        self.age = age

    @abc.abstractmethod
    def drive(self):
        pass

class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        raise Exception('No drive')


class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        print('ok')

class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

    def ride(self,person):
        person.drive()

baby = Baby()
adult = Adult()

car = Car()
#car.ride(baby)
car.ride(adult)


################################
#多重継承
################################
#このように利用できるが、使わなくてよいにこしたことはない
class Person(object):
    def talk(self):
        print('talk')

    def run(selfs):
        print('person run')

class Car(object):
    def run(self):
        print('car run')

class PersonCarRobot(Car,Person):
    def fly(self):
        print('fly')


person_car_robot = PersonCarRobot()
person_car_robot.talk()
person_car_robot.run() #引数でCar、Person先に書いたほうが優先される
person_car_robot.fly()


################################
#クラス変数
################################
class Person(object):

    #すべてのインスタンスで共有される
    kind = 'human'

    def __init__(self,name):
        self.name = name

    def who_are_you(self):
        print(self.name,self.kind)

a = Person('A')
a.who_are_you()
b = Person('B')
b.who_are_you()

class T(object):

    words = []

    def add_word(self,word):
        self.words.append(word)

c = T()
c.add_word('add 1')
c.add_word('add 2')

d = T()
d.add_word('add 3')
d.add_word('add 4')

print(d.words) #全部共有されているため加算される、便利な分、注意が必要。



################################
#クラスメソッドとスタティックメソッド
################################
class Person(object):

    kind = 'human'

    def __init__(self):
        self.x = 100

    @classmethod   #これを付ければインスタンス化しなくても呼び出せる
    def what_is_your_human(self):
        return self.kind

    @staticmethod   #あまり使う機会はない
    def about(year):
        print('about human {}'.format(year))

#インスタンス
a = Person()
print(a.what_is_your_human())

#クラスメソッド
print(Person.what_is_your_human())

#スタティックメソッド
Person.about(1999)



################################
#抽象メソッド
################################
class Word(object):

    def __init__(self,text):
        self.text = text

    #文字列として読み込まれたときに使われる  #頻出
    def __str__(self):
        return 'Word!!!!'

    #文字数を返す
    def __len__(self):
        return len(self.text)

    def __add__(self, word):
        return self.text.lower() + word.text.lower()

    def __eq__(self, word):
        return self.text.lower() == word.text.lower()

w = Word('test')
w2 = Word('###########')

print(w)  #__str__使われる
print(len(w))
print(len(w2))

print(w + w2) #__add__

print(w == w2) #__eq__ 値で判定する。使わないとidで判定されるため同値でFalseになる




##################################################################################
# セクション８　ファイル操作とシステム Todo
##################################################################################

################################
#ファイルの作成
################################
f = open('text.txt','w')  #上書きするので気をつける
f.write('test\n')
#print('I am Print', file=f)
f.close()


################################
#withステートメントでファイルをopenする
################################
#自動的にcloseしてくれる。この書き方が推奨されている
with open('text.txt','w') as f:
    f.write('test\ntanaka')

################################
#ファイルの読み込み
################################
s = """\
AAA
BBB
CC
DDD
"""

# with open('text.txt','w') as f:
#      f.write(s)

with open('text.txt','r') as f:
#    print(f.read())
    while True:
        #chunk = 2
        #line = f.read(chunk)
        #line = f.read()
        line = f.readline()
        print(line)
        if not line:
            break


################################
#CSVファイルへの書き込みと読み込み
################################
import csv

with open('test.csv','w') as csv_file:
    fieldnames = ['Name','Count']
    writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Name':'A','Count':1})
    writer.writerow({'Name':'B','Count':2})





##################################################################################
# セクション１０　コードスタイル　 Todo
##################################################################################

##################################################################################
# セクション１１　コンフィグとロギング　（以降：応用編）　 Todo
##################################################################################

################################
#configparsar
################################

#設定ファイルを作成を補助するライブラリ
#実行すると以下コメントのような設定内容を含めたファイルを生成する
"""
[DEFAULT]
debug = False

[web_server]
host = 127.0.0.1
port:80

[db_server]
host = 127.0.0.1
port:3306

"""
#設定ファイル作成・書き込み
import configparser
config = configparser.ConfigParser()
config['DEFAULT'] = {
    'debug':False
}
config['web_server'] = {
    'host' : '127.0.0.1',
    'port' : 80
}
config['db_server'] = {
    'host' : '127.0.0.1',
    'port' : 3306
}
with open('config.ini','w') as config_file:
    config.write(config_file)

#設定ファイル読み込み
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
print(config['web_server'])
print(config['web_server']['host'])
print(config['web_server']['port'])

print(config['DEFAULT']['debug'])


################################
#yaml
################################



################################
#ロギング
################################
"""
CRITICAL
ERROR
WARNING
INFO
DEBUG
"""

import logging

#ログレベルを変更（デフォルトはWARNING）
#filenameを指定することで、logging関連のログを出力できる
logging.basicConfig(filename='test.log',level=logging.DEBUG)

logging.critical('critical')
logging.error('error')
logging.warning('warning')
logging.info('info')
logging.debug('debug') #開発段階のみ利用

#logging.info('info {}'.format('test)
logging.info('info %s %s' , 'test', 'test2')

################################
#ロギング　フォーマッタ
################################
#logging --- Python 用ロギング機能¶
#https://docs.python.org/ja/3/library/logging.html?highlight=%E3%83%AD%E3%82%AE%E3%83%B3%E3%82%B0

import logging

#logging.basicConfig(filename='test.log',level=logging.DEBUG)

#formatでログをどういった表示をしたいのか変えることができる
formatter = '%(asctime)s:%(levelname)s:%(message)s'
logging.basicConfig(level=logging.DEBUG,format=formatter)

logging.critical('critical')
logging.error('error')
logging.warning('warning')
logging.info('info')
logging.debug('debug') #開発段階のみ利用

#logging.info('info {}'.format('test)
logging.info('info %s %s' , 'test', 'test2')

"""
2020-08-21 18:01:53,332:CRITICAL:critical
2020-08-21 18:01:53,332:ERROR:error
2020-08-21 18:01:53,332:WARNING:warning
2020-08-21 18:01:53,332:INFO:info
2020-08-21 18:01:53,332:DEBUG:debug
2020-08-21 18:01:53,332:INFO:info test test2
"""

################################
#ロギング　ロガー　再度受講要
################################
#開発ではメインの部分で通常のログレベルを設定し、他の部分は必要に応じてカスタマイズ
#loggerは必ず使うので覚えておく

import logging

logging.basicConfig(level=logging.INFO)
logging.info('info')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.debug('debug')


##################################################################################
# セクション１２　データベース　 Todo
##################################################################################

################################
#データベースに関して
################################









##################################################################################
# セクション１３　WEBとネットワーク　 Todo
##################################################################################

################################
#xml
################################



##################################################################################
# セクション１４　テスト　 Todo
##################################################################################

################################
#doctest
################################
class Cal(object):
    def add_num_and_double(self,x,y):
        """Add and double

        >>> c = Cal()
        >>> c.add_num_and_double(1,1)
        4

        >>> c.add_num_and_double('1','1')
        Traceback (most recent call last):
        ...
        ValueError
        """

        if type(x) is not int or type(y) is not int:
            raise ValueError
        result = x + y
        result *= 2
        return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()

################################
#Unittest
################################
"""
calculation.py
"""
class Cal(object):
    def add_num_and_double(self,x,y):

        if type(x) is not int or type(y) is not int:
            raise ValueError
        result = x + y
        result *= 2
        return result

"""
test_calculation.py
構成の編集よりunittestの構成を選択して実行する
"""
import unittest
import calculation

class CalTest(unittest.TestCase):
    def test_add_num_and_double(self):
        cal = calculation.Cal()
        cal.add_num_and_double(1,1)

        #第一引数が、第二引数の値と同じものを返すかを判定
        self.assertEqual(cal.add_num_and_double(1,1),4)

################################
#Unittestで例外テスト
################################
"""
calculation.py
"""
class Cal(object):
    def add_num_and_double(self,x,y):

        if type(x) is not int or type(y) is not int:
            raise ValueError
        result = x + y
        result *= 2
        return result

"""
test_calculation.py
構成の編集よりunittestの構成を選択して実行する
"""
import unittest
import calculation

class CalTest(unittest.TestCase):

    # 例外処理をテストしたい場合
    def test_add_num_and_double_raise(self):
        cal = calculation.Cal()
        # 以下で例外で期待する例外を書けば、その通りかを判定してくれる
        with self.assertRaises(ValueError):
            cal.add_num_and_double('1', '1')

################################
#Unittestのsetupとteardown
################################
#ユニットテストが実行される前と後に行われる設定
#各テストメソッドで共通して使われるものを事前にやっておくと便利
"""
calculation.py　
"""
#同上、省略

"""
test_calculation.py
構成の編集よりunittestの構成を選択して実行する

-----以下、実行結果
Ran 2 tests in 0.006s

OK
setup
clean up
setup
clean up

プロセスは終了コード 0 で完了しました

"""
import unittest
import calculation

class CalTest(unittest.TestCase):

    def setUp(self):
        print('setup')
        self.cal = calculation.Cal()

    def tearDown(self):
        print('clean up')
        del self.cal

    def test_add_num_and_double(self):
        self.cal.add_num_and_double(1, 1)

        # 第一引数が、第二引数の値と同じものを返すかを判定
        self.assertEqual(self.cal.add_num_and_double(1, 1), 4)

    #例外処理をテストしたい場合
    def test_add_num_and_double_raise(self):
        #以下で例外で期待する例外を書けば、その通りかを判定してくれる
        with self.assertRaises(ValueError):
            self.cal.add_num_and_double('1','1')

################################
#Unittestのスキップ
################################
"""
test_calculation.py
構成の編集よりunittestの構成を選択して実行する
"""
import unittest
import calculation

#通常にアサーションでスキップを入れてもいいが、
#条件に合致したものを一気に適用したい場合は、skipIfを使うと効率的
release_name = 'lesson'

class CalTest(unittest.TestCase):
    def setUp(self):
        print('setup')
        self.cal = calculation.Cal()

    def tearDown(self):
        print('clean up')
        del self.cal

    #@unittest.skip('skip!')
    @unittest.skipIf(release_name=='lesson','skip!!')
    def test_add_num_and_double(self):
        self.cal.add_num_and_double(1, 1)

        # 第一引数が、第二引数の値と同じものを返すかを判定
        self.assertEqual(self.cal.add_num_and_double(1, 1), 4)

    #例外処理をテストしたい場合
    def test_add_num_and_double_raise(self):
        #以下で例外で期待する例外を書けば、その通りかを判定してくれる
        with self.assertRaises(ValueError):
            self.cal.add_num_and_double('1','1')

################################
#pytest
################################
#unittestよりも機能が多く、これを使ってテストしている企業も多い。


##################################################################################
# セクション１５　並列化　 Todo
##################################################################################

##################################################################################
# セクション１６　暗号化　 Todo
##################################################################################

##################################################################################
# セクション１７　インフラ構築自動化　 Todo
##################################################################################

##################################################################################
# セクション１８　Pythonの便利なライブラリ　 Todo
##################################################################################

################################
#正規表現 re
################################



##################################################################################
# セクション１９　グラフィックス　 Todo
##################################################################################

##################################################################################
# セクション２０　データ解析　 Todo
##################################################################################

##################################################################################
# セクション２１　キューイングシステム　 Todo
##################################################################################

##################################################################################
# セクション２２　非同期処理 asynico　 Todo
##################################################################################


