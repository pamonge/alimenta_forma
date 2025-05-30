import React from "react";
import Header from "../components/Header";
import Title from "../components/Title";
import FaqsCard from "../components/FaqsCard";

const Faqs = () => {
	return (
		<div>
			<Header />
			<Title text="Preguntas Frecuentes" />
			<FaqsCard />
		</div>
			
	)
}

export default Faqs;