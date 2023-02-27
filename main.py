import colorama

from leet import testit
from leet.medium.designbrowserhistory import BrowserHistory
from leet.structures import TreeNode
from leet.testit import print_matrix
from smallapps.games import minesweeper

colorama.init()

# print(lektioneinz.frequentsymbol('asdaffbbfbbaaa'))
# print(lektioneinz.findmax([]))
# print(lektioneinz.findmax([1]))
# print(lektioneinz.findmax([1,2,3,6,9,1,2]))
# print(lektioneinz.findmaxandsecond([1,2,3,4,5,6,7,8,9]))
# print(lektioneinz.findmaxandsecond([]))
# print(lektioneinz.findmaxandsecond([1]))
# print(lektioneinz.findmaxandsecond([3, 3]))
# print(lektioneinz.findmaxandsecond([1,2,3,9, 4, 5, 7, 9]))
# print('3')
# print(lektioneinz.findmaxandsecond1([1,2,3,4,5,6,7,8,9]))
# print(lektioneinz.findmaxandsecond1([3, 3]))
# print(lektioneinz.findmaxandsecond1([1, 2, 3]))

# print(lektioneinz.findmineven([]))
# print(lektioneinz.findmineven([1]))
# print(lektioneinz.findmineven([1, 3, 5, 7]))
# print(lektioneinz.findmineven([1, 3, 5, 7, 2]))
# print(lektioneinz.findmineven([1, 3, 5, 7, 4, 8, 9, 2]))
# print(lektioneinz.findmineven([4, 6, 8, 10, 2, 1]))

# print(lektioneinz.shortwords(['aa', 'bbb', 'bb', 'b']))
# print(lektioneinz.shortwords(['aa', 'bbb', 'bb', 'bb', 'ffff', 'cc']))

# print(lektioneinz.rle('AAAABBBCCXYZDDDDEEEFFFAAAAAA' + 'B' * 28))
# print(lektioneinz.rle('ABCDEFGDH'))

# print(lektioneinz.checkdictmiss(['abc', 'dbe', 'pfgd'], ['abcd', 'dbeq', 'pf']))

# print([1, 2, 5, 6, 7, 1, 6, 3, 10, 11, 12, 11, 13, 17, 8, 0, -16, 150])
# print(lektionvier.sortscores([1, 2, 5, 6, 7, 1, 6, 3, 10, 11, 12, 11, 13, 17, 8, 0, -16, 150]))
#
# print(lektionvier.checknumbers(111, 112))
# print(lektionvier.checknumbers(111, 111))
# print(lektionvier.checknumbers(57, 75))
# print(lektionvier.checknumbers(3121, 1123))
# print(lektionvier.checknumbers(3111, 1123))
#
# print(lektionvier.checknumbers1(111, 112))
# print(lektionvier.checknumbers1(111, 111))
# print(lektionvier.checknumbers1(57, 75))
# print(lektionvier.checknumbers1(3121, 1123))
# print(lektionvier.checknumbers1(3111, 1123))

# print(lektionvier.beatingrooks([(1, 1), (1, 5), (2, 5)]))
# print(lektionvier.hist('Hello, World!'))
# print(lektionvier.hist('TestimTestim srakin pestim lorem ipsum schrödinger kater'))
#
# print([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(lektionfunf.prefixsum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# print([1, 2, 0, 1, 0, 2, 1, 0])
# print(lektionfunf.prefzeroes([1, 2, 0, 1, 0, 2, 1, 0]))
# print(lektionfunf.prefzeroes1([1, 2, 0, 1, 0, 2, 1, 0]))
# print('#')
# print([1, 0, 1, 1, 0, 0, 1])
# print(lektionfunf.prefzeroes([1, 0, 1, 1, 0, 0, 1]))
# print(lektionfunf.prefzeroes1([1, 0, 1, 1, 0, 0, 1]))
#
# print(lektionfunf.rsm(lektionfunf.prefzeroes1([1, 2, 0, 1, 0, 2, 1, 0]), 5, 8))


