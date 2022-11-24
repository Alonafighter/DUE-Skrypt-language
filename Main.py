from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
import Character
from os import path


def save():
    if character_name.get() != '' and character_race.get() != '' and character_class.get() != '':
        character = Character.Character(character_name.get(), character_class.get(), character_race.get())
        f = open('sheet.txt', 'w')
        f.write(f"{character.name}\n{character.classification}\n{character.race}")
        f.close()


def reset():
    character_name.set('')
    character_race.set('')
    character_class.set('')


def load():
    file_path_string = filedialog.askopenfilename()
    if path.exists(file_path_string):
        f = open(file_path_string, 'r')
        file_import = f.readlines()
        f.close()
    else:
        return
    character_name.set(file_import[0])
    character_class.set(file_import[1])
    character_race.set(file_import[2])


main_window = Tk()
main_window.geometry('300x400')
main_window.title('DnD Sheet Editor')

bottom_frame = Frame(main_window)
bottom_frame.pack(side=BOTTOM)
save_frame = Frame(bottom_frame)
save_frame.pack(side=LEFT)

character_name = StringVar()
character_class = StringVar()
character_race = StringVar()
race_list = ['Human', 'Dwarf', 'Elf', 'Gnome', 'Halfling', 'Half-orc']
class_list = ['Warrior', 'Barbarian', 'Warlock', 'Mage', 'Paladin', 'Cleric', 'Hunter', 'Rouge']


Label(main_window, text='Character Name').pack()
Entry(main_window, textvariable=character_name).pack()

Label(main_window, text='Character Class').pack()
Combobox(main_window, values=class_list, textvariable=character_class).pack()

Label(main_window, text='Character Race').pack()
Combobox(main_window, values=race_list, textvariable=character_race).pack()

Button(save_frame, text='Save', command=save).pack(side=LEFT)
Button(save_frame, text='Load', command=load).pack(side=RIGHT)
Button(bottom_frame, text='Reset', command=reset).pack(side=RIGHT)

mainloop()