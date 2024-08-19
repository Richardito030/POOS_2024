-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 13-08-2024 a las 09:30:04
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd_agencia`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `administradores`
--

CREATE TABLE `administradores` (
  `clave_administrador` varchar(10) NOT NULL,
  `privilegio` tinyint(2) NOT NULL,
  `CURP_persona` varchar(18) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `administradores`
--

INSERT INTO `administradores` (`clave_administrador`, `privilegio`, `CURP_persona`) VALUES
('ADMIN101', 2, 'TISA050501HDGNNLA6');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `calificaciones`
--

CREATE TABLE `calificaciones` (
  `id_calificacion` int(11) NOT NULL,
  `calificacion` decimal(3,2) NOT NULL,
  `observaciones` varchar(80) NOT NULL,
  `clave_materia` varchar(20) NOT NULL,
  `matricula_estudiante` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `calificaciones`
--

INSERT INTO `calificaciones` (`id_calificacion`, `calificacion`, `observaciones`, `clave_materia`, `matricula_estudiante`) VALUES
(1, 9.70, 'Un estudiante muy dedicado', 'Espanol101', '3141230056'),
(2, 8.20, 'Un estudiante muy dedicado', 'Matematicas101', '3141230056'),
(4, 7.20, 'REPROBADO', 'Matematicas101', '3141230055'),
(5, 9.20, 'Estudiante muy dedicado', 'Espanol101', '3141230056');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiantes`
--

