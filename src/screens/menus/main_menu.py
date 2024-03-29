from os.path import abspath
from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP, QUIT
from pygame import mouse, event, mixer
from src import settings


from ...base import MenuBase
from ...assets import keys


class MainMenu(MenuBase):
    music: mixer.Sound = None
    title: str = "|_| |_ |_"

    def __init__(self) -> None:
        super().__init__(self.title, [keys.buttons.play, keys.buttons.quit])
        self.next_screen: str = "level"
        mouse.set_visible(True)
        self.music = mixer.Sound(file=abspath(f"{self.sound_path}/{settings.main_menu_theme}"))
        self.music.set_volume(0.1)
        self.music.play(-1)

    def __del__(self) -> None:
        self.music.stop()

    def check_events(self, _event: event.Event) -> None:
        if _event.type == MOUSEBUTTONDOWN:
            for button in self.buttons:
                button.check_button(_event.pos)
        elif _event.type == MOUSEBUTTONUP:
            for button in self.buttons:
                if button.check_button(_event.pos, True):
                    if button.key == keys.buttons.play:
                        event.post(event.Event(self.CHANGESCREEN))
                    elif button.key == keys.buttons.quit:
                        event.clear()
                        event.post(event.Event(QUIT))

    def update(self):
        self.image.fill((0, 0, 0))
        self.image.blits(self.button_blit_seq)
        self.image.blit(self.title, self.title_rect)
