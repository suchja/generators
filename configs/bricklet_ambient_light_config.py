# -*- coding: utf-8 -*-

# Ambient Light Bricklet communication config

com = {
    'author': 'Olaf Lüke (olaf@tinkerforge.com)',
    'version': '1.0',
    'type': 'Bricklet',
    'name': ('AmbientLight', 'ambient_light'),
    'manufacturer': 'Tinkerforge',
    'description': 'Device for sensing Ambient Light',
    'packets': []
}

com['packets'].append({
'type': 'method', 
'name': ('GetIlluminance', 'get_illuminance'), 
'elements': [('illuminance', 'uint16', 1, 'out')],
'doc': ['bm', {
'en':
"""
Returns the illuminance of the ambient light sensor. The value
has a range of 0 to 9000 and is given in Lux/10, i.e. a value
of 4500 means that an illuminance of 450 Lux is measured.

If you want to get the illuminance periodically, it is recommended to use the
callback :func:`Illuminance` and set the period with 
:func:`SetIlluminanceCallbackPeriod`.
""",
'de':
"""
"""
}]
})

com['packets'].append({
'type': 'method', 
'name': ('GetAnalogValue', 'get_analog_value'), 
'elements': [('value', 'uint16', 1, 'out')],
'doc': ['am', {
'en':
"""
Returns the value as read by a 12 bit analog to digital converter.
The value is between 0 and 4095.

 .. note::
  The value returned by :func:`GetIlluminance` is averaged over several samples
  to yield less noise, while :func:`GetAnalogValue` gives back raw
  unfiltered analog values. The only reason to use :func:`GetAnalogValue` is,
  if you need the full resolution of the analog to digital converter.

  Also, the analog to digital converter covers three different ranges that are
  set dynamically depending on the light intensity. It is impossible to
  distinguish between these ranges with the analog value.

If you want the analog value periodically, it is recommended to use the 
callback :func:`AnalogValue` and set the period with 
:func:`SetAnalogValueCallbackPeriod`.
""",
'de':
"""
"""
}]
})


com['packets'].append({
'type': 'method', 
'name': ('SetIlluminanceCallbackPeriod', 'set_illuminance_callback_period'), 
'elements': [('period', 'uint32', 1, 'in')],
'doc': ['ccm', {
'en':
"""
Sets the period in ms with which the :func:`Illuminance` callback is called 
periodically. A value of 0 turns the callback off.

:func:`Illuminance` is only called if the illuminance has changed since the
last call.

The default value is 0.
""",
'de':
"""
"""
}]
})

com['packets'].append({
'type': 'method', 
'name': ('GetIlluminanceCallbackPeriod', 'get_illuminance_callback_period'), 
'elements': [('period', 'uint32', 1, 'out')],
'doc': ['ccm', {
'en':
"""
Returns the period as set by :func:`SetIlluminanceCallbackPeriod`.
""",
'de':
"""
"""
}]
})

com['packets'].append({
'type': 'method', 
'name': ('SetAnalogValueCallbackPeriod', 'set_analog_value_callback_period'), 
'elements': [('period', 'uint32', 1, 'in')],
'doc': ['ccm', {
'en':
"""
Sets the period in ms with which the :func:`AnalogValue` callback is called 
periodically. A value of 0 turns the callback off.

:func:`AnalogValue` is only called if the analog value has changed since the
last call.

The default value is 0.
""",
'de':
"""
"""
}]
})

com['packets'].append({
'type': 'method', 
'name': ('GetAnalogValueCallbackPeriod', 'get_analog_value_callback_period'), 
'elements': [('period', 'uint32', 1, 'out')],
'doc': ['ccm', {
'en':
"""
Returns the period as set by :func:`SetAnalogValueCallbackPeriod`.
""",
'de':
"""
"""
}]
})

com['packets'].append({
'type': 'method', 
'name': ('SetIlluminanceCallbackThreshold', 'set_illuminance_callback_threshold'), 
'elements': [('option', 'char', 1, 'in'), 
             ('min', 'int16', 1, 'in'),
             ('max', 'int16', 1, 'in')],
'doc': ['ccm', {
'en':
"""
Sets the thresholds for the :func:`IlluminanceReached` callback. 

The following options are possible:

.. csv-table::
 :header: "Option", "Description"
 :widths: 10, 100

 "'x'", "Callback is turned off."
 "'o'", "Callback is called when the illuminance is *outside* the min and max values"
 "'i'", "Callback is called when the illuminance is *inside* the min and max values"
 "'<'", "Callback is called when the illuminance is smaller than the min value (max is ignored)"
 "'>'", "Callback is called when the illuminance is greater than the min value (max is ignored)"

The default value is ('x', 0, 0).
""",
'de':
"""
"""
}]
})