CREATE TABLE `estudiantes` (
  `matricula_estudiante` varchar(10) NOT NULL,
  `grado_estudiante` varchar(1) NOT NULL,
  `grupo_estudiante` varchar(1) NOT NULL,
  `promedio_estudiante` decimal(3,2) NOT NULL,
  `modalidad_estudiante` varchar(10) NOT NULL,
  `carrera_estudiante` varchar(20) NOT NULL,
  `privilegio` tinyint(2) NOT NULL,
  `CURP_persona` varchar(18) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `estudiantes`
--

INSERT INTO `estudiantes` (`matricula_estudiante`, `grado_estudiante`, `grupo_estudiante`, `promedio_estudiante`, `modalidad_estudiante`, `carrera_estudiante`, `privilegio`, `CURP_persona`) VALUES
('3141230055', '2', 'A', 9.20, 'BILINGUE', 'TICS', 0, 'ROAR051003HDGDLCA9'),
('3141230056', '2', 'B', 9.20, 'BILINGUE', 'TICS', 0, 'TISA050501HDGNNLA8');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `materias`
--

CREATE TABLE `materias` (
  `clave_materia` varchar(20) NOT NULL,
  `nombre_materia` varchar(20) NOT NULL,
  `descripcion_materia` varchar(80) NOT NULL,
  `creditos_materia` int(2) NOT NULL,
  `matricula_profesor` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `materias`
--

INSERT INTO `materias` (`clave_materia`, `nombre_materia`, `descripcion_materia`, `creditos_materia`, `matricula_profesor`) VALUES
('Espanol101', 'Espanol', 'Materia usada para mejorar el lenguaje', 3, '3141230057'),
('Matematicas101', 'Matematicas', 'Materia usada para el desarrollo logico matematico', 4, '3141230057');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `personas`
--

CREATE TABLE `personas` (
  `CURP_persona` varchar(18) NOT NULL,
  `nombre_persona` varchar(40) NOT NULL,
  `apellidop_persona` varchar(40) NOT NULL,
  `apellidom_persona` varchar(40) NOT NULL,
  `edad_persona` int(3) NOT NULL,
  `telefono_persona` varchar(12) NOT NULL,
  `email_persona` varchar(30) NOT NULL,
  `direccion_persona` varchar(40) NOT NULL,
  `contrasena_persona` varchar(40) NOT NULL,
  `escuela_persona` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `personas`
--

INSERT INTO `personas` (`CURP_persona`, `nombre_persona`, `apellidop_persona`, `apellidom_persona`, `edad_persona`, `telefono_persona`, `email_persona`, `direccion_persona`, `contrasena_persona`, `escuela_persona`) VALUES
('GOGH730518MTSNRY09', 'CYNTHIA', 'GONZALEZ', 'HERNANDEZ', 30, '6182304892', 'CYNTHIA@GMAIL.COM', 'CALLE PRINCIPAL 103', 'password123', 'INSTITUTO TECNOLOGICO DE DURANGO'),
('ROAR051003HDGDLCA9', 'RICARDO', 'RODRIGUEZ', 'ALARCON', 19, '6182788938', 'RICARDO@GMAIL.COM', 'CALLE SECUNDARIA 202', 'password123', 'UNIVERSIDAD TECNOLOGICA DE DURANGO'),
('TISA050501HDGNNLA6', 'ALEXANDER', 'ADMIN', 'ADMIN', 19, '6182318481', 'alexander_3141230056@utd.edu.m', 'ANDADOR TARAHUMARA 111', 'password', 'UNIVERSIDAD TECNOLOGICA DE DURANGO'),
('TISA050501HDGNNLA8', 'ALEXANDER', 'TINOCO', 'SANCHEZ', 19, '6182318481', 'ALEXNUEVO040@GMAIL.COM', 'ANDADOR TARAHUMARA 111 HUIZACHE 1', 'password123', 'UNIVERSIDAD TECNOLOGICA DE DURANGO');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `profesores`
--

CREATE TABLE `profesores` (
  `matricula_profesor` varchar(10) NOT NULL,
  `puesto_profesor` varchar(30) NOT NULL,
  `salario_profesor` varchar(20) NOT NULL,
  `antiguedad_profesor` varchar(2) NOT NULL,
  `titulo_profesor` varchar(20) NOT NULL,
  `privilegio` tinyint(2) NOT NULL,
  `CURP_persona` varchar(18) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `profesores`
--

INSERT INTO `profesores` (`matricula_profesor`, `puesto_profesor`, `salario_profesor`, `antiguedad_profesor`, `titulo_profesor`, `privilegio`, `CURP_persona`) VALUES
('3141230057', 'PROFESOR TITULAR', '5000', '10', 'DOCTORADO', 1, 'GOGH730518MTSNRY09');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `administradores`
--
ALTER TABLE `administradores`
  ADD PRIMARY KEY (`clave_administrador`),
  ADD KEY `CURP_persona` (`CURP_persona`);

--
-- Indices de la tabla `calificaciones`
--
ALTER TABLE `calificaciones`
  ADD PRIMARY KEY (`id_calificacion`) USING BTREE,
  ADD KEY `clave_materia` (`clave_materia`),
  ADD KEY `matricula_estudiante` (`matricula_estudiante`);

--
-- Indices de la tabla `estudiantes`
--
ALTER TABLE `estudiantes`
  ADD PRIMARY KEY (`matricula_estudiante`),
  ADD KEY `CURP_persona` (`CURP_persona`);

--
-- Indices de la tabla `materias`
--
ALTER TABLE `materias`
  ADD PRIMARY KEY (`clave_materia`),
  ADD KEY `matricula_profesor` (`matricula_profesor`);

--
-- Indices de la tabla `personas`
--
ALTER TABLE `personas`
  ADD PRIMARY KEY (`CURP_persona`);

--
-- Indices de la tabla `profesores`
--
ALTER TABLE `profesores`
  ADD PRIMARY KEY (`matricula_profesor`),
  ADD KEY `CURP_persona` (`CURP_persona`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `calificaciones`
--
ALTER TABLE `calificaciones`
  MODIFY `id_calificacion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `administradores`
--
ALTER TABLE `administradores`
  ADD CONSTRAINT `administradores_ibfk_1` FOREIGN KEY (`CURP_persona`) REFERENCES `personas` (`CURP_persona`);

--
-- Filtros para la tabla `calificaciones`
--
ALTER TABLE `calificaciones`
  ADD CONSTRAINT `calificaciones_ibfk_1` FOREIGN KEY (`matricula_estudiante`) REFERENCES `estudiantes` (`matricula_estudiante`),
  ADD CONSTRAINT `calificaciones_ibfk_2` FOREIGN KEY (`clave_materia`) REFERENCES `materias` (`clave_materia`);

--
-- Filtros para la tabla `estudiantes`
--
ALTER TABLE `estudiantes`
  ADD CONSTRAINT `estudiantes_ibfk_1` FOREIGN KEY (`CURP_persona`) REFERENCES `personas` (`CURP_persona`);

--
-- Filtros para la tabla `materias`
--
ALTER TABLE `materias`
  ADD CONSTRAINT `materias_ibfk_1` FOREIGN KEY (`matricula_profesor`) REFERENCES `profesores` (`matricula_profesor`);

--
-- Filtros para la tabla `profesores`
--
ALTER TABLE `profesores`
  ADD CONSTRAINT `profesores_ibfk_1` FOREIGN KEY (`CURP_persona`) REFERENCES `personas` (`CURP_persona`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
