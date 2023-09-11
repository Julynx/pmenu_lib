# pmenu
*Sleek dmenu alternative written in Python and powered by curses.*

<br>
<p align="center">
  <img width="600" src="https://i.imgur.com/2omHG8y.png">
</p>
<br>

Comes in different flavors:

- The ```pmenu``` CLI, for your terminal and shell scripts. [[📂 GitHub]](https://github.com/Julynx/pmenu)
- The ```pmenu_lib``` package, for your Python projects. [[📦 PyPi]](https://pypi.org/project/pmenu-lib/) [[📂 GitHub]](https://github.com/Julynx/pmenu_lib)

You are now looking at the ```pmenu_lib``` Python package.

<br>

## Usage
The ```pmenu(list_of_options)``` function will display a menu and return the selected option as a ```str```, or ```None``` if the menu is closed without selecting an option.

```python
from pmenu_lib import pmenu

selected_option = pmenu(list_of_options)
```

<br>

## Menu bindings

- **Up arrow**: Highlight the previous menu entry.
- **Down arrow**: Highlight the next menu entry.
- **Enter**: Select the highlighted entry.
- **Esc**: Close the menu.
