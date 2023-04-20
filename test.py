class student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s: %s' % (self.name, self.score, self.get_grade()))

    def get_grade(self):
        if self.score >= 90:
            print('A')
        elif self.score >= 60:
            print('B')
        else:
            print('C')

student1 = student()
student2 = student()

student1.__init__('John', 100)
student2.__init__('Mary', 80)

student1.print_score()
student1.get_grade()
student2.print_score()
student2.get_grade()
