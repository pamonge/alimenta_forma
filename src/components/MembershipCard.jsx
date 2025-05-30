import React from "react";
import styles from "./MembershipCard.module.css";
import PropTypes from 'prop-types'; 

const MembershipCard = ({type, detail}) => {
	return (
		<div className={styles.container}>
			<h4>{type}</h4>
			<h4>$20000</h4>
			<p>incluye:</p>
			<p>{detail}</p>
		</div>
	)
}

MembershipCard.propTypes = {
	type : PropTypes.string.isRequired,
	detail : PropTypes.string.isRequired
}

export default MembershipCard;