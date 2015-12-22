from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfile, askdirectory
from tkinter.messagebox import showerror, askokcancel, showinfo
import os
import webbrowser
master = Tk()
master.iconbitmap(default='PyPad.ico')
master.title("PyPad")
text = ""
pyregistry = "C:/Python32_32bit"
mainfontpath = "fontgui.TTF"
progLang = "Plain Text"
whereFileIs = None
runwords = False

# dictionary to hold words and colors
highlightWordsPy = {'if': 'orange',
                  'else': 'orange',
                  'str': 'purple',
                  'in': 'orange',
                  'elif': 'orange',
                  '\'': 'darkgreen',
                  '#': 'red',
                  '\'\'\'': 'red',
                  'BaseException': '#9932CC',
                  'Exception': '#9932CC',
                  'ArithmeticError': '#9932CC',
                  'BufferError': '#9932CC',
                  'LookupError': '#9932CC',
                  'EnvironmentError': '#9932CC',
                  'AssertionError': '#9932CC',
                  'AttributeError': '#9932CC',
                  'EOFError': '#9932CC',
                  'FloatingPointError': '#9932CC',
                  'GerneratorError': '#9932CC',
                  'IOError': '#9932CC',
                  'ImportError': '#9932CC',
                  'IndexError': '#9932CC',
                  'KeyError': '#9932CC',
                  'KeyboardInterrupt': '#9932CC',
                  'MemoryError': '#9932CC',
                  'NameError': '#9932CC',
                  'NotImplementedError': '#9932CC',
                  'OSError': '#9932CC',
                  'OverflowError': '#9932CC',
                  'ReferenceError': '#9932CC',
                  'RuntimeError': '#9932CC',
                  'StopIteration': '#9932CC',
                  'SyntaxError': '#9932CC',
                  'IndentationError': '#9932CC',
                  'TabError': '#9932CC',
                  'SystemError': '#9932CC',
                  'SystemExit': '#9932CC',
                  'TypeError': '#9932CC',
                  'UnboundLocalError': '#9932CC',
                  'UnicodeError': '#9932CC',
                  'UnicodeEncodeError': '#9932CC',
                  'UnicodeDecodeError': '#9932CC',
                  'UnicodeTranslateError': '#9932CC',
                  'ValueError': '#9932CC',
                  'VMSError': '#9932CC',
                  'WindowsError': '#9932CC',
                  'ZeroDivisionError': '#9932CC',
                  'Warning': '#cccc00',
                  'UserWarning': '#cccc00',
                  'DeprecationWarning': '#cccc00',
                  'PendingDeprecationWarning': '#cccc00',
                  'SyntaxWarning': '#cccc00',
                  'RuntimeWarning': '#cccc00',
                  'ImportWarning': '#cccc00',
                  'FutureWarning': '#cccc00',
                  'UnicodeWarning': '#cccc00',
                  'BytesWarning': '#cccc00',
                  'ResourceWarning': '#cccc00',
                  'try': 'orange',
                  'except': 'orange',
                  'from': 'orange',
                  'import': 'orange',
                  'int': 'purple',
                  'as': 'orange',
                  'for': 'orange',
                  'while': 'orange',
                  'range': 'blue',
                  'len': 'blue',
                  'True': 'darkorange',
                  'False': 'darkorange',
                  'def': 'darkorange',
                  'print': 'purple'
                  }

highlightWordsHtml = {'<': 'red',
                     '>': 'red',
                     '&nbsp;': 'orange',
                     '\'': 'purple',
                     '"': 'purple'
                     }

highlightWordsCss = {'{': 'darkgreen',
                    '}': 'darkgreen',
                    'url': 'darkcyan',
                    'color': 'darkorange',
                    'background': 'darkorange',
                    'border': 'darkorange',
                    'margin': 'darkorange',
                    'orange': 'pink',
                    'red': 'pink',
                    'green': 'pink',
                    'blue': 'pink',
                    'pink': 'pink',
                    'purple': 'pink',
                    'gray': 'pink',
                    '#': 'purple',
                    '.': 'purple',
                    ';': 'green',
                    'px': 'red',
                    'em': 'red',
                    'pc': 'red',
                    'in': 'red',
                    'cm': 'red',
                    '0': '#cccc00',
                    '1': '#cccc00',
                    '2': '#cccc00',
                    '3': '#cccc00',
                    '4': '#cccc00',
                    '5': '#cccc00',
                    '6': '#cccc00',
                    '7': '#cccc00',
                    '8': '#cccc00',
                    '9': '#cccc00',
                    '\'': 'green',
                    '"': 'green'
                    }

