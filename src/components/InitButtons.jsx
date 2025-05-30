import React from "react";
import { Link } from "react-router-dom";
import styles from "./InitButtons.module.css"

const InitButtons = () => {
	return (
		<div className={styles.container}>
			<h4>!Crea tu usuario!</h4>
			<div className={styles.buttons}>
				<button className={styles.registerButton}>
					<Link to={'/register'}>Registrarse</Link>
				</button>
				<button className={styles.loginButton}>
					<Link to={'/login'}>Iniciar Sesión</Link>
				</button>
			</div>
		</div>
	)
}

export default InitButtons;