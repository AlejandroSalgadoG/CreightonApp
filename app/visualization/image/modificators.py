from datetime import date
from PIL import Image, ImageDraw
from typing import Optional

from visualization.image.observation import Observation


class ImageModificator:
    def __init__(self, image: Image):
        self.image = image.copy()
        self.img_w, self.img_h = self.image.size
        self.draw = ImageDraw.Draw(self.image)

    def get_text_box_dim(self, msg: str, font_size: int) -> tuple[int, int]:
        l, t, r, b = self.draw.textbbox((0, 0), msg, font_size=font_size)
        return r-l, b-t

    def write_text(self, x: int, y: int, msg: str, font_size: int) -> Image:
        self.draw.text((x, y), msg, font_size=font_size, fill="black")
        return self.image

    def draw_cell(self, color: str) -> Image:
        self.draw.rectangle([0, 0, self.img_w, self.img_h], fill=color, outline="black", width=2)
        return self.image


class TitleModificator(ImageModificator):
    def __init__(self, image: Image, font_size: int):
        super().__init__(image)
        self.font_size = font_size

    def write_id(self, msg: str) -> Image:
        self.draw_cell("white")
        box_w, box_h = self.get_text_box_dim(msg, self.font_size)
        return self.write_text(x=(self.img_w-box_w)/2, y=(self.img_h-box_h)/2, msg=msg, font_size=self.font_size)


class AnnotationModificator(ImageModificator):
    def __init__(self, image: Image, font_size: int):
        super().__init__(image)
        self.font_size = font_size

    def write_date(self, date: date) -> Image:
        msg = date.strftime("%d-%m-%y")
        box_w, box_h = self.get_text_box_dim(msg, self.font_size)
        return self.write_text(x=(self.img_w-box_w)/4, y=(self.img_h-box_h)/4, msg=msg, font_size=self.font_size)

    def write_observation(self, observation: str, code: Optional[str]) -> Image:
        msg = observation + (code or "")
        box_w, box_h = self.get_text_box_dim(msg, self.font_size)
        return self.write_text(x=2*(self.img_w-box_w)/4, y=2*(self.img_h-box_h)/4, msg=msg, font_size=self.font_size)

    def write_frequency(self, frequency: str) -> Image:
        box_w, box_h = self.get_text_box_dim(frequency, self.font_size)
        return self.write_text(x=3*(self.img_w-box_w)/4, y=3*(self.img_h-box_h)/4, msg=frequency, font_size=self.font_size)

    def write_comment(self, comment: str) -> Image:
        box_w, box_h = self.get_text_box_dim(comment, self.font_size)
        return self.write_text(x=(self.img_w-box_w), y=(self.img_h-box_h), msg=comment, font_size=self.font_size)

    def write_annotation(self, observation: Observation) -> Image:
        self.draw_cell("white")
        self.write_date(observation.date)
        self.write_observation(observation.observation, observation.code)
        self.write_frequency(observation.frequency)
        return self.write_comment(observation.comment) if observation.comment else self.image


class TagModificator(ImageModificator):
    def write_baby(self) -> Image:
        font_size = 30
        box_w, box_h = self.get_text_box_dim("B", font_size)
        return self.write_text(x=(self.img_w-box_w)/4, y=(self.img_h-box_h)/4, msg="B", font_size=font_size)

    def write_peak_indication(self, peak_indication: str) -> Image:
        font_size = 30
        box_w, box_h = self.get_text_box_dim(peak_indication, font_size)
        return self.write_text(x=2*(self.img_w-box_w)/4, y=2*(self.img_h-box_h)/4, msg=peak_indication, font_size=font_size)

    def write_tag(self, observation: Observation) -> Image:
        self.draw_cell(observation.color)

        if observation.baby:
            self.write_baby()

        if observation.peak_indication:
            self.write_peak_indication(observation.peak_indication)

        return self.image
