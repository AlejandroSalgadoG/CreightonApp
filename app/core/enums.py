from dataclasses import dataclass
from enum import Enum


class ColorEnum(Enum):
    white = "white"
    red = "red"
    yellow = "yellow"
    green = "green"


@dataclass
class EnumElement:
    code: str
    description: str


class ObservationEnum(Enum):
    OBS_H = EnumElement("H", "H - flujo abundante")
    OBS_M = EnumElement("M", "M - flujo moderado")
    OBS_L = EnumElement("L", "L - flujo ligero")
    OBS_VL = EnumElement("VL", "VL - flujo muy ligero")
    OBS_B = EnumElement("B", "B - sangrado cafe/marron/negro")
    OBS_0 = EnumElement("0", "0 - seco")
    OBS_2 = EnumElement("2", "2 - humedo sin lubricacion")
    OBS_2W = EnumElement("2W", "2W - mojado sin lubricacion")
    OBS_4 = EnumElement("4", "4 - brillo sin lubricacion")
    OBS_6 = EnumElement("6", "6 - pegajoso (0.5 cm | 1/4 inch)")
    OBS_8 = EnumElement("8", "8 - ligoso (1-2 cm | 1/2 - 3/4 inch)")
    OBS_10 = EnumElement("10", "10 - elastico (2.5 cm | 1 inch)")
    OBS_10DL = EnumElement("10DL", "10DL - humedo con lubricacion")
    OBS_10SL = EnumElement("10SL", "10SL - brillo con lubricacion")
    OBS_10WL = EnumElement("10WL", "10WL - mojado con lubricacion")


class CodeEnum(Enum):
    CODE_B = EnumElement("B", "B - sangrado cafe/marron/negro")
    CODE_C = EnumElement("C", "C - nublado (blanco)")
    CODE_K = EnumElement("K", "K - transparente")
    CODE_L = EnumElement("L", "L - lubricante")
    CODE_P = EnumElement("P", "P - pastoso (cremoso)")
    CODE_R = EnumElement("R", "R - rojo")
    CODE_Y = EnumElement("Y", "Y - amarillo (aun muy palido)")


class FrequencyEnum(Enum):
    FREQ_x1 = EnumElement("x1", "x1 - una vez al dia")
    FREQ_x2 = EnumElement("x2", "x2 - dos veces al dia")
    FREQ_x3 = EnumElement("x3", "x3 - tres veces al dia")
    FREQ_AD = EnumElement("AD", "AD - a lo largo del dia")
