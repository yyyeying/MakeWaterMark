source_code = [0, 0, 1, 1, 0, 1]
[Hamcode,num_zero] = haming_encode(source_code)
size(Hamcode)
Hamcode(2) = 1;
source = haming_decode(Hamcode, num_zero)