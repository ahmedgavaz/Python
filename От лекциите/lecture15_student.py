class Student:
    def __init__(self, fnum, name, mark):
        self.fnum = fnum
        self.name = name
        self.mark = mark

    def __str__(self):
        return '['+str(self.fnum)+', '+self.name+', '+str(self.mark)+']'


class StudentGroup:
    def __init__(self):
        self.group = []

    def append(self, student):
        self.group.append(student)

    def __str__(self):
        # return str([str(student) for student in self.group])
        result = ''
        for student in self.group:
            result += str(student)+' '
        return result

    def min_mark(self):
        min = self.group[0]
        for student in self.group:
            if (min.mark > student.mark):
                min = student
        return min

    def max_mark(self):
        max = self.group[0]
        for student in self.group:
            if (max.mark < student.mark):
                max = student
        return max

    def average_mark(self):
        sum = 0
        for student in self.group:
            sum += student.mark
        return round(sum/len(self.group))

    def sort(self):
        for i in range(len(self.group)):
            min = i
            for j in range(i+1, len(self.group)):
                if self.group[min].mark > self.group[j].mark:
                    min = j
            # temp = self.group[i]
            # self.group[i] = self.group[min]
            # self.group[min] = temp
            self.group[min], self.group[i] = self.group[i], self.group[min]


st1 = Student(122, 'Ivan', 5.66)
st2 = Student(123, 'Lili', 5.55)
print(st1.__str__())
print(st2)

group = StudentGroup()
group.append(st1)
print(group.__str__())
group.append(st2)
print(group)

st11 = Student(222, 'Petyr', 5.11)
st21 = Student(223, 'Maria', 5.22)
st12 = Student(322, 'Dimityr', 5.33)
st22 = Student(323, 'Georgi', 5.44)
group.append(st11)
group.append(st21)
group.append(st12)
group.append(st22)
print(group)
print(group.max_mark())
print(group.min_mark())
print(group.average_mark())
print(group)
group.sort()
print(group)