highlightWordsJs = {'alert': 'purple',
                   'prompt': 'purple',
                   'document': 'red',
                   'Date': 'red',
                   'window': 'red',
                   '$': 'cyan',
                   '*': 'darkcyan',
                   '/': 'darkcyan',
                   '-': 'darkcyan',
                   '+': 'darkcyan'
                   }

def highlighter(event):
    global progLang, highlightWordsJs, highlightWordsPy, highlightWordsHtml, highlightWordsCss
    highlightWords = None
    if progLang == "Python":
        highlightWords = highlightWordsPy
    elif progLang == "HTML":
        highlightWords = highlightWordsHtml
    elif progLang == "CSS":
        highlightWords = highlightWordsCss
    elif progLang == "JavaScript":
        highlightWords = highlightWordsJs
    else:
    	return
    for tag in mainbox.tag_names():
        mainbox.tag_delete(tag)
    '''the highlight function, called when a Key-press event occurs'''
    for k, v in highlightWords.items():  # iterate over dict
        startIndex = '1.0'
        while True:        
            startIndex = mainbox.search(k, startIndex, END)
            if startIndex:
                endIndex = mainbox.index('%s+%dc' % (startIndex, (len(k))))
                mainbox.tag_add(k, startIndex, endIndex)  # add tag to k
                mainbox.tag_config(k, foreground=v)      # and color it with v
                startIndex = endIndex  # reset startIndex to continue searching
            else:
                break


def selectall(event):
    event.widget.tag_add("sel", "1.0", "end")


def restart_program():
    if askokcancel("Restart Program",
                   "Do you wish to restart the program?" +
                   "\nThis will delete ALL of your progress."):
        python = sys.executable
        os.execl(python, python, * sys.argv)
    else:
        showinfo("Restart Program", "Request cancelled.")


def NewFile(f=0):
    print("New File!")
    mainbox.delete(1.0, END)
    master.title("PyPad")


def OpenFile(f=0):
    fname = askopenfilename()
    try:
        opened_file = open(fname, "r+")
        text = opened_file.read()
        mainbox.delete(1.0, END)
        mainbox.insert(END, text)
        global whereFileIs
        whereFileIs = fname
        master.title("PyPad - " + fname)
    except:
        showerror("PyPad - Error", "You have given an incorrect file.")


def SaveFile(f=0):
    global whereFileIs
    if whereFileIs is None:
        whereFileIs = tkinter.filedialog.asksaveasfile(mode='w')
        if whereFileIs is None:
            return
        text2save = str(mainbox.get(1.0, END))
        try:
            whereFileIs.write(text2save)
        except:
            whereFileIs = open(whereFileIs, "r+")
            whereFileIs.write(text2save)
    else:
        text2save = str(mainbox.get(1.0, END))
        try:
            whereFileIs.write(text2save)
        except:
            whereFileIs = open(whereFileIs, "r+")
            whereFileIs.write(text2save)
    try:
        master.title("PyPad - " + whereFileIs.name)
    except:
        master.title("PyPad - " + whereFileIs)
    whereFileIs.close()
    whereFileIs = open(whereFileIs.name, "r+")


def SaveFileAs(f=0):
    global whereFileIs
    SaveFileWhere = tkinter.filedialog.asksaveasfile(mode='w')
    if SaveFileWhere is None:
        return
    else:
        whereFileIs = SaveFileWhere
        SaveFile()


def About():
    print("This is a simple example of a menu")


