# sacct --jobs=747008,747009,745642,747010,745448,747011,747012,747013,747004,747014,747015,747016,747005,747017,745641,747006,747007 --format="JobName%100,ConsumedEnergyRaw"



# NPROC1x2x2x2_nrhs1:		ninversions = 32
# NPROC1x2x2x2_nrhs2:		ninversions = 32
# NPROC1x2x2x2_nrhs4:		ninversions = 64
# NPROC1x2x2x2_nrhs6:		ninversions = 120
# NPROC1x2x2x2_nrhs8:		ninversions = 128
# NPROC1x2x2x2_nrhs10:	ninversions = 100
# NPROC1x2x2x2_nrhs12:	ninversions = 120
# NPROC1x2x2x2_nrhs14:	ninversions = 112
# NPROC1x2x2x2_nrhs16:	ninversions = 128
# NPROC1x2x2x2_nrhs20:	ninversions = 160
# NPROC1x2x2x2_nrhs24:	ninversions = 192
# NPROC1x2x2x2_nrhs28:	ninversions = 224
# NPROC1x2x2x2_nrhs32:	ninversions = 256
# NPROC1x2x2x2_nrhs40:	ninversions = 320
# NPROC1x2x2x2_nrhs48:	ninversions = 384



d = {
	"NPROC1x2x2x2_nrhs1": 	189971 / 32,
	"NPROC1x2x2x2_nrhs2": 	562493 / 32,
	"NPROC1x2x2x2_nrhs4": 	940673 / 64,
	"NPROC1x2x2x2_nrhs6": 	1440773 / 120,
	"NPROC1x2x2x2_nrhs8": 	1618976 / 128,
	"NPROC1x2x2x2_nrhs10": 	1496859 / 100,
	"NPROC1x2x2x2_nrhs12": 	1709585 / 120,
	"NPROC1x2x2x2_nrhs14": 	1810577 / 112,
	"NPROC1x2x2x2_nrhs16": 	479914 / 128,
	"NPROC1x2x2x2_nrhs20": 	2443812 / 160,
	"NPROC1x2x2x2_nrhs24": 	2906284 / 192,
	"NPROC1x2x2x2_nrhs28": 	3512251 / 224,
	"NPROC1x2x2x2_nrhs32": 	890606 / 256,
	"NPROC1x2x2x2_nrhs40": 	2871147 / 320,
	"NPROC1x2x2x2_nrhs48": 	3183034 / 384,
}

import pprint
pprint.pp(d)

{'NPROC1x2x2x2_nrhs1': 5936.59375,
 'NPROC1x2x2x2_nrhs2': 17577.90625,
 'NPROC1x2x2x2_nrhs4': 14698.015625,
 'NPROC1x2x2x2_nrhs6': 12006.441666666668,
 'NPROC1x2x2x2_nrhs8': 12648.25,
 'NPROC1x2x2x2_nrhs10': 14968.59,
 'NPROC1x2x2x2_nrhs12': 14246.541666666666,
 'NPROC1x2x2x2_nrhs14': 16165.86607142857,
 'NPROC1x2x2x2_nrhs16': 3749.328125,
 'NPROC1x2x2x2_nrhs20': 15273.825,
 'NPROC1x2x2x2_nrhs24': 15136.895833333334,
 'NPROC1x2x2x2_nrhs28': 15679.691964285714,
 'NPROC1x2x2x2_nrhs32': 3478.9296875,
 'NPROC1x2x2x2_nrhs40': 8972.334375,
 'NPROC1x2x2x2_nrhs48': 8289.151041666666}

