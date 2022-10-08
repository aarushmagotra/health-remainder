import pygame
import time
import datetime
print()
print("=======================================")
print('WELCOME TO THE HEALTH REMINDER SYSTEM')
print("=======================================")
print()
print('In this system we will constantly remind you to "DRINK WATER",')
print()
print('"MASSAGE YOUR EYES" & to do some "PHYSICAL ACTIVITY" in regular intervals ')
print()
print('between 9 am to 5 pm')

def time_():
    return datetime.datetime.now()
check_w = 1

def write_w():
    global check_w
    date_w = datetime.datetime.now()
    date = str(date_w.date())

    if check_w == 1:
        filee = open('water.txt', 'a+')
        filee.write(date)
        filee.write(':')
        filee.close()
        
    if check_w >= 1:
        filee = open('water.txt', 'a+')
        filee.write('\n')
        filee.write('\t')
        filee.write('[')
        filee.write(str(time_()))
        filee.write(']')
        filee.write(' - ')
        filee.write('Drank 200 ml of water')
        filee.write('\n')
        filee.close()

        
def write_e():
    global check_w
    date_w = datetime.datetime.now()
    date = str(date_w.date())
    check_w += 1
    if check_w == 2:
        filee = open('eye.txt', 'a+')
        filee.write(date)
        filee.write(':')
        filee.close()
    if check_w >= 2:
        filee = open('eye.txt', 'a+')
        filee.write('\n')
        filee.write('\t')
        filee.write('[')
        filee.write(str(time_()))
        filee.write(']')
        filee.write(' - ')
        filee.write('Did Eye Massage')
        filee.write('\n')
        filee.close()

def write_ex():
    global check_w
    date_w = datetime.datetime.now()
    date = str(date_w.date())
    check_w += 1
    if check_w == 2:
        filee = open('exer.txt', 'a+')
        filee.write(date)
        filee.write(':')
        filee.close()
    if check_w >= 2:
        filee = open('exer.txt', 'a+')
        filee.write('\n')
        filee.write('\t')
        filee.write('[')
        filee.write(str(time_()))
        filee.write(']')
        filee.write(' - ')
        filee.write('Did some Physical Activity')
        filee.write('\n')
        filee.close()

