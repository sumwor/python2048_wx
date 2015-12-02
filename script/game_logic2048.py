class Unit:
    # define the unit class (2, 4, 8....)
    def __init__(self, value, pos):
        """value : value of the unit: 2, 4, 8...
           pos : position of the unit: (x,y)
        """
        self.value = value
        self.pos = pos

    def __str__(self):
        # print the unit in a human readable form
        return str(self.value) + str(self.pos)

    def add(self, unit):
        """only two units with the same value can be added up"""
        if self.value == unit.value:
            self.value = 2 * self.value
            unit.value = 0
        elif self.value == 0:
            self.value = unit.value
            unit.value = 0

    def move(self, new_pos):
        #move the unit to the new_pos
        self.value = self.value
        self.pos[0] = new_pos[0]
        self.pos[1] = new_pos[1]

class Map:
    # define the whole Map
    def __init__(self, dimension):
        self.dimension = []
        for i in range(dimension):
            line = []
            for j in range(dimension):
                line.append(Unit(0, [i, j]))
            self.dimension.append(line)
        self.full = False

    def __str__(self):
        #print the map in a human-readable form
        string = ""
        for line in self.dimension:
            for unit in line:
                string = string + str(unit.value) + "\t"
                    #print unit
            string += "\n"
        return string

    def add_unit(self, unit):
        #add a unit into the map
        self.dimension[unit.pos[0]][unit.pos[1]].value = unit.value

    def del_unit(self,pos):
        #delete a unit
        self.dimension[pos[0]][pos[1]].value = None

    def is_full(self):
        #logic that used to determine whether the map is full of units
        i = 0
        for line in self.dimension:
            for unit in self.dimension:
                if unit.value != None:
                    i += 1
        #print i, len(self.dimension)
        if i == len(self.dimension) ** 2:
            self.full = True
        return self.full

    def is_done(self):
        #determined whether the map is moved to the last form
        is_done = True
        for i in range(1,len(self.dimension)):
            for unit in self.dimension[i]:
                #print unit
                if unit.value != 0 and (self.dimension[unit.pos[0]-1][unit.pos[1]].value == 0 or self.dimension[unit.pos[0]-1][unit.pos[1]].value == unit.value):
                    is_done = False
                    break
        return is_done

    def rot(self):
        """rotate the map counterclockwise once
            key_value = 1, left, flip the map couterclockwise once
            key_value = 2, down, flip the map couterclockwise twice
            key_value = 3, right, flip the map conterclockwise for three times
            key_value = 4, up, no flip
        """
        dim = len(self.dimension)
        for j in range(dim/2):
            print m,j
            for i in range(j, dim - 1 -j):
                self.dimension[j][i].value, self.dimension[i][dim-1-j].value,self.dimension[dim-1-j][dim-1-i].value,self.dimension[dim-1-i][j].value \
                = self.dimension[dim-1-i][j].value,self.dimension[j][i].value,self.dimension[i][dim-1-j].value,self.dimension[dim-1-j][dim-1-i].value
            #print "m after j"
            #print m




    def move(self):
        while not self.is_done():
            for i in range(1, len(self.dimension)):
                for unit in self.dimension[i]:
                    if unit.value != 0:
                        mv = i
                        while (self.dimension[mv-1][unit.pos[1]].value == 0 or self.dimension[mv-1][unit.pos[1]].value == unit.value) and mv > 0:
                            self.dimension[mv-1][unit.pos[1]].add(unit)
                            mv -= 1


                        #elif self.dimension[mv-1][unit.pos[1]].value ==

"""
m = Map(5)
#m1 = Map(5)
u1 = Unit(2, [0,1])
#m1.add_unit(u1)
#print "m1:", m1
#print m1.is_done()

#print m
u6 = Unit(2, [1,1])
u2 = Unit(2, [3, 4])
u3 = Unit(2, [4,1])
u4 = Unit(2, [3,1])
u5 = Unit(2, [2,1])
#print m

m.add_unit(u2)
m.add_unit(u3)
m.add_unit(u4)
m.add_unit(u5)
m.add_unit(u6)
m.add_unit(u1)
print "dddd"
print m, m.is_done()
#m.move()
#print m, m.is_done()
#print len(m.dimension)

u = Unit(0, [5,5])
uu = Unit(1, [4,4])
#u.add(uu)
#print u, uu
#print m.is_done()
m.rot()
print "m after flip:"
print m
"""
