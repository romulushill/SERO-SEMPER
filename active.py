import win32gui # Import the windows API for getting open apps
apps = [] # Leave blank as the getWindows() function will autofill this in
ignoredApps = ['ABC'] # Any apps you want to exclude (such as built-in apps or extra windows such as paint.net windows) go here, or leave the list empty
def getWindows(hwnd, *args)->list: # This returns always returns a list, and it takes in a hwnd argument and multiple other arguments to be ignored.
 global apps
 if win32gui.IsWindowVisible( hwnd ):
  title = win32gui.GetWindowText( hwnd ) # Gets title
  if not title == '': # To ensure the title of the program is not blank
   if not title in apps and not title in ignoredApps: # Prevent duplicate app listings and listing ignored apps
    apps.append(title) # Append to public apps variable, you can do other stuff with the title variable such as only get the content after the last dash symbol as I did for my overlay

win32gui.EnumWindows( getWindows, '' ) # Call the function with hwnd argument filled
print(apps) # Print the list of open apps, excluding any apps in ignoredApps