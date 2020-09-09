import os
from shutil import rmtree, copyfile

from family_foto.models.file import File
from family_foto.models.video import Video
from tests.base_test_case import BaseTestCase

VIDEOS_SAVE_PATH = './videos'
RESIZED_SAVE_PATH = './resized-images'


class VideoBaseTestCase(BaseTestCase):
    """
    Base Setup for usage of videos.
    """

    def setUp(self):
        super().setUp()
        if not os.path.exists(VIDEOS_SAVE_PATH):
            os.mkdir(VIDEOS_SAVE_PATH)
        if os.path.exists(RESIZED_SAVE_PATH):
            rmtree(RESIZED_SAVE_PATH)
        File.query.delete()
        Video.query.delete()

        copied_path = copyfile('./data/example.mp4', f'{VIDEOS_SAVE_PATH}/example.mp4')
        if not os.path.exists(copied_path):
            raise FileNotFoundError(f'{copied_path} does not exists.')
        self.video = Video(filename='example.mp4', url='/videos/example.mp4')

    def tearDown(self):
        if os.path.exists(VIDEOS_SAVE_PATH):
            rmtree(VIDEOS_SAVE_PATH)
        super().tearDown()
