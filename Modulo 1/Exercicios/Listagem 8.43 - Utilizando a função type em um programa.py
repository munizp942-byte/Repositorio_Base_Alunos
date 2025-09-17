import types

def diz_o_tipo(a):
  tipo = type(a)
  if tipo == str:
    return("String")
  elif tipo == list:
    return("Lista")
  elif tipo == dict:
    return("Dicionário")
  elif tipo == int:
    return("Número inteiro")
  elif tipo == float:
    return("Número decimal")
  elif tipo == types.FunctionType:
    return("Função")
  elif tipo == types.BuiltinFunctionType:
    return("Função interna")
  else:
    return(str(tipo))
print(diz_o_tipo("Alô"))
print(diz_o_tipo(print))
print(diz_o_tipo(len))
print(diz_o_tipo(type))
print(diz_o_tipo(input))
print(diz_o_tipo(range))
print(diz_o_tipo(str.replace))