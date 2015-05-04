#!/usr/bin/python3

import tkinter

from main_module.application import Application

TEST_NUM_REGIONS = 4
UNR_LOGO_FILE_NAME = 'C:/Users/Terence/Pictures/unr.jpg'
FIRE_FILE_NAME = 'C:/Users/Terence/Desktop/Homewood_BGsmokey.050_10.d/Homewood_BGsmokey.050_10.d/image-2019.jpeg'
TEST_JSON_FILE_NAME = 'C:/Users/Terence/Documents/GitHub/STAT775/GuiProject/z_test_resources/test_annotations00.json'

def main():

    # NEXT STEPS:
    #  - implement 'free-tag' mode
    #  - complete the menus
    #  - setup some kind of easy install method

    my_app = Application()
    my_app.mainloop()


def init_selection_buttons(parent):
    region_buttons = []
    for i in range(0, TEST_NUM_REGIONS):
        region_buttons.append(tkinter.Button(parent, text="{}".format(i), width=25, command=parent.destroy))
    region_buttons.append(tkinter.Button(parent, text="No regions with smoke!", width=25, command=parent.destroy))
    for button in region_buttons:
        button.pack()


def init_checkboxes(parent, num_boxes, start_row):
    region_selections = []
    for i in range(0, num_boxes + 1):
        region_selections.append(tkinter.IntVar())
        b = tkinter.Checkbutton(parent, text="Region {}".format(i), variable=region_selections[i])
        b.grid(row=start_row + i, column=1)

    def show_check_responses():
        print('Selections:')
        for selection in region_selections:
            print(selection.get())

    show_button = tkinter.Button(parent, text="show", width=20, command=show_check_responses)
    show_button.grid(row=start_row, column=1)

    return region_selections


if __name__ == '__main__':
    main()
