# eolicosasinon
Ferramentas para a defensa do territorio contra os macroparques eolicos

## Uso

1. Utiliza unha folla de cálculo para almacenar todos os datos de coordenadas do parque.
2. Exporta o documento a un ficheiro de texto con valores separados por comas (CSV).
3. Configura o script "procesar_todo.py" indicando os rangos dos diferentes elementos do mapa.
4. Executa o script sobre o teu ficheiro de datos en csv.


## Exemplo

No directorio "sample" tes algúns ficheiros que te poden axudar a entender como funciona o script

1. Todos os datos do parque eólico poden engadirse nun único ficheiro de folla de cálculo como LibreOffice, utilizando unicamente tres columnas.

![Exemplo de folla de cálculo ODS](img/sample_modelo_datos_ods.png)

2. Ademais de gardar a folla de cálculo no seu formato orixinal é necesario exportar os datos a un ficheiro de texto con valores separados por comas (CSV). LibreOffice permite configurar o filtro de exportación, de xeito que cada valor estea delimitado por punto e coma (;) e non se utilice ningún carácter para delimitar as cadeas.

![Configuración de filtro exportación a CSV](img/filtro_exportar_csv.png)

3. O resultado da exportación é un ficheiro CSV coma o seguinte. (A numeración que se ve á esquerda é parte do programa de visualización e non forma parte do ficheiro.)

![Exemplo de ficheiro de datos CSV](img/sample_modelo_datos_csv.png)

4. Antes de executar o script sobre os datos é necesario configurar os rangos onde se encontran os datos (a numeración que se pode ver na marxe esquerda na imaxe anterior).

![Exemplo de configuración de script](img/sample_configuracion_script.png)

5. Unha vez executado o script obtense un ficheiro KMZ que se pode importar nas ferramentas de mapas de Google. O resultado do exemplo pode verse na imaxe.

![Resultado de visualización](img/sample_resultado_parque.png)
