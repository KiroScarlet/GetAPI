json_array = [{"time": 20150312, "value": "c","value11": "c"}, {"time": 20150301, "value": "a","value11": "c"}, {"time": 20150305, "value": "b","value11": "c"}]

json_array.sort(key=lambda x: x["time"])

print(json_array)