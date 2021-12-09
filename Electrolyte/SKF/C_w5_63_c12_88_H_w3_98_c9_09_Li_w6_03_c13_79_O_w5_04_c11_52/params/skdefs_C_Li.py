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
    "C": SlaterBasis(
        exponents=[[0.50, 1.14, 2.62, 6.0],  # s
                   [0.50, 1.14, 2.62, 6.0],  # p
                  ],
        maxpowers=[ 3,  # s
                    3,  # p
                     ]
        ),
   "Li": SlaterBasis(
        exponents=[[0.50, 3.0],
                   [0.50, 3.0]],  # s
        maxpowers=[ 3,  # s
                    3, ]
        ),
	}
