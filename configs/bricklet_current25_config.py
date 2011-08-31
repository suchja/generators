# -*- coding: utf-8 -*-

# Rotary Poti Bricklet communication config

com = {
    'author': 'Olaf Lüke (olaf@tinkerforge.com)',
    'version': '1.0',
    'type': 'Bricklet',
    'name': ('Current25', 'current25'),
    'manufacturer': 'Tinkerforge',
    'description': 'Device for sensing current of up to 25A',
    'packets': []
}

com['packets'].append({
'type': 'method', 
'name': ('GetCurrent', 'get_current'), 
'elements': [('current', 'int16', 1, 'out')],
'doc': ['bm', {
'en':
"""
Returns the current of the sensor. The value is in mA
and between -25000mA and 25000mA.

If you want to get the current periodically, it is recommended to use the
callback :func:`Current` and set the period with 
:func:`SetCurrentCallbackPeriod`.
""",
'de':
"""
"""
}]
})

com['packets'].append({
'type': 'method', 
'name': ('Calibrate', 'calibrate'), 
'elements': [],
'doc': ['am', {
'en':
"""
Calibrates the 0 value of the sensor. You have to call this function
when there is no current present. 

The zero point of the current sensor
is depending on the exact properties of the analog to digital converter,
the length of the Bricklet cable and the temperature. Thus, if you change
the Brick or the environment in which the Bricklet is used, you might
have to recalibrate.

The resulting calibration will be saved on the eeprom of the Current
Bricklet.
""",
'de':
"""
"""
}]
})


com['packets'].append({
'type': 'method', 
'name': ('IsOverCurrent', 'is_over_current'), 
'elements': [('over', 'bool', 1, 'out')],
'doc': ['am', {
'en':
"""
Returns true if more than 25A were measured.

 .. note::
  To reset this value you have to power cycle the Bricklet.

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
  The value returned by :func:`GetCurrent` is averaged over several samples
  to yield less noise, while :func:`GetAnalogValue` gives back raw
  unfiltered analog values. The only reason to use :func:`GetAnalogValue` is,
  if you need the full resolution of the analog to digital converter.

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
'name': ('SetCurrentCallbackPeriod', 'set_current_callback_period'), 
'elements': [('period', 'uint32', 1, 'in')],
'doc': ['ccm', {
'en':
"""
Sets the period in ms with which the :func:`Current` callback is called 
periodically. A value of 0 turns the callback off.

:func:`Current` is only called if the current has changed since the
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
'name': ('GetCurrentCallbackPeriod', 'get_current_callback_period'), 
'elements': [('period', 'uint32', 1, 'out')],
'doc': ['ccm', {
'en':
"""
Returns the period as set by :func:`SetCurrentCallbackPeriod`.
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
'name': ('SetCurrentCallbackThreshold', 'set_current_callback_threshold'), 
'elements': [('option', 'char', 1, 'in'), 
             ('min', 'int16', 1, 'in'),
             ('max', 'int16', 1, 'in')],
'doc': ['ccm', {
'en':
"""
Sets the thresholds for the :func:`CurrentReached` callback. 

The following options are possible:

.. csv-table::
 :header: "Option", "Description"
 :widths: 10, 100

 "'x'", "Callback is turned off."
 "'o'", "Callback is called when the current is *outside* the min and max values"
 "'i'", "Callback is called when the current is *inside* the min and max values"
 "'<'", "Callback is called when the current is smaller than the min value (max is ignored)"
 "'>'", "Callback is called when the current is greater than the min value (max is ignored)"

The default value is ('x', 0, 0).
""",
'de':
"""
"""
}]
})

com['packets'].append({
'type': 'method', 
'name': ('GetCurrentCallbackThreshold', 'get_current_callback_threshold'), 
'elements': [('option', 'char', 1, 'out'), 
             ('min', 'int16', 1, 'out'),
             ('max', 'int16', 1, 'out')],
'doc': ['ccm', {
'en':
"""
Returns the threshold as set by :func:`SetCurrentCallbackThreshold`.
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
 "'o'", "Callback is called when the current is *outside* the min and max values"
 "'i'", "Callback is called when the current is *inside* the min and max values"
 "'<'", "Callback is called when the current is smaller than the min value (max is ignored)"
 "'>'", "Callback is called when the current is greater than the min value (max is ignored)"

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

 :func:`CurrentReached`, :func:`AnalogValueReached`

are called, if the thresholds 

 :func:`SetCurrentCallbackThreshold`, :func:`SetAnalogValueCallbackThreshold`

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
'name': ('Current', 'current'), 
'elements': [('current', 'int16', 1, 'out')],
'doc': ['c', {
'en':
"""
This callback is called periodically with the period that is set by 
:func:`SetCurrentCallbackPeriod`. The parameter is the current of the
sensor.

:func:`Current` is only called if the current has changed since the
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
sensor.

:func:`AnalogValue` is only called if the current has changed since the
last call.
""",
'de':
"""
"""
}]
})

com['packets'].append({
'type': 'signal', 
'name': ('CurrentReached', 'current_reached'), 
'elements': [('current', 'int16', 1, 'out')],
'doc': ['c', {
'en':
"""
This callback is called when the threshold as set by
:func:`SetCurrentCallbackThreshold` is reached.
The parameter is the current of the sensor.

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
The parameter is the analog value of the sensor.

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
'name': ('OverCurrent', 'over_current'), 
'elements': [],
'doc': ['c', {
'en':
"""
This callback is called when an over current is measured
(see :func:`IsOverCurrent`).
""",
'de':
"""
"""
}]
})