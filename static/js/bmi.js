function calculateBMI() {
			var feet = Number(document.getElementById("feet").value);
			var inch = Number(document.getElementById("inch").value);
			var weight = Number(document.getElementById("weight").value);
			var height = ((feet * 12 + inch)*  2.54) / 100;
			var calculate = (weight / (height * height));
			document.getElementById("calculate").innerText = calculate;
			if (calculate < 18.5) {
				document.getElementById("bmi").innerText = "Underweight";
			}
			else if (calculate > 18.5 && calculate < 24.9) {
				document.getElementById("bmi").innerHTML = "Normal Weight HEALTHY";
			}
			else if (calculate > 25 && calculate < 29.9){
				document.getElementById("bmi").innerHTML = "Overweight";
			}
			else if(calculate>30){
				document.getElementById("bmi").innerHTML = "Obese";
			}
			else{
				document.getElementById("bmi").innerHTML = "";
			}
}