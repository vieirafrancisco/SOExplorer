import os
import sys
import datetime

def get_files_reference(path, contents):
	absolute_paths = map(lambda x: os.path.join(os.path.abspath(path), x), contents)
	return filter(lambda y: os.path.isfile, absolute_paths)
		
if __name__ == "__main__":
	path = sys.argv[1]
	path_contents = os.listdir(path)
	files = get_files_reference(path, path_contents)

	print("Nome                | Propritetario | Tamanho | Data de Criação | Data de Alteração")

	for f in files:
		s = os.stat(f)
		print(f.split("/")[-1], s.st_uid, s.st_size, datetime.datetime.fromtimestamp(s.st_ctime).strftime("%d/%m/%Y"), 				datetime.datetime.fromtimestamp(s.st_mtime).strftime("%d/%m/%Y"))
