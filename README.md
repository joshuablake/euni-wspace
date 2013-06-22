euni-wspace
===========
A Django app to extend [eve-wspace](https://github.com/marbindrakon/eve-wspace) for use internally in EVE University.

Installation
-------------
Assuming pip and eve-wspace are installed:

1. `pip install git+git://github.com/joshuablake/euni-wspace.git`
2. Add euniwspace to your INSTALLED_APPS in settings.py
3. Run `python manage.py migrate euniwspace`

Alternative Step 2
-------------------
If you do not wish to edit settings.py the following can be added to local_settings.py
```python
from settings import INSTALLED_APPS
INSTALLED_APPS += ('euniwspace',)
```
