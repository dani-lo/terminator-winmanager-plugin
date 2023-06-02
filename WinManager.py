from gi.repository import Gtk

import terminatorlib.plugin as plugin

from terminatorlib.util import dbg, err
from terminatorlib.config import Config

CONFIG_DISPLAY_NAME = 'Win Manager'
CONFIG_SAVE_TITLE = 'save size and position to layout'

TERMINATOR_EVENT_ACTIVATE = 'activate'
TERMINATOR_EVENT_CLICKED = 'clicked'
TERMINATOR_EVENT_DESTROY = 'destroy'
TERMINATOR_EVENT_DELETE = 'delete_event'

AVAILABLE = ['WinManager']

CONFIG_PROFILE_WINDOW_KEY = 'window0'
CONFIG_PROFILE_CHILD_KEY = 'child0'

class ConfigWithPositionAndSize (Config):
    
    def __init__ (self, profile):
        """
        Extend Terminator module Config, add the new
        saving functionality for terminal window size and position
        @param profile: terminatorlib - Profile
        """

        super(ConfigWithPositionAndSize, self).__init__(profile)


    def set_win_size_pos (self, w, h, position):
        """
        Write new w, h and position to active profile settings
        @param w: number
        @param h: number
        @param position: number
        """

        new_size_list = [w,h]

        self.base.layouts[self.profile][CONFIG_PROFILE_WINDOW_KEY]['size'] = new_size_list
        self.base.layouts[self.profile][CONFIG_PROFILE_WINDOW_KEY]['position'] = position
        
        self.base.save()

        self.save()

class WinManager(plugin.MenuItem):
    capabilities = ['terminal_menu']

    def __init__(self):

        self.plugin_name = self.__class__.__name__
    
    def callback(self, menuitems, menu, terminal):
        """
        Click call back invoked from Terminator when user right clicks window
        @param menuitems: List of menu items, that will be displayed. Mutable
        @param menu: GTK menu instance
        @param terminal Terminal class instance pased from erminator
        """

        plugin_menu_item = Gtk.MenuItem(CONFIG_DISPLAY_NAME)
        plugin_submenu = Gtk.Menu()

        plugin_menu_item.set_submenu(plugin_submenu)

        plugin_submenu.append(self.create_save_win_pos_submenu_item(terminal))
        plugin_submenu.append(Gtk.SeparatorMenuItem())

        menuitems.append(plugin_menu_item)

    def create_save_win_pos_submenu_item(self, terminal):
        """
        @param terminal: Terminal class instance pased from terminator
        """

        save_item = Gtk.ImageMenuItem(CONFIG_SAVE_TITLE)

        image = Gtk.Image()
        image.set_from_icon_name(Gtk.STOCK_FLOPPY, Gtk.IconSize.MENU)

        save_item.set_image(image)
        save_item.connect(TERMINATOR_EVENT_ACTIVATE, self.save_callback, terminal)

        return save_item

    
    def save_callback(self, _, terminal):
        """
        Called by gtk, if user clicked the save menu item.
        @param _: full menu item; not used
        @param terminal: The terminal this context menu item belongs to.
        """

        alloc = terminal.terminalbox.get_allocation()

        current_profile_name =  terminal.config.get_profile()
        current_layout = terminal.terminator.describe_layout()

        config_editor = ConfigWithPositionAndSize(current_profile_name)

        new_width = alloc.width
        new_height = alloc.height
        new_position = current_layout[CONFIG_PROFILE_CHILD_KEY]['position']

        config_editor.set_win_size_pos(new_width, new_height, new_position)
        