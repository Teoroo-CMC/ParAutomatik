atomconfigs = {
     "H": AtomConfig(
        znuc=1,
        mass=1.008,
        occupations=[[[1.00, 0.0]],  # s
                     ],
        valenceqns=[[1, ],  # s
                    ],
        relativistic=False
        ),
	}

skbases = {
   "H": SlaterBasis(
        exponents=[[0.50, 1.0, 2.0],  # s
                   ],
        maxpowers=[ 3,  # s
                    ]
        ),
	}
compressions = {
	 "H": Compression(
		potcomp='potential',
		potcomp_parameters=[(2, 9.09090909090909), (2, 9.09090909090909)],
		wavecomp='potential',
		wavecomp_parameters=[(2, 3.977272727272727), (2, 3.977272727272727)],
		)
	}