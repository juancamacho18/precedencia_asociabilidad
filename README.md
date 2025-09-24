# precedencia_asociabilidad
este proyecto es una comparativa y prueba de dos calculadora en ANTLR4 para lenguaje objetivo Python, una utilizando precedencia y asociatividad (a la izquierda) normal, y otra invirtiendo la precedencia y la asociatividad de tal manera que se comprueben los resultados que muestran cada uno a diferentes expresiones matematicas.

# Estructura
calculadora:

-original:
    original.g4,
    EvalVisitor.py,
    main.py,
    (demas archivos generados..)
    
-modificado:
    modificado.g4,
    EvalVisitor.py,
    main.py,
    (demas archivos generados..)
    
  -pruebas.txt

ambas calculadoras aceptan el mismo archivo de pruebas, que contiene diferentes operaciones a comprobar y comparar 

# Como ejecutar
Lo primero es asegurarse que se tenga instalado ANTLR4 en su entorno de trabajo y que este correspondientemente configurado, luego para cada calculadora se puede realizar el mismo proceso; dentro de la ruta de estos mismos.

Ahora estando en la ruta de la caluladora que se quiere probar, para el desarrollo de este caso, se puede crear un entorno virtual en el que se le pueda instalar de manera segura el runtime de ANTLR4 para Python si no se tiene instalado previamente en su sistema:

*Primero se crea y se activa la maquina virtual
>python3 -m venv venv
>
>source venv/bin/activate

*Despues ya activado, se hace la instalación del runtime para Python (dependiendo que version de python tenga instalado)
>pip install antlr4-python3-runtime

*Y por ultímo ya se puede ejecutar la calculadora en la ruta en la que se encuentre así:

>python3 main.py ../entradas.txt (el archivo de entradas se encuentra arriba de ambas carpetas ya que es el mismo archivo de prueba para ambas)

# Pruebas
Como ya se menciono, este proyecto es una prueba para una calculadora usando la precedencia y asociatividad que normalmente tiene, y otra con la asociatividad hacia la derecha, por lo que probando con diferentes expresiones matematicas, se hara comparativa de los resultados que muestra para cada caso, las expresiones a probar estan incluidas en el archivo "entradas.txt"

# Resultados
Probando las expresiones para la calculadora original y la modificada, algunos de los resultados que muestran son los siguientes:
| Expresion | Resultado calculadora normal | Resultado calculadora modificada |
| --- | --- | --- |
| 5-6-1 | -2.0 |  |
| 2+5*7 | 37.0 |  |
| 4/2*5 | 10.0 | |
| (2/1)+3*5-1 | 16.0 |  |
| 134+45-35*2 | 109.0 |  |
| 45-7*(8-3) | 10.0 |  |
| 6+7*8-6/2 | 59.0 |  |
| sqrt(9) | 3.0 |  |

# Conclusiones


    
  
