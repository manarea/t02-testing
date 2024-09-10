# Lambdas simples asignadas a variables
add = lambda a, b: a + b
multiply = lambda x, y: x * y

# Lambdas dentro de listas
operations = [
    lambda a, b: a - b,
    lambda x, y: x / y if y != 0 else 0
]

# Lambdas como argumentos de funciones
def apply_operation(op, a, b):
    return op(a, b)

result_add = apply_operation(lambda a, b: a + b, 10, 5)
result_subtract = apply_operation(lambda a, b: a - b, 10, 5)

# Lambdas en expresiones complejas
complex_expr = (lambda a, b: (a + b) * (a - b))(5, 2)

# Lambdas en estructuras condicionales
max_value = lambda x, y: x if x > y else y

# Usar las lambdas asignadas
result_multiply = multiply(6, 7)
result_list_op1 = operations[0](9, 4)
result_list_op2 = operations[1](8, 2)

# Imprimir resultados
print(add(1, 2))
print(result_add)
print(result_subtract)
print(complex_expr)
print(max_value(10, 20))
print(result_multiply)
print(result_list_op1)
print(result_list_op2)