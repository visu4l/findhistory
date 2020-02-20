
alerts = ["[17-Feb-2020 22:22:46] WARNING: [pool www]", "[17-Feb-2020 21:15:57] NOTICE: [pool www]"]

for msg in alerts:

	if msg.split(": ")[0].endswith("NOTICE"):
	    print("notice")
	else:
	    print("not notice")
	    