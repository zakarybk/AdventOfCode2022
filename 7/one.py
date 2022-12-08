from pathlib import Path
from dataclasses import dataclass
from typing import List, Union


MOVE_UP = '..'


@dataclass
class File:
    name: str
    size: int = 0


@dataclass
class Folder:
    name: str = ""
    parent: 'Folder' = None
    _size: int = 0
    files: Union[List[File], None] = None
    folders: Union[List['Folder'], None] = None

    @property
    def size(self) -> int: return self._size

    @size.setter
    def size(self, value: int):
        self._size = value
        if self.parent: self.parent.size += value


def dirs_below_size(root: Folder, max_size: int=0) -> List[Folder]:
    folders = []

    if root.size <= max_size: folders.append(root)
    if root.folders:
        for folder in root.folders: folders += dirs_below_size(folder, max_size)

    return folders


def run(lines: List[str]) -> Folder:
    """ Return root folder, which links to all parsed folders """
    top_dir = Folder()
    cur_dir = top_dir

    is_command = lambda s: s.startswith('$')
    listing_dirs = False

    for line in lines:
        if is_command(line):
            # Change directory
            if line.startswith('$ cd'):
                move_to = line.replace('$ cd', '').strip()
                if move_to == MOVE_UP:
                    cur_dir = cur_dir.parent
                    print(line, "UP")
                elif not cur_dir.folders or not any(f.name==move_to for f in cur_dir.folders):
                    new_dir = Folder(name=move_to, parent=cur_dir)
                    if not cur_dir.folders:
                        cur_dir.folders = [new_dir]
                    else:
                        cur_dir.folders.append(new_dir)
                    cur_dir = new_dir
                    print(line, "NEW")
                else:
                    cur_dir = next(f for f in cur_dir.folders if f.name==move_to)
                    print(line, "MOV")
            
            # Not actually needed
            # elif line == '$ ls':
            #     listing_dirs = True

        else:
            # Again, not needed
            # if line.startswith('dir'):
            #     if not any(f.name==move_to for f in cur_dir.folders):

            if not line.startswith('dir'):
                size, name = line.split()
                file = File(name, int(size))
                if not cur_dir.files:
                    cur_dir.files = [file]
                else:
                    cur_dir.files.append(file)
                cur_dir.size += file.size

    return top_dir


if __name__ == '__main__':
    data = Path("i.txt").read_text()
    root = run(data.splitlines())
    dirs = dirs_below_size(root, 100000)
    print(sum(map(lambda f: f.size, dirs)))



