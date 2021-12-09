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
   "Li": SlaterBasis(
        exponents=[[0.50, 3.0],
                   [0.50, 3.0]],  # s
        maxpowers=[ 3,  # s
                    3, ]
        ),
    "O": SlaterBasis(
        exponents=[[0.50, 1.26, 3.17, 8.0],  # s
                   [0.50, 1.26, 3.17, 8.0],  # p
                   ],
        maxpowers=[ 3,  # s
                    3,  # p
                    ] # d
        ),
	}
