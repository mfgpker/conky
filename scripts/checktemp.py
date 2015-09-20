#${acpitemp}

import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

QMessageBox.information('Info Message', '''You pressed Cancel''',
            QMessageBox.Ok)
#QgsMessageLog.logMessage("message")

#from gi.repository import Gtk

#dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
#            Gtk.ButtonsType.OK, "This is an INFO MessageDialog")
#dialog.format_secondary_text(
#    "And this is the secondary text that explains things.")
#dialog.run()
#print "INFO dialog closed"
