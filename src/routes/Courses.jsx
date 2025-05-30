import React from "react";
import Header from "../components/Header";
import Title from "../components/Title";
import CourseCard from "../components/CourseCard";

const Courses = () => {
	return (
		<div>
			<Header />
			<Title text="Nuestros Cursos" />
			<CourseCard />
		</div>		
	)
}

export default Courses;