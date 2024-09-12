class Process:
    def __init__(self, pid=0, maxT=0, elapsedT=0, batch=0, a=0, b=0):
        self.pid = pid
        self.maxT = maxT
        self.elapsedT = elapsedT
        self.remainingT = maxT - elapsedT
        self.batch = batch
        self.a = a
        self.b = b
        self.op = ""
        self.result = ""

    # Class getters
    def get_pid(self):
        return self.id

    def get_maxT(self):
        return self.maxT

    def get_elapsedT(self):
        return self.elapsedT

    def get_remainingT(self):
        return self.remainingT

    def get_batch(self):
        return self.batch

    def get_result(self):
        return self.result

    def get_op(self):
        return self.op
    
    # Class Setters
    def set_maxT(self, maxT):
        self.maxT = maxT
        self.remainingT = maxT - self.elapsedT

    def set_elapsedT(self, elapsedT):
        self.elapsedT = elapsedT
        self.remainingT = self.maxT - elapsedT

    def set_batch(self, batch):
        self.batch = batch

    def set_a(self, a):
        self.a = a
        self.result = self.calculate_result(self.a, self.b)

    def set_b(self, b):
        self.b = b
        self.result = self.calculate_result(self.a, self.b)

    # Class methods
    def update_time(self):
        self.elapsedT += 1
        self.remainingT = self.maxT - self.elapsedT