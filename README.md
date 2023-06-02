## Terminator window size and position manager plugin

### About

Terminator cli plugin allows to save Terminator's window position and layout (width, height) to the layout settings, so these can be replicated upon launch.

### Usage

- Follow the Install instructions and re-launch Terminator,
- In Terminator ***preferences**, under the **Plugins** tab, you should now see a **WinManager** plugin entry: activate it by clicking on its corresponding checkbox,
- After launching Terminator again and modifying its position and size, right click on its window to start the contextual menu,
- If the plugin is activated, you will see a menu item (at the bottom) named **Win Manager**,
- The **Win Manager** submenu has an action (**Save size and position to layout**). By clicking on it, the current position and size will be saved to your layout settings, and all future instances will respect those layout parameters upon launch.

### Install

Copy the python plugin file (**WinManager.py**) to the Terminator plugins directory - wehre this is located is system dependant: on Linux it will be at 
**~/.config/terminator/plugins** - Included in this repo is a basic shell script  (**deploy_local.sh**) to copy the plugin there .

See notes on plugins for Terminator at [Read The Docs](https://terminator-gtk3.readthedocs.io/en/latest/plugins.html).

