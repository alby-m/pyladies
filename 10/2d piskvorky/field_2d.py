# def field(rows, columns):
#     matrix = [['-' for x in range(rows)] for y in range(columns)]
#     # matrix = []
#     # for r in range(rows):
#     #     row = []
#     #     for c in range(columns):
#     #         row.append(0)
#     #     matrix.append(row)
#     for r in matrix:
#         for c in r:
#             print(c,end = " ")
#         print()

# board=(field(5,5))
# board[1][1] = 'x'
# print(board)

def matrix(rows, columns):
    m = [['-' for i in range(columns)] for j in range(rows)]
    return m

field=(matrix(5,5))
# counting = 0
# for i in field:
#     for j in i:
#         if j == '-':
#             counting += 1


# for r in field:
#         for c in r:
#             print(c,end = " ")
#         print()

