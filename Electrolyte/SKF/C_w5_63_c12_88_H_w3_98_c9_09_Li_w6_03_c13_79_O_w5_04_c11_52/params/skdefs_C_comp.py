atomconfigs = {
     "C": AtomConfig(
        znuc=6,
        mass=12.01,
        occupations=[[[1.0, 1.0], [1.0, 1.0]],  # s
                     [[1.0, 1.0]],  # p
                     ],
        valenceqns=[[2, ],  # s
                    [2, ],  # p
                    ], #d  
        relativistic=True
        ),
	}

skbases = {
    "C": SlaterBasis(
        exponents=[[0.50, 1.14, 2.62, 6.0],  # s
                   [0.50, 1.14, 2.62, 6.0],  # p
                  ],
        maxpowers=[ 3,  # s
                    3,  # p
                     ]
        ),
	}
compressions = {
	 "C": Compression(
		potcomp='potential',
		potcomp_parameters=[(2, 12.878787878787877), (2, 12.878787878787877), (2, 12.878787878787877)],
		wavecomp='potential',
		wavecomp_parameters=[(2, 5.634469696969697), (2, 5.634469696969697), (2, 5.634469696969697)],
		)
	}