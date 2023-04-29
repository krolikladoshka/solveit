import heapq
import itertools
import random
from typing import List, Tuple, Optional

import colorama

from interviewquestions.decorators.countclassmethodcalls import test_method_calls_counter, \
    test_bound_method_calls_counter
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

# from codeforces.problemset.e.interview import solution
# solution()

# jewelry = input()
# stones = input()
#
# jewelry = set(jewelry)
#
# counter = 0
# for stone in stones:
#     if stone in jewelry:
#         counter += 1
# print(counter)

# n = int(input())
#
# vector = []
# for i in range(n):
#     vector.append(int(input()))
#
# max_sequence_length = 0
# length = 0
#
# for val in vector:
#     if val == 1:
#         length += 1
#     else:
#         max_sequence_length = max(max_sequence_length, length)
#         length = 0
# if length != 0:
#     max_sequence_length = max(max_sequence_length, length)
# print(max_sequence_length, flush=True)

# n = int(input())
#
# current = float('-inf')
# for i in range(n):
# 	next = int(input())
# 	if current == next:
# 		continue
# 	else:
# 		print(next)
# 		current = next
#

# n = int(input())
#
#
# def generate_parentheses(lefts, rights, result):
#     if len(result) == 2 * n:
#         print(''.join(result), flush=True)
#
#         return
#
#     if lefts < n:
#         result.append('(')
#         generate_parentheses(lefts + 1, rights, result)
#         result.pop()
#     if rights < lefts and rights < n:
#         result.append(')')
#         generate_parentheses(lefts, rights + 1, result)
#         result.pop()
#
#
# generate_parentheses(0, 0, [])

# s1 = input()
# s2 = input()
#
#
# def solve():
#     if len(s1) != len(s2):
#         print(0, flush=True)
#
#         return
#
#     counter = [0] * 26
#
#     for c1, c2 in zip(s1, s2):
#         counter[ord(c1) - ord('a')] += 1
#         counter[ord(c2) - ord('a')] -= 1
#
#     for count in counter:
#         if count != 0:
#             print(0, flush=True)
#
#             return
#     print(1, flush=True)
#
#
# solve()

# from collections import deque
#
# n = int(input())
# coords: List[Tuple[int, int]] = []
# graph = [
#     [j for j in range(n) if i != j] for i in range(n)
# ]
#
# for i in range(n):
#     x, y = map(int, input().split())
#     coords.append((x, y))
#
# max_length = int(input())
# start, end = map(int, input().split())
#
# start -= 1
# end -= 1
# queue = deque([(start, 0)])
# visited = set()
#
#
# def distance(city1, city2) -> int:
#     return abs(coords[city2][0] - coords[city1][0]) + abs(coords[city2][1] - coords[city1][1])
#
#
# while queue:
#     node, path_size = queue.popleft()
#     if node == end:
#         print(path_size, flush=True)
#
#         break
#
#     for neighbour in graph[node]:
#         if neighbour not in visited:
#             if distance(node, neighbour) > max_length:
#                 continue
#             queue.append((neighbour, path_size + 1))
# else:
#     print(-1, flush=True)
#
# try:
#     n = int(input())
#     coords: List[Tuple[int, int]] = []
#     for i in range(n):
#         x, y = map(int, input().split())
#         coords.append((x, y))
#
#     max_length = int(input())
#     start, end = map(int, input().split())
#
#     start -= 1
#     end -= 1
#     queue = [(start, 0)]
#     visited = set()
#
#     def distance(city1, city2) -> int:
#         return abs(coords[city2][0] - coords[city1][0]) + abs(coords[city2][1] - coords[city1][1])
#
#
#     while queue:
#         node, path_size = queue.pop(0)
#         if node == end:
#             print(path_size, flush=True)
#
#             break
#
#         for neighbour in range(n):
#             if neighbour == node:
#                 continue
#             if neighbour not in visited:
#                 if distance(node, neighbour) > max_length:
#                     continue
#                 visited.add(neighbour)
#                 queue.append((neighbour, path_size + 1))
#     else:
#         print(-1, flush=True)
# except Exception as e:
#     import traceback
#     print(e)
#     print(traceback.print_tb(e.__traceback__))

