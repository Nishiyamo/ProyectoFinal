CREATE DATABASE  IF NOT EXISTS `stocksdb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `stocksdb`;
-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: stocksdb
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `securities`
--

DROP TABLE IF EXISTS `securities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `securities` (
  `name` varchar(200) DEFAULT NULL,
  `symbol` varchar(45) NOT NULL,
  `stock` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`symbol`),
  KEY `fk_stock_idx` (`stock`),
  CONSTRAINT `fk_stock` FOREIGN KEY (`stock`) REFERENCES `stocks_exchange` (`symbol`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `securities`
--

LOCK TABLES `securities` WRITE;
/*!40000 ALTER TABLE `securities` DISABLE KEYS */;
/*!40000 ALTER TABLE `securities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `securities_historico`
--

DROP TABLE IF EXISTS `securities_historico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `securities_historico` (
  `symbol` varchar(45) NOT NULL,
  `adj_close` float DEFAULT NULL,
  `date` date NOT NULL,
  KEY `fk_symbol_idx` (`symbol`),
  CONSTRAINT `fk_symbol` FOREIGN KEY (`symbol`) REFERENCES `securities` (`symbol`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `securities_historico`
--

LOCK TABLES `securities_historico` WRITE;
/*!40000 ALTER TABLE `securities_historico` DISABLE KEYS */;
/*!40000 ALTER TABLE `securities_historico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stocks_exchange`
--

DROP TABLE IF EXISTS `stocks_exchange`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stocks_exchange` (
  `name` varchar(45) NOT NULL,
  `url` varchar(200) DEFAULT NULL,
  `symbol` varchar(45) NOT NULL,
  PRIMARY KEY (`symbol`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stocks_exchange`
--

LOCK TABLES `stocks_exchange` WRITE;
/*!40000 ALTER TABLE `stocks_exchange` DISABLE KEYS */;
INSERT INTO `stocks_exchange` VALUES ('Bolsa de Valores de Londres','https://es.finance.yahoo.com/quote/%5EFTSE/components?p=%5EFTSE','FTSE'),('Bolsa de Valores de España','https://es.finance.yahoo.com/quote/%5EIBEX/components?p=%5EIBEX','IBEX'),('Bolsa de Valores NASDAQ','https://finance.yahoo.com/quote/%5EIXIC/components?p=%5EIXIC','IXIC');
/*!40000 ALTER TABLE `stocks_exchange` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-16  8:34:09