# print(lektionfunf.greaterk([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))
# print(lektionfunf.greaterk1([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))

# testit.run('easy.twosum', [
#     [[3, 2, 4], 6],
#     [[3, 3], 6],
#     [[2,7,11,15], 9],
#     [[11, 2, 15, 7], 9]
# ])

# testit.run('easy.palindromenumber', [
#     [121],
#     [10],
#     [0],
#     [-1],
#     [-123],
#     [123],
#     [97879],
#     [90788709]
# ])

# testit.run('easy.longestcommonprefix',[
#     [["flower","flow","flight"]],
#     [["reflower","flow","flight"]],
#     [["dog","racecar","car"]],
#     [["dog"]],
#     [[]],
#     [[""]],
#     [["doggo", "dogging", "doggostyle"]],
#     [["aa", "bb", "aaa", "bbbb", "bbbb", "b", "bbbc"]]
# ])

# testit.run('easy.validparenthesis', [
#     ["()"],
#     ["()[]{}"],
#     [")))((("],
#     ["([()])"],
#     ["({[()]})"],
#     ["({[()]}}"],
# ])

# testit.run('easy.mergetwosortedlists', [
#     [[1, 2, 3], [4, 5, 6]],
#     [[1,2,4], [1,3,4]],
#     [[], []],
#     [[1, 2, 3], []],
#     [[], [1,2,3]],
#     [[1,2,4], [-1, 1,3,4]],
#     [[-5, 0, 4, 5], [1, 2, 4, 6]],
# ])

# testit.run('easy.removeduplicatesfromsortedarray', [
#     [[1,1,2]],
#     [[0,0,1,1,1,2,2,3,3,4]],
#     [[1, 2, 3, 4, 5]],
#     [[1]],
#     [[]]
# ])

# testit.run('easy.removeelement', [
#     [[3, 2, 2, 3], 3],
#     [[0, 1, 2, 2, 3, 0, 4, 2], 2],
#     [[], 10],
#     [[1, 2, 3, 4, 5, 5], 6],
#     [[1], 1],
#     [[], None]
# ])

# testit.run('easy.lengthoflastword', [
#     ["Hello World"],
#     ["   fly me   to   the moon  "],
#     ["   "],
#     ["test"],
#     ["   test   "],
#     [" test test  t "],
#     ["t"],
# ])

# testit.run('easy.searchindexposition', [
#     [[1, 3, 5, 6], 5],
#     [[1, 3, 5, 6], 2],
#     [[1, 3, 5, 6], 7],
#     [[], 1],
# ])

# testit.run('easy.sqrtx', [
#     [1],
#     [2],
#     [4],
#     [5],
#     [8],
#     [9],
#     [121],
#     [400],
#     [99 * 99],
#     [99 * 100],
# ])

# testit.run('easy.mergesortedarrays', [
#     [[1, 2, 3, 0, 0, 0], 3, [4, 5, 6], 3],
#     [[1, 2, 4, 0, 0, 0], 3, [1, 3, 4], 3],
#     [[], 0, [], 0],
#     [[1, 2, 3], 3, [], 0],
#     [[0, 0, 0], 0, [1, 2, 3], 3],
#     [[1, 2, 4, 0, 0, 0, 0], 3, [-1, 1, 3, 4], 4],
#     [[-5, 0, 4, 5, 0, 0, 0, 0], 4, [1, 2, 4, 6], 4],
# ])

# testit.run('easy.removeduplicatesfromsortedlist', [
#     [[1, 1, 2]],
#     [[1, 1, 2, 3]],
#     [[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]],
#     [[1, 2, 3, 4, 5]],
#     [[1]],
#     [[]]
# ])

