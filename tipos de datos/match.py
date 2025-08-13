status = "Solido"

match status:
    case "Solido":
        print("El estado es solido")
    case "liquido":
        print("el estado es liquido")
    case "gaseoso":
        print("El estado es gaseoso")
    case _:
        print("No existe")