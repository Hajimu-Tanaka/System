

##################################################################################
# tkinterの基本 Todo
##################################################################################
import tkinter as tk
root = tk.Tk()

root.title('位置指定') #ウィンドウのタイトル
root.geometry('450x350') #画面サイズ（幅＊高さ）
root.geometry('+450+350') #x座標４５０ y座標３５０
root.geometry('450x350+350+250')  #幅＊高さ＋x座標＋y座標

root.mainloop()


################################
#アクションの組込み
################################
import tkinter as tk

#ボタンが押された時に呼び出される
def action_btn_press():
    print("ボタンが押されました")

root = tk.Tk()
root.title('アクションの組込み')
root.geometry('350x150')

#部品の作成
lb = tk.Label(text="ラベル")
bt = tk.Button(text="ボタン",command=action_btn_press())

#配置
lb.pack()
bt.pack()

root.mainloop()

################################
#テキストボックス内容の取得
################################
import tkinter as tk

#ボタンが押された時に呼び出される
def print_txtval():
    val_en = en.get()
    print(val_en)

root = tk.Tk()
root.title('テキストボックス内容の取得')
root.geometry('350x150')
lb = tk.Label(text="ラベル")

#テキストボックスの作成
en = tk.Entry()
bt = tk.Button(text="ボタン",command=print_txtval)

[widget.pack() for widget in (lb,en,bt)]

root.mainloop()


################################
#クラスを使って雛形を作る
################################

import tkinter as tk

class Application(tk.Frame):

    '''
    初期設定
    '''
    def __init__(self,master=None):
        super().__init__(master)
        master.title('テキストボックス内容の取得')
        master.geometry('350x150')
        self.pack()
        self.create_widgets()

    '''
    部品作成
    '''
    def create_widgets(self):

        #ラベル作成
        self.lb = tk.Label(self)
        self.lb['text'] = "ラベル"
        self.lb.pack(side="top")

        #テキストボックス作成
        self.en = tk.Entry(self)
        self.en.pack()
        self.en.focus_set()

        #ボタン作成
        self.bt = tk.Button(self)
        self.bt['text'] = "ボタン"
        self.bt['command'] = self.print_txtval
        self.bt.pack(side='bottom')

    '''
    テキストボックスに入力された文字列を表示
    '''
    def print_txtval(self):
        val_en = self.en.get()
        print(val_en)

root = tk.Tk()
app = Application(master=root)
app.mainloop()


##################################################################################
# tkinterの各種ウィジェット
##################################################################################



