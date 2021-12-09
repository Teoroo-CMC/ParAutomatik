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
