import socket           # it helps to check Internet Coneection.
import pyautogui        # its use for keyboard inputs.
import time             # use for add delay in between inputs.
import subprocess       # to run the cmd command.
from _thread import *   # to run the bot thread
import keyboard         # to type the instructions on console
import pyperclip        # to use 'paste'
class SubBot:
    # javascript console commandes
    # Instr_1 = r"console.log(document.querySelector('textarea'));"
    Instr_2 = r"var textareaI = document.querySelector('textarea');"
    Instr_3 = r"textareaI.value = 'hello, how are you?';"

    # open a new tab of chatGPT, you must be logged in
    url = "https://chat.openai.com/chat"

    # store command code list in order to perform
    listOfBrowser = ['start chrome '+url,'start firefox '+url]
    # next we have to store key to open console in list.s
    listOfCommand = ['j','i']
    # you can change waitTime according to your pc speed
    waitTime = 1
    flag = True
    count = 0

    # function to check internet connection
    def is_connected(self):
        # try:
            # socket.create_connection(("www.google.com", 80))
            return True
        # except OSError:
            # pass
        # return False

    # function used to press enter, we have to run its in thread so make another separate function
    def enter(self,val):
        time.sleep(self.waitTime)
        pyautogui.press('enter')
    
    # main loop    
    def main(self):
        # once we get the internet connection set falg value to false so its not going to loop again
        while self.flag:
            # you can add 5 sec of interval
            time.sleep(self.waitTime+4)
            
            # check for connection
            if self.is_connected() == True:
                # now iterate the list of browser
                for i in self.listOfBrowser:
                    # now call the enter function in thread
                    # it help to enter key when command not avlaible else just enter which have not affacts
                    start_new_thread(self.enter,(1,))

                    # now perform command operation over cmd
                    process = subprocess.Popen(i, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                    process.communicate()
                    if process.returncode == 1:
                        self.count = self.count + 1
                        if self.count == len(self.listOfBrowser):
                            self.flag = False
                        continue
                    time.sleep(self.waitTime+4)
                    
                    # oce browser is open use key of combiniation to open the console
                    pyautogui.hotkey('ctrl','shift',self.listOfCommand[self.listOfBrowser.index(i)])

                    # and simply give an interval and past and enter the javascript code step by step
                    time.sleep(self.waitTime+1)
                    pyautogui.moveTo(x=1700, y=750, duration=1) # change it with your screen size, you can remove duration to speed up process
                    pyautogui.click()   # to click on console, this allow cursor to write in console
                    # keyboard.write(self.Instr_1)
                    # pyautogui.press('enter')

                    # time.sleep(self.waitTime)
                    keyboard.write(self.Instr_2)
                    pyautogui.press('enter')

                    keyboard.write(self.Instr_3)
                    time.sleep(self.waitTime+1+1)
                    pyautogui.press('enter')

                    # for quitting console
                    time.sleep(self.waitTime+5)
                    pyautogui.hotkey('fn','f12')
                    pyautogui.press('enter')

                    # select the responce
                    time.sleep(self.waitTime+10) # you change wait time if you think that your question is too long to responce
                    left = 660    # the first caracter of question x position (adapt it with your screen size)
                    top = 210     # the first caracter of question y position (adapt it with your screen size)
                    width = 1200  # untill the end of the line in chatgpt     (adapt it with your screen size)
                    height = 1100 # untill the windows bar                    (adapt it with your screen size)
                    pyautogui.moveTo(left, top, duration=2)
                    pyautogui.mouseDown()
                    pyautogui.dragTo(width, height, duration=6)
                    pyautogui.mouseUp()
                    pyautogui.hotkey('ctrl', 'c')     # copy the selected text
                    selected_text = pyperclip.paste() # paste it here
                    # print(selected_text)
                    return selected_text

                    # for quitting.
                    # pyautogui.hotkey('alt','f4')

                    # once all code works then simply set flag value to false so it will not loop again.
                    self.flag = False;
                    break
            else:
                print("No Internet Connection!")

# subBot = SubBot()
# subBot.main()