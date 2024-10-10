import hashlib;




def fruity_hash(data:bytes)->str:
	h = hashlib.new("sha256");
	h.update(data);
	d = h.hexdigest();
	output:str = str();
	for index in range(0, len(d), 2):
		output += chr(0x1F435+
			eval(f"0x{d[index]}{d[index+1]}")
			);
	return output

print(fruity_hash("HELLO WORLD".encode()));
print();
print(fruity_hash("HELLO WORLDY".encode()));