# testit.run('medium.addtwonumbers', [
#     [[9, 9, 9], [9, 9]],
#     [[0], [9, 9, 9, 9]],
#     [[9, 9], [9, 9, 9, 9]],
#     [[9, 9, 9, 9, 9], [1]],
#     [[3, 2],  [7, 1]],
#     [[3, 1], [4, 1]],
#     [[], [1]],
#     [[1], [0]],
#     [[0], [9, 9, 9, 9, 9]]
# ])

# testit.run('hard.mergeksortedlists', [
#     [[[1, 4, 5], [1, 3, 4], [2, 6]]],
#     [[[1, 4, 5], [1, 3, 4]]],
#     [[[1, 4, 5], [], [1, 3, 4], [2, 6], []]],
#     [[[1, 4, 5], [], [1, 3, 4], [2, 6], []]],
# ])

# testit.run('easy.reverselinkedlist', [
#     [[1, 2, 3]],
#     [[1, 2, 3, 4]],
#     [[1, 2]],
#     [[1]],
#     [[]],
# ])

# testit.run('hard.reversenodesinkgroup', [
#     [[1, 2, 3, 4, 5], 2],
#     [[1, 2], 2],
#     [[1, 2, 3], 4],
#     [[1, 2, 3, 4, 5], 3],
#     [[1, 2, 3, 4, 5], 4],
#     [[1, 2, 3, 4, 5, 6], 3],
#     [[1, 2, 3, 4, 5, 6, 7], 3],
#     [[1], 1],
#     [[], 5]
# ])

# testit.run('medium.reverselinkedlist2', [
#     [[1, 2, 3], 1, 2],
#     [[1, 2, 3, 4], 2, 3],
#     [[1, 2], 2, 2],
#     [[1, 2], 1, 2],
#     [[1], 1, 1],
#     [[], 0, 0],
# ])

# testit.run('medium.findfirstandlastpositionofelementinsortedarray', [
#     [[5, 7, 7, 8, 8, 10], 6],
#     [[5, 7, 7, 8, 8, 10], 8],
#     [[5, 7, 7, 8, 8, 8], 8],
#     [[8, 8, 8, 8], 8],
#     [[1], 1],
#     [[], 4],
# ])

# testit.run('easy.runningsumof1darray', [
#     [[1, 2, 3, 4]],
#     [[1, 1, 1, 1]],
#     [[3, 1, 2, 10, 1]],
#     [[1]],
#     [[1, 2, 1, 1]],
#     [[0]]
# ])

# testit.run('easy.findpivotindex', [
#     [[1, 2, 3, 4]],
#     [[2, 1, -1]],
#     [[1, 7, 3, 6, 5, 6]],
#     [[1, 1, 1, 1]],
#     [[3, 1, 2, 10, 1]],
#     [[1]],
#     [[1, 2, 1, 1]],
#     [[0]]
# ])

# testit.run('easy.plusone', [
#     [[1, 2, 3, 4]],
#     [[9, 8, 9, 9]],
#     [[9]]
# ])

# testit.run('medium.dailytemperatures', [
#     [[73, 74, 75, 71, 69, 72, 76, 73]],
#     [[30, 40, 50, 60]],
#     [[30, 60, 90]],
#     [[90, 30, 30, 30, 31, 91]],
#     [[90, 30, 30, 30, 31]],
#     [[90, 30, 30, 30, 30]],
# ])

# testit.run('hard.nqueens', [
#     [1],
#     [2],
#     [3],
#     [4],
#     [5],
#     [6],
#     [7],
#     [8],
#     [9],
# ])

# testit.run('hard.sudokusolver', [
#     [
#         [
#             ["5", "3", ".", ".", "7", ".", ".", ".", "."],
#             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#             [".", "9", "8", ".", ".", ".", ".", "6", "."],
#             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#             [".", "6", ".", ".", ".", ".", "2", "8", "."],
#             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#             [".", ".", ".", ".", "8", ".", ".", "7", "9"]
#         ]
#     ],
# ])

