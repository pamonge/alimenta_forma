import React, { useState } from "react";
import { Link } from "react-router-dom";
import styles from "./HeaderStyles.module.css"
import { FaBars, FaTimes } from "react-icons/fa";

const Header = () => {

	const [click, setClick] = useState(false);
	const handleClick = () => {
		
		setClick(!click);
	}

	return (
		<div className={styles.container} >
			<div className={styles.appName} >
				<h1>Alimenta</h1>
				<h4>Forma</h4>
			</div>
			<div>
				<ul className={click ? `${styles.menuActive}` : `${styles.menu}`} >
					<li>
						<Link to={'/'}>Inicio</Link>
					</li>
					<li>
						<Link to={'/courses'}>Nuestros Cursos</Link>
					</li>
					<li>
						<Link to={'/membership'}>Nuestros Precios</Link>
					</li>
					<li>
						<Link to={'/about'}>Acerca de</Link>
					</li>
					<li>
						<Link to={'/faqs'}>Preguntas Frecuentes</Link>
					</li>
				</ul>
			</div>
			<div className={styles.hamburger} onClick={handleClick} >
				{click ? (
						<FaTimes className={styles.icon} />
					) : (
						<FaBars className={styles.icon} />
					)
				}
			</div>
		</div>
	)
}

export default Header;