# MIS 207 HW08
#
# Link to JSON Example:
# https://opensource.adobe.com/Spry/samples/data_region/JSONDataSetSample.html

data = [
	{
		"color": "red",
		"value": "#f00"
	},
	{
		"color": "green",
		"value": "#0f0"
	},
	{
		"color": "blue",
		"value":"#00f"
	},
	{
		"color": "cyan",
		"value": "#0ff"
	},
	{
		"color": "magenta",
		"value": "#f0f"
	}
]

magenta_hex = data[4]['value']
print(magenta_hex)

second_color = data[1]["color"]
print(second_color)