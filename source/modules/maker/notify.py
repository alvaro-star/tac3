'''class Interested:
    def __init__(self):
        self.events = []
    
    def set_notify(self, id:int):
        self.events.append(id)

    def events_get(self):
        ret = self.events.copy()
        self.events = []
        return ret'''


class Event:
    def __init__(self, type:int, value:object):
        self.type = type
        self.value = value


class Notify:
    def __init__(self):
        self.events:list[Event] = []
    
    def add_event(self, type:int, value):
        self.events.append(Event(type, value))

    def get_events(self):        
        return self.events

    def clear(self):
        self.events = []

notify = Notify()




'''class Notify2():
    def __init__(self, 
                 interested:list[Interested], 
                 id:int):
        self.interested = interested
        self.id = id

    def event(self):        
        for i in self.interested:            
            i.set_notify(self.id)'''

    