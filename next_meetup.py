# -*- coding: utf-8 -*-
from dateutil.rrule import rrule, MONTHLY, WE
import locale
import os

template = """
{date_text}
{underline}
:date: {nextdate:%Y-%m-%d}
:category: News

Das nächste Treffen findet statt am:

Datum:
  Mi, {nextdate:%d.%m.%Y}
Uhrzeit:
  19:00
Ort:
  Chaos Computer Club Cologne, Heliosstr. 6a 50825 Köln (Anfahrt_)

Das Programm für das Treffen steht noch nicht fest.

Wir suchen noch Themen! Wenn Du einen Vortrag halten oder andere Programmpunkte
anmelden willst, schreibe einfach auf die Mailingliste! Daneben gibt es Raum für
spontan eingebrachte Themen, z.B. Buch- und Programm-Vorstellungen, Fragen,
Ankündigungen und alles was euch so zum Thema Python einfällt.

Ab ca. 21:00 Uhr werden wir den Abend gemütlich in einer nahe gelegenen
Kneipe (Herbrands) ausklingen lassen.

Hast Du vor, zu kommen oder bist verhindert? Sag' uns unverbindlich
über Meetup_ Bescheid (kostenlose Anmeldung erforderlich).

Etherpad Protokoll_

.. _Anfahrt: /pages/anfahrt-c4.html
.. _Meetup: http://www.meetup.com/pyCologne/
.. _Protokoll: http://yourpart.eu/p/pyc_{nextdate:%Y%m%d}
"""

locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')
nextdate = list(rrule(MONTHLY, byweekday=WE(+2), byhour=19, byminute=0, count=10))[0]

date_text = nextdate.strftime('%d. %B %Y')
underline = '=' * len(date_text)

rendered = template.format(**locals())

filepath = '/'.join(['.', 'content', '{0:%Y-%m-%d}.rst'.format(nextdate)])
print(filepath)
if not os.path.exists(filepath):
    print('generating')
    with open(filepath, 'w') as f:
        f.write(rendered)
else:
    print(rendered)
