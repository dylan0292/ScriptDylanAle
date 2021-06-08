import os
import sys
import webbrowser

print("Credit Proyect Dylan")
def banner_fachero():
    print("""
    Menú de opciones:
        1) SACAR DNI POR NOMBRE             
        2) VERIFICAR SIS             
        3) RUC           
        4) MULTAS           
        5) COMPAÑIA TELEFÓNICA           
        6) SERVICIOS BIOMETRICOS           
        7) FECHA DE NACIMIENTO           
        8) ESSALUD
        9) ACTAS 
        10) SAT
        11) PADRON GENERAL DE HOGARES (PGH) 
        12) BONO 600
        13) LICENCIA DE CONDUCIR
        14) ESTUDIOS UNIVERSITARIOS
        15) COLEGIATURA
        16) COLEGIO DE PROFESORES
        17) CONSULTAR A QUIEN LE PERTENECE UNA PLACA DE AUTO
        18) EMERGENCIAS BOMBEROS 24 HORAS
         GITHUB CREATOR https://github.com/dylan0292

            Compañias telefónicas:
                c) Claro
                m) Movistar
                e) Entel
                b) Bitel

        f) volver al menú principal       
""")
def menusito():
    opcion2 = input("Dylan/Opción: ")
    if opcion2 == "1":
        webbrowser.open_new("https://eldni.com/pe/buscar-por-nombres")
        menusito()
    elif opcion2 == "2":
        webbrowser.open_new("http://app.sis.gob.pe/SisConsultaEnLinea/Consulta/frmConsultaEnLinea.aspx")
        menusito()
    elif opcion2 == "3":
        webbrowser.open_new("https://e-consultaruc.sunat.gob.pe/cl-ti-itmrconsruc/FrameCriterioBusquedaMovil.jsp") 
        menusito()
    elif opcion2 == "4":
        webbrowser.open_new("http://aplicaciones007.jne.gob.pe/multas/")
        menusito()
    elif opcion2 == "5":
        webbrowser.open_new("http://www.deperu.com/celulares/")
        menusito()
    elif opcion2 == "6":
        webbrowser.open_new("https://serviciosbiometricos.reniec.gob.pe/appConsultaHuellas/index.htm")
        menusito()
    elif opcion2 == "7":
        webbrowser.open_new("http://dniperu.online/buscar-dni-por-nombres-y-apellidos/")
        menusito()
    elif opcion2 == "8":
        webbrowser.open_new("http://ww4.essalud.gob.pe:7777/acredita/")
        menusito()
    elif opcion2 == "9":
        webbrowser.open_new("https://www.reniec.gob.pe/concer/concer.do")
        menusito()
    elif opcion2 == "10":
        webbrowser.open_new("https://www.sat.gob.pe/Websitev9")
        menusito()
    elif opcion2 == "11":
        webbrowser.open_new("https://operaciones.sisfoh.gob.pe/cse/")
        menusito()
    elif opcion2 == "12":
        webbrowser.open_new("https://consultas.bono600.gob.pe/")
        menusito()
    elif opcion2 == "13":
        webbrowser.open_new("http://slcp.mtc.gob.pe/")
        menusito()
    elif opcion2 == "14":
        webbrowser.open_new("https://enlinea.sunedu.gob.pe/")
        menusito()
    elif opcion2 == "15":
        webbrowser.open_new("http://cipvirtual.cip.org.pe/sicecolegiacionweb/externo/consultaCol/#")
        menusito()
    elif opcion2 == "16":
        webbrowser.open_new("https://sistema.cppe.org.pe/view/Colegiado/")
        menusito()
    elif opcion2 == "17":
        webbrowser.open_new("https://www.sunarp.gob.pe/seccion/servicios/detalles/0/c3.html")
        menusito()
    elif opcion2 == "18":
        webbrowser.open_new("https://sgonorte.bomberosperu.gob.pe/24horas")
        print("https://github.com/dylan0292")
        menusito()
    elif opcion2 == "c":
        webbrowser.open_new("http://www.claro.com.pe/consulta-de-lineas/")
        menusito()
    elif opcion2 == "m":
        webbrowser.open_new("http://www.movistar.com.pe/atencion-al-cliente/conoce-tus-numeros-moviles")
        menusito()
    elif opcion2 == "e":
        webbrowser.open_new("http://www.entel.pe/app-privado/?app=consulta_lineas")
        menusito()
    elif opcion2 == "b":
        webbrowser.open_new("https://bitel.com.pe/asistencia/consulta-linea")
        menusito()
    elif opcion2 == "f":
        os.system("clear")
        os.system("cd .. && python3 peru.py")
    else:
        print("""
      ▄▄▄▄
      ▀▀▄██►     :(
      ▀▀███►
       ▀███► █►
       ▄████▀▀   opción invalida
    """)
    print("Github Creador Dylan")
    print("https://github.com/dylan0292")
    menusito()
    print("Hola")

# empezar 
banner_fachero()
menusito()