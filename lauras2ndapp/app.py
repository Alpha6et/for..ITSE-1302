"""
My second application
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

terms_dict = {
    "Darknet" : "A part of the World Wide Web only accessible through special software or tools, like a TOR browser.",
    "IP Address" : "Internet Protocol Address, a string of numbers associated with a computer.",
    "VPN" : "Virtual Private Network, an encrypted internet connection.",
    "Programming" : "A technological process for telling a computer which tasks to perform in order to solve problems.",
    "Endpoint" : "A physical device connected to a computer network.",
    "Evil Twin" : "A frauldulent wifi access point that mimics a legitimate wifi access point."
}

class Lauras2ndApp(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        self.word_list = toga.Selection(items=list(terms_dict.keys()),style=Pack(flex=1, padding=(0,10)))
        self.define_button = toga.Button("Click for Definition!", on_press=self.define_word,style=Pack(padding=(10,0)))
        self.result_label = toga.Label("Definition: ",style=Pack(padding=(10,0)))
        main_box.add(self.word_list)
        main_box.add(self.define_button)
        main_box.add(self.result_label)
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()
    def define_word(self,widget):
        word = self.word_list.value
        definition = terms_dict.get(word, "Definition not found!")
        self.result_label.text = definition


def main():
    return Lauras2ndApp()
