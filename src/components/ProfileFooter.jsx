import React from "react";
import { Link } from "react-router-dom";
import { FaHome, FaHeart, FaListUl, FaSearch, FaUserCircle, FaClipboardList, FaIdBadge } from "react-icons/fa";
import styles from "./ProfileFooter.module.css";

const ProfileFooter = () => {
  return (
		<div className={styles.container}>
			<i><Link to={'/'}><FaHome /></Link></i>
			<i><Link><FaSearch /></Link></i>
			<i><Link><FaIdBadge /></Link></i>
			<i><Link><FaListUl /></Link></i>
			<i><Link><FaClipboardList /></Link></i>
			<i><Link><FaHeart /></Link></i>
			<i><Link to={'/profile'}><FaUserCircle /></Link></i>
		</div>
	)
}

export default ProfileFooter;