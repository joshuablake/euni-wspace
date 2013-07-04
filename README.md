euni-wspace
===========
A Django app to extend [eve-wspace](https://github.com/marbindrakon/eve-wspace) for use internally in EVE University.

Installation
-------------
Assuming pip and eve-wspace are installed:

1. `pip install git+git://github.com/joshuablake/euni-wspace.git`
2. Add the following to `local_settings.py`:

    ```python
    from settings import INSTALLED_APPS
    INSTALLED_APPS += ('euniwspace',)
    EUNI_AUTH = 'sekrit_alphanumeric_code'
    ```
3. Run `python manage.py migrate euniwspace`

Usage
------
Call url of format: https://&lt;domain&gt;/euni/scanners/&lt;auth&gt;/&lt;map_id&gt;/&lt;from&gt;/&lt;to&gt;.&lt;format&gt;
Parameters are as follows:
* &lt;domain&gt;: domain of your mapper
* &lt;auth&gt;: the EUNI_AUTH setting you placed above
* &lt;map_id&gt;: id of the map you want to find scanners for
* &lt;from&gt;: date in YYYY-MM-DD (eg 2013-01-31) format for start date of query
* &lt;to&gt;: (optional) date in YYYY-MM-DD format for end date of query (defaults to current day)
* &lt;format&gt;: either xml or csv

Example URL to get all scanning logs since the start of 2013 on map with id 1:
https://euni.evewspace.com/euni/scanners/AUTH/1/2013-01-01.xml

### Example Output ###
XML
```XML
<scanners>
  <log>
    <user>Terra</user>
    <time>2013-06-22T12:00:54+00:00</time>
    <system>NJ4X-S</system>
    <id>AAS</id>
    <type>Gas Site</type>
    <info></info>
    <strength>None</strength>
  </log>
  <log>
    <user>Marbin</user>
    <time>2013-07-04T14:35:32+00:00</time>
    <system>J211036</system>
    <id>AIG-472</id>
    <type>Ore Site</type>
    <info>Ordinary</info>
    <strength>None</strength>
  </log>
</scanners>
```

CSV
```CSV
Scanner,Time,System,Signature ID,Type,Info,Strength
josh,2013-06-22 12:00,NJ4X-S,AAS,Gas Site,,
josh,2013-07-04 14:35,J211036,AIG-472,Ore Site,Ordinary ,
```
