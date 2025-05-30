import React from "react";
import { Link } from "react-router-dom";
import styles from "./FooterButtons.module.css"

const FooterButtons = () => {
	return (
		<div className={styles.buttons}>
			<i><Link to={'/'}>Inicio</Link></i>
			<i><Link to={'/login'}>Iniciar Sesión</Link></i>
		</div>
	)
}

export default FooterButtons;
