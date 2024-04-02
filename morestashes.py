import tkinter as tk
from tkinter import ttk 
import ttkbootstrap as ttkb

def main():
    style = ttkb.Style('darkly')
    root = style.master
    #placeholder values
    numberOfActive = 8
    statsToDisplay = 8
    columnsOfInactive = 10
    rowsOfInactive = 15
    lastActive = ttkb.IntVar()
    currentActive = ttkb.IntVar()
    lastInactive = ttkb.IntVar()
    currentInactive = ttkb.IntVar()
    currentInactive.set(10)



    storageUsedActive = 40
    
    #GUI setup begins:
    #main window setup

    root.title('DMD More Stash')
    root.iconbitmap('Assets/MS.ico')
    root.geometry('800x700')
    root.minsize(800, 700)
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

    activeStashButtons = []
    for i in range(numberOfActive):
        def buttonAction(x=i):
            print(x)
            lastActive.set(currentActive.get())
            currentActive.set(x)
        activeStashButtons.append(ttkb.Button(activeStashFrame, text=f'Stash {i+1}', bootstyle=f'{styleActive}, outline', command=buttonAction))
        activeStashButtons[i].pack(side='top', fill='both', padx=5, pady=3)

    #Actions
    actionsFrame.pack(side='bottom', fill='both', expand=True, padx='2', pady='5')
    actionButtonExport = ttkb.Button(actionsFrame, text='<- Export', bootstyle=styleActions)
    actionButtonSwap = ttkb.Button(actionsFrame, text='<- Swap ->', bootstyle=styleActions)
    actionButtonDelete = ttkb.Button(actionsFrame, text='Delete ->', bootstyle='warning')
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

    inactiveStashButtons = []
    for row in range(rowsOfInactive):
        for column in range(columnsOfInactive):
            currentBox = (row*columnsOfInactive)+column
            #buttonAction = lambda 
            def buttonAction(x=currentBox):
                lastInactive.set(currentInactive.get())
                currentInactive.set(x)

            button = ttkb.Button(inactiveStashFrame, text=str(currentBox+1), bootstyle=f'{styleInactive}, outline', command=buttonAction)
            button.grid(row=row, column=column, sticky='nsew')
            inactiveStashButtons.append(button)

    for row in range(rowsOfInactive):
        inactiveStashFrame.rowconfigure(row, weight=1)
    for column in range(columnsOfInactive):
        inactiveStashFrame.columnconfigure(column, weight=1)


    
    #GUI implemented

    #Functionality begins:
    
    #TEST CODE
    currentInactive.trace_add("write", lambda *args: activeStorageStats[0].config(text=currentInactive.get()))
    currentInactive.trace_add("write", lambda *args: inactiveStashButtons[currentInactive.get()].config(bootstyle=f'{styleInactive}'))
    currentInactive.trace_add("write", lambda *args: inactiveStashButtons[lastInactive.get()].config(bootstyle=f'{styleInactive}, outline'))
    currentActive.trace_add("write", lambda *args: activeStorageStats[1].config(text=currentActive.get()))
    currentActive.trace_add("write", lambda *args: activeStashButtons[currentActive.get()].config(bootstyle=f'{styleActive}'))
    currentActive.trace_add("write", lambda *args: activeStashButtons[lastActive.get()].config(bootstyle=f'{styleActive}, outline'))
    #activeStorageStats[0].config(text=currentInactive)

    root.mainloop()
    print(lastActive.get())
    print(currentActive.get())

if __name__ == '__main__':
    main()