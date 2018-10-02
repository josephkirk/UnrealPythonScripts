#!/usr/bin/python3
import unreal_engine as ue
import os
from re import compile
from unreal_engine import SWindow, SVerticalBox, SButton, SPythonListView, SHeaderRow, STextBlock
def show():
    rootDir = ue.get_content_dir()
    matchType = compile(r'\.uasset\Z')
    folders = (root for root, subdirs, files in os.walk(rootDir) if any(matchType.search(file) for file in files))
    window = SWindow().resize(512,1024).set_title("Export Static Mesh")
    vertical = SVerticalBox()
    vertical.add_slot(STextBlock().set_text("Export Folders:"), v_align=2, h_align=0)
    for folder in folders:
        button = SButton().set_content(STextBlock().set_text(os.path.relpath(folder, rootDir))).set_v_align(2)
        #vertical.add_slot(button, v_align=2, h_align=2)
        vertical.add_slot(button, v_align=0, h_align=0)
    window.set_content(vertical)
    #window.set_modal(True)