class SettingsMenuFunc():
    def FontSet(huh=None):
        fontAsk = askopenfilename()
        global mainfontpath
        mainfontpath = fontAsk
        # fontget = Font(mainbox)
        # print([fontget])
        # fontget.config(family=mainfontpath)    # Modify font attributes
        # mainbox['font'] = fontget
        mainbox.config(font=mainfontpath)

    def PyRegistry():
        global pyregistry
        where = tkinter.filedialog.askdirectory()
        if where is None:
            return
        pyregistry = where
        print(where)


class ToolsMenuFunc:
    def cmdLanguageCSS():
        global progLang
        progLang = "CSS"

    def cmdLanguageJS():
        global progLang
        progLang = "JavaScript"

    def cmdLanguageHTML():
        global progLang
        progLang = "HTML"

    def cmdLanguageTEXT():
        global progLang
        progLang = "Plain Text"

    def cmdLanguagePY():
        global progLang
        progLang = "Python"

    def run(n=None):
        global progLang
        if whereFileIs is None:
            asking = askokcancel("Save File?",
                                 "File has not been saved. Save?")
            if not asking:
                return
            SaveFile()
        if progLang == "Python":
            try:
                os.system("C:/Python32_32bit/python.exe \"" +
                          whereFileIs.name + "\"")
            except:
                os.system("C:/Python32_32bit/python.exe \"" +
                          whereFileIs + "\"")
        elif progLang in ["HTML", "CSS", "JavaScript"]:
            try:
                webbrowser.open(whereFileIs.name)
            except:
                webbrowser.open(whereFileIs)

    def langCheck():
        global progLang
        print(progLang)
        showinfo("Coding Language", "You are using " + progLang + '.')

menu = Menu(master)
master.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile, accelerator="Ctrl+N")
master.bind_all("<Control-n>", NewFile)
filemenu.add_command(label="Open...", command=OpenFile, accelerator="Ctrl+O")
master.bind_all("<Control-o>", OpenFile)
filemenu.add_command(label="Save", command=SaveFile, accelerator="Ctrl+S")
master.bind_all("<Control-s>", SaveFile)
filemenu.add_command(label="Save As...", command=SaveFileAs,
                     accelerator="Ctrl+Shift+S")
master.bind_all("<Control-Shift-S>", SaveFileAs)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=master.quit, accelerator="Alt+F4")

settingsmenu = Menu(menu)
menu.add_cascade(label="Settings", menu=settingsmenu)
settingsmenu.add_command(label="Set Font", command=SettingsMenuFunc.FontSet)
settingsmenu.add_command(label="Restart", command=restart_program)


toolsMenu = Menu(menu)
menu.add_cascade(label="Tools", menu=toolsMenu)
progLangMenu = Menu(toolsMenu)
toolsMenu.add_cascade(label="Set Programming Language", menu=progLangMenu)
progLangMenu.add_command(label="CSS", command=ToolsMenuFunc.cmdLanguageCSS)
progLangMenu.add_command(label="HTML", command=ToolsMenuFunc.cmdLanguageHTML)
progLangMenu.add_command(label="JavaScript",
                         command=ToolsMenuFunc.cmdLanguageJS)
progLangMenu.add_command(label="Plain Text",
                         command=ToolsMenuFunc.cmdLanguageTEXT)
progLangMenu.add_command(label="Python", command=ToolsMenuFunc.cmdLanguagePY)
toolsMenu.add_command(label="Run", command=ToolsMenuFunc.run,
                      accelerator="Ctrl+R")
master.bind_all("<Control-r>", ToolsMenuFunc.run)
toolsMenu.add_command(label="Coding Language", command=ToolsMenuFunc.langCheck)
toolsMenu.add_command(label="Change Directory of Python",
                      command=SettingsMenuFunc.PyRegistry)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)
menu.entryconfig("Help", state="disabled")


mainbox = Text(master, font=mainfontpath, width=100,
               height=25, yscrollcommand=None)
scrollbar = Scrollbar(master)
scrollbar.pack(side=RIGHT, fill=Y)
mainbox.pack(fill=BOTH, expand=1)
mainbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=mainbox.yview)
mainbox.bind('<Key>', highlighter)  # bind key event to highlighter()
master.bind_class("Text", "<Control-a>", selectall)


mainloop()
