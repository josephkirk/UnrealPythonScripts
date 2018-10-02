#!/usr/bin/python3
import unreal_engine as ue
import unreal.QWidgets as uQWidgets
import json
from os import path
from inspect import ismodule, ismethod, isclass, isfunction
docPath = "D:/Works/Code/Unreal/docs"
def get_error(fnc):
    try:
        result = fnc()
    except Exception as why:
        result = (fnc, why)
    return result

def gen_doc(mod):
    docdict = {m:("{}__{}".format(n, n.__class__), dir(n))
        for m,n in mod.__dict__.items() if not m.startswith("_")}
    
    with open(path.join(docPath,"{}.py".format(mod)), 'w') as write_file:
        json.dump(docdict, write_file, indent=4, sort_keys=True, separators=(',\n', ':\n\t    '))

def gen_docs():
    gen_doc(unreal_engine)
    gen_doc(uQWidgets)

    uedict = {m:[(i,str(get_error(f))) for i,f in n.__dict__.items()] for m,n in ue.__dict__.items()
        if not m.startswith("_") and any(testType(n) for testType in 
            [ismodule, ismethod, isclass, isfunction])}

    for method, docs in uedict.items():
        with open(path.join(docPath,"{}.py".format(method)), 'w') as write_file:
            json.dump(docs, write_file, indent=4, sort_keys=True, separators=(',\n', ':\n\t    '))