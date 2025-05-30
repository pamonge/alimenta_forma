import React from "react";
import FooterButtons from "./FooterButtons"
import styles from "./LoginForm.module.css";

const LoginForm = () => {
	return (
		<div className={styles.container}>
			<div>
				<h2>Inicio de Sesión</h2>
			<h4>Ingrese sus Credenciales</h4>
			</div>
			<form className={styles.form}>
				<label htmlFor="user">Nombre de usuario *</label>
				<input id="user" type="text" />

				<label htmlFor="password">Contraseña *</label>
				<input id="password" type="password" />

				<button type="submit" >Iniciar Sesion</button>
			</form>
			<FooterButtons />
		</div>
	)
}

export default LoginForm;