from dataclasses import dataclass


@dataclass
class Encoding:
    name: str
    code: dict[int, str]

    def __getitem__(self, key: int) -> str:
        return self.code[key]

    def __contains__(self, key: int) -> bool:
        return key in self.code


ASCII = Encoding(
    name="ASCII",
    code={i: chr(i) for i in range(32, 127)},
)

CP437 = Encoding(
    name="CP437",
    code={
        i + 1: v
        for i, v in enumerate(
            """☺☻♥♦♣♠•◘○◙♂♀♪♫☼►◄↕‼¶§▬↨↑↓→←∟↔▲▼"""
            """ !"#$%&'()*+,-./0123456789:;<=>?"""
            """@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_"""
            """`abcdefghijklmnopqrstuvwxyz{|}~⌂"""
            """ÇüéâäàåçêëèïîìÄÅÉæÆôöòûùÿÖÜ¢£¥₧ƒ"""
            """áíóúñÑªº¿⌐¬½¼¡«»░▒▓│┤╡╢╖╕╣║╗╝╜╛┐"""
            """└┴┬├─┼╞╟╚╔╩╦╠═╬╧╨╤╥╙╘╒╓╫╪┘┌█▄▌▐▀"""
            """αßΓπΣσµτΦΘΩδ∞φε∩≡±≥≤⌠⌡÷≈°∙·√ⁿ²■"""
        )
    },
)

HEXLY = Encoding(
    name="HEXLY",
    code=dict(
        enumerate(
            """ø☺☻♥♦♣♠•◘○◙♂♀♪♫☼►◄↕‼¶§▬↨↑↓→←∟↔▲▼"""
            """␣!"#$%&'()*+,-./0123456789:;<=>?"""
            """@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_"""
            """`abcdefghijklmnopqrstuvwxyz{|}~⌂"""
            """ÇüéâäàåçêëèïîìÄÅÉæÆôöòûùÿÖÜ¢£¥₧ƒ"""
            """áíóúñÑªº¿⌐¬½¼¡«»░▒▓│┤╡╢╖╕╣║╗╝╜╛┐"""
            """└┴┬├─┼╞╟╚╔╩╦╠═╬╧╨╤╥╙╘╒╓╫╪┘┌█▄▌▐▀"""
            """αßΓπΣσµτΦΘΩδ∞φε∩≡±≥≤⌠⌡÷≈°∙·√ⁿ²■⍽"""
        )
    ),
)
