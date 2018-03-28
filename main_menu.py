import os

def main_menu():
  print("\n\t\t\tMAIN MENU OPTIONS:")
  print('\n\t0. Open Spreadsheet Program to Create *.csv Data File')
  print("\t(Remember to 'Save As' .csv Format)")
  print("\n\t1. Create a New Song from a *.csv File and Upload to OptoBox")
  print("\t   (currently only works for single column/channel LED control)")
  print("\n\t2. See a List of Previously Transposed Songs")
  print("\n\t3. Upload a Previously Transposed Song to OptoBox")
  print("\t    (NOTE: After viewing, press 'q' to return to the main menu)")
  print("\n\t4. See a Log of Songs Previously Uploaded to OptoBox")
  print("\n\t5. Quit")
  main_menu_choice = input("\n\nWhat would you like to do?\n>")
  if main_menu_choice == '0':
      main_menu_0()
  elif main_menu_choice == '1':
      main_menu_1()
  elif main_menu_choice == '2':
      main_menu_2()
  elif main_menu_choice == '3':
      main_menu_3()
  elif main_menu_choice == '4':
      main_menu_4()
  elif main_menu_choice == '5':
      quit()
  else:
      os.system('clear')
      print("\nPlease Choose a Valid Option:\n")
      main_menu()

def main_menu0():
    to_open_libre_calc= "libreoffice --calc"
    os.system(to_open_libre_calc)
    os.system('clear')
    print('--remember to save your data in CSV format!')

def main_menu_1():
    os.system('clear')
    os.system('python3 transpose_song.py')
    main_menu()

def main_menu_2():
    os.system("ls -lu --time-style=long-iso ./output_songs | awk '{print $6, $7, $8, $9}' | less")
    main_menu()

def main_menu_3():
    os.system('python3 upload_song.py')
    os.system('clear')
    main_menu()

def main_menu_4():
    os.system('clear')
    print("sorry, option4 not yet implemented")
    main_menu()



# this is the main start
os.system('clear')
print("\nWelcome to OptoBoxComposer (version alpha, for single 35mm dish only)")
main_menu()
