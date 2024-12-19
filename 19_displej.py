from ili934xnew import ILI9341, color565
from machine import Pin, SPI
import glcdfont
import tt14
import tt24
import tt32
import utime
import time
from machine import RTC
from machine import ADC
import random

colors = [color565(255,0,0),color565(255,255,0),color565(0,255,0),color565(0,255,255),color565(0,0,255),color565(255,0,255),color565(255,255,255),color565(0,0,0)]
fonts = [glcdfont,tt14,tt24,tt32]
text = 'Hello'
utime.sleep_ms(5000)

fg = color565(255,255,0)
bg = color565(0,0,0)
fg_thanks = color565(0,0,0)
bg_thanks = color565(0,255,0)
bg_title = color565(0, 255, 255)

fg_fw = color565(0,255,0)
fg_ph = color565(255,255,255)

cs = Pin(13, Pin.OUT)
rst = Pin(14, Pin.OUT)
dc = Pin(15, Pin.OUT)
spi = SPI(1, 10000000, mosi=Pin(11), miso=Pin(12), sck=Pin(10))
display = ILI9341(spi, cs,dc,rst, w=320, h=240, r=0)

display.erase()

#for c in colors:
#    display.fill_rectangle(0,0,239,319, c)
#    utime.sleep_ms(1000)
    
display.set_pos(50,20)
display.set_font(tt32)
display.set_color(fg, bg)
display.print("AHOJ ENGETO")
display.print("        ")

display.set_pos(20,80)
display.set_font(tt24)
display.set_color(fg_fw, bg)
display.print("Jako dalo to praci, bez googlu ani ranu, ale alespon vim co v kodu znamena a dokazu to upravit")


# display.set_pos(80,140)
# display.set_font(tt24)
# display.set_color(fg_ph, bg)
# display.print("malá zkouška")
# display.set_pos(80,150)
# display.set_font(tt14)
# display.print("")


display.set_pos(50,220)
display.set_font(tt24)
display.set_color(fg_thanks, bg_thanks)
display.print("\"Diky kurze\"")

display.set_pos(25,245)
display.set_font(tt24)
display.set_color(fg, bg)
display.print("\"Python rulez.....\"")

utime.sleep_ms(5000)
display.erase()
#utime.sleep_ms(5000)
#display.fill_rectangle(255,0,0)

display.set_pos(20,20)
display.set_font(tt32)
display.set_color(fg_fw, bg)
display.print("AHOJ ENGETO")
display.print("----------------------")

display.set_pos(20,130)
display.set_font(tt24)
display.set_color(fg_fw, bg)
display.print("Dnes je 16.12.2024")

# Inicializace ADC pro interní snímač teploty
sensor_temp = ADC(4)

# Napájecí napětí (3.3 V)
conversion_factor = 3.3 / 65535

while True:
    # Přečtení hodnoty z ADC
    reading = sensor_temp.read_u16() * conversion_factor
    
    # Výpočet teploty (dle dokumentace)
    temperature = 27 - (reading - 0.706) / 0.001721
    
    print("Interní teplota: {:.2f} °C".format(temperature))
    display.set_pos(10,200)
    display.set_color(fg, bg)
    display.print("Aktualni teplota z interniho teplomeru cipu je: {:.2f} Celsia".format(temperature))
    time.sleep(2)  # Zpoždění 1 sekundu
    break


utime.sleep_ms(10)
display.erase()
#display.fill_rectangle(10, 120, 300, 20, bg)

#display.set_color(fg, bg)
# Vytvorte list moznosti
moznosti = ['kamen', 'nuzky', 'papir']

# Vytvorte promennou hrac a ulozte do ni hodnotu kamen
hrac = "kamen"

# Vytvorte promennou pocitac
pocitac = random.choice(moznosti)
def odpocet(sekundy):
    for i in range(5, -1, -1):
        display.erase()
        display.set_pos(10, 50)
        display.print("Dalsi hra za {} s".format(i))
        time.sleep(1)
        display.erase()
    
# Vytisknete volbu cloveka a pocitace
# Nastav pozici před výpisem volby hráče a počítače
for _ in range(5):
    display.erase()
    pocitac = random.choice(moznosti)
    display.set_pos(10, 50)  # Nastavení pozice pro text
    display.set_font(tt32)
    #display.set_color(fg, bg)
    display.print("Hrac: {}".format(hrac))
    
    display.set_pos(10, 80)  # Další pozice pro počítač
    display.print("Pocitac: {}".format(pocitac))
    
    # Logika hry
    if hrac == 'kamen' and pocitac == 'nuzky':
        display.set_pos(10, 120)  # Pozice pro výsledek
        display.print("Vyhral jsi!")
    elif hrac == 'kamen' and pocitac == 'papir':
        display.set_pos(10, 120)
        display.print("Prohral jsi!")
    else:
        display.set_pos(10, 120)
        display.print("Nerozhodne")
        
    time.sleep(5)
    odpocet(5)
    
display.print("Dohrali jsme, zahrajeme si zase priste. Diky za hru.")