com['packets'].append({
'type': 'method', 
'name': ('GetIlluminanceCallbackThreshold', 'get_illuminance_callback_threshold'), 
'elements': [('option', 'char', 1, 'out'), 
             ('min', 'int16', 1, 'out'),
             ('max', 'int16', 1, 'out')],
'doc': ['ccm', {
'en':
"""
Returns the threshold as set by :func:`SetIlluminanceCallbackThreshold`.
""",
'de':
"""
"""
}]
})

com['packets'].append({
'type': 'method', 
'name': ('SetAnalogValueCallbackThreshold', 'set_analog_value_callback_threshold'), 
'elements': [('option', 'char', 1, 'in'), 
             ('min', 'uint16', 1, 'in'),
             ('max', 'uint16', 1, 'in')],
'doc': ['ccm', {
'en':
"""
Sets the thresholds for the :func:`AnalogValueReached` callback. 

The following options are possible:

.. csv-table::
 :header: "Option", "Description"
 :widths: 10, 100

 "'x'", "Callback is turned off."
 "'o'", "Callback is called when the illuminance is *outside* the min and max values"
 "'i'", "Callback is called when the illuminance is *inside* the min and max values"
 "'<'", "Callback is called when the illuminance is smaller than the min value (max is ignored)"
 "'>'", "Callback is called when the illuminance is greater than the min value (max is ignored)"

The default value is ('x', 0, 0).
""",
'de':
"""
"""
}]
})

com['packets'].append({
'type': 'method', 
'name': ('GetAnalogValueCallbackThreshold', 'get_analog_value_callback_threshold'), 
'elements': [('option', 'char', 1, 'out'), 
             ('min', 'uint16', 1, 'out'),
             ('max', 'uint16', 1, 'out')],
'doc': ['ccm', {
'en':
"""
Returns the threshold as set by :func:`SetAnalogValueCallbackThreshold`.
""",
'de':
"""
"""
}]
})

com['packets'].append({
'type': 'method', 
'name': ('SetDebouncePeriod', 'set_debounce_period'), 
'elements': [('debounce', 'uint32', 1, 'in')],
'doc': ['ccm', {
'en':
"""
Sets the period in ms with which the threshold callbacks

 :func:`IlluminanceReached`, :func:`AnalogValueReached`

are called, if the thresholds 

 :func:`SetIlluminanceCallbackThreshold`, :func:`SetAnalogValueCallbackThreshold`

keep beeing reached.

The default value is 100.
""",
'de':
"""
"""
}]
})

com['packets'].append({
'type': 'method', 
'name': ('GetDebouncePeriod', 'get_debounce_period'), 
'elements': [('debounce', 'uint32', 1, 'out')],
'doc': ['ccm', {
'en':
"""
Returns the debounce period as set by :func:`SetDebouncePeriod`.
""",
'de':
"""
"""
}]
})

com['packets'].append({
'type': 'signal', 
'name': ('Illuminance', 'illuminance'), 
'elements': [('illuminance', 'uint16', 1, 'out')],
'doc': ['c', {
'en':
"""
This callback is called periodically with the period that is set by 
:func:`SetIlluminanceCallbackPeriod`. The parameter is the illuminance of the
ambient light sensor.

:func:`Illuminance` is only called if the illuminance has changed since the
last call.
""",
'de':
"""
"""
}]
})

com['packets'].append({
'type': 'signal', 
'name': ('AnalogValue', 'analog_value'), 
'elements': [('value', 'uint16', 1, 'out')],
'doc': ['c', {
'en':
"""
This callback is called periodically with the period that is set by 
:func:`SetAnalogValueCallbackPeriod`. The parameter is the analog value of the
ambient light sensor.

:func:`AnalogValue` is only called if the illuminance has changed since the
last call.
""",
'de':
"""
"""
}]
})

com['packets'].append({
'type': 'signal', 
'name': ('IlluminanceReached', 'illuminance_reached'), 
'elements': [('illuminance', 'uint16', 1, 'out')],
'doc': ['c', {
'en':
"""
This callback is called when the threshold as set by
:func:`SetIlluminanceCallbackThreshold` is reached.
The parameter is the illuminance of the ambient light sensor.

If the threshold keeps beeing reached, the callback is called periodically 
with the period as set by :func:`SetDebouncePeriod`.
""",
'de':
"""
"""
}]
})

com['packets'].append({
'type': 'signal', 
'name': ('AnalogValueReached', 'analog_value_reached'), 
'elements': [('value', 'uint16', 1, 'out')],
'doc': ['c', {
'en':
"""
This callback is called when the threshold as set by
:func:`SetAnalogValueCallbackThreshold` is reached.
The parameter is the analog value of the ambient light sensor.

If the threshold keeps beeing reached, the callback is called periodically 
with the period as set by :func:`SetDebouncePeriod`.
""",
'de':
"""
"""
}]
})