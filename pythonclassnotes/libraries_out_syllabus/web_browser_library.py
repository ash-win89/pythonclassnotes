#Opening a URL with Default Browser:

import webbrowser
webbrowser.open("http://stackoverflow.com")

#Webbrowser can also try to open URLs in new windows with the open_new method:

import webbrowser
webbrowser.open_new("http://stackoverflow.com")

#Opening a new tab can be tried by the module using the open_new_tab method:

import webbrowser
webbrowser.open_new_tab("http://stackoverflow.com")

#Opening a URL with Dierent Browsers:

import webbrowser
ff_path = webbrowser.get("C:/Program Files/Mozilla Firefox/firefox.exe")
ff = webbrowser.get(ff_path)
ff.open("http://stackoverflow.com/")

#Registering a browser type:
import webbrowser
ff_path = webbrowser.get("C:/Program Files/Mozilla Firefox/firefox.exe")
ff = webbrowser.get(ff_path)
webbrowser.register('firefox', None, ff)
# Now to refer to use Firefox in the future you can use this
webbrowser.get('firefox').open("https://stackoverflow.com/")