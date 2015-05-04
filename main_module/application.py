import base64
import logging
import tempfile
import tkinter
import tkinter.messagebox
import zlib

import annotation_tools.annotation_filtering_frame as filtering_frame
import annotation_tools.annotation_tagging_frame as tagging_frame

FILTER_MODE = 'filter'
TAG_MODE = 'tag'

class Application(tkinter.Frame):
    def __init__(self, master=None):
        self.logger = logging.getLogger('smok3_tagg3r')

        tkinter.Frame.__init__(self, master)

        self.master.title('Smok3 Tagg3r')
        self.master.iconbitmap(default=TRANSPARENT_ICON_PATH)

        self.grid()

        self.menu_parent = tkinter.Menu(master=self)

        self.mode = FILTER_MODE

        file_menu = tkinter.Menu(self.menu_parent, tearoff=0)
        file_menu.add_command(label='Exit', command=self.quit)

        mode_menu = tkinter.Menu(self.menu_parent, tearoff=0)
        mode_menu.add_command(label="'Filtering' mode", command=self.switch_mode)
        mode_menu.add_separator()
        mode_menu.add_command(label="'Tagging' mode", command=self.switch_mode)

        help_menu = tkinter.Menu(self.menu_parent, tearoff=0)
        help_menu.add_command(label='About...', command=self.show_about_info)
        help_menu.add_separator()
        help_menu.add_command(label='How to use this program', command=self.show_usage_info)

        self.master.config(menu=self.menu_parent)
        self.menu_parent.add_cascade(label='File', menu=file_menu)
        self.menu_parent.add_cascade(label='Mode', menu=mode_menu)
        self.menu_parent.add_cascade(label='Help', menu=help_menu)

        self.init_filter_mode()

    def switch_mode(self):
        widgets = self.winfo_children()
        for widget in widgets:
            if widget != self.menu_parent:
                widget.destroy()

        if self.mode == FILTER_MODE:
            self.mode = TAG_MODE
            self.init_tagging_mode()
        elif self.mode == TAG_MODE:
            self.mode = FILTER_MODE
            self.init_filter_mode()
        else:
            self.mode = FILTER_MODE
            self.init_filter_mode()

    def init_filter_mode(self):
        self.logger.info('Switching to filter mode')
        tkinter.Label(self, text='FILTER MODE', bg='light blue', fg='black', font='Times 20 bold').grid(row=0, column=0)
        filtering_frame.AnnotationFilteringFrame(parent = self).grid(row = 1, column = 0)

    def init_tagging_mode(self):
        self.logger.info('Switching to tagging mode')
        tkinter.Label(self, text='TAGGING MODE', bg='light green', fg='black', font='Times 20 bold').grid(row=0,
                                                                                                          column=0)
        tagging_frame.AnnotationTaggingFrame(parent = self).grid(row = 1, column = 0)

    def show_about_info(self):
        tkinter.messagebox.showinfo(title='About', message=ABOUT_MESSAGE)

    def show_usage_info(self):
        tkinter.messagebox.showinfo(title='Usage', message=USAGE_MESSGAE)


TRANSPARENT_ICON = zlib.decompress(base64.b64decode('eJxjYGAEQgEBBiDJwZDBy'
                                                    'sAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc='))

_, TRANSPARENT_ICON_PATH = tempfile.mkstemp()
with open(TRANSPARENT_ICON_PATH, 'wb') as icon_file:
    icon_file.write(TRANSPARENT_ICON)

ABOUT_MESSAGE = \
"""
This program was written in Python 3.4.3 using the tkinter GUI library.

This program uses the GPL v2.0 software license (for now).

This program was created by Terence Henriod, who can offer
minimal (and probably delayed) support if you contact him at
t-r0d@hotmail.com (that's a zero in 't-r0d').
(But at least there's an offer for support)
"""

USAGE_MESSGAE = \
"""
How do I use this? Instructions are under development.
"""