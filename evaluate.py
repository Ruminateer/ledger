# ref https://stackoverflow.com/questions/2371436

import ast
import operator as op

# supported operators
operators = {
    ast.Add: op.add, ast.Sub: op.sub,
    ast.Mult: op.mul, ast.Div: op.truediv, ast.Pow: op.pow,
    ast.USub: op.neg
}

def evaluate(expr):
    def eval_(node):
        if isinstance(node, ast.Num):
            return node.n
        if isinstance(node, ast.BinOp):
            return operators[type(node.op)](eval_(node.left), eval_(node.right))
        if isinstance(node, ast.UnaryOp):
            return operators[type(node.op)](eval_(node.operand))
        raise TypeError(node)

    return eval_(ast.parse(expr, mode='eval').body)
