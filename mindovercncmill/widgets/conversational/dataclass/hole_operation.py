from mindovercncmill.widgets.conversational.dataclass.program_operation import ProgramOperation


class HoleOperation(ProgramOperation):
    def __init__(self):
        ProgramOperation.__init__(self)

    def generate_code(self):
        return "G1"

    def has_valid_inputs(self):
        return True
