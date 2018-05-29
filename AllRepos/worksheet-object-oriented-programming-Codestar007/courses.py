class BirkbeckCourse:
    def __init__(self, department, code, title):
        self.department = department
        self.code = code
        self.title = title


class BirkbeckCSISCourse(BirkbeckCourse):
    def __init__(self, department, code, title, recorded=False):
        super().__init__(department, code, title)
        self.is_recorded = recorded