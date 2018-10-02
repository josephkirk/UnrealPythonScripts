#!/usr/bin/python3
import unreal_engine as ue
import os
from re import compile, match
from functools import partial
#from .. import unreal_libs as ul
from unreal_engine import SWindow, SVerticalBox, SButton, SPythonListView, SHeaderRow, STextBlock, SFilePathPicker, FLinearColor
from unreal_engine.structs import ButtonStyle, SlateBrush, SlateColor
def path_picked(path):
    print(path)
    #window.request_destroy()
def export(uobjects,dir):
    ue.export_assets(uobjects, dir)
    print("export {} objects:\n{}".format(len(uobjects), str(uobjects)) )
def show():
    #Data
    saveDir = r"\\vietsap002\projects\R6\04_WIP\tools\perforce\proxyCheck"
    rootDir = ue.get_content_dir()
    matchType = compile(r'\.uasset\Z')
    allstaticmeshes = ue.get_assets_by_class("StaticMesh")
    uassetfolders = ((root,files) for root, subdirs, files in os.walk(rootDir)
        if any(matchType.search(file) for file in files))
    filterstaticmeshfolder = ((folder, list(
            staticmesh for staticmesh in allstaticmeshes
            if any(match("^{}".format(staticmesh.get_name()), ufile) for ufile in ufiles )))
        for folder, ufiles in uassetfolders)
    staticmeshfolder = ((folder, files) for folder, files in filterstaticmeshfolder if files)
    #UI
    window = SWindow().resize(512,1024).set_title("Export Static Mesh")
    vertical = SVerticalBox()
    #style = ButtonStyle(Normal=SlateBrush(TintColor=SlateColor(SpecifiedColor=FLinearColor(1, 0, 0))))
    #picker = SFilePathPicker(browse_title='Export To', browse_button_style=style, on_path_picked=path_picked)
    button = SButton().set_content(STextBlock().set_text("Export All").set_v_align(2)
    vertical.add_slot(button, v_align=0, h_align=0)
    vertical.add_slot(STextBlock().set_text("Export Folders:"), v_align=0, h_align=0)
    vertical.add_slot(picker, v_align=0, h_align=0)
    vertical.add_slot(STextBlock().set_text("Static Mesh Folders:"), v_align=0, h_align=0)
    for folder, ufiles in staticmeshfolder:
        button = SButton().set_content(STextBlock().set_text(os.path.relpath(folder, rootDir))).set_v_align(2)
        button.bind_on_clicked(partial(export, ufiles, saveDir))
        #vertical.add_slot(button, v_align=2, h_align=2)
        vertical.add_slot(button, v_align=0, h_align=0)
    window.set_content(vertical)
    #window.set_modal(True)
show()