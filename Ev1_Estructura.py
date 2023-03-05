# Evidencia numero "1"
# Import
import os

# Diccionario
dic_libros = {0: ("PINOCHO", "NARVICK", "INFANTIL",
                  2010, 1819140, "03/03/2023"), }

# Menu principal
while True:

    print("\n** MENU PRINCIPAL **")
    print("\n[1] REGISTRAR NUEVO EJEMPLAR")
    print("\n[2] CONSULTAS Y REPORTES")
    print("\n[3] SALIR")
    op = int(input("\nINGRESE EL NUMERO DE OPERACION QUE SE DESEA REALIZAR : "))
    os.system("cls")

    # Opcion "1"
    if op == 1:
        while True:

            print("\nREGISTRAR UN NUEVO EJEMPLAR")
            titulo = input("\nINGRESE EL TITULO DEL EJEMPLAR : ").upper()
            os.system("cls")
            autor = input("\nINGRESE EL NOMBRE DEL AUTOR : ").upper()
            os.system("cls")
            genero = input("\nINGRESE EL GENERO DEL LIBRO : ").upper()
            os.system("cls")
            año_de_publicacion = int(
                input("\nINGRESE EL AÑO DE PUBLICACION : "))
            os.system("cls")
            isbn = int(input("\nINGRESE EL ISBN : "))
            os.system("cls")
            fecha_adquisicion = input(
                "\nINGRESE LA FECHA DE ADQUISICION EN EL FORMATO (DD/MM/AAAA) : ")
            os.system("cls")

            # Clave del registro
            if dic_libros:
                clave = max(dic_libros) + 1
            else:
                clave = 1

            os.system("cls")
            print("\nREGISTRO TERMINADO")
            # Diccionario donde se guardan los datos
            dic_libros[clave] = titulo, autor, genero, año_de_publicacion, isbn, fecha_adquisicion
            respuesta = input(
                "DESEA SEGUIR AGREGANDO EJEMPLARES [SI/NO]").upper()
            if respuesta == "NO":
                break

            os.system("cls")

    # Opcion "2"
    elif op == 2:

        # Sub menu "1"
        while True:

            print("\n** MENU DE CONSULTAS Y REPORTES **")
            print("\n[1] CONSULTA DE TITULO")
            print("\n[2] REPORTES")
            print("\n[3] VOLVER AL MENU PRINCIPAL ")
            op2 = int(
                input("\nINGRESE EL NUMERO DE OPERACION QUE SE DESEA REALIZAR : "))
            os.system("cls")

            # Opcion "1"
            if op2 == 1:

                # Sub menu "2"
                while True:

                    print("\n** MENU DE CONSULTA DE TITULO **")
                    print("\n[1] POR TITULO")
                    print("\n[2] POR ISBN")
                    print("\n[3] VOLVER AL MENU DE CONSULTAS Y REPORTES")
                    op3 = int(
                        input("\nINGRESE EL NUMERO DE OPERACION QUE DESEA REALIZAR : "))
                    os.system("cls")
                    # Opcion "1"
                    if op3 == 1:
                        # while True:
                        titulo = input(
                            "\nINGRESE EL TITULO DEL LIBRO QUE BUSCAS : ").upper()

                        os.system("cls")
                        print("\nTITULO ENCONTRADO\n")
                        print("*"*97)
                        print(
                            "CLAVE     TITULO      AUTOR      GENERO      AÑO DE PUBLICACION      ISBN      AÑO DE ADQUISICIÓN")
                        print("*"*97)
                        print("*"*97)

                        for clave, datos in dic_libros.items():
                            if titulo in datos:
                                clave_del_titulo = clave
                                print(" ", clave_del_titulo, "    ", dic_libros[clave_del_titulo][0], "  ", dic_libros[clave_del_titulo][1], "    ", dic_libros[clave_del_titulo][
                                      2], "            ", dic_libros[clave_del_titulo][3], "          ", dic_libros[clave_del_titulo][4], "      ", dic_libros[clave_del_titulo][5])
                                print("*"*97)
                                regreso = input(
                                    "\nPULSA ENTER PARA REGRESAR AL MENU DE CONSULTA DE TITULO : ")
                                os.system("cls")
                            else:
                                print("\nLO SENTIMOS, NO CONTAMOS CON ESE TITULO")
                                regreso = input(
                                    "\nPULSA ENTER PARA REGRESAR AL MENU DE CONSULTA DE TITULO : ")
                                os.system("cls")

                    # Opcion "2"
                    elif op3 == 2:
                        isbn = int(
                            input("\nINGRESE EL ISBN DEL LIBRO QUE BUSCAS : "))
                        os.system("cls")
                        for clave, datos in dic_libros.items():
                            if isbn in datos:
                                clave_del_titulo = clave

                                print("\ISBN ENCONTRADO\n")
                                print("*"*97)
                                print(
                                    "CLAVE     TITULO      AUTOR      GENERO      AÑO DE PUBLICACION      ISBN      AÑO DE ADQUISICIÓN")
                                print("*"*97)
                                print("*"*97)
                                print(" ", clave_del_titulo, "    ", dic_libros[clave_del_titulo][0], "  ", dic_libros[clave_del_titulo][1], "    ", dic_libros[clave_del_titulo][
                                      2], "            ", dic_libros[clave_del_titulo][3], "          ", dic_libros[clave_del_titulo][4], "      ", dic_libros[clave_del_titulo][5])
                                print("*"*97)
                                regreso = input(
                                    "\nPULSA ENTER PARA REGRESAR AL MENU DE CONSULTA DE TITULO : ")
                                os.system("cls")

                            else:
                                print("\nLO SENTIMOS, NO CONTAMOS CON ESE TITULO")
                                regreso = input(
                                    "\nPULSA ENTER PARA REGRESAR AL MENU DE CONSULTA DE TITULO : ")
                                os.system("cls")

                    # Opcion "3"
                    elif op3 == 3:
                        regreso = input(
                            "\nPULSA ENTER PARA REGRESAR AL MENU DE CONSULTAS Y REPORTES : ")
                        os.system("cls")
                        break

                    # Error
                    else:

                        print("\nEL DATO QUE INGRESO ES INCORRECTO")
                        regreso = input(
                            "\nPULSA ENTER PARA REGRESAR AL MENU DE CONSULTA DE TITULO : ")
                        os.system("cls")

            # Opcion "2"
            elif op2 == 2:
                # Sub menu "3"
                while True:

                    print("\n** MENU DE REPORTES **")
                    print("\n[1] CATALAGO COMPLETO")
                    print("\n[2] REPORTE POR AUTOR")
                    print("\n[3] REPORTE POR GENERO")
                    print("\n[4] REPORTE POR AÑO DE PUBLICACION")
                    print("\n[5] VOLVER AL MENU DE CONSULTAS Y REPORTES")
                    op4 = int(
                        input("\nINGRESE EL NUMERO DE OPERACION QUE DESEA REALIZAR : "))
                    os.system("cls")

                    # Opcion "1"
                    if op4 == 1:
                        print("\nCATALAGO COMPLETO\n")
                        print("*"*97)
                        print(
                            "CLAVE     TITULO      AUTOR      GENERO      AÑO DE PUBLICACION      ISBN      AÑO DE ADQUISICIÓN")
                        print("*"*97)
                        for clave, datos in dic_libros.items():
                            print("*"*97)
                            print(" ", clave, "    ", datos[0], "  ", datos[1], "    ", datos[2],
                                  "            ", datos[3], "          ", datos[4], "      ", datos[5])
                            print("*"*97)
                        regreso = input(
                            "\nPULSA ENTER PARA REGRESAR AL MENU DE REPORTES :")
                        os.system("cls")

                    # Opcion "2"
                    elif op2 == 2:
                        while True:

                            print("\nREPORTE POR AUTOR")
                            autor = input(
                                "\nINGRESE EL NOMBRE DEL AUTOR QUE BUSCAS : ").upper()
                            respuesta = input(
                                "¿DESEA SEGUIR BUSCANDO POR AUTOR? [SI/NO]").upper()
                            if respuesta == "NO":
                                break
                            os.system("cls")

                            for clave, datos in dic_libros.items():
                                if autor in datos:
                                    clave_del_titulo = clave
                                    print("\AUTOR ENCONTRADO\n")
                                    print("*"*97)
                                    print(
                                        "CLAVE     TITULO      AUTOR      GENERO      AÑO DE PUBLICACION      ISBN      AÑO DE ADQUISICIÓN")
                                    print("*"*97)
                                    print("*"*97)
                                    print(" ", clave_del_titulo, "    ", dic_libros[clave_del_titulo][0], "  ", dic_libros[clave_del_titulo][1], "    ", dic_libros[clave_del_titulo][
                                          2], "            ", dic_libros[clave_del_titulo][3], "          ", dic_libros[clave_del_titulo][4], "      ", dic_libros[clave_del_titulo][5])
                                    print("*"*97)

                                regreso = input(
                                    "\nPULSA ENTER PARA REGRESAR AL MENU DE REPORTES : ")
                                os.system("cls")

                    # Opcion "3"
                    elif op3 == 3:
                        while True:
                            print("\nREPORTE POR GENERO")
                            os.system("cls")
                            genero = input(
                                "\nINGRESE EL GENERO QUE BUSCAS : ").upper()
                            respuesta = input(
                                "¿DESEA SEGUIR BUSCANDO POR GENERO? [SI/NO]").upper()
                            if respuesta == "NO":
                                break
                            for clave, datos in dic_libros.items():
                                if genero in datos:
                                    clave_del_titulo = clave
                                    print("\AUTOR ENCONTRADO\n")
                                    print("*"*97)
                                    print(
                                        "CLAVE     TITULO      AUTOR      GENERO      AÑO DE PUBLICACION      ISBN      AÑO DE ADQUISICIÓN")
                                    print("*"*97)
                                    print("*"*97)
                                    print(" ", clave_del_titulo, "    ", dic_libros[clave_del_titulo][0], "  ", dic_libros[clave_del_titulo][1], "    ", dic_libros[clave_del_titulo][
                                        2], "            ", dic_libros[clave_del_titulo][3], "          ", dic_libros[clave_del_titulo][4], "      ", dic_libros[clave_del_titulo][5])
                                    print("*"*97)

                                    regreso = input(
                                        "\nPULSA ENTER PARA REGRESAR AL MENU DE REPORTES : ")
                                    os.system("cls")

                    # Opcion "4"
                    elif op4 == 4:
                        while True:
                            print("\nREPORTE POR AÑO DE PUBLICACION")
                            año_de_publicacion = int(
                                input("\nINGRESE EL AÑO DE PUBLICACION QUE BUSCAS : "))
                            respuesta = input(
                                "¿DESEA SEGUIR BUSCANDO POR AÑO DE PUBLICACION? [SI/NO]").upper()
                            if respuesta == "NO":
                                break
                            os.system("cls")
                            for clave, datos in dic_libros.items():
                                if año_de_publicacion in datos:
                                    clave_del_titulo = clave
                                    print("\AÑO DE PUBLICACION  ENCONTRADO\n")
                                    print("*"*97)
                                    print(
                                        "CLAVE     TITULO      AUTOR      GENERO      AÑO DE PUBLICACION      ISBN      AÑO DE ADQUISICIÓN")
                                    print("*"*97)
                                    print("*"*97)
                                    print(" ", clave_del_titulo, "    ", dic_libros[clave_del_titulo][0], "  ", dic_libros[clave_del_titulo][1], "    ", dic_libros[clave_del_titulo][
                                        2], "            ", dic_libros[clave_del_titulo][3], "          ", dic_libros[clave_del_titulo][4], "      ", dic_libros[clave_del_titulo][5])
                                    print("*"*97)
                                    regreso = input(
                                        "\nPULSA ENTER PARA REGRESAR AL MENU DE REPORTES : ")
                                    os.system("cls")
                    # Opcion "5"
                    elif op4 == 5:
                        regreso = input(
                            "\nPULSA ENTER PARA REGRESAR AL MENU DE CONSULTAS Y REPORTES : ")
                        os.system("cls")
                        break

                    # Error
                    else:
                        print("\nEL DATO QUE INGRESO ES INCORRECTO")
                        regreso = input(
                            "\nPULSA ENTER PARA REGRESAR AL MENU DE REPORTES : ")
                        os.system("cls")
            # Opcion "3"
            elif op2 == 3:
                regreso = input(
                    "\nPULSA ENTER PARA REGRESAR AL MENU PRINCIPAL : ")
                os.system("cls")
                break
            # Error
            else:
                print("\nEL DATO QUE INGRESO ES INCORRECTO")
                regreso = input(
                    "\nPULSA ENTER PARA REGRESAR AL MENU DE CONSULTAS Y REPORTES : ")
                os.system("cls")
    # Opcion "3"
    elif op == 3:
        os.system("cls")
        print("\nGRACIAS POR SU VISITA")
        print("\nPROGRAMA FINALIZADO\n")
        break
    # Error
    else:
        print("\nEL DATO QUE INGRESO ES INCORRECTO")
        os.system("cls")
