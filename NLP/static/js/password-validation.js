function validatePassword() {
    var password = document.getElementById("password").value;
    var requirements = document.getElementById("password-requirements");
    var regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;

    if (!regex.test(password)) {
        requirements.style.color = "red";
        requirements.innerHTML = "Password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, one number, and one special character.";
        return false;
    } else {
        requirements.style.color = "green";
        requirements.innerHTML = "Password meets all requirements.";
        return true;
    }
}