# testit.run('medium.validsudoku', [
#     [
#         [
#             ["5", "3", ".", ".", "7", ".", ".", ".", "."],
#             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#             [".", "9", "8", ".", ".", ".", ".", "6", "."],
#             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#             [".", "6", ".", ".", ".", ".", "2", "8", "."],
#             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#             [".", ".", ".", ".", "8", ".", ".", "7", "9"]
#         ],
#     ],
#     [
#         [
#             ["8", "3", ".", ".", "7", ".", ".", ".", "."],
#             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#             [".", "9", "8", ".", ".", ".", ".", "6", "."],
#             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#             [".", "6", ".", ".", ".", ".", "2", "8", "."],
#             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#             [".", ".", ".", ".", "8", ".", ".", "7", "9"]
#         ],
#     ],
#     [
#         [
#             ["5", "3", ".", ".", "7", ".", ".", ".", "."],
#             ["6", "8", ".", "1", "9", "5", ".", ".", "."],
#             [".", "9", "8", ".", ".", ".", ".", "6", "."],
#             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#             [".", "6", ".", ".", ".", ".", "2", "8", "."],
#             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#             [".", ".", ".", ".", "8", ".", ".", "7", "9"]
#         ],
#     ]
# ])


# testit.run('medium.mergeintervals', [
#     [[[1, 3], [2, 6], [8, 10], [15, 18]]],
#     [[[1, 4], [4, 5]]]
# ])

# testit.run('medium.numberofislands', [
#     [
#         [
#             ["1", "1", "1", "1", "0"],
#             ["1", "1", "0", "1", "0"],
#             ["1", "1", "0", "0", "0"],
#             ["0", "0", "0", "0", "0"]
#         ]
#     ],
#     [
#         [
#             ["1", "1", "0", "0", "0"],
#             ["1", "1", "0", "0", "0"],
#             ["0", "0", "1", "0", "0"],
#             ["0", "0", "0", "1", "1"]
#         ]
#     ],
#     [
#         [
#             ["1", "1", "1"],
#             ["0", "1", "0"],
#             ["1", "1", "1"]
#         ]
#     ],
#
#     [
#         [
#             ["1", "0", "1", "1", "1"],
#             ["1", "0", "1", "0", "1"],
#             ["1", "1", "1", "0", "1"]
#         ]
#     ]
# ])

# testit.run('medium.decodestring', [
#     ["3[a]2[bc]"],
#     ["3[a2[c]]"],
#     ["10[leet]"],
#     ["3[a2[c]4[bf]]"],
#     ["2[abc]3[cd]ef"],
# ])

# testit.run('hard.trappingrainwater', [
#     [[2, 0, 2]],
#     [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]],
#     [[4, 2, 0, 3, 2, 5]],
# ])

# testit.run('hard.sumofprefixscoresofstrings', [
#     [["abcd"]],
#     [["abc", "ab", "bc", "b"]],
# ])

# testit.run('medium.generateparentheses', [
#     [0],
#     [1],
#     [2],
#     [3],
#     [4],
#     [5],
#     [6],
#     [7],
#     [8],
#     [9],
# ])

# testit.run('medium.combinations', [
#     [5, 2],
#     [4, 2],
#     [1, 1],
#     [4, 1],
#     [4, 3],
#     [2, 1],
#     [2, 2],
#     [5, 2],
# ])

# testit.run('medium.findleavesofbinarytree', [
#     [
#         TreeNode(
#             1,
#             TreeNode(
#                 2,
#                 TreeNode(
#                     4,
#                     TreeNode(
#                         6,
#                     ),
#                     TreeNode(
#                         7,
#                     ),
#                 ),
#                 TreeNode(
#                     5,
#                 )
#             ),
#             TreeNode(
#                 3,
#             )
#         )
#     ]
# ])

# testit.run('medium.permutations', [
#     [[1,2,3]],
#     [[1, 2]],
#     [[1, 2, 3, 4]]
# ])

