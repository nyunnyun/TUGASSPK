arrdata = [
	{"lampu":1, "value":""},
	{"lampu":2, "value":""},
	{"lampu":3, "value":""},
	{"lampu":4, "value":""}]

input = 5
for i in range(0, len(arrdata)):
	if arrdata[i]["lampu"] == input:
		arrdata[i]["value"]="hijau"
	else:
		arrdata[i]["value"]="merah"
print(arrdata)