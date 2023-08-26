"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangeable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""


class Classy(object):
    def __init__(self):
        self.items = []
        self.classiness = 0

    def getPoints(self, item) -> int:
        match item:
            case "tophat":
                return 2
            case "bowtie":
                return 4
            case "monocle":
                return 5
            case default:
                return 0

    def getClassiness(self):
        return self.classiness

    def addItem(self, item) -> None:
        self.items.append(item)
        self.classiness += self.getPoints(item)


# Test cases
me = Classy()

# Should be 0
print(me.getClassiness())

me.addItem("tophat")
# Should be 2
print(me.getClassiness())

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print(me.getClassiness())

me.addItem("bowtie")
# Should be 15
print(me.getClassiness())
