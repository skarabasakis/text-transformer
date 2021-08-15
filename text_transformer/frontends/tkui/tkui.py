import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
from text_transformer import transformers

def transform(text, transformer_name):
    return getattr(transformers, transformer_name)(text)

def transform_button_clicked(gui):
    transformer_option = gui.get_variable('transformer_option').get()
    input_text = gui.get_object('input_text').get('1.0', 'end-1c')
    output_text = transform(input_text, transformer_option)

    output_text_widget = gui.get_object('output_text')
    output_text_widget.delete('1.0', tk.END)
    output_text_widget.insert(tk.INSERT, output_text)

def clear_button_clicked(gui):
    gui.get_variable('transformer_option').set(None)
    gui.get_object('input_text').delete('1.0', tk.END)
    gui.get_object('output_text').delete('1.0', tk.END)

def run():
    global gui
    gui = pygubu.Builder()
    gui.add_from_file('data/tkui/mainwindow.ui')
    window = gui.get_object('main_window')
    gui.connect_callbacks({
        'transform_button_clicked': lambda: transform_button_clicked(gui),
        'clear_button_clicked':  lambda: clear_button_clicked(gui),
    })
    window.mainloop()
