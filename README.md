Proyecto Final Ivan Lorenzo Mediavilla 2020

> Proceso de utilizacion: <br>
    -->Necesitamos:<br>
        --->Python<br>
        --->NPM<br>
        --->Node<br>
        --->MySql<br><br>
    -->En primer lugar crearemos la base de datos, con el .sql alojado en el directorio SQLdumps<br><br><br>
    -->Necesitaremos las dependencias tanto de python como de nodejs para poder ejecutar el proyecto.<br>
    ---->Para instalar las dependencias de python prodecederos a posicionarnos en la raiz del proyecto y ejecutar el comando:<br>
    ------->*pip install -r requirements.txt*<br>
    ---->Para instalar las dependencias de node procederemos a posicionarnos en la carpeta FrontendStocks y ejecutar el comando:<br>
    ------->*npm install*

> Dentro de la carpeta DataStatsStockExchange estaran ubicados los adaptadores y toda la parte backend del proyecto <br>
    --> Sacar de https://es.finance.yahoo.com/ el nombre de los stocks a ser la libreria que usa Yahoo Finance,<br>
       esto solo se usara para obtener los datos para alimentar la base de datos.<br>
    --> La parte backend encargada de alimentar al servicio web estara alojada dentro de los archivos del frontend.<br><br>
>Comandos para el arranque y carga de los datos:<br>
    --> Para arrancar el servidor flask usaremos el comando "python -m DataStatsStockExchange.application.app" para arrancarlo.<br>
    --> Para poblar la base de datosusaremos el comando "python -m test_main" para arrancarlo.<br>
