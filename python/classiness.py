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
        self.classiness_points = {
            "tophat": 2,
            "bowtie": 4,
            "monocle": 5
        }

    def get_points(self, item) -> int:
        match item:
            case "tophat":
                return 2
            case "bowtie":
                return 4
            case "monocle":
                return 5
            case default:
                return 0

    def get_classiness(self):
        return self.classiness

    def add_item(self, item):
        self.items.append(item)
        self.classiness += self.get_points(item)  # use get_points
        # use dictionary
        # self.classiness += self.classiness_points.get(item, 0)


# Test cases
me = Classy()

# Should be 0
print(me.get_classiness())

me.add_item("tophat")
# Should be 2
print(me.get_classiness())

me.add_item("bowtie")
me.add_item("jacket")
me.add_item("monocle")
# Should be 11
print(me.get_classiness())

me.add_item("bowtie")
# Should be 15
print(me.get_classiness())
