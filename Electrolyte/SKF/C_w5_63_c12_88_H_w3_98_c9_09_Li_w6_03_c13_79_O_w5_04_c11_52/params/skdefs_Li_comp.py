atomconfigs = {
    "Li": AtomConfig(
        znuc=3,
        mass=6.939,
        occupations=[[[1.0, 1.0], [1.0, 0.0]],  # s
                    [[0.0, 0.0]]],   # p 
        valenceqns=[[2,], # s
                    [2,], # p
                   ], 
        relativistic=True
        ),
	}

skbases = {
   "Li": SlaterBasis(
        exponents=[[0.50, 3.0],
                   [0.50, 3.0]],  # s
        maxpowers=[ 3,  # s
                    3, ]
        ),
	}
compressions = {
	 "Li": Compression(
		potcomp='potential',
		potcomp_parameters=[(2, 13.787878787878787), (2, 13.787878787878787)],
		wavecomp='potential',
		wavecomp_parameters=[(2, 6.03219696969697), (2, 6.03219696969697)],
		)
	}