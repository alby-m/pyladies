BORDER OUT
#         ((r+self.size) > abs(x) and self.size-self.intercept < y < self.intercept-self.size) or
#         ((r+self.size) > abs(y) and self.size-self.intercept < x < self.intercept-self.size) or
#         (r > dist_f1 or r > dist_f2 or r > dist_f3 or r > dist_f4) and
#         -1*self.size < x < self.size and -1*self.size < y < self.size

# dist_f1 = abs((-1*x + -1*y + self.intercept)/ (2**(1/2)))
# dist_f2 = abs(( 1*x + -1*y - self.intercept)/ (2**(1/2)))
# dist_f3 = abs((-1*x + -1*y - self.intercept)/ (2**(1/2)))
# dist_f4 = abs(( 1*x + -1*y + self.intercept)/ (2**(1/2)))
# dist_h1 = abs( 1*self.size - y)
# dist_h2 = abs(-1*self.size - y)
# dist_v1 = abs( 1*self.size - x)
# dist_v2 = abs(-1*self.size - x)
# dist_f1 = abs((-1*x + -1*y + self.intercept)/ (2**(1/2)))
# dist_f2 = abs(( 1*x + -1*y - self.intercept)/ (2**(1/2)))
# dist_f3 = abs((-1*x + -1*y - self.intercept)/ (2**(1/2)))
# dist_f4 = abs(( 1*x + -1*y + self.intercept)/ (2**(1/2)))
# dist_h1 = abs( 1*self.size - y)
# dist_h2 = abs(-1*self.size - y)
# dist_v1 = abs( 1*self.size - x)
# dist_v2 = abs(-1*self.size - x)

# class Vizualization():
#     def grid(self):
#         ax = plt.gca()
#         ax.set_xticks(numpy.arange(-250, 250, 25))
#         ax.set_yticks(numpy.arange(-250, 250, 25))
#         ax.tick_params(axis='both', which='major', labelsize=5)
#         plt.axis('square')
#         plt.grid(True)
#         fuel = plt.Circle(output.get_coordinates()[0], output.get_coordinates()[1], output.get_coordinates()[2])
#         ax.add_artist(fuel)
#         plt.show()


# ax = plt.gca()
# ax.set_xticks(numpy.arange(-250, 250, 25))
# ax.set_yticks(numpy.arange(-250, 250, 25))
# ax.tick_params(axis='both', which='major', labelsize=5)
# plt.axis('square')
# plt.grid(True)
# fuel = plt.Circle((x, y), r)
# ax.add_artist(fuel)

# plt.show()        

# # class Drawing_fuel(Vizualization):
# #     def inside(self):
# #         print(fuel)
# #         # ax.add_artist(fuel)
# #         # plt.show()

# plot = Vizualization()
# plot.grid()

