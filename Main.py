data = 'Akatsuki' #Taking Data from the User
# conversion Chart
la="abcdefghijklmnopqrstuvwxyz"
ua="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lra=la[::-1]
ura=ua[::-1]
# Creating converted output
converted_data = ""
 
 
for i in range(0, len(data)):
    if data[i] in la:
        converted_data+=lra[la.index(data[i])]
    elif data[i] in ua:
        converted_data+=ura[ua.index(data[i])]
    else:
        converted_data+=" "
# Printing converted output
print(converted_data)

#Be carefull because before editing the code as this might cause an error
