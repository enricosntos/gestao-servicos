from clientes import criar_cliente, listar_clientes, buscar_cliente, deletar_cliente 

criar_cliente("Maria Silva", "12 99999-0000", "mariafolote@email.com")
print (listar_clientes()) 
print(buscar_cliente(1))
print(deletar_cliente(1))
