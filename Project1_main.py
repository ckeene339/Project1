'''
This is my improved code on Lab 1
'''


from Project1_gui import *


def main():
    window = Tk()
    window.title('Project 1')
    window.geometry('340x270')
    window.resizable(False, False)
    GUI(window)
    window.mainloop()
    

if __name__ == "__main__":
    main()