# testit.run('hard.slidingwindowsmaximum',[
#     [[1,3,-1,-3,5,3,6,7], 3],
#     [[1,3,-1,-3,5,3,6,7], 4]
# ])

# testit.run('medium.stringtointegeratoi', [
#     # ['42'],
#     # ['+42'],
#     # ['-42'],
#     # ['+42 with words'],
#     # ['0'],
#     # ['-0'],
#     # ['   -42'],
#     # ['-91283472332'],
#     [''],
#     ['   '],
#     [' sadfasdf '],
#     [' -asdf'],
# ])

# testit.run('medium.searcha2dmatrix', [
#     [
#         [
#             [1, 3, 5, 7],
#             [10, 11, 16, 20],
#             [23, 30, 34, 60]
#         ],
#         13
#     ],
#     [
#         [
#             [1, 3, 5, 7],
#             [10, 11, 16, 20],
#             [23, 30, 34, 60]
#         ],
#         3
#     ],
#     [
#         [[1, 2, 3, 5, 7]], 3
#     ],
#     [
#         [
#             [1],
#             [2],
#             [3],
#             [5],
#             [7],
#         ],
#         3
#     ],
#     [
#         [], 3
#     ],
#     [
#         [[]], 4
#     ]
# ])

# testit.run('medium.searchina2dmatrix2', [
#     [
#         [
#             [1, 4, 7, 11, 15],
#             [2, 5, 8, 12, 19],
#             [3, 6, 9, 16, 22],
#             [10, 13, 14, 17, 24],
#             [18, 21, 23, 26, 30]
#         ],
#         5
#     ],
#     [
#         [
#             [1, 4, 7, 11, 15],
#             [2, 5, 8, 12, 19],
#             [3, 6, 9, 16, 22],
#             [10, 13, 14, 17, 24],
#             [18, 21, 23, 26, 30]
#         ],
#         20
#     ],
# ])

# testit.run('medium.wordsearch', [
#     [
#         [
#             ["A", "B", "C", "E"],
#             ["S", "F", "C", "S"],
#             ["A", "D", "E", "E"]
#         ],
#         "ABCCED"
#     ],
#     [
#         [
#             ["A", "B", "C", "E"],
#             ["S", "F", "C", "S"],
#             ["A", "D", "E", "E"]
#         ],
#         "SEE"
#     ],
#     [
#         [
#             ["A", "B", "C", "E"],
#             ["S", "F", "C", "S"],
#             ["A", "D", "E", "E"]
#         ],
#         "ABCB"
#     ],
#     [
#         [
#             ["A"],
#         ],
#         "A"
#     ]
# ])

# testit.run('medium.spiralmatrix', [
#     [
#         [
#             [1, 2, 3],
#             [4, 5, 6],
#             [7, 8, 9]
#         ]
#     ],
#     [
#         [
#             [1, 2, 3, 4],
#             [5, 6, 7, 8],
#             [9, 10, 11, 12]
#         ]
#     ]
# ])
#
# testit.run('easy.pascaltriangle', [
#     [1],
#     [2],
#     [3],
#     [4],
#     [5],
#     [6],
# ])

# testit.run('hard.dungeongame', [
#     [
#         [
#             [-2, -3, 3],
#             [-5, -10, 1],
#             [10, 30, -5]
#         ]
#     ],
#     [
#         [
#             [0, 0, 0],
#             [1, 1, -1]
#         ]
#     ]
# ])

# testit.run('medium.minimumpathsum', [
#     [
#         [
#             [1, 3, 1],
#             [1, 5, 1],
#             [4, 2, 1]
#         ],
#     ]
# ])

# testit.run('medium.threesum', [
#     # [[-1, 0, 1, 2, -1, -4]],
#     # [[0, 1, 1]],
#     # [[0, 0, 0]],
#     [[0, 0, 0, 0]]
# ])
#
# testit.run('medium.productofarrayexceptself', [
#     [[1,2,3,4]],
#     [[-1,1,0,-3,3]],
# ])

