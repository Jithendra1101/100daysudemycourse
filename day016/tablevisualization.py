from prettytable import prettytable
table = prettytable.PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"]) 
table.add_column("Type", ["Electric", "Water", "Fire"])
table.add_row(["jithendra","all"]) 
table.align = "l"
table.add_row(["jithendra","all","hehe"])
print(table)
