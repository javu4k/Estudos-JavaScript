print ("\n--- Cadastro de Usuário ---")

evento_nome = input ("Insira o nome do evento: ")
evento_data = input ("Insrira a data do evento (DD/MM/AA): ")
evento_hora = input ("Insira o horário do evento: ")
evento_local = input ("Insira o local do evento: ")
evento_categoria = input ("Insira a categora do evento: ")
evento_descricao = input ("Insira a descrição do evento: ")

print("\n--- Evento Cadastrado com Sucesso ---")

print(f"Nome: {evento_nome}")
print(f"Data: {evento_data}")
print(f"Horário: {evento_hora}")
print(f"Local: {evento_local}")
print(f"Categoria: {evento_categoria}")
print(f"Descrição: {evento_descricao}")