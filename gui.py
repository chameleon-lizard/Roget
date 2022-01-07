from tkinter import filedialog as fd
from pathlib import Path
import tkinter as tk
import json

from vectorize import frequences, vectorize

class App():
    def __init__(self) -> None:
        self.window = tk.Tk()
        
        self.convertion_table = json.loads(Path("convert.json").read_text())
        
        l_input = tk.Label(self.window, text="Input")
        l_input.grid(row=0, column=0, columnspan=3)

        self.tb_input = tk.Text(self.window)
        self.tb_input.grid(row=1, column=0, columnspan=3)

        b_vectorize = tk.Button(self.window, text="Vectorize", command=self.vectorize)
        b_vectorize.grid(row=2, column=1)

        l_output = tk.Label(self.window, text="Output")
        l_output.grid(row=0, column=4, columnspan=3)

        self.tb_output_vector = tk.Text(self.window)
        self.tb_output_vector.grid(row=1, column=4, columnspan=3)
        
        self.tb_output_freq = tk.Text(self.window)
        self.tb_output_freq.grid(row=2, column=4, columnspan=3)
    
        self.window.mainloop()
    
    def preprocess(self, text: str) -> str:
        return "".join((i for i in text.lower() if i.isalpha() or i.isspace()))

    def vectorize(self) -> None:
        self.tb_output_freq.delete(1.0, tk.END)
        self.tb_output_vector.delete(1.0, tk.END)

        text = self.tb_input.get(1.0, tk.END)
        if len(text) == 1:
            filename = fd.askopenfile(defaultextension="*.txt")
            text = Path(filename.name).read_text()
            self.tb_input.insert(1.0, text)
        
        text = self.preprocess(text)

        vector = vectorize(text)

        vector = dict(reversed(sorted(vector.items(), key=lambda item: item[1])))
        converted = {str((key, self.convertion_table[key])): value for key, value in vector.items()}
        vectorized = json.dumps(converted, indent=2)
        self.tb_output_vector.insert(1.0, vectorized)

        everything = {str((key, self.convertion_table[key])): 0 for key in self.convertion_table.keys()}
        for key in converted.keys():
            everything[key] = converted[key]
        everything = json.dumps(everything, indent=2)

        freq = frequences(vector)
        converted = {str((key, self.convertion_table[key])): value for key, value in freq.items()}
        freq = dict(reversed(sorted(freq.items(), key=lambda item: item[1])))
        frequenced = json.dumps(converted, indent=2)
        self.tb_output_freq.insert(1.0, frequenced)


        Path("input.txt").write_text(text)
        Path("vector.json").write_text(vectorized)
        Path("frequences.json").write_text(frequenced)
        Path("everything.json").write_text(everything)
        

if __name__ == "__main__":
    app = App()
