# 夏休み終盤にリハビリがてら、tkinterで電卓作ってみた！

import tkinter as tk
from tkinter import ttk

BUTTONS = [
    ['', 'B', 'C', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['00', '0', '.', '=']
]

SYMBOL = ['+', '-', '*', '/']

class CalcGui():
    def __init__(self, root):

        self.calc_str = ''

        root.title('電卓')
        root.geometry('300x510+700+150')
        self.calc_frame, self.button_frame = self.tkinter_frame(root)
        self.frame_content(self.calc_frame)


    def tkinter_frame(self,root):
        calc_frame = tk.Frame(root, width=300, height= 105)
        # サイズ固定
        calc_frame.propagate(False)
        # pack は widget を縦または横に１次元的に配列するときに使う
        # side は packのオプションで、配置方向を、上、下、左、右の中から指定
        # 参考サイト : https://imagingsolution.net/program/python/tkinter/widget_layout_pack/
        calc_frame.pack(side=tk.TOP, pady=10)

        button_frame = tk.Frame(root, width=300, height=405)
        button_frame.propagate(False)
        button_frame.pack(side=tk.TOP)
        return calc_frame, button_frame


    def frame_content(self, calc_frame):
        self.calc_var = tk.StringVar()
        self.ans_var = tk.StringVar()

        # widthとheightは、「指定した値×１文字の幅」になる→フォントサイズに依存するため、ここで指定はしない
            # 本来？は、pixelらしい
        calc_label = tk.Label(calc_frame, textvariable=self.calc_var, font=("",30), bg='ghost white')
        ans_label = tk.Label(calc_frame, textvariable=self.ans_var, font=("",15), bg='ghost white')

        # anchorキーワードを指定することで、ラベルの文字列自体をラベル内のどこの方向に寄せるかを設定することができる
        # expand：親フレームの余ったスペースに対して，その分配を決定
            # expandは比率を上手いこと分配をしてくれる　→　今回でいうと、文字幅(縦)のみだと、親Frameの内側の高さに余りのスペースができてしまうが、それを埋めてくれる
        # fill：該当フレームの利用可能なスペースに対して，指定された方向に拡大
            # fill=tk.BOTH は，縦方向と横方向の両方に拡張
        calc_label.pack(anchor=tk.E, fill=tk.BOTH, expand=True)
        ans_label.pack(anchor=tk.E, fill=tk.BOTH, expand=True)

        self.button_placement(self.button_frame)


    def button_placement(self, button_frame):
        for y, line in enumerate(BUTTONS, 1):
            for x, num in enumerate(line):
                button = tk.Button(button_frame, text=num, font=("", 15), width=6, height=3)
                button.grid(row=y, column=x)
                button.bind('<ButtonPress>', self.click_button)


    def click_button(self, event):
        check = event.widget['text']

        if check == "=":
            if self.calc_str[-1:] in SYMBOL:
                self.calc_str= self.calc_str[:-1]

            res = "= " + str(eval(self.calc_str))
            self.ans_var.set(res)

        elif check == "C":
            self.calc_str = ''
            self.ans_var.set('')

        elif check == "B":
            self.calc_str = self.calc_str[:-1]

        elif check in SYMBOL: # calc_strの最後の文字が記号以外の場合、そのまま記号を追加
            if self.calc_str[-1:] not in SYMBOL and self.calc_str != '':
                self.calc_str += check
            elif self.calc_str[-1:] in SYMBOL: # calc_strの最後の文字が記号の場合、記号を置き換える
                self.calc_str = self.calc_str[:-1] + check

        else: # 数字の場合
            self.calc_str += check

        self.calc_var.set(self.calc_str)


def main():
    root = tk.Tk()
    root.resizable(width=False, height=False)
    root.configure(bg='snow')
    CalcGui(root)
    root.mainloop()

if __name__ == '__main__':
    main()