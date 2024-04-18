class RangeOperator:
    from enum import Enum

    class Operator(Enum):
        EQ = 1  # Equal
        LT = 2  # Less Than
        LTE = 3  # Less Than or Equal to
        GT = 4  # Greater Than
        GTE = 5  # Greater Than or Equal to

    OPERATOR_MAP = {
        Operator.EQ: "=",
        Operator.LT: "<",
        Operator.LTE: "<=",
        Operator.GT: ">",
        Operator.GTE: ">=",
    }

    def __init__(self, operator: "RangeOperator.Operator", value: int):
        self._operator = operator
        self._value = value

    def operator(self) -> str:
        return self.OPERATOR_MAP[self._operator]

    def value(self) -> int:
        return self._value