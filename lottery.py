import tkinter as tk
from tkinter import ttk
import random

# 抽奖函数
def draw_lottery():
    prizes = ["一等奖", "二等奖", "三等奖", "感谢参与"]
    weights = [0.001, 0.1, 0.3, 1-0.001-0.1-0.3]  # 设置不同奖项的概率权重
    prize = random.choices(prizes, weights=weights, k=1)[0]  # k=1表示选择一个元素
    label_result.config(text=f"恭喜你获得: {prize}")

# 创建主窗口
root = tk.Tk()
root.title("抽奖程序")

# 设置窗口大小
root.geometry("300x150")

# 创建一个标签显示抽奖结果
label_result = ttk.Label(root, text="点击下方按钮开始抽奖", font=("Arial", 12))
label_result.pack(pady=20)

# 创建抽奖按钮
button_draw = ttk.Button(root, text="抽奖", command=draw_lottery)
button_draw.pack()

# 运行主循环
root.mainloop()
