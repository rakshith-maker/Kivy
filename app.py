from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast

Window.size = (300, 500)
KV = '''
BoxLayout:
    orientation: 'vertical'

    MDToolbar:
        title: "Fake Detector"
        right_action_items: [["information",lambda x: app.navigation_draw()]]
        elevation:8
        


    FloatLayout:

        MDRoundFlatIconButton:
            text: "Upload file"
            icon: "file-upload"
            pos_hint: {'center_x': .5, 'center_y': .1}
            on_release: app.file_manager_open()
'''


class Example(MDApp):
    dialog = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            # previous=True,
        )

    def build(self):
        return Builder.load_string(KV)

    def file_manager_open(self):
        self.file_manager.show('/')  # output manager to the screen
        self.manager_open = True

    def select_path(self, path):
        """It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        """

        self.exit_manager()
        toast(path)

    def exit_manager(self, *args):
        """Called when the user reaches the root of the directory tree."""

        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text):
        """Called when buttons are pressed on the mobile device."""

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

    def navigation_draw(self):
        self.dialog = MDDialog(title="Fake detector is an app that helps you detect fake currency", size_hint=(0.7, 1))
        self.dialog.open()


Example().run()
