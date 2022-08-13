possui_passaporte = False
passagem_comprada = False
menor_de_idade = False

print((possui_passaporte and passagem_comprada) and not menor_de_idade)
print((possui_passaporte or passagem_comprada) and not menor_de_idade)
print((not passagem_comprada or possui_passaporte) and not menor_de_idade)
print
