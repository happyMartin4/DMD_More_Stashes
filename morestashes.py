#from SupportingScripts import filehandle
import tkinter as tk
from tkinter import ttk 
import ttkbootstrap as ttkb
from SupportingScripts import filehandle
import os

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
    styleActions = 'success'
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
    activeStashHeader = ttkb.Label(activeStashFrameOuter, text='Active Stash Tabs', font=('ariel', 18), anchor='center', bootstyle=f'{styleActiveOuter}, inverse')
    actionsHeader = ttkb.Label(actionsFrameOuter, text='Actions', font=('ariel', 18), anchor='center', bootstyle=f'{styleActionsOuter}, inverse')
    inactiveStashHeader = ttkb.Label(inactiveStashFrameOuter, text='Inactive Stash Tabs', font=('ariel', 18), anchor='center', bootstyle=f'{styleInactiveOuter}, inverse')

    headerFrame.pack(side='top', fill='x', padx='10', pady='5')
    activeStashFrameOuter.pack(side='left', fill='both', expand=True, padx='10', pady='5')
    actionsFrameOuter.pack(side='left', fill='both', expand=True, padx='10', pady='5')
    inactiveStashFrameOuter.pack(side='left', fill='both', expand=True, padx='10', pady='5')
    headerLabel.pack(padx=10, pady=10)

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
    actionButtonExport = ttkb.Button(actionsFrame, text='<- Export', bootstyle=styleActions, command=saveManager.export)
    actionButtonSwap = ttkb.Button(actionsFrame, text='<- Swap ->', bootstyle=styleActions, command=saveManager.swap)
    actionButtonDelete = ttkb.Button(actionsFrame, text='Delete ->', bootstyle='warning', command=saveManager.delete)
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


    
    #GUI implemented

    #Functionality begins:
    
    #TEST CODE

    def updateCurrentActive(value):
        saveManager.activeStash = value

    def updateCurrentInactive(value):
        saveManager.inactiveStash = value
    

    currentInactive.trace_add("write", lambda *args: updateCurrentInactive(currentInactive.get()))
    currentInactive.trace_add("write", lambda *args: inactiveStashButtons[currentInactive.get()].config(bootstyle=inactiveButtonStyling(currentInactive.get(), isTarget=True)))
    currentInactive.trace_add("write", lambda *args: inactiveStashButtons[lastInactive.get()].config(bootstyle=inactiveButtonStyling(lastInactive.get())))
    currentActive.trace_add("write", lambda *args: updateCurrentActive(currentActive.get()))
    currentActive.trace_add("write", lambda *args: activeStashButtons[currentActive.get()].config(bootstyle=rf'{styleActive}'))
    currentActive.trace_add("write", lambda *args: activeStashButtons[lastActive.get()].config(bootstyle=rf'{styleActive}, outline'))
    #activeStorageStats[0].config(text=currentInactive)

    root.mainloop()
    print(lastActive.get())
    print(currentActive.get())

if __name__ == '__main__':
    main()