import os
import sys
import datetime

def frmt(name, size):
	name_size = len(name)
	return " " + name[:size-3]+"..." if name_size > size else " " + name + (size-name_size)*" "

def print_curr_path_contents(files, directories, path):
	print("|        Nome        | Propritetario | Tamanho | Data de Criação | Data de Alteração |     Aplicação")
	
	for f in files:
		try:
			s = os.stat(os.path.join(path, f))
			print(frmt(f, 20), frmt(str(s.st_uid), 15), frmt(str(s.st_size), 9), frmt(datetime.datetime.fromtimestamp(s.st_ctime).strftime("%d/%m/%Y"), 17), frmt(datetime.datetime.fromtimestamp(s.st_mtime).strftime("%d/%m/%Y"), 18))
		except FileNotFoundError as e:
			print(e)
	for d in directories:
		print(d + " (DIR)")

def generate_contents_from_path(path):
	path_contents = os.listdir(path)
	join_path = lambda abs_path, content: os.path.join(os.path.abspath(abs_path), content)
	files = []
	directories = []
	for content in path_contents:
		joined_path = join_path(path, content)
		if os.path.isfile(joined_path):
			files.append(content)
		else:
			directories.append(content)

	print_curr_path_contents(files, directories, path)

	while(True):
		user_input = input("Digite 'nome do diretorio' para acessar o diretorio, ou digite '..' se deseja retornar: ")
		if user_input == "Q":
			return
		if user_input == "..":
			return generate_contents_from_path(join_path(path, ".."))
		if user_input not in directories:
			print("Não existe esse diretório!")
			continue
		break

	return generate_contents_from_path(join_path(path, user_input))
	

if __name__ == "__main__":
	path = sys.argv[1]
	generate_contents_from_path(path)
	print("END")
