import requests
from flask import Flask, redirect, url_for, request, jsonify, render_template,make_response,send_file
import os
from colorthief import ColorThief
import shutil
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
print('\n')
print(r'''
░██████╗░░█████╗░███╗░░██╗███████╗     ███████╗██╗░██████╗██╗░░██╗██╗███╗░░██╗██╗
██╔════╝░██╔══██╗████╗░██║██╔════╝     ██╔════╝██║██╔════╝██║░░██║██║████╗░██║╚█║
██║░░██╗░██║░░██║██╔██╗██║█████╗░░     █████╗░░██║╚█████╗░███████║██║██╔██╗██║░╚╝
██║░░╚██╗██║░░██║██║╚████║██╔══╝░░     ██╔══╝░░██║░╚═══██╗██╔══██║██║██║╚████║░░░
╚██████╔╝╚█████╔╝██║░╚███║███████╗     ██║░░░░░██║██████╔╝██║░░██║██║██║░╚███║░░░
░╚═════╝░░╚════╝░╚═╝░░╚══╝╚══════╝     ╚═╝░░░░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░░░''')
print('\n')

## get current path
cwd=os.getcwd()



##### get user site name
sitename='websites\\'+(input("\nEnter New Site Name:\n"))

if not os.path.exists(f'{cwd}\\{sitename}'):
  #os.mkdir(sitename)
  os.mkdir(f'{sitename}')
  #open(f'{sitename}\\setup.py','w').close()
  open(f'{sitename}\\logo.png','w').close()
  open(f'{sitename}\\index.html','w').close()
  #open(f'{sitename}\\iframe.html','w').close()
  open(f'{sitename}\\script.js','w').close()
  open(f'{sitename}\\style.css','w').close()
  #open(f'{sitename}\\ups.txt','w').close()

## create script.js
with open("templates/scripttemplate.js",'r') as scripttemp:
  scriptjs=scripttemp.read()
with open(sitename+"\\script.js",'w') as scripttemp:
    scripttemp.write(scriptjs)

for it in os.scandir('templates'):
  if it.is_dir():
    print(it.path)

## template choice
tempc=input('select a template number:')
temp="design"+tempc


## create style.css
with open("templates/"+temp+"/style.css",'r') as styletemp:
  stylecss=styletemp.read()
with open(sitename+"\\style.css",'w') as styletemp:
  styletemp.write(stylecss)

## create index.html
with open ("templates/"+temp+"/index.html",'r') as itemp:
  itemphtml=itemp.read()
with open(sitename+"\\index.html",'w') as itemp:
    itemp.write(itemphtml)


## get image source and save to logo.png
logosource=input("select:\n1. Local png file,\n2. online imagelink:\n")

if logosource == '1':
  #logo = input("enter path:\n")[1:-1]
  Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
  filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
  print(filename)
  logo=filename
  shutil.copy(logo, sitename+"\\logo.png")

if logosource=='2':
  logo=input("Enter logo link:\n")
  img_data = requests.get(logo).content
  with open(sitename+"\\logo.png", 'wb') as handler:
      handler.write(img_data)

print()
back=input('1. use bg color\n2. use image url\n3. bg img local :\n')
if back =='1':
  bgimg=''
if back =='3':
  Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
  bgimg = askopenfilename() # show an "Open" dialog box and return the path to the selected file
if back =='2':
  bgimg=input('enter url:\n')

## get pallete
color_thief = ColorThief(sitename+"\\logo.png")
dominant_color = color_thief.get_color(quality=1)
palette = color_thief.get_palette(color_count=6)
print(palette)

## save bg color in hex
def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb
bgcolor=rgb_to_hex(palette[1])
color2=rgb_to_hex(palette[0])
color3=rgb_to_hex(palette[0])

print(bgcolor)
print(color2)
print(color3)
## insert colors into index.html
with open(sitename+"\\index.html","r") as mf:
  md=mf.read()
  
  md=md.replace('<bgimg>',bgimg)
  md=md.replace('<bgcolor>',bgcolor)
  md=md.replace('<color2>',color2)
  md=md.replace('<color3',color3)
  md=md.replace("<title>Client Portal</title>",f'<title>{sitename}</title>')
with open(sitename+"\\index.html","w") as mf:
  mf.write(md)

## insert colors into style.css
with open(sitename+"\\style.css","r") as mf:
  md=mf.read()
  md=md.replace('<bgcolor>',bgcolor)
  md=md.replace('<color2>',color2)
  md=md.replace('<color3',color3)
  md=md.replace("<title>Client Portal</title>",f'<title>{sitename}</title>')
with open(sitename+"\\style.css","w") as mf:
  mf.write(md)

os.system(f"start {sitename}\\index.html")