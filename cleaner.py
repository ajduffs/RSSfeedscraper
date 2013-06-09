#Takes a raw text file of links with possible duplications and outputs a clean file, no duplicates.

outfile = open('cleanest.txt', 'w')

prev = None
for line in sorted(open('urltest.txt')):
  line = line.strip()
  if prev is not None and not line.startswith(prev):
	outfile.write(prev + '\n')
  prev = line
  
if prev is not None:
  outfile.write(prev + '\n')