#
# print('test')
# a = [0] * 10
# '''
# Suggest a solution to find the number of adults by name in a database
# '''
# '''
# create table "persons_less_than_18"
# (
#     id bigint primary key not null,
#     birth_date date not null,
#     name varchar(36) not null
# )
#
# select
#     count(*)
# from persons
# where (current_date() - birth_date) >= 18 and name == $1
# '''
# '''
# Suppose we have an array of integers.
# We have to return the indices of two integers, such that if we add them up,
# we will reach to a specific target.
# '''
#
#
# def find_target(array: List[int], target: int) -> Optional[List[int]]:
#     '''
#     {
#         (target - a[i]) -> i
#         if target - a[j] in set:
#             return j, s
#     '''
#     differences = {}
#     # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
#     for i in range(len(array)):
#         difference = target - array[i]
#
#         if array[i] in differences:
#             return [differences[array[i]], i]
#         differences[difference] = i
#
#
# array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # print(find_indicies(array, 10))
#
# # print(find_indicies([2,8,12,15], 20))
#
# assert find_target([2,8,12,15], 20) == [1, 2]
# assert find_target([1, 2, 3], 4) == [0, 2]
# assert find_target([2, 2, 3], 4) in [[0, 1], [1, 0]]
# assert find_target([2, 2], 4) in [[0, 1], [1, 0]]
# assert find_target([8, 7, 2, 5, 3, 1], 10) in [[0, 2], [2, 0], [1, 4], [4, 1]]
# assert find_target([1234, 5678, 9012], 14690) == [1, 2]
# assert find_target([2,7,11,15], 9) == [0, 1]
# assert find_target([3,2,4], 6) == [1, 2]
# assert find_target([3,3], 6) == [0, 1]
# assert find_target([1, 4, 45, 6, 10, 8], 16) == [3, 4]
# assert find_target([0, 6], 6) == [0, 1]
# assert find_target([6], 6) is None
#
# '''
# Given a number of intervals, find all overlapping intervals,
# merge the overlapping intervals and return the merged intervals in ascending order.
# |-----------------|
#          |---------------|
#                              |------|
#                  |--------------|
#
#  |-----------------------------------|
# '''
#
# def merged_intervals(intervals: List[List[int]]) -> List[List[int]]:
#     '''
#     [1, 3],  [2, 4], [12, 14], [11, 15], [8, 10],
#     [9, 11], [10, 13], [5, 7], [16, 20]
#     '''
#     result = []
#     intervals.sort(key=lambda interval: interval[0])
#
#     start = intervals[0]
#     i = 1
#     while i < len(intervals):
#         if intervals[i][0] > start[1]:
#             result.append(start)
#             start = intervals[i]
#         else:
#             start = [min(start[0], intervals[i][0]), max(start[1], intervals[i][1])]
#         i += 1
#     result.append(start)
#
#     return result
#
# intervals = [
#     [1, 3], [12, 14], [2, 4], [11, 15], [8, 10],
#     [9, 11], [10, 13], [5, 7], [16, 20]
# ]
# expected_intervals = [[1,4], [5, 7], [8, 15], [16, 20]]
# assert merged_intervals(intervals) == expected_intervals
# assert merged_intervals([[1,4], [5, 7], [8, 15]]) == [[1,4], [5, 7], [8, 15]]
# assert merged_intervals([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
# # Explanation: since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
#
# assert merged_intervals([[1,4],[4,5]]) == [[1,5]]
# # Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#
# assert merged_intervals([[6, 8], [1, 9], [2, 4], [4, 7]]) == [[1, 9]]
#
# testit.run('codeforces.problemset.b.taxi', [
#     [
#         '5\n1 2 4 3 3'
#     ],
#     [
#         # 1 - 2, 2 -2, 3 - 2, 4 - 2
#         '8\n2 3 4 4 2 1 3 1'
#     ],
#     [
#         '3\n3 3 2'
#     ]
# ])

