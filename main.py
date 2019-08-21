import os
import sys
import datetime
from gi.repository import Gio

def frmt(name, size):
	name_size = len(name)
	if name_size > size:
		return " " + name[:size-3]+"..."
	else:
		return " " + name + (size-name_size)*" "

def get_files_references(path, contents):
	absolute_paths = map(lambda x: os.path.join(os.path.abspath(path), x), contents)
	return filter(lambda y: os.path.isfile, absolute_paths)
		
if __name__ == "__main__":
	path = sys.argv[1]
	path_contents = os.listdir(path)
	files = get_files_references(path, path_contents)

	print("|        Nome        | Propritetario | Tamanho | Data de Criação | Data de Alteração |     Aplicação")

	for f in files:
		s = os.stat(f)
		
		t = Gio.content_type_guess(f)
		if t.result_uncertain == False:
			appi = Gio.app_info_get_all_for_type(t[0])
			app = appi[0].get_name()
		else:
			app = "None"

		print(frmt(f.split("/")[-1], 20), frmt(str(s.st_uid), 15), frmt(str(s.st_size), 9), frmt(datetime.datetime.fromtimestamp(s.st_ctime).strftime("%d/%m/%Y"), 17), frmt(datetime.datetime.fromtimestamp(s.st_mtime).strftime("%d/%m/%Y"), 18), frmt(app,20))
		
		
		
