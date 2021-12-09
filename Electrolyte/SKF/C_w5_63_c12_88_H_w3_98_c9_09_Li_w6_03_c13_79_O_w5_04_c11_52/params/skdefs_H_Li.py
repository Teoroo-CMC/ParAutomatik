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
   "H": SlaterBasis(
        exponents=[[0.50, 1.0, 2.0],  # s
                   ],
        maxpowers=[ 3,  # s
                    ]
        ),
   "Li": SlaterBasis(
        exponents=[[0.50, 3.0],
                   [0.50, 3.0]],  # s
        maxpowers=[ 3,  # s
                    3, ]
        ),
	}
