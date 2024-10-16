import tkinter as tk
from tkinter import messagebox

class GestorTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        
        self.tareas = []
        
        # Frame superior
        self.frame_superior = tk.Frame(self.root)
        self.frame_superior.pack(pady=10)
        
        self.entry_tarea = tk.Entry(self.frame_superior, width=40)
        self.entry_tarea.pack(side=tk.LEFT, padx=5)
        
        self.boton_agregar = tk.Button(self.frame_superior, text="Agregar Tarea", command=self.agregar_tarea)
        self.boton_agregar.pack(side=tk.LEFT)
        
        # Lista de tareas
        self.lista_tareas = tk.Listbox(self.root, width=50)
        self.lista_tareas.pack(pady=10)
        
        # Botón eliminar
        self.boton_eliminar = tk.Button(self.root, text="Eliminar Tarea Seleccionada", command=self.eliminar_tarea)
        self.boton_eliminar.pack(pady=5)
    
    def agregar_tarea(self):
        tarea = self.entry_tarea.get()
        if tarea:
            self.tareas.append(tarea)
            self.lista_tareas.insert(tk.END, tarea)
            self.entry_tarea.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada vacía", "Por favor, ingresa una tarea.")
    
    def eliminar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            indice = seleccion[0]
            self.lista_tareas.delete(indice)
            del self.tareas[indice]
        else:
            messagebox.showwarning("Sin selección", "Por favor, selecciona una tarea para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GestorTareas(root)
    root.mainloop()
