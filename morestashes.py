#from SupportingScripts import filehandle
import tkinter as tk
from tkinter import ttk 
import ttkbootstrap as ttkb
from SupportingScripts import filehandle
import os
import time


def main():
    style = ttkb.Style('darkly')
    root = style.master
    #value intiliazing
    saveManager = filehandle.FileHandler()
    numberOfActive = 8
    statsToDisplay = 8
    columnsOfInactive = 10
    rowsOfInactive = 50
    lastActive = ttkb.IntVar()
    currentActive = ttkb.IntVar()
    lastInactive = ttkb.IntVar()
    currentInactive = ttkb.IntVar()



    storageUsedActive = 40
    
    #GUI setup begins:
    #main window setup

    root.title('DMD More Stash')
    root.iconbitmap('Assets/MS.ico')
    root.state('zoomed')
    root.minsize(1050, 600)
    styleHeader = 'primary'
    styleActiveOuter = 'primary'
    styleActionsOuter = 'primary'
    styleInactiveOuter = 'primary'
    styleActive = 'info'
    styleActions = 'info'
    styleInactive = 'info'

    #Setup Frames
    headerFrame = ttkb.Frame(root, style=f'{styleHeader}')
    
    activeStashFrameOuter = ttkb.Frame(root, style=styleActiveOuter)
    actionsFrameOuter = ttkb.Frame(root, style=styleActionsOuter)
    inactiveStashFrameOuter = ttkb.Frame(root, style=f'{styleInactiveOuter}')
    
    activeStashFrame = ttkb.Frame(activeStashFrameOuter, style=styleActive)
    actionsFrame = ttkb.Frame(actionsFrameOuter, style=styleActions)
    inactiveStashFrame = ttkb.Frame(inactiveStashFrameOuter, style=styleInactive)

    headerLabel = ttkb.Label(headerFrame, text='More Stashes', font=('ariel', 20), anchor='center', bootstyle=f'{styleHeader}, inverse')
    warningLabel = ttkb.Label(headerFrame, text='WARNING: This product is mostly untested. You are the only one responsible for your data safety. Ensure that any files are backed up from "\\AppData\\LocalLow\\Realm Archive\\Death Must Die\\Saves" before using this program. Further, it is recommended that you use this program while the game is completely shut down. ',
    font=('ariel', 16), bootstyle = 'danger, inverse')
    activeStashHeader = ttkb.Label(activeStashFrameOuter, text='Active Stash Tabs', font=('ariel', 18), anchor='center', bootstyle=f'{styleActiveOuter}, inverse')
    actionsHeader = ttkb.Label(actionsFrameOuter, text='Actions', font=('ariel', 18), anchor='center', bootstyle=f'{styleActionsOuter}, inverse')
    inactiveStashHeader = ttkb.Label(inactiveStashFrameOuter, text='Inactive Stash Tabs', font=('ariel', 18), anchor='center', bootstyle=f'{styleInactiveOuter}, inverse')

    headerFrame.pack(side='top', fill='x', padx='10', pady='5')
    activeStashFrameOuter.pack(side='left', fill='both', expand=True, padx='10', pady='5')
    actionsFrameOuter.pack(side='left', fill='both', expand=True, padx='10', pady='5')
    inactiveStashFrameOuter.pack(side='left', fill='both', expand=True, padx='10', pady='5')
    headerLabel.pack(padx=10, pady=10)
    warningLabel.pack(padx=10, pady = 2, fill='both', expand=True, side='top')
    warningLabel.config(anchor='center', wraplength=800)

    #Active Storage
    activeStashHeader.pack(side='top', fill='x', pady='2')
    actionsHeader.pack(side='top', fill='x', pady='2')
    inactiveStashHeader.pack(side='top', fill='x', pady='2')

    progressLabel = ttkb.Label(activeStashFrameOuter, bootstyle=f'{styleActiveOuter}, inverse', text='used:', font=('ariel', 10), anchor='center')
    progressLabel.pack()


    activeStorageBar = ttkb.Progressbar(activeStashFrameOuter, bootstyle=f'info, Striped', value=75)
    activeStorageBar.pack(fill='x', padx=20, pady=5)
    activeStorageStats = []    
    for i in range(statsToDisplay):
        activeStorageStats.append(ttkb.Label(activeStashFrameOuter, text=f'stat {i+1}: Placeholder', bootstyle=f'{styleActiveOuter}, inverse', font=('ariel', 8), anchor='center'))
        activeStorageStats[i].pack(expand=True, padx=10, pady=5)
    activeStashFrame.pack(side='bottom', fill='both', expand=False, padx='2', pady='5')

    activeStashCanvas = ttkb.Canvas(activeStashFrame)
    activeStashScrollBar = ttkb.Scrollbar(activeStashFrame, orient='vertical', command=activeStashCanvas.yview)
    activeStashCanvas.configure(yscrollcommand=activeStashScrollBar.set)
    activeStashScrollBar.pack(side='right', padx=2, pady=5, fill='y')
    activeStashCanvas.pack(fill='both', expand=True)
    ASBFrame = ttkb.Frame(activeStashCanvas)
    ASBFrame.pack(fill='both', expand=True)
    activeStashCanvas.create_window((0,0), window=ASBFrame, anchor='nw', tags='ASBFrame')

    def ASBFconfig(event):
        activeStashCanvas.configure(scrollregion=activeStashCanvas.bbox('all'))
        width = event.width
        activeStashCanvas.itemconfig('ASBFrame', width=width)
        ASBFrame.config(width=width)

    activeStashCanvas.bind('<Configure>', ASBFconfig)

    def ASBFmousewheel(event):
        activeStashCanvas.yview_scroll(int(-1*(event.delta/120)), 'units')
    ASBFrame.bind("<Enter>", lambda event: ASBFrame.bind_all('<MouseWheel>', lambda e: ASBFmousewheel(e)))
    ASBFrame.bind("<Leave>", lambda event: ASBFrame.unbind_all('<MouseWheel>'))


    activeStashButtons = []
    for i in range(numberOfActive):
        def buttonAction(x=i):
            lastActive.set(currentActive.get())
            currentActive.set(x)
        activeStashButtons.append(ttkb.Button(ASBFrame, text=f'Stash {i+1}', bootstyle=f'{styleActive}, outline', command=buttonAction))
        activeStashButtons[i].pack(side='top', fill='both', expand=True, padx=5, pady=3)
    #Actions
    actionsFrame.pack(side='bottom', fill='both', expand=True, padx='2', pady='5')

    exportIndex = ttkb.IntVar()
    def exportAndUpdate():
        exportIndex.set(saveManager.export()) #exports stash and returns index of what place it had to write to
    actionButtonExport = ttkb.Button(actionsFrame, text='<- Export', bootstyle=styleActions, command=exportAndUpdate)

    swapStatusImport = ttkb.BooleanVar()
    swapStatusExport = ttkb.BooleanVar()
    def swapAndUpdate():
        exported, imported = saveManager.swap()
        swapStatusImport.set(imported)
        swapStatusExport.set(exported)
    actionButtonSwap = ttkb.Button(actionsFrame, text='<- Swap ->', bootstyle=styleActions, command=swapAndUpdate)

    deleteStatus = ttkb.IntVar()
    def deleteAndUpdate():
        deleteStatus.set(saveManager.delete())
    actionButtonDelete = ttkb.Button(actionsFrame, text='Delete ->', bootstyle='warning', command=deleteAndUpdate)
    actionButtons=[actionButtonExport, actionButtonSwap, actionButtonDelete]
    for button in actionButtons:
        button.pack(side='top', fill='both', expand=True, padx=5, pady=5)


    #Inactive
    inactiveStorageBar = ttkb.Progressbar(inactiveStashFrameOuter, bootstyle=f'info, Striped', value=75)
    inactiveStorageBar.pack(fill='x', padx=20, pady=5)
    inactiveStorageStats = []    
    for i in range(statsToDisplay):
        inactiveStorageStats.append(ttkb.Label(inactiveStashFrameOuter, text=f'stat {i+1}: Placeholder', bootstyle=f'{styleInactiveOuter}, inverse', font=('ariel', 8), anchor='center'))
        inactiveStorageStats[i].pack(expand=True, padx=10, pady=5)
    inactiveStashFrame.pack(side='bottom', fill='both', expand=False, padx='2', pady='5')

    inactiveStashCanvas = ttkb.Canvas(inactiveStashFrame)
    inactiveStashScrollBar = ttkb.Scrollbar(inactiveStashFrame, orient='vertical', command=inactiveStashCanvas.yview)
    inactiveStashCanvas.configure(yscrollcommand=inactiveStashScrollBar.set)
    inactiveStashScrollBar.pack(side='right', fill='y',padx=2, pady=5)
    inactiveStashCanvas.pack(fill='both', expand=True)
    ISBFrame = ttkb.Frame(inactiveStashCanvas)
    ISBFrame.pack(fill='both', expand=True)
    inactiveStashCanvas.create_window((0,0), window=ISBFrame, anchor='nw', tags='ISBFrame')

    def ISBFconfig(event):
        inactiveStashCanvas.configure(scrollregion=inactiveStashCanvas.bbox('all'))
        width = event.width
        inactiveStashCanvas.itemconfig('ISBFrame', width=width)
        ISBFrame.config(width=width)
    inactiveStashCanvas.bind('<Configure>', ISBFconfig)

    def ISBFmousewheel(event):
        inactiveStashCanvas.yview_scroll(int(-1*(event.delta/120)), 'units')

    ISBFrame.bind('<Enter>', lambda event: ISBFrame.bind_all('<MouseWheel>', lambda e: ISBFmousewheel(e)))
    ISBFrame.bind('<Leave>', lambda event: ISBFrame.unbind_all('<MouseWheel>'))
    inactiveStashCanvas.bind('<MouseWheel>', ISBFmousewheel)

    def inactiveButtonStyling(currentPosition, isTarget=False):
        if isTarget:
            return f'{styleInactive}'
        try:
            with open(os.path.join(saveManager.outputPath, rf'Stashes\Stash_{currentPosition+1}'), 'r', encoding='utf-8') as file:
                return f'{styleInactive}, outline'
        except:
            return f'{styleInactive}, link'
        
    def activeButtonStyling(currentPosition, isTarget=False):
        if isTarget:
            return f'{styleActive}'
        else:
            return f'{styleActive}, outline'

    inactiveStashButtons = []
    for row in range(rowsOfInactive):
        for column in range(columnsOfInactive):
            currentBox = (row*columnsOfInactive)+column
            #buttonAction = lambda 
            def buttonAction(x=currentBox):
                lastInactive.set(currentInactive.get())
                currentInactive.set(x)
            isActive = False
            if currentInactive.get() == currentBox:
                isActive = True
            button = ttkb.Button(ISBFrame, text=str(currentBox+1), bootstyle=inactiveButtonStyling(currentBox, isTarget=isActive), command=buttonAction)
            button.grid(row=row, column=column, sticky='nsew')
            inactiveStashButtons.append(button)

    for row in range(rowsOfInactive):
        ISBFrame.rowconfigure(row, weight=1)
    for column in range(columnsOfInactive):
        ISBFrame.columnconfigure(column, weight=1)


    def updateCurrentActive(value):
        saveManager.activeStash = value

    def updateCurrentInactive(value):
        saveManager.inactiveStash = value
    
    def colorExported(buttonIndex):
        if buttonIndex == -1:
            actionButtonExport.config(bootstyle='danger')
            actionButtonExport.after(500, lambda: actionButtonExport.config(bootstyle=styleActions))
        elif buttonIndex != saveManager.inactiveStash:
            inactiveStashButtons[buttonIndex].config(bootstyle='success, outline')
        else:
            inactiveStashButtons[buttonIndex].config(bootstyle='success')
        inactiveStashButtons[buttonIndex].after(3500, lambda: resetColor(buttonIndex))
    
    def colorSwapped(active, inactive):
        activeIndex=active
        inactiveIndex=inactive
        if swapStatusImport.get():
            activeStashButtons[activeIndex].config(bootstyle='success')
            activeStashButtons[activeIndex].after(700, lambda: activeStashButtons[activeIndex].config(bootstyle=activeButtonStyling(activeIndex, activeIndex == currentActive.get())))
        else:
            activeStashButtons[activeIndex].config(bootstyle='danger')
            activeStashButtons[activeIndex].after(700, lambda: activeStashButtons[active].config(bootstyle=activeButtonStyling(activeIndex, activeIndex == currentActive.get())))
        if swapStatusExport.get():
            inactiveStashButtons[inactiveIndex].config(bootstyle='success')
            inactiveStashButtons[inactiveIndex].after(700, lambda: inactiveStashButtons[inactiveIndex].config(bootstyle=inactiveButtonStyling(inactiveIndex, inactiveIndex == currentInactive.get())))
        else:
            inactiveStashButtons[inactiveIndex].config(bootstyle='danger')
            inactiveStashButtons[inactiveIndex].after(700, lambda: inactiveStashButtons[inactiveIndex].config(bootstyle=inactiveButtonStyling(inactiveIndex, inactiveIndex == currentInactive.get())))

    def colorDeleted(statusInt):
        if statusInt == 0:
            actionButtonDelete.config(bootstyle='success')
            actionButtonDelete.after(500, lambda: actionButtonDelete.config(bootstyle='warning'))
        elif statusInt == 1:
            actionButtonDelete.config(bootstyle='danger')
            actionButtonDelete.after(500, lambda: actionButtonDelete.config(bootstyle='warning'))
    
        
    def resetColor(buttonIndex):
        if buttonIndex == saveManager.inactiveStash:
            inactiveStashButtons[buttonIndex].config(bootstyle=inactiveButtonStyling(buttonIndex))
        else:
            inactiveStashButtons[buttonIndex].config(bootstyle=inactiveButtonStyling(buttonIndex))

    #Updates filemanagers values based on local version controlled by GUI
    currentInactive.trace_add("write", lambda *args: updateCurrentInactive(currentInactive.get()))
    currentActive.trace_add("write", lambda *args: updateCurrentActive(currentActive.get()))


    #Recolor inactive button based on which one is exported to
    exportIndex.trace_add("write", lambda *args: colorExported(exportIndex.get()))
    #?
    exportIndex.trace_add("write", lambda *args: inactiveStashButtons[exportIndex.get()].config(bootstyle=inactiveButtonStyling(exportIndex.get(), exportIndex.get() == saveManager.inactiveStash)))
    #add special style to current active to show it is selected
    currentActive.trace_add("write", lambda *args: activeStashButtons[currentActive.get()].config(bootstyle=rf'{styleActive}'))
    #Redo style of the last active selected to undo special style indicating it is active
    currentActive.trace_add("write", lambda *args: activeStashButtons[lastActive.get()].config(bootstyle=rf'{styleActive}, outline'))
    #recolor buttons that are affected by swap with color based on outcome. CURRENTLY BUGGED TO SET THE STYLE TO CURRENT EVEN IF SWAPPED OFF.
    swapStatusExport.trace_add("write", lambda *args: colorSwapped(currentActive.get(), currentInactive.get()))
    #update delete button with color based on result of call
    deleteStatus.trace_add("write", lambda *args: colorDeleted(deleteStatus.get()))
    #Trace for changing the style of the button clicked on in inactive
    currentInactive.trace_add("write", lambda *args: inactiveStashButtons[currentInactive.get()].config(bootstyle=inactiveButtonStyling(currentInactive.get(), isTarget=True)))
    #Trace for changing the style of the button before the current one in inactive list (back to normal after adjusting it to be special for being active)
    currentInactive.trace_add("write", lambda *args: inactiveStashButtons[lastInactive.get()].config(bootstyle=inactiveButtonStyling(lastInactive.get())))
    
    
    
    #activeStorageStats[0].config(text=currentInactive)

    root.mainloop()

if __name__ == '__main__':
    main()