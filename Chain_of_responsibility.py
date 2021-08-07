class NullHandler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, obj, event):
        if self.successor is not None:
            return self.successor.handle(obj, event)


class IntHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event, EventGet):
            if event.type == int:
                return obj.integer_field
            else:
                return super().handle(obj, event)
        elif isinstance(event, EventSet):
            if type(event.value) == int:
                obj.integer_field = event.value
            else:
                return super().handle(obj, event)


class FloatHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event, EventGet):
            if event.type == float:
                return obj.float_field
            else:
                return super().handle(obj, event)
        elif isinstance(event, EventSet):
            if type(event.value) == float:
                obj.float_field = event.value
            else:
                return super().handle(obj, event)


class StrHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event, EventGet):
            if event.type == str:
                return obj.string_field
            else:
                return super().handle(obj, event)
        elif isinstance(event, EventSet):
            if type(event.value) == str:
                obj.string_field = event.value
            else:
                return super().handle(obj, event)


class EventGet:
    def __init__(self, type):
        self.type = type


class EventSet:
    def __init__(self, value):
        self.value = value
