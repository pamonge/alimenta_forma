import React from "react";
import { Link } from "react-router-dom";
import styles from "./RegisterForm.module.css"
import FooterButtons from "./FooterButtons";

const RegisterForm = () => {
  return (
    <div className={styles.container}>
			<h2>Registro de Usuario</h2>
			<h4>Ingrese sus Datos</h4>
			<form className={styles.form} action="">

				<label htmlFor="user">Nombre de Usuario *</label><br />
				<input id="user" type="text" /><br />

				<p>Obligatorio. Longitud máxima de 150 caracteres. Solo puede estar formado por letras, números y los caracteres @/./+/-/_.</p><br />

				<label htmlFor="email">Correo Electrónico *</label><br />
				<input id="email" type="email" /><br />

				<label htmlFor="name">Nombre *</label><br />
				<input id="name" type="text" /><br />

				<label htmlFor="lastName">Apellido *</label><br />
				<input id="lastName" type="text" /><br />

				<label htmlFor="password">Contraseña *</label><br />
				<input id="password" type="password" />

				<p>Su contraseña no puede ser similar a otros componentes de su información personal.</p>
				<p>Su contraseña debe contener por lo menos 8 caracteres.</p>
				<p>Su contraseña no puede ser una contraseña usada muy comúnmente.</p>
				<p>Su contraseña no puede estar formada exclusivamente por números.</p>
				<label htmlFor="password2">Confirmación de Contraseña *</label><br />
				<input id="password2" type="password" /><br />
				<p>Introduzca la misma contraseña nuevamente, para poder verificar la misma.</p>

				<button type="submit">Registrarse</button>
			</form>

			<FooterButtons />
			
    </div>
  )
}

export default RegisterForm;