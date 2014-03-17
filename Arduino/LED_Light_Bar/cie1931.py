INPUT_SIZE = 255     # Input integer size
OUTPUT_SIZE = 255      # Output integer size
INT_TYPE = 'const unsigned char'
TABLE_NAME = 'cie';

def cie1931(L):
    L = L*100.0
    if L <= 8:
        return (L/902.3)
    else:
        return ((L+16.0)/116.0)**3

x = range(0,int(INPUT_SIZE+1))
y = [round(cie1931(float(L)/INPUT_SIZE)*OUTPUT_SIZE) for L in x]

f = open('cie1931.h', 'w')
f.write('// CIE1931 correction table\n')
f.write('// Automatically generated\n\n')

f.write('%s %s[%d] = {\n' % (INT_TYPE, TABLE_NAME, INPUT_SIZE+1))
f.write('\t')
for i,L in enumerate(y):
    f.write('%d, ' % int(L))
    if i % 10 == 9:
        f.write('\n\t')
f.write('\n};\n\n')