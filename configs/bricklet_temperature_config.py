# -*- coding: utf-8 -*-

# Temperature Bricklet communication config

com = {
    'author': 'Olaf Lüke (olaf@tinkerforge.com)',
    'version': '1.0',
    'type': 'Bricklet',
    'name': ('Temperature', 'temperature'),
    'manufacturer': 'Tinkerforge',
    'description': 'Device for sensing Temperature',
    'packets': []
}

com['packets'].append({
'type': 'method', 
'name': ('GetTemperature', 'get_temperature'), 
'elements': [('temperature', 'int16', 1, 'out')],
'doc': ['bm', {
'en':
"""
Returns the temperature of the sensor. The value
has a range of -2500 to 8500 and is given in °C/100,
e.g. a value of 4223 means that a temperature of 42.23 °C is measured.

If you want to get the temperature periodically, it is recommended 
to use the callback :func:`Temperature` and set the period with 
:func:`SetTemperatureCallbackPeriod`.
""",
'de':
"""
"""
}]
})

com['packets'].append({
'type': 'method', 
'name': ('SetTemperatureCallbackPeriod', 'set_temperature_callback_period'), 
'elements': [('period', 'uint32', 1, 'in')],
'doc': ['ccm', {
'en':
"""
Sets the period in ms with which the :func:`Temperature` callback is called 
periodically. A value of 0 turns the callback off.

:func:`Temperature` is only called if the temperature has changed since the
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
'name': ('GetTemperatureCallbackPeriod', 'get_temperature_callback_period'), 
'elements': [('period', 'uint32', 1, 'out')],
'doc': ['ccm', {
'en':
"""
Returns the period as set by :func:`SetTemperatureCallbackPeriod`.
""",
'de':
"""
"""
}]
})

com['packets'].append({
'type': 'method', 
'name': ('SetTemperatureCallbackThreshold', 'set_temperature_callback_threshold'), 
'elements': [('option', 'char', 1, 'in'), 
             ('min', 'int16', 1, 'in'),
             ('max', 'int16', 1, 'in')],
'doc': ['ccm', {
'en':
"""
Sets the thresholds for the :func:`TemperatureReached` callback. 

The following options are possible:

.. csv-table::
 :header: "Option", "Description"
 :widths: 10, 100

 "'x'", "Callback is turned off."
 "'o'", "Callback is called when the temperature is *outside* the min and max values"
 "'i'", "Callback is called when the temperature is *inside* the min and max values"
 "'<'", "Callback is called when the temperature is smaller than the min value (max is ignored)"
 "'>'", "Callback is called when the temperature is greater than the min value (max is ignored)"

The default value is ('x', 0, 0).
""",
'de':
"""
"""
}]
})

com['packets'].append({
'type': 'method', 
'name': ('GetTemperatureCallbackThreshold', 'get_temperature_callback_threshold'), 
'elements': [('option', 'char', 1, 'out'), 
             ('min', 'int16', 1, 'out'),
             ('max', 'int16', 1, 'out')],
'doc': ['ccm', {
'en':
"""
Returns the threshold as set by :func:`SetTemperatureCallbackThreshold`.
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
Sets the period in ms with which the threshold callback

 :func:`TemperatureReached`

is called, if the threshold

 :func:`SetTemperatureCallbackThreshold`

keeps beeing reached.

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
'name': ('Temperature', 'temperature'), 
'elements': [('temperature', 'int16', 1, 'out')],
'doc': ['c', {
'en':
"""
This callback is called periodically with the period that is set by 
:func:`SetTemperatureCallbackPeriod`. The parameter is the temperature of the
sensor.

:func:`Temperature` is only called if the temperature has changed since the
last call.
""",
'de':
"""
"""
}]
})

com['packets'].append({
'type': 'signal', 
'name': ('TemperatureReached', 'temperature_reached'), 
'elements': [('temperature', 'int16', 1, 'out')],
'doc': ['c', {
'en':
"""
This callback is called when the threshold as set by
:func:`SetTemperatureCallbackThreshold` is reached.
The parameter is the temperature of the sensor.

If the threshold keeps beeing reached, the callback is called periodically 
with the period as set by :func:`SetDebouncePeriod`.
""",
'de':
"""
"""
}]
})