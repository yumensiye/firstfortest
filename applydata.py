test = "[15Fall . MS . AD无奖 ] [ DateScience/Analytics @ MSDS@NYU ] - 2015-03-07 - T : 107 + G : 321 () 本科：南大，浙大，复旦，上交 , ... 2 3"

new_string = test.replace(" " , "").split("]")
univer_info =  new_string[1].replace("[", "").split("@")
date = new_string[2].split("-")
print(date)
print(univer_info)


