// Login Validation

function validateForm() {
	let username = document.forms["login"]["username"].value;
	let warn1 = document.getElementById("warning1");
	let warn2 = document.getElementById("warning2");

	if (username.trim() == "") {
		warn1.innerHTML = "Username is required.";
		return false;
	}
	let password = document.forms["login"]["password"].value;
	if (password.trim() == "") {
		warn1.innerHTML = "";
		warn2.innerHTML = "Password is required.";
		return false;
	}
}
