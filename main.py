import tkinter as tk
import math
window = tk.Tk()
window.title('波段')
window.geometry('400x300')

def _principal_percent(event):
#    try:
#        CheckVar = CheckVar1.get()
#    except:
#        CheckVar = 0
    try:
        buy = float(buy_entry.get())
    except:
        buy = 0
    try:
        stoploss = float(stop_loss_entry.get())
    except:
        stoploss = 0
    try:
        principal = float(principal_entry.get())
    except:
        principal = 0
    try:
        percent = float(percent_entry.get())/100
    except:
        percent = 0
    try:
        multiplier = float(multiplier_entry.get())/100
    except:
        multiplier = 1    
    value = round(principal * percent)
    sell = buy - (buy*(stoploss/100)*multiplier)
    try:
        sheets_number_formula =  math.floor((value-((buy*0.001425)+(sell*0.001425)+(sell*0.03))/(buy-sell)))
    except:
        sheets_number_formula = 0
    result = 'R：{}'.format(value)
    result2 = '張數：{} '.format(str(sheets_number_formula))
    return _principal_percent_text.set(result),_sheets_number_text.set(result2)

def _buy_estimated_cost_text(event):
    try:
        buy = float(buy_entry.get())
    except:
        buy = 0
    try:
        stoploss = float(stop_loss_entry.get())
    except:
        stoploss = 0
    try:
        principal = float(principal_entry.get())
    except:
        principal = 0
    try:
        percent = float(percent_entry.get())/100
    except:
        percent = 0
    try:
        multiplier = float(multiplier_entry.get())/100
    except:
        multiplier = 1    
    value = round(principal * percent)
    sell = buy - (buy*(stoploss/100)*multiplier)
    formula = buy*1000*0.001425
    try:
        sheets_number_formula =  math.floor((value-((buy*0.001425)+(sell*0.001425)+(sell*0.03))/(buy-sell)))
    except:
        sheets_number_formula = 0
    result = '預估成本：{}'.format(str(formula))
    result2 = '張數：{} '.format(str(sheets_number_formula))
    return _buy_estimated_cost_text.set(result),_sheets_number_text.set(result2)

def _sell_text(event):
    try:
        buy = float(buy_entry.get())
    except:
        buy = 0
    try:
        stoploss = float(stop_loss_entry.get())
    except:
        stoploss = 0
    try:
        principal = float(principal_entry.get())
    except:
        principal = 0
    try:
        percent = float(percent_entry.get())/100
    except:
        percent = 0
    try:
        multiplier = float(multiplier_entry.get())/100
    except:
        multiplier = 1    
    value = round(principal * percent)
    sell = buy - (buy*(stoploss/100)*multiplier)
    formula = (sell*1000*0.001425)+(sell*1000*0.003)
    try:
        sheets_number_formula =  math.floor((((value-((buy*1000*0.001425)+(sell*1000*0.001425)+(sell*1000*0.003)))/(buy-sell)))/1000)
    except:
        sheets_number_formula = 0
    result = '賣：{} '.format(str(sell))
    result1 = '預估成本：{} '.format(str(formula))
    result2 = '張數：{} '.format(str(sheets_number_formula))
    return _sell_text.set(result),_sell_estimated_cost_text.set(result1),_sheets_number_text.set(result2)

#def Change():
#    try:
#        CheckVar = CheckVar1.get()
#    except:
#        CheckVar = 0
#    if (CheckVar == 1):
#        buy_label['text'] = "賣"
#    elif(CheckVar == 0):
#        buy_label['text'] = "買"
#    result = '賣：test'
#    result1 = '預估成本：test '
#    result2 = '張數：test'
#    return _sell_text.set(result),_sell_estimated_cost_text.set(result1),_sheets_number_text.set(result2)
        
first_row_frame = tk.Frame(window)
first_row_frame.pack(side=tk.TOP)

#CheckVar1 = tk.IntVar()
#checkbox = tk.Checkbutton(first_row_frame, text='空',variable=CheckVar1, onvalue=1, offvalue=0,command=Change)
#checkbox.pack()

principal_label = tk.Label(first_row_frame, text='本金：')
principal_label.pack(side=tk.LEFT)
principal_entry = tk.Entry(first_row_frame)
principal_entry.bind('<KeyRelease>', _principal_percent)
principal_entry.pack(side=tk.LEFT)

percent_label = tk.Label(first_row_frame, text='%：')
percent_label.pack(side=tk.LEFT)
percent_entry = tk.Entry(first_row_frame)
percent_entry.bind('<KeyRelease>', _principal_percent)
percent_entry.pack(side=tk.LEFT)

_principal_percent_text = tk.StringVar()
R_label = tk.Label(window, textvariable=_principal_percent_text,font=('Arial', 20))
R_label.pack()


second_row = tk.Frame(window)
second_row.pack(side=tk.TOP)

buy_label = tk.Label(second_row, text='買：')
buy_label.pack(side=tk.LEFT)
buy_entry = tk.Entry(second_row)
buy_entry.bind('<KeyRelease>', _buy_estimated_cost_text)
buy_entry.pack(side=tk.LEFT)

_buy_estimated_cost_text = tk.StringVar()
estimated_cost_label = tk.Label(window, textvariable=_buy_estimated_cost_text,font=('Arial', 20))
estimated_cost_label.pack()

third_row = tk.Frame(window)
third_row.pack(side=tk.TOP)

stop_loss_label = tk.Label(third_row, text='停損：')
stop_loss_label.pack(side=tk.LEFT)
stop_loss_entry = tk.Entry(third_row)
stop_loss_entry.bind('<KeyRelease>' ,_sell_text)
stop_loss_entry.pack(side=tk.LEFT)
stop_loss_label = tk.Label(third_row, text='%')
stop_loss_label.pack(side=tk.LEFT)
multiplier_entry = tk.Entry(third_row)
multiplier_entry.bind('<KeyRelease>' ,_sell_text)
multiplier_entry.pack(side=tk.RIGHT)

_sell_text = tk.StringVar()
sell_label = tk.Label(window, textvariable=_sell_text,font=('Arial', 20))
sell_label.pack()

_sell_estimated_cost_text = tk.StringVar()
_sell_estimated_cost_label = tk.Label(window, textvariable=_sell_estimated_cost_text,font=('Arial', 20))
_sell_estimated_cost_label.pack()

_sheets_number_text = tk.StringVar()
_sheets_number_label = tk.Label(window, textvariable=_sheets_number_text,font=('Arial', 20))
_sheets_number_label.pack()

window.mainloop()