# s = RandomizedSet()
# print(s.insert(0))
# print(s.insert(1))
# print(s.remove(0))
# print(s.insert(2))
# print(s.remove(1))
# print(s.getRandom())
# s = RandomizedSet()
# print(s.remove(0))
# print(s.remove(0))
# print(s.insert(0))
# print(s.getRandom())
# print(s.remove(0))
# print(s.insert(0))

# testit.run('easy.issubsequence', [
#     ["aaaaaa", "bbaaaa"],
# ])

# from smallapps.games.gameoflifeascii.main import start

# start(delay=1/45, r=50, c=170)
# restart(delay=1/60)

# testit.run('medium.setmatrixzeroes', [
#     [
#         [
#             [0, 1, 2, 0],
#             [3, 4, 5, 2],
#             [1, 3, 1, 5]
#         ]
#     ]
# ])

# testit.run('medium.substringxorqueries', [
#     ["101101", [[0, 5], [1, 2]]]
# ])

# testit.run('medium.spiralmatrix', [
#     [
#         [
#             [1, 2, 3],
#             [4, 5, 6],
#             [7, 8, 9]
#         ]
#     ],
#     [
#         [
#             [1, 2, 3, 4],
#             [5, 6, 7, 8],
#             [9, 10, 11, 12]
#         ]
#     ]
# ])

# testit.run('medium.jumpgame2', [
#     [[2, 3, 1, 1, 4]],
#     [[0]],
# ])

# testit.run('easy.pathsum', [
#     [
#         TreeNode(1, left=TreeNode(2)), 1
#     ],
#     [
#         TreeNode(1, left=TreeNode(2)), 0
#     ]
# ])

# testit.run('easy.mergetwo2darrayssummingvalues', [
#     [[[1, 2], [2, 3], [4, 5]], [[1, 4], [3, 2], [4, 1]]]
# ])

# testit.run('easy.floodfill', [
#     [
#         [[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2
#     ]
# ])

# testit.run('medium.powxn', [
#     # [2, 10],
#     [2, -10]
#     # [2, 2 ** 32 - 1],
# ])

# testit.run('medium.minesweeper', [
#     [
#         [
#             ["E", "E", "E", "E", "E"],
#             ["E", "E", "M", "E", "E"],
#             ["E", "E", "E", "E", "E"],
#             ["E", "E", "E", "E", "E"]
#         ],
#         [3, 0]
#     ],
#     [
#         [
#             ["E", "E", "E", "E", "E", "E", "E", "E"],
#             ["E", "E", "E", "E", "E", "E", "E", "M"],
#             ["E", "E", "M", "E", "E", "E", "E", "E"],
#             ["M", "E", "E", "E", "E", "E", "E", "E"],
#             ["E", "E", "E", "E", "E", "E", "E", "E"],
#             ["E", "E", "E", "E", "E", "E", "E", "E"],
#             ["E", "E", "E", "E", "E", "E", "E", "E"],
#             ["E", "E", "M", "M", "E", "E", "E", "E"]
#         ],
#         [0, 0],
#     ]
# ], output_formatter=print_matrix)

# testit.run('medium.flattenbinarytreetolinkedlist', [
#     [
#         TreeNode(
#             val=1,
#             left=TreeNode(
#                 val=2,
#                 left=TreeNode(val=3),
#                 right=TreeNode(val=4)
#             ),
#             right=TreeNode(
#                 val=5,
#                 right=TreeNode(val=6)
#             )
#         )
#     ]
# ])

# history = BrowserHistory('1')
# history.visit('2')
# history.visit('3')
# history.visit('4')
# history.visit('5')
# print(history.back(2))
# print(history.forward(2))
#

# from smallapps.games.minesweeper.main import main
# main()

from smallapps.games.gameoflifeascii.main import  main_pygame
main_pygame()
