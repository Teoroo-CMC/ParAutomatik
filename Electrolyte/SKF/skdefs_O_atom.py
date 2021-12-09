atomconfigs = {
     "O": AtomConfig(
        znuc=8,
        mass=16.01,
        occupations=[[[1.0, 1.0], [1.0, 1.0]],  # s
                     [[2.00, 2.00]],  # p
                     ], # d 
        valenceqns=[[2, ],  # s
                    [2, ],  # p
                    ],  # d 
        relativistic=True
        ),

	}

skbases = {
    "O": SlaterBasis(
        exponents=[[0.50, 1.26, 3.17, 8.0],  # s
                   [0.50, 1.26, 3.17, 8.0],  # p
                   ],
        maxpowers=[ 3,  # s
                    3,  # p
                    ] # d
        ),
	}
