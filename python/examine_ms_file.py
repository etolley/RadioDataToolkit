import casacore.tables as ct
import astropy.units as u
import pathlib, sys

if len(sys.argv) > 2:
    print("Program does not understand extra arguments. Expected input:\npython examine_ms_file.py {file_name} ")
    sys.exit()
elif len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    print("No input file received. Expected input:\npython examine_ms_file.py {file_name} ")
    sys.exit()

def examine(filename):

	print("ms file:", filename)

	path = pathlib.Path(filename).absolute()

	if not path.exists():
	    raise FileNotFoundError(f"{filename} does not exist.")

	if not path.is_dir():
	    raise NotADirectoryError(f"{filename} is not a directory, so cannot be an MS file.")

	print ("Columns are:")
	print(ct.taql(f"select * from {filename}").colnames())

	print ("Frequencies are:")
	query = f"select CHAN_FREQ, CHAN_WIDTH from {filename}::SPECTRAL_WINDOW"
	table = ct.taql(query)
	freq = table.getcell("CHAN_FREQ", 0).flatten() * u.Hz
	print(freq)


examine(file_name)



