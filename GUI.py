from guizero import App, Text, PushButton, Box
import Rune

rc = Rune.RuneCounter()

def add_to_val(num):
    rc.runes[rc.get_rune_name(num)].add_one()
    column0_size = int(rc.get_size()/2 + 1)
    if (num < column0_size):
        rune_vals0[num].value=rc.runes[rc.get_rune_name(num)].get_count()
    else:
        rune_vals1[num - column0_size].value=rc.runes[rc.get_rune_name(num)].get_count()

def subtract_to_val(num):
    rc.runes[rc.get_rune_name(num)].subtract_one()
    column0_size = int(rc.get_size()/2 + 1)
    if (num < column0_size):
        rune_vals0[num].value=rc.runes[rc.get_rune_name(num)].get_count()
    else:
        rune_vals1[num - column0_size].value=rc.runes[rc.get_rune_name(num)].get_count()

def load():
    rc.load_file()
    i = 0
    for rv in rune_vals0:
        rv.value=rc.runes[rc.get_rune_name(i)].get_count()
        i+=1
    for rv in rune_vals1:
        rv.value=rc.runes[rc.get_rune_name(i)].get_count()
        i+=1

def save():
    rc.save_file()

app = App(bg='grey')
menu = Box(app, layout='grid')
#rune_list = Box(app, layout='grid')
rune_lists = Box(app, layout='grid') #update

save = PushButton(menu, text='Save Runes', command=save, grid=[0,0])
load = PushButton(menu, text='Load Runes', command=load, grid=[1,0])
list_column0 = Box(rune_lists, layout='grid', grid=[0,0]) #update
list_column1 = Box(rune_lists, layout='grid', grid=[1,0]) #update

'''
rune_types = [Text(rune_list, text=rc.get_rune_name(num) + ':', grid=[0,num]) for num in range(rc.get_size())]
rune_vals = [Text(rune_list, text=rc.runes[rc.get_rune_name(num)].get_count(), grid=[1,num]) for num in range(rc.get_size())]

rune_add_buttons = [PushButton(rune_list, text='+', grid=[2,num], command=add_to_val, args=[num]) for num in range(rc.get_size())]
rune_subtract_buttons = [PushButton(rune_list, text='-', grid=[3,num], command=subtract_to_val, args=[num]) for num in range(rc.get_size())]
'''

# ''' update
# rune column 0
rune_types0 = [Text(list_column0, text=rc.get_rune_name(num) + ':', grid=[0,num]) for num in range(int(rc.get_size()/2) + 1)]
rune_vals0 = [Text(list_column0, text=rc.runes[rc.get_rune_name(num)].get_count(), grid=[1,num]) for num in range(int(rc.get_size()/2) + 1)]

rune_add_buttons0 = [PushButton(list_column0, text='+', grid=[2,num], command=add_to_val, args=[num]) for num in range(int(rc.get_size()/2) + 1)]
rune_subtract_buttons0 = [PushButton(list_column0, text='-', grid=[3,num], command=subtract_to_val, args=[num]) for num in range(int(rc.get_size()/2)+ 1)]

#rune column 1
rune_types1 = [Text(list_column1, text=rc.get_rune_name(num) + ':', grid=[0,num]) for num in range(int(rc.get_size()/2) + 1, rc.get_size())]
rune_vals1 = [Text(list_column1, text=rc.runes[rc.get_rune_name(num)].get_count(), grid=[1,num]) for num in range(int(rc.get_size()/2) + 1, rc.get_size())]

rune_add_buttons1 = [PushButton(list_column1, text='+', grid=[2,num], command=add_to_val, args=[num]) for num in range(int(rc.get_size()/2) + 1 ,rc.get_size())]
rune_subtract_buttons1 = [PushButton(list_column1, text='-', grid=[3,num], command=subtract_to_val, args=[num]) for num in range(int(rc.get_size()/2)+ 1, rc.get_size())]
# '''

app.display()
