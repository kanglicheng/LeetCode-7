# You are given an array x of n positive numbers. You start at point (0,0) and moves x[0] metres to the north, then x[1] metres to the west, x[2] metres to the south, x[3] metres to the east and so on. In other words, after each move your direction changes counter-clockwise.
#
# Write a one-pass algorithm with O(1) extra space to determine, if your path crosses itself, or not.
#
# Example 1:
# Given x = [2, 1, 1, 2],

#
# Return true (self crossing)
# Example 2:
# Given x = [1, 2, 3, 4],

#
# Return false (not self crossing)
# Example 3:
# Given x = [1, 1, 1, 1],

#
# Return true (self crossing)
class Route(object):
	def __init__(self, sX, sY, eX, eY, d):
		self.startX = sX;
		self.startY = sY;
		self.endX = eX;
		self.endY = eY;
		self.direction = d

class Solution(object):
	def __init__(self):
		self.route = []
		self.currentX = 0
		self.currentY = 0

	def isSelfCrossing(self, x):

		if(len(x) < 4):
			return False

		for key in range(len(x)):
			val = x[key]
			if key % 4 == 0:
				route = Route(self.currentX, self.currentY, self.currentX, self.currentY + val, "V")
				self.currentX, self.currentY = self.currentX, self.currentY + val
				if self.isTouch(route):
					return True
				else:
					self.route.append(route)

			elif key % 4 == 1:
				route = Route(self.currentX, self.currentY, self.currentX - val, self.currentY, "H")
				self.currentX, self.currentY = self.currentX - val, self.currentY
				if self.isTouch(route):
					return True
				else:
					self.route.append(route)

			elif key % 4 == 2:
				route = Route(self.currentX, self.currentY, self.currentX, self.currentY - val, "V")
				self.currentX, self.currentY = self.currentX, self.currentY - val
				if self.isTouch(route):
					return True
				else:
					self.route.append(route)

			else:
				route = Route(self.currentX, self.currentY, self.currentX + val, self.currentY, "H")
				self.currentX, self.currentY = self.currentX + val, self.currentY
				if self.isTouch(route):
					return True
				else:
					self.route.append(route)
		return False

	def isTouch(self, route):
		if route.direction == "H":
			vList = [r for r in self.route if r.direction == "V"]
			for v in vList:
				if route.startY >= min(v.startY, v.endY) \
					and route.startY <= max(v.startY, v.endY) \
					and route.startX != v.startX \
					and (route.startX < v.endX <= route.endX or route.startX > v.endX >= route.endX):
					return True

			hList = [r for r in self.route if r.direction == "H"]
			for h in hList:
				if(route.endY == h.startY and route.endX == h.startX):
					return True

			return False
		else:
			hList = [r for r in self.route if r.direction == "H"]
			for h in hList:
				if route.startX >= min(h.startX, h.endX) \
					and route.startX <= max(h.startX, h.endX) \
					and route.startY != h.startY \
					and (route.startY < h.endY <= route.endY or route.startY > h.endY >= route.endY):
					return True

			vList = [r for r in self.route if r.direction == "V"]
			for v in vList:
				if(route.endY == v.startY and route.endX == v.startX):
					return True

			return False


s = Solution()
#temp = [3,3,4,2,2,]
#temp = [100,100,99,99,98,98,97,97,96,96,95,95,94,94,93,93,92,92,91,91,90,90,89,89,88,88,87,87,86,86,85,85,84,84,83,83,82,82,81,81,80,80,79,79,78,78,77,77,76,76,75,75,74,74,73,73,72,72,71,71,70,70,69,69,68,68,67,67,66,66,65,65,64,64,63,63,62,62,61,61,60,60,59,59,58,58,57,57,56,56,55,55,54,54,53,53,52,52,51,51,50,50,49,49,48,48,47,47,46,46,45,45,44,44,43,43,42,42,41,41,40,40,39,39,38,38,37,37,36,36,35,35,34,34,33,33,32,32,31,31,30,30,29,29,28,28,27,27,26,26,25,25,24,24,23,23,22,22,21,21,20,20,19,19,18,18,17,17,16,16,15,15,14,14,13,13,12,12,11,11,10,10,9,9,8,8,7,7,6,6,5,5,4,4,3,3,2,2,1,1]
#temp = [2,1,1,2]
temp = [1,1,2,1,1]
print s.isSelfCrossing(temp)
