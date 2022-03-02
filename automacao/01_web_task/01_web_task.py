import time
import pyautogui
import webbrowser

def show_posi():     
      '''
      Mostra a posição atual do cursos do mouse.
      '''
      while True:
        time.sleep(5)
        print(pyautogui.position())

def main():
    
    '''
    Entra em um site, preenche o campo de login e senha e clica no campo indicado para autentica-los.
    '''

    url = 'xxxxxxxxxxxxxxx'
    login = 'xxxxxx'
    password = 'xxxxx'


    webbrowser.open(url)

    time.sleep(8)
    pyautogui.click(296,370)
    pyautogui.write(login, interval=0.05)

    pyautogui.press('tab') 
    pyautogui.write(password, interval=0.05)

    pyautogui.doubleClick(321,493)


'show_posi()'
main()
