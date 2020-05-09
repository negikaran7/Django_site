from tkinter import *
import tkinter.simpledialog as simpledialog
import pdfkit 

def url_to_pdf():
    n = simpledialog.askinteger('', 'How many entries?', initialvalue=1, minvalue=1, maxvalue=10)
    if not n: # 'Cancel'
        return
    for i in range(n):
        url = simpledialog.askstring('', 'url #%s from #%s' % (i+1, n))
        if url is None: # 'Cancel'
            return
        print(url)
        pdfkit.from_url(f'{url}',f'url_{i}.pdf') 

root = Tk()
Button(root, text='Add url', command=url_to_pdf).pack(padx=50, pady=50)
Button(root, text='Quit', command=root.destroy).pack(pady=30)
root.mainloop()