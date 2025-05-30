import React from "react";
import styles from "./Title.module.css";

const Title = (props) => {
  return (
		<div className={styles.container}>
			<h2>{props.text}</h2>
		</div>
	)
}

export default Title;