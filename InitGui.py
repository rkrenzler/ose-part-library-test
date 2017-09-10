#########################################################################################
#  This file is part of the Open Source Ecology D3D 3D Printer Workbench for FreeCAD.
#
#  Copyright (C) 2017 Stephen Kaiser <freesol29|at|gmail.com>
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2 of the License, or (at your option) any later version.
#                                                                                     
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library; if not, If not, see 
#  <http://www.gnu.org/licenses/>.
#
#########################################################################################
#!/usr/bin/python

class D3DWorkbench (Workbench):

    MenuText = "D3D Printer Workbench"
    ToolTip = "A workbench for designing D3D 3D printers by Open Source Ecology"
    #Icon = """paste here the contents of a 16x16 xpm icon"""

    def Initialize(self):
        "This function is executed when FreeCAD starts"
        import AddFrame # import here all the needed files that create your FreeCAD commands
        self.list = ["AddFrame"] # A list of command names created in the line above
        self.appendToolbar("D3D", self.list) # creates a new toolbar with your commands
        #FreeCADGui.addIconPath( ':/d3d/icons' )
        #FreeCADGui.addPreferencePage( ':/d3d/ui/assembly2_prefs.ui','Assembly2' )
        self.appendMenu("Design Menu", self.list) # creates a new menu
        #self.appendMenu(["An existing Menu", "My submenu"], self.list) # appends a submenu to an existing menu

    def Activated(self):
        "This function is executed when the workbench is activated"
        return

    def Deactivated(self):
        "This function is executed when the workbench is deactivated"
        return

    def ContextMenu(self, recipient):
        "This is executed whenever the user right-clicks on screen"
        # "recipient" will be either "view" or "tree"
        self.appendContextMenu("D3D commands", self.list) # add commands to the context menu

    def GetClassName(self): 
        # this function is mandatory if this is a full python workbench
        return "Gui::PythonWorkbench"
       
Gui.addWorkbench(D3DWorkbench())