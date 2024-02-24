INF = float('inf')

#Below are the input graphs for the algorithms.

graph_3 = [[0, 4, 2],
			[INF, 0, 3],
			[INF,1, 0]
			]

graph_4 = [[0, 5, INF, 8],
			[INF, 0, 3, INF],
			[INF, INF, 0, 5],
			[2,INF, INF, 0]
			]

graph_5 =[[0, 5, 4, INF,INF],
			[3, 0, INF, 4,2],
			[INF, INF, 0, 3, INF],
			[INF, INF, INF, 0,1],
            [INF, INF, INF, INF,0]
			]

graph_6 = [[0, 5, 4, INF,INF,INF],
		    [3, 0, INF, 4,2,INF],
			[INF, INF, 0, 3, INF,INF],
			[INF, INF, INF, 0,1,4],
            [INF, INF, INF, INF,0,3],
            [INF, INF, INF, INF,2,0]
			]


dense_graph_8 = [[0, 9, 2, 2, 10, 10, 3, 9],
                [4, 0, 3, 2, 5, 2, 2, 7],
                [9, 2, 0, 4, 1, 5, 1, 3],
                [6, 1, 7, 0, 4, 2, 5, 1],
                [4, 7, 2, 2, 0, 7, 1, 1],
                [5, 2, 6, 8, 6, 0, 5, 2],
                [10, 8, 4, 10, 3, 10, 0, 2],
                [10, 1, 4, 4, 4, 8, 7, 0]
]

#Below are the expected output graphs for the algorithms.

output_3 = [[0, 3, 2],
            [INF, 0, 3],
            [INF, 1, 0]
            ]

output_4 = [[0, 5, 8, 8],
            [10, 0, 3, 8],
            [7, 12, 0, 5],
            [2, 7, 10, 0]
            ]

output_5 = [[0, 5, 4, 7, 7],
            [3, 0, 7, 4, 2],
            [INF, INF, 0, 3, 4],
            [INF, INF, INF, 0, 1],
            [INF, INF, INF, INF, 0]
            ]

output_6 = [[0, 5, 4, 7, 7, 10],
            [3, 0, 7, 4, 2, 5],
            [INF, INF, 0, 3, 4, 7],
            [INF, INF, INF, 0, 1, 4],
            [INF, INF, INF, INF, 0, 3],
            [INF, INF, INF, INF, 2, 0]
            ]

output_dense_8 = [[0, 3, 2, 2, 3, 4, 3, 3],
                [4, 0, 3, 2, 4, 2, 2, 3],
                [5, 2, 0, 3, 1, 4, 1, 2],
                [5, 1, 4, 0, 4, 2, 3, 1],
                [4, 2, 2, 2, 0, 4, 1, 1],
                [5, 2, 5, 4, 6, 0, 4, 2],
                [7, 3, 4, 5, 3, 5, 0, 2],
                [5, 1, 4, 3, 4, 3, 3, 0]
                ]
