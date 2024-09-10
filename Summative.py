def print_menu():
  """() -> none
  Prints out the menu."""
  option1 = "1. Move the first song of the playlist to the end of the playlist.\n"
  option2 = "2. Move the last song of the playlist to the start of the playlist.\n"
  option3 = "3. Swap the first two songs of the playlist.\n"
  option4 = "4. Swap the last two songs of the playlist.\n"
  option5 = "5. Swap the second and the n-1 songs of the playlist.\n"
  option6 = "6. Stop rearranging songs and output the final playlist.\n"
  print(option1 + option2 + option3 + option4 + option5 + option6)

def get_selection():
  """() -> int
  Gets selection from the user."""
  while True:
    try:
      selection = int(input("Enter your selection: "))
      if selection >= 1 and selection <=6: #Checks if selection is a valid option
        return selection
      else:
        print("Enter a valid selection\n")
    except:
      print("Enter a valid selection\n")

def get_songs():
  """() -> (int, list)
  Gets number of songs and the initial order of the songs."""
 
  while True:
    num_songs = (input("Enter number of songs in playlist >=4: "))
    if num_songs.isdigit() and int(num_songs) >= 4: #Checks if input is a number greater than 4
      playlist = input("Enter the names of the songs in playlist seperated by a space: ")
      playlist = playlist.split(" ") #Converts string into a list
      if len(playlist) >= 4: #Checks if list has more than 4 songs
        return playlist
      else:
        print("Not enough songs were inputted")
    else:
      print("Try again\n")

def move_first_to_last(playlist):
  """(list) -> list
  Moves the first song of the playlist to the end of the playlist"""
  return playlist[1:] + [playlist[0]]

def move_last_to_first(playlist):
  """(list) -> list
   Moves the last song of the playlist to the start of the playlist"""
  return [playlist[-1]] + playlist[:-1]

def swap_first_two(playlist):
  """(list) -> list
  Swaps the first two songs of the playlist"""
  return [playlist[1]] + [playlist[0]] + playlist[2:]

def swap_last_two(playlist):
  """(list) -> list
  Swaps the last two songs of the playlist"""
  return playlist[:-2] + [playlist[-1]] + [playlist[-2]]

def swap_second_and_second_last(playlist):
  """(list) -> list
  Swap the second and the second last songs of the playlist"""
  return [playlist[0]] + [playlist[-2]] + playlist[2:-2] + [playlist[1]] + [playlist[-1]] 

playlist = get_songs()
print_menu()
while True:
  selection = get_selection()
  #Chooses which function to call based on what option is selected
  if selection == 1:
    playlist = move_first_to_last(playlist)
    print("Your current playlist is: ", playlist)
    
  elif selection == 2:
    playlist = move_last_to_first(playlist)
    print("Your current playlist is: ", playlist)
  
  elif selection == 3:
    playlist = swap_first_two(playlist)
    print("Your current playlist is: ", playlist)
    
  elif selection == 4:
    playlist = swap_last_two(playlist)
    print("Your current playlist is: ", playlist)
  
  elif selection == 5:
    playlist = swap_second_and_second_last(playlist)
    print("Your current playlist is: ", playlist)
    
  elif selection == 6:
    print("Your final playlist is: ", playlist)
    break #Ends the program