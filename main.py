from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Calculator(BaseModel):
    first_num: float
    operation: str
    second_num: float


@app.post("/calculate")
def calculate(arguments: Calculator):
    if arguments.operation == "+":
        return {"Addition result": arguments.first_num + arguments.second_num}
    if arguments.operation == "-":
        return {"Subtraction result": arguments.first_num - arguments.second_num}
    if arguments.operation == "*":
        return {"Multiplication result": arguments.first_num * arguments.second_num}
    if arguments.operation == "/":
        if arguments.second_num == 0:
            return {"Can't divide by 0"}
        else:
            return {"Division result": arguments.first_num / arguments.second_num}
    return {"You used the wrong operator, expected: +, -, * or /"}
