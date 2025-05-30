import React from "react";
import styles from "./Announcement.module.css"

const Announcement = () => {
	return (
		<div className={styles.container}>
				<p className={styles.p1}>¿Eres del sector de Alimentación y Hostelería?</p>
				<p className={styles.p2}>¿Buscas oportunidades de Empleo y Formación?</p>
		</div>
	)
}

export default Announcement;