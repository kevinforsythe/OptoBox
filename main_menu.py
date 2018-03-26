import os

def main_menu():
  print("\n\t\t\tMAIN MENU OPTIONS:")
  print("\n\t1. Upload a Previously Written Song to OptoBox")
  print("\n\t2. Create a New Song from a *.csv File and Upload to OptoBox")
  print("\t   (currently works only for single column/channel LED control)")
  print("\n\t3. See a List of Previously Written Songs")
  print("\t    (Press 'q' to return to the main menu)")
  print("\n\t4. See a Log of Songs Previously Uploaded to OptoBox")
  print("\n\t5. Quit")
  main_menu_choice = input("\n\nWhat would you like to do?\n>")
  if main_menu_choice == '1':
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
      print("\n\n\n\n\nPlease Choose a Valid Option:\n")
      main_menu()


def main_menu_1():
    os.system('clear')
    print("\nsorry, option1 not yet implemented\n\n")
    main_menu()

def main_menu_2():
    os.system('python3 transpose_song.py')
    # call compile&upload function here
    main_menu()

def main_menu_3():
    os.system("ls -lu --time-style=long-iso ./output_songs | awk '{print $6, $7, $8, $9}' | less")
    os.system('clear')
    main_menu()

def main_menu_4():
    os.system('clear')
    print("sorry, option4 not yet implemented")
    main_menu()



# this is the main start
os.system('clear')
print("\n\n\nWelcome to OptoBoxComposer (version alpha, for single 35mm dish)")
main_menu()
