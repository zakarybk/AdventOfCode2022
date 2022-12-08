from unittest import TestCase

from one import File, Folder


class TestFolderSizeUpdate(TestCase):


    def test_when_updating_folder_also_updates_parent(self):
        parent = Folder()
        folder = Folder(parent=parent)

        folder.size = 10
        assert parent.size == 10