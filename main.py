import random

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

# testit.run('leet.easy.twosum', [
#     [[3, 2, 4], 6],
#     [[3, 3], 6],
#     [[2,7,11,15], 9],
#     [[11, 2, 15, 7], 9]
# ])

# testit.run('leet.easy.palindromenumber', [
#     [121],
#     [10],
#     [0],
#     [-1],
#     [-123],
#     [123],
#     [97879],
#     [90788709]
# ])

# testit.run('leet.easy.longestcommonprefix',[
#     [["flower","flow","flight"]],
#     [["reflower","flow","flight"]],
#     [["dog","racecar","car"]],
#     [["dog"]],
#     [[]],
#     [[""]],
#     [["doggo", "dogging", "doggostyle"]],
#     [["aa", "bb", "aaa", "bbbb", "bbbb", "b", "bbbc"]]
# ])

# testit.run('leet.easy.validparenthesis', [
#     ["()"],
#     ["()[]{}"],
#     [")))((("],
#     ["([()])"],
#     ["({[()]})"],
#     ["({[()]}}"],
# ])

# testit.run('leet.easy.mergetwosortedlists', [
#     [[1, 2, 3], [4, 5, 6]],
#     [[1,2,4], [1,3,4]],
#     [[], []],
#     [[1, 2, 3], []],
#     [[], [1,2,3]],
#     [[1,2,4], [-1, 1,3,4]],
#     [[-5, 0, 4, 5], [1, 2, 4, 6]],
# ])

# testit.run('leet.easy.removeduplicatesfromsortedarray', [
#     [[1,1,2]],
#     [[0,0,1,1,1,2,2,3,3,4]],
#     [[1, 2, 3, 4, 5]],
#     [[1]],
#     [[]]
# ])

# testit.run('leet.easy.removeelement', [
#     [[3, 2, 2, 3], 3],
#     [[0, 1, 2, 2, 3, 0, 4, 2], 2],
#     [[], 10],
#     [[1, 2, 3, 4, 5, 5], 6],
#     [[1], 1],
#     [[], None]
# ])

# testit.run('leet.easy.lengthoflastword', [
#     ["Hello World"],
#     ["   fly me   to   the moon  "],
#     ["   "],
#     ["test"],
#     ["   test   "],
#     [" test test  t "],
#     ["t"],
# ])

# testit.run('leet.easy.searchindexposition', [
#     [[1, 3, 5, 6], 5],
#     [[1, 3, 5, 6], 2],
#     [[1, 3, 5, 6], 7],
#     [[], 1],
# ])

# testit.run('leet.easy.sqrtx', [
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

# testit.run('leet.easy.mergesortedarrays', [
#     [[1, 2, 3, 0, 0, 0], 3, [4, 5, 6], 3],
#     [[1, 2, 4, 0, 0, 0], 3, [1, 3, 4], 3],
#     [[], 0, [], 0],
#     [[1, 2, 3], 3, [], 0],
#     [[0, 0, 0], 0, [1, 2, 3], 3],
#     [[1, 2, 4, 0, 0, 0, 0], 3, [-1, 1, 3, 4], 4],
#     [[-5, 0, 4, 5, 0, 0, 0, 0], 4, [1, 2, 4, 6], 4],
# ])

# testit.run('leet.easy.removeduplicatesfromsortedlist', [
#     [[1, 1, 2]],
#     [[1, 1, 2, 3]],
#     [[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]],
#     [[1, 2, 3, 4, 5]],
#     [[1]],
#     [[]]
# ])

# testit.run('leet.medium.addtwonumbers', [
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

# testit.run('leet.hard.mergeksortedlists', [
#     [[[1, 4, 5], [1, 3, 4], [2, 6]]],
#     [[[1, 4, 5], [1, 3, 4]]],
#     [[[1, 4, 5], [], [1, 3, 4], [2, 6], []]],
#     [[[1, 4, 5], [], [1, 3, 4], [2, 6], []]],
# ])

# testit.run('leet.easy.reverselinkedlist', [
#     [[1, 2, 3]],
#     [[1, 2, 3, 4]],
#     [[1, 2]],
#     [[1]],
#     [[]],
# ])

# testit.run('leet.hard.reversenodesinkgroup', [
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

