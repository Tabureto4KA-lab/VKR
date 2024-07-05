idx = await server.register_namespace("VKR")

# экструдер
extruder = await server.nodes.objects.add_object(idx, 'Extruder')

# температура первой зоны
extruder_temperature_zone_1 = await extruder.add_variable(idx, 'Temperature in first zone', 0.0)

# температура второй зоны
extruder_temperature_zone_2 = await extruder.add_variable(idx, 'Temperature in second zone', 0.0)

# температура третьей зоны
extruder_temperature_zone_3 = await extruder.add_variable(idx, 'Temperature in third zone', 0.0)

# давление экструдера
extruder_pressure = await extruder.add_variable(idx, 'Extruder pressure', 0.0)

# холодильник
chiller = await server.nodes.objects.add_object(idx, 'Chiller')

# температура холодильника
chiller_temperature = await chiller.add_variable(idx, 'Temperature in chiller', 0.0)

# система укрепления
streighthening_system = await server.nodes.objects.add_object(idx, 'Streighthening System')

# температура в системе укрепления
streighthening_system_temperature = await streighthening_system.add_variable(idx, 'Temperature in streighthening system', 0.0)

# система намотки
rolling_system = await server.nodes.objects.add_object(idx, 'Rolling System')

# корость намотки
rolling_system_speed = await rolling_system.add_variable(idx, 'Rolling speed', 0.0)