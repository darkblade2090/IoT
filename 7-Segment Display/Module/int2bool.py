def convert(a):
	temp = bin(a)[2:]
	temp_bin = [0,0,0,0,0,0,0,0]
	i = -1
	for x in range(len(temp)):
		temp_bin[i] = int(temp[i])
		i-=1
	return(temp_bin)

#[0,0,0,0,1,1,0,0]
