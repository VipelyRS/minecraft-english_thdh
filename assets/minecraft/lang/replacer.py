# This file “won't work” after one use since all "th"s
# will have already been converted and the file itself
# replaced.
f = open("enws.json", 'r');
json = f.read();
f.close();



in_string = False;  # In a string.
on_rhs    = False;  # On the value side of a JSON key/value pair.
out       = "";     # The output of the translation.
pos       = 0;

while pos < len(json):
	if in_string:
		snippet += json[pos];
		if json[pos].isspace():
			snippet = "";
	
	if in_string and on_rhs:
		if (json[pos]+json[pos+1]).lower() == "th":
			# Only replaces "th" with thorn because I'm too
			# lazy to make a determination algorithm;
			# all inappropriate 'ð's will be replaced with
			# 'þ' manually.
			if json[pos] == 'T':
				out += 'Ð';
			else:
				out += 'ð';
			pos += 2;
			print();
			continue;
	
	if json[pos] == '"':
		if not in_string:
			in_string = True;
		elif in_string and json[pos-1] != '\\':
			in_string = False;
	
	if json[pos] == ':' and not in_string and not on_rhs:
		on_rhs = True;
	
	if json[pos] == ',' and not in_string:
		on_rhs = False;
	
	out += json[pos];
	pos += 1;



f = open("out.json", 'x');
f.write(out);
f.close();