# testit.run('leet.medium.reverselinkedlist2', [
#     [[1, 2, 3], 1, 2],
#     [[1, 2, 3, 4], 2, 3],
#     [[1, 2], 2, 2],
#     [[1, 2], 1, 2],
#     [[1], 1, 1],
#     [[], 0, 0],
# ])

# testit.run('leet.medium.findfirstandlastpositionofelementinsortedarray', [
#     [[5, 7, 7, 8, 8, 10], 6],
#     [[5, 7, 7, 8, 8, 10], 8],
#     [[5, 7, 7, 8, 8, 8], 8],
#     [[8, 8, 8, 8], 8],
#     [[1], 1],
#     [[], 4],
# ])

# testit.run('leet.easy.runningsumof1darray', [
#     [[1, 2, 3, 4]],
#     [[1, 1, 1, 1]],
#     [[3, 1, 2, 10, 1]],
#     [[1]],
#     [[1, 2, 1, 1]],
#     [[0]]
# ])

# testit.run('leet.easy.findpivotindex', [
#     [[1, 2, 3, 4]],
#     [[2, 1, -1]],
#     [[1, 7, 3, 6, 5, 6]],
#     [[1, 1, 1, 1]],
#     [[3, 1, 2, 10, 1]],
#     [[1]],
#     [[1, 2, 1, 1]],
#     [[0]]
# ])

# testit.run('leet.easy.plusone', [
#     [[1, 2, 3, 4]],
#     [[9, 8, 9, 9]],
#     [[9]]
# ])

# testit.run('leet.medium.dailytemperatures', [
#     [[73, 74, 75, 71, 69, 72, 76, 73]],
#     [[30, 40, 50, 60]],
#     [[30, 60, 90]],
#     [[90, 30, 30, 30, 31, 91]],
#     [[90, 30, 30, 30, 31]],
#     [[90, 30, 30, 30, 30]],
# ])

# testit.run('leet.hard.nqueens', [
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

# testit.run('leet.hard.sudokusolver', [
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

# testit.run('leet.medium.validsudoku', [
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


# testit.run('leet.medium.mergeintervals', [
#     [[[1, 3], [2, 6], [8, 10], [15, 18]]],
#     [[[1, 4], [4, 5]]]
# ])

# testit.run('leet.medium.numberofislands', [
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

# testit.run('leet.medium.decodestring', [
#     ["3[a]2[bc]"],
#     ["3[a2[c]]"],
#     ["10[leet]"],
#     ["3[a2[c]4[bf]]"],
#     ["2[abc]3[cd]ef"],
# ])

# testit.run('leet.hard.trappingrainwater', [
#     [[2, 0, 2]],
#     [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]],
#     [[4, 2, 0, 3, 2, 5]],
# ])

# testit.run('leet.hard.sumofprefixscoresofstrings', [
#     [["abcd"]],
#     [["abc", "ab", "bc", "b"]],
# ])

# testit.run('leet.medium.generateparentheses', [
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

# testit.run('leet.medium.combinations', [
#     [5, 2],
#     [4, 2],
#     [1, 1],
#     [4, 1],
#     [4, 3],
#     [2, 1],
#     [2, 2],
#     [5, 2],
# ])

# testit.run('leet.medium.findleavesofbinarytree', [
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

# testit.run('leet.medium.permutations', [
#     [[1,2,3]],
#     [[1, 2]],
#     [[1, 2, 3, 4]]
# ])

# testit.run('leet.hard.slidingwindowsmaximum',[
#     [[1,3,-1,-3,5,3,6,7], 3],
#     [[1,3,-1,-3,5,3,6,7], 4]
# ])

# testit.run('leet.medium.stringtointegeratoi', [
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

# testit.run('leet.medium.searcha2dmatrix', [
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

# testit.run('leet.medium.searchina2dmatrix2', [
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

# testit.run('leet.medium.wordsearch', [
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

# testit.run('leet.medium.spiralmatrix', [
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
# testit.run('leet.easy.pascaltriangle', [
#     [1],
#     [2],
#     [3],
#     [4],
#     [5],
#     [6],
# ])

# testit.run('leet.hard.dungeongame', [
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

# testit.run('leet.medium.minimumpathsum', [
#     [
#         [
#             [1, 3, 1],
#             [1, 5, 1],
#             [4, 2, 1]
#         ],
#     ]
# ])

# testit.run('leet.medium.threesum', [
#     # [[-1, 0, 1, 2, -1, -4]],
#     # [[0, 1, 1]],
#     # [[0, 0, 0]],
#     [[0, 0, 0, 0]]
# ])
#
# testit.run('leet.medium.productofarrayexceptself', [
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

# testit.run('leet.easy.issubsequence', [
#     ["aaaaaa", "bbaaaa"],
# ])

# from smallapps.games.gameoflifeascii.main import start

# start(delay=1/45, r=50, c=170)
# restart(delay=1/60)

# testit.run('leet.medium.setmatrixzeroes', [
#     [
#         [
#             [0, 1, 2, 0],
#             [3, 4, 5, 2],
#             [1, 3, 1, 5]
#         ]
#     ]
# ])

# testit.run('leet.medium.substringxorqueries', [
#     ["101101", [[0, 5], [1, 2]]]
# ])

# testit.run('leet.medium.spiralmatrix', [
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

# testit.run('leet.medium.jumpgame2', [
#     [[2, 3, 1, 1, 4]],
#     [[0]],
# ])

# testit.run('leet.easy.pathsum', [
#     [
#         TreeNode(1, left=TreeNode(2)), 1
#     ],
#     [
#         TreeNode(1, left=TreeNode(2)), 0
#     ]
# ])

# testit.run('leet.easy.mergetwo2darrayssummingvalues', [
#     [[[1, 2], [2, 3], [4, 5]], [[1, 4], [3, 2], [4, 1]]]
# ])

# testit.run('leet.easy.floodfill', [
#     [
#         [[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2
#     ]
# ])

# testit.run('leet.medium.powxn', [
#     # [2, 10],
#     [2, -10]
#     # [2, 2 ** 32 - 1],
# ])

# testit.run('leet.medium.minesweeper', [
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

# testit.run('leet.medium.flattenbinarytreetolinkedlist', [
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
#
# from smallapps.games.gameoflifeascii.main import  main_pygame
# main_pygame()
# from smallapps.games.zuma.main import main
#
# main()


# def construct():
#     visited = set()
#     directions = [
#         # down, up
#         (1, 0), (-1, 0), (0, -1), (0, 1)
#     ]
#     n = 80
#     m = 80
#     r = []
#     end = (79, 79)
#     def can_step(i, j) -> bool:
#         if i >= n or j >= m or j < 0 or i < 0:
#             return False
#         return (i, j) not in visited
#
#     def backtrack(i, j, result: list):
#         if (i, j) == end:
#             nonlocal r
#             result.append((i, j))
#             r = result[:]
#             return True
#         visited.add((i, j))
#         possible_direction = []
#         for direction in directions:
#             next_i, next_j = i + direction[0], j + direction[1]
#             if can_step(next_i, next_j):
#                 possible_direction.append((next_i, next_j))
#         while possible_direction:
#             next = random.choice(possible_direction)
#             result.append((i, j))
#             if backtrack(next[0], next[1], result):
#                 return True
#             possible_direction.pop()
#             result.pop()
#         return False
#     backtrack(0, 0, [])
#     result = [[False] * m for _ in range(n)]
#     for i, j in r:
#         result[i][j] = True
#     for i in range(n):
#         for j in range(m):
#             print(int(result[i][j]), end=' ')
#         print()
#     print(len(r))
#     return r
#
# def construct_iterative(n, m, end):
#     visited = set()
#     directions = [
#         # down, up
#         (1, 0), (-1, 0), (0, -1), (0, 1)
#     ]
#     r = []
#     def can_step(i, j) -> bool:
#         if i >= n or j >= m or j < 0 or i < 0:
#             return False
#         return (i, j) not in visited
#
#     stack = []
#     stack.append((0, 0))
#     # result = []
#     while stack:
#         i, j = stack.pop()
#         if (i, j) == end:
#             r.append((i, j))
#             # r = result + [(i, j)]
#             break
#         visited.add((i, j))
#         possible_direction = []
#         for direction in directions:
#             next_i, next_j = i + direction[0], j + direction[1]
#
#             if not can_step(next_i, next_j):
#                 continue
#             possible_direction.append((next_i, next_j))
#
#         if possible_direction:
#             random.shuffle(possible_direction)
#             for next_i, next_j in possible_direction:
#                 r.append((i, j))
#                 stac
#                 # stack.append((next_i, next_j, result + [(i, j)]))
#
#     result = [[False] * m for _ in range(n)]
#     for i, j in r:
#         result[i][j] = True
#     for i in range(n):
#         for j in range(m):
#             print(int(result[i][j]), end=' ')
#         print()
#     print(len(r))
#     return r

# for i in range(3):
# import sys
# construct_iterative(4, 4, (3, 3))
#     # print('####')

# testit.run('leet.easy.checkifbinarystringhasatmostonesegmentofones', [
#     ['100'],
#     ['101'],
#     ['1011110'],
# ])

# testit.run('codeforces.problemset.aplusb', [
#     ['1 2'],
#     ['3 4'],
# ])
# testit.run('codeforces.problemset.apowerbminusbpowera', [
#     ['50 40'],
#     ['98 99'],
#     ['1 2'],
# ])
# testit.run('codeforces.problemset.thesum', [
#     ['1'],
#     ['2'],
#     ['3'],
#     ['4'],
#     ['5'],
#     ['10']
# ])

# testit.run('codeforces.problemset.scientificproblem', [
#     ['1'],
#     ['2'],
#     ['3'],
#     ['4'],
#     ['5'],
#     ['10']
# ])
# testit.run('codeforces.problemset.watermelon', [
#     ['1'],
#     ['2'],
#     ['3'],
#     ['4'],
#     ['5'],
#     ['10']
# ])

# testit.run('codeforces.problemset.b.icpcballoons', [
#     [
#         '6',
#         '3', 'ABA',
#         '1', 'A',
#         '3', 'ORZ',
#         '5', 'BAAAA',
#         '4', 'BKPT',
#         '10', 'CODEFORCES',
#     ]
# ])

# testit.run('codeforces.problemset.c.poweringtheheroeasy', [
#     [
#         '5\n3 3 3 0 0',
#         '6\n0 3 3 0 0 3',
#         '7\n1 2 3 0 4 5 0',
#         '7\n1 2 5 0 4 3 0',
#         '5\n3 1 0 0 4',
#     ],
# ],
#    many_cases=True
# )

# testit.run('codeforces.problemset.a.isitacat', [
#     [
#         '4\nmeOw',
#         '14\nmMmeoOoWWWwwwW',
#         '3\nmew',
#         '7\nMmeEeUw',
#         '4\nMEOW',
#         '6\nMmyaVw',
#         '5\nmeowA'
#     ],
# ],
#    many_cases=True
# )
# testit.run('codeforces.problemset.c.scoringsubsequences', [
#     [
#         '3\n1 2 3',
#         '2\n1 1',
#         '5\n5 5 5 5 5',
#         '6\n5 5 5 5 6',
#     ],
# ],
#    many_cases=True
# )

# testit.run('leet.medium.validgraphtree', [
#     # [5, [[0, 1], [0, 2], [0, 3], [1, 4]]],
#     [5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]]
# ])

# testit.run('codeforces.problemset.a.walkingmaster', [
#     [
#         '-1 0 -1 2',
#         '0 0 4 5',
#         '-2 -1 1 1',
#         '-3 2 -3 2',
#         '2 -1 -1 -1',
#         '1 1 0 2',
#     ]
# ], many_cases=True)

# testit.run('codeforces.problemset.b.grabthecandles', [
#     [
#         '4\n1 2 3 4',
#         '4\n1 1 1 2',
#         '3\n1 4 3',
#     ]
# ], many_cases=True)

# testit.run('codeforces.problemset.d.oddqueries', [
#     [
#         '''2
# 5 5
# 2 2 1 3 2
# 2 3 3
# 2 3 4
# 1 5 5
# 1 4 9
# 2 4 3
# 10 5
# 1 1 1 1 1 1 1 1 1 1
# 3 8 13
# 2 5 10
# 3 8 10
# 1 10 2
# 1 9 100'''
#     ]
# ])
#

from codeforces.problemset.e.interview import solution
solution()
