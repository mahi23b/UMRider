"""
This is simple script to invoke parallel conversion function from um2grb2
and pass the assimilated / forecasted hour as argument.

hour : 00
Output : It creates both analysis - 1 file (um_ana_00hr_date.grib2) and 
         forecast - 40 files (um_prg_00hr_date.grib2, ..., um_prg_240hr_date.grib2).
Written by : Arulalan.T
Date : 07.Dec.2015
"""

import os, sys 
#from g2utils.um2grb2 import convertAnlFiles, convertFcstFiles
# get this script abspath
scriptPath = os.path.dirname(os.path.abspath(__file__))
print "Reading configure file to load the paths"
# get the configure lines
clines = [l.strip() for l in open(os.path.join(scriptPath, 'configure')).readlines() \
                if not l.startswith(('#', '/', '!', '\n', '%'))]
# get the dictionary keys, values
cdic = {k.strip(): v.strip() for k,v in [l.split('=') for l in clines]}

# store into local variables
inPath = cdic.get('inPath', None)  
outPath = cdic.get('outPath', None)
tmpPath = cdic.get('tmpPath', None)

# check the variable's path 
for name, path in [('inPath', inPath), ('outPath', outPath), ('tmpPath', tmpPath)]:
    if path is None:
        raise ValueError("In configure file, '%s' path is not defined !" % name)
    if not os.path.exists(path):
        raise ValueError("In configure file, '%s = %s' path does not exists" % (name, path))
    print name, " = ", path
# end of for name, path in [...]:

print "Successfully loaded the above paths from configure file!"

### call analysis conversion function w.r.t data assimilated during short forecast hour.
#convertAnlFiles(inPath, outPath, tmpPath, hr='00')
##    
### call forecast conversion function w.r.t data assimilated at 00z long forecast hour.
#convertFcstFiles(inPath, outPath, tmpPath, hr='00')