# testit.run('codeforces.problemset.c.cdandpwdcommands', [
#     ['7\npwd\ncd /home/vasya\npwd\ncd ..\npwd\ncd vasya/../petya\npwd'],
#     ['4\ncd /a/b\npwd\ncd ../a/b\npwd']
# ])

# testit.run('leet.medium.checkknighttourconfiguration', [
#     [
#         [
#             [0, 11, 16, 5, 20],
#             [17, 4, 19, 10, 15],
#             [12, 1, 8, 21, 6],
#             [3, 18, 23, 14, 9],
#             [24, 13, 2, 7, 22]
#         ],
#     ],
#     [
#         [
#             [0, 3, 6],
#             [5, 8, 1],
#             [2, 7, 4]
#         ]
#     ],
#     [
#         [
#             [24, 11, 22, 17,  4],
#             [21, 16,  5, 12,  9],
#             [ 6, 23, 10,  3, 18],
#             [15, 20,  1,  8, 13],
#             [ 0,  7, 14, 19,  2]
#         ]
#     ]
# ])

# test_method_calls_counter()

# # test_bound_method_calls_counter()
#
# nes_palette = '''
#  84  84  84    0  30 116    8  16 144   48   0 136   68   0 100   92   0  48   84   4   0   60  24   0   32  42   0    8  58   0    0  64   0    0  60   0    0  50  60    0   0   0
# 152 150 152    8  76 196   48  50 236   92  30 228  136  20 176  160  20 100  152  34  32  120  60   0   84  90   0   40 114   0    8 124   0    0 118  40    0 102 120    0   0   0
# 236 238 236   76 154 236  120 124 236  176  98 236  228  84 236  236  88 180  236 106 100  212 136  32  160 170   0  116 196   0   76 208  32   56 204 108   56 180 204   60  60  60
# 236 238 236  168 204 236  188 188 236  212 178 236  236 174 236  236 174 212  236 180 176  228 196 144  204 210 120  180 222 120  168 226 144  152 226 180  160 214 228  160 162 160
# '''
#
# palette = [x for x in map(lambda q: q.strip(), nes_palette.split(' ')) if x != '']
#
#
# def grouper(iterable, n):
#     args = [iter(iterable)] * n
#     return zip(*args, strict=True)
#
#
# with open('palette.txt', 'r') as fin, open('palette.rs', 'w') as fout:
#     fout.write('pub const PALETTE: [[u8; 3]; 64] = [\n')
#     prefix = '    '
#
#     palette = [line.strip() for line in fin.readlines()]
#     for palette_line in palette:
#         colors = [
#             int(x.strip())
#             for x in palette_line.split(' ')
#             if x.strip() != ''
#         ]
#         for group in grouper(colors, 3):
#             fout.write(f'{prefix}{list(group)},\n')
#         fout.write(f'{prefix}[0, 0, 0],\n')
#         fout.write(f'{prefix}[0, 0, 0],\n')
#     fout.write('];')

# testit.run('leet.medium.searchinrotatedsortedarray', [
#     [
#         [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1], 2
#     ]
# ])

# testit.run('leet.medium.removenthnodefromendoflistt', [
#     [
#         [1,2,3,4,5], 2
#     ],
#     [
#         [1, 2], 2
#     ],
# ])

"""
1. Дан набор прямоугольников, необходимо получить минимальный bbox,
   который включает в себя все прямоугольники
    
    [
        [(10, 10), (20, 0)],
        [(15, 11), (22, 7)],
    ]
"""


def find_bbox(rects: List):
    first = rects[0]
    most_left_x = first[0][0]
    most_left_y = first[0][1]
    most_right_x = first[1][0]
    most_right_y = first[1][1]

    for ((t_x, t_y), (b_x, b_y)) in rects:
        if most_left_x > t_x:
            most_left_x = t_x
        if most_left_y < t_y:
            most_left_y = t_y
        if most_right_x < b_x:
            most_right_x = b_x
        if most_right_y > b_y:
            most_right_y = b_y

    return [
        (most_left_x, most_left_y),
        (most_right_x, most_right_y),
    ]


rects = [
    [(10, 10), (20, 0)],
    [(15, 11), (22, 7)],
    [(0, 0), (7, -20)]
]

print(find_bbox(rects))
