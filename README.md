# Realtime DataStreaming Users

This project simulates user registrations on a platform using APIs and processes the data through various technologies for storage, management, and visualization. Key components include:

Data Collection
📊 Simulating user registration data and collecting it intermittently using Apache Airflow.

Storage
💾 Storing collected data in PostgreSQL.

Data Streaming
🔄 Streaming data from PostgreSQL to Apache Kafka via Apache Airflow.

Management
🛠️ Using Apache Zookeeper to manage Kafka broadcasts and Control Center to visualize data from different topics.

Schema Handling
📜 Employing Schema Registry to manage and understand the schemas of incoming Kafka records.

Processing
⚙️ Streaming data from Kafka to Apache Spark using a master schema architecture for processing.

Final Storage
🗄️ Streaming processed data from Apache Spark to Cassandra.

Environment
🐳 Running the entire setup on Docker for containerized deployment.