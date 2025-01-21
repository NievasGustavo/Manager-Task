from classTask import Task


def renglones(texto: str, max_car: int = 20) -> list[str]:
    """Divide el texto en varias líneas si excede el número máximo de caracteres"""
    if len(texto) > max_car:
        palabras = texto.split()
        renglones = []
        renglon_actual = ""
        for palabra in palabras:
            if len(renglon_actual) + len(palabra) + 1 <= max_car:
                renglon_actual += (palabra + " ")
            else:
                renglones.append(renglon_actual.rstrip())
                renglon_actual = palabra + " "
        renglones.append(renglon_actual.rstrip())
    else:
        renglones = [texto]
    
    return renglones


def formatOutput(tasks: list[Task]):
    header = "║ {:<10} ║ {:<20} ║ {:<13} ║ {:<20} ║ {:<20} ║".format(
        "ID", "Description", "Status", "Created At", "Updated At"
    )
    
    separator = "╠════════════╬══════════════════════╬═══════════════╬══════════════════════╬══════════════════════╣"
    
    rows = ""
    for task in tasks:
        description_lines = renglones(task.description)
        
        row = "║ {:<10} ║ {:<20} ║ {:<24} ║ {:<20} ║ {:<20} ║".format(
            task.id, 
            description_lines[0][:20],
            task.colourTask(),
            task.createdAt, 
            task.updatedAt
        )
        rows += row + "\n"

        for line in description_lines[1:]:
            row = "║ {:<10} ║ {:<20} ║ {:<13} ║ {:<20} ║ {:<20} ║".format(
                "",
                line[:20],
                "",
                "",
                ""
            )
            rows += row + "\n"

        if task != tasks[-1]:
            rows += separator + "\n"
    
    def printTable(header, rows):
        print("╔" + "═" * (len(header) - 2) + "╗")
        print(header)
        print(separator)
        print(rows, end="")
        print("╚" + "═" * (len(header) - 2) + "╝")
    printTable(header, rows)


if __name__ == "__main__":
    tasks = [Task(1, "Comprar pan", "todo", "2025-01-18", "2025-01-18"),
             Task(2, "Estudiar Python para mejorar mis habilidades y conseguir un mejor trabajo", "in-progress", "2025-01-19", "2025-01-19"),
             Task(3, "Hacer ejercicio", "done", "2025-01-17", "2025-01-18")]
    
    formatOutput(tasks)