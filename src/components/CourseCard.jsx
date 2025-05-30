import React from "react";
import styles from "./CourseCard.module.css";

const CourseCard = () => {
	return (
		<div className={styles.container}>
			<h4>Gastronomía Creativa: Explorando la Fusión de Sabores</h4>
			<img src="../assets/img/55b012da676dc7fda607f73d119c7e3b.png" alt="food, gourmet" />
			<p>Explora técnicas innovadoras para combinar ingredientes y crear platos únicos y deliciosos, en este curso de gastronomía creativa. Desde la fusión de sabores tradicionales hasta la experimentación con ingredientes exóticos. Aprende a desarrollar tu creatividad en la cocina y a sorprender a tus comensales con nuevas experiencias gastronómicas.</p>
			<ul>
				<li>Profesor: Laura Fernández</li>
				<li>Cantidad de Clases: 8</li>
				<li>Cantidad de Inscriptos: 3</li>
				<li>Categoría del Curso: ALIMENTACIÓN </li>
			</ul>

		</div>
	)
}

export default CourseCard;