def audio_water():
    global check_w
    while True:
        pygame.mixer.init()
        pygame.mixer.music.load("sounds\\audio.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        pause = input('Type "done" when you finish doing it: ')
        if pause == 'done':
            pygame.mixer.music.pause()
            break
    write_w()

def audio_eye():
    while True:
        pygame.mixer.init()
        pygame.mixer.music.load("sounds\\audio.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        pause = input('Type "done" when you finish doing it: ')
        if pause == 'done':
            pygame.mixer.music.pause()
            break
    write_e()

def audio_exe():
    while True:
        pygame.mixer.init()
        pygame.mixer.music.load("sounds\\audio.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        pause = input('Type "done" when you finish doing it: ')
        if pause == 'done':
            pygame.mixer.music.pause()
            break
    write_ex()

def __time():
    now = datetime.datetime.now()
    a = now.hour
    b = now.minute
    c = [str(a), str(b)]
    d = ':'.join(c)
    return d

aw, ae, aex = 1, 1, 1
bw, be, bex = 1, 1, 1
cw, ce, cex = 1, 1, 1
dw, de, dex = 1, 1, 1
ew, ee, eex = 1, 1, 1
fw, fe, fex = 1, 1, 1
gw, ge, gex = 1, 1, 1
hw, he, hexx = 1, 1, 1
iw, ie, iex = 1, 1, 1
jw, je, jex = 1, 1, 1
kw, ke, kex = 1, 1, 1
le, lex = 1, 1
me, mex = 1, 1
ne, nex = 1, 1
oe, oex = 1, 1
pe, pex = 1, 1

while True:
    if __time() == '9:25':
        if aw == 1:
            aw += 1
            print()
            print("It's time to DRINK WATER :)")
            print()
            print('Drink a 200 ml glass of water')
            print()
            audio_water()
    if __time() == '10:15':
        if bw == 1:
            bw += 1
            print()
            print("It's time to DRINK WATER :)")
            print()
            print('Drink a 200 ml glass of water')
            print()
            audio_water()
    if __time() == '11:5':
        if cw == 1:
            cw += 1
            print()
            print("It's time to DRINK WATER :)")
            print()
            print('Drink a 200 ml glass of water')
            print()
            audio_water()
    if __time() == '11:45':
        if dw == 1:
            dw += 1
            print()
            print("It's time to DRINK WATER :)")
            print()
            print('Drink a 200 ml glass of water')
            print()
            audio_water()
    if __time() == '12:35':
        if ew == 1:
            ew += 1
            print()
            print("It's time to DRINK WATER :)")
            print()
            print('Drink a 200 ml glass of water')
            print()
            audio_water()

    if __time() == '13:15':
        if fw == 1:
            fw += 1
            print()
            print("It's time to DRINK WATER :)")
            print()
            print('Drink a 200 ml glass of water')
            print()
            audio_water()
    if __time() == '14:5':
        if gw == 1:
            gw += 1
            print()
            print("It's time to DRINK WATER :)")
            print()
            print('Drink a 200 ml glass of water')
            print()
            audio_water()
    if __time() == '14:45':
        if hw == 1:
            hw += 1
            print()
            print("It's time to DRINK WATER :)")
            print()
            print('Drink a 200 ml glass of water')
            print()
            audio_water()
    if __time() == '15:35':
        if iw == 1:
            iw += 1
            print()
            print("It's time to DRINK WATER :)")
            print()
            print('Drink a 200 ml glass of water')
            print()
            audio_water()
    if __time() == '16:15':
        if jw == 1:
            jw += 1
            print()
            print("It's time to DRINK WATER :)")
            print()
            print('Drink a 200 ml glass of water')
            print()
            audio_water()
    elif __time() == '16:50':
        if kw == 1:
            kw += 1
            print()
            print("It's time to DRINK WATER :)")
            print()
            print('Drink a 200 ml glass of water')
            print()
            audio_water()
    elif __time() == '9:30':
        if ae == 1:
            ae += 1
            print()
            print("It's time for an EYE MASSAGE")
            print()
            audio_eye()
    elif __time() == '10:0':
        if be == 1:
            be += 1
            print()
            print("It's time for an EYE MASSAGE")
            print()
            audio_eye()
    elif __time() == '10:30':
        if ce == 1:
            ce += 1
            print()
            print("It's time for an EYE MASSAGE")
            print()
            audio_eye()
    elif __time() == '11:0':
        if de == 1:
            de += 1
            print()
            print("It's time for an EYE MASSAGE")
            print()
            audio_eye()
    elif __time() == '11:30':
        if ee == 1:
            ee += 1
            print()
            print("It's time for an EYE MASSAGE")
            print()
            audio_eye()
    elif __time() == '12:0':
        if fe == 1:
            fe += 1
            print()
            print("It's time for an EYE MASSAGE")
            print()
            audio_eye()
    elif __time() == '12:30':
        if ge == 1:
            ge += 1
            print()
            print("It's time for an EYE MASSAGE")
            print()
            audio_eye()
    elif __time() == '13:0':
        if he == 1:
            he += 1
            print()
            print("It's time for an EYE MASSAGE")
            print()
            audio_eye()
    elif __time() == '13:30':
        if ie == 1:
            ie += 1
            print()
            print("It's time for an EYE MASSAGE")
            print()
            audio_eye()
    elif __time() == '14:0':
        if je == 1:
            je += 1
            print()
            print("It's time for an EYE MASSAGE")
            print()
            audio_eye()
    elif __time() == '14:30':
        if ke == 1:
            ke += 1
            print()
            print("It's time for an EYE MASSAGE")
            print()
            audio_eye()
    elif __time() == '15:0':
        if le == 1:
            le += 1
            print()
            print("It's time for an EYE MASSAGE")
            print()
            audio_eye()
    elif __time() == '15:30':
        if me == 1:
            me += 1
            print()
            print("It's time for an EYE MASSAGE")
            print()
            audio_eye()
    elif __time() == '16:0':
        if ne == 1:
            ne += 1
            print()
            print("It's time for an EYE MASSAGE")
            print()
            audio_eye()
    elif __time() == '16:30':
        if oe == 1:
            oe += 1
            print()
            print("It's time for an EYE MASSAGE")
            print()
            audio_eye()
    elif __time() == '16:55':
        if pe == 1:
            pe += 1
            print()
            print("It's time for an EYE MASSAGE")
            print()
            audio_eye()
    elif __time() == '9:45':
        if aex == 1:
            aex += 1
            print()
            print("It's time to do some PHYSICAL ACTIVITY")
            print()
            audio_exe()
    elif __time() == '10:20':
        if bex == 1:
            bex += 1
            print()
            print("It's time to do some PHYSICAL ACTIVITY")
            print()
            audio_exe()
    elif __time() == '10:50':
        if cex == 1:
            cex += 1
            print()
            print("It's time to do some PHYSICAL ACTIVITY")
            print()
            audio_exe()
    elif __time() == '11:33':
        if dex == 1:
            dex += 1
            print()
            print("It's time to do some PHYSICAL ACTIVITY")
            print()
            audio_exe()
    elif __time() == '12:7':
        if eex == 1:
            eex += 1
            print()
            print("It's time to do some PHYSICAL ACTIVITY")
            print()
            audio_exe()
    elif __time() == '12:47':
        if fex == 1:
            fex += 1
            print()
            print("It's time to do some PHYSICAL ACTIVITY")
            print()
            audio_exe()
    elif __time() == '13:37':
        if gex == 1:
            gex += 1
            print()
            print("It's time to do some PHYSICAL ACTIVITY")
            print()
            audio_exe()
    elif __time() == '14:6':
        if hexx == 1:
            hexx += 1
            print()
            print("It's time to do some PHYSICAL ACTIVITY")
            print()
            audio_exe()
    elif __time() == '14:46':
        if iex == 1:
            iex += 1
            print()
            print("It's time to do some PHYSICAL ACTIVITY")
            print()
            audio_exe()
    elif __time() == '15:28':
        if jex == 1:
            jex += 1
            print()
            print("It's time to do some PHYSICAL ACTIVITY")
            print()
            audio_exe()
    elif __time() == '15:58':
        if kex == 1:
            kex += 1
            print()
            print("It's time to do some PHYSICAL ACTIVITY")
            print()
            audio_exe()
    elif __time() == '16:48':
        if lex == 1:
            lex += 1
            print()
            print("It's time to do some PHYSICAL ACTIVITY")
            print()
            audio_exe()
    elif __time() > '17:0':
        print()
        choice = input('Would you like to retrieve data(y/n): ')
        if choice == 'n':
            break
        elif choice == 'y':
            print()
            ask = input('What would you like to see(w/e/ex): ')
            if ask == 'w':
                file = open('water.txt', 'r')
                file.seek(0)
                print()

                for i in file:
                    print(i)
                    print()
                file.close()
                print('Thanks for using:)')
                print()
                print('Closing in 10 sec')
                print()

                time.sleep(10)
                print('BYE')
                break
            elif ask == 'e':
                file = open('eye.txt', 'r')
                file.seek(0)
                print()

                for i in file:
                    print(i)
                    print()
                file.close()
                print('Thanks for using:)')
                print()
                print('Closing in 10 sec')
                print()

                time.sleep(10)
                print('BYE')
                break
            elif ask == 'ex':
                file = open('exer.txt', 'r')
                file.seek(0)
                print()

                for i in file:
                    print(i)
                    print()
                file.close()
                print('Thanks for using:)')
                print()
                print('Closing in 10 sec')
                print()

                time.sleep(10)
                print('BYE')
                break
            else:
                print()
                print('INVALID INPUT :(')
                print()
                print('Exiting in 5 sec')
                time.sleep(5)
                print()
                print('BYE')
                break
        else:
            print()
            print('INVALID INPUT :(')
            print()
            print('Exiting in 5 sec')
            time.sleep(5)
            print()
            print('BYE')
            break

quit()
#code ends here
