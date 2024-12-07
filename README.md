# 🚀 **Proyecto de Ingeniería de Datos: Transmisión de Datos en Tiempo Real**

## 📖 **Tabla de Contenidos**
- [📢 Introducción](#introducción)
- [🛠️ Arquitectura del Sistema](#arquitectura-del-sistema)
- [🎯 Objetivos de Aprendizaje](#objetivos-de-aprendizaje)
- [💻 Tecnologías Utilizadas](#tecnologías-utilizadas)
- [🚀 Cómo Empezar](#cómo-empezar)

---

## 📢 **Introducción**
Este proyecto es una guía integral para construir un pipeline de datos desde cero, abarcando todas las etapas: **ingestión, procesamiento y almacenamiento**. Utiliza una arquitectura robusta basada en herramientas modernas como:

- **Apache Airflow**: Orquestación del flujo de datos.
- **Apache Kafka** y **Zookeeper**: Streaming en tiempo real y sincronización distribuida.
- **Apache Spark**: Procesamiento de datos distribuido.
- **Cassandra** y **PostgreSQL**: Almacenamiento confiable de datos procesados.

Todo el proyecto está completamente **contenedorizado con Docker**, lo que facilita la implementación y escalabilidad.

---

## 🛠️ **Arquitectura del Sistema**

![Arquitectura del Sistema](https://www2.udec.cl/~joseparra/2.png)

El proyecto incluye los siguientes componentes:

- **Fuente de Datos**: Utiliza la API `randomuser.me` para generar datos aleatorios de usuarios.
- **Apache Airflow**: Orquesta el pipeline y almacena los datos en una base de datos PostgreSQL.
- **Apache Kafka y Zookeeper**: Transmiten los datos de PostgreSQL al motor de procesamiento.
- **Control Center y Schema Registry**: Supervisan y gestionan los esquemas de los streams de Kafka.
- **Apache Spark**: Procesa los datos con nodos maestro y trabajador.
- **Cassandra**: Almacena los datos procesados para su consulta y análisis.

---

## 🎯 **Objetivos de Aprendizaje**
Con este proyecto, se ponen a prueba las siguientes habilidades:

- Configurar un pipeline de datos con **Apache Airflow**.
- Implementar **streaming de datos en tiempo real** con **Apache Kafka**.
- Sincronizar procesos distribuidos utilizando **Apache Zookeeper**.
- Procesar datos con **Apache Spark**.
- Almacenar datos en bases de datos como **Cassandra** y **PostgreSQL**.
- Contenerizar una arquitectura completa de datos con **Docker**.

---

## 💻 **Tecnologías Utilizadas**

Este proyecto emplea las siguientes herramientas y tecnologías modernas:

- **Apache Airflow**
- **Python**
- **Apache Kafka**
- **Apache Zookeeper**
- **Apache Spark**
- **Cassandra**
- **PostgreSQL**
- **Docker**

---

## 🚀 **Cómo Empezar**

1. Clona el repositorio:
    ```bash
    git clone https://github.com/Siderck/RTDataStream.git
    ```

2. Navega al directorio del proyecto:
    ```bash
    cd RTDataStream
    ```

3. Inicia los servicios con Docker Compose:
    ```bash
    docker-compose up
    ```

4. Accede al servidor de Airflow en tu navegador:  
   [http://localhost:8080](http://localhost